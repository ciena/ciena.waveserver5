"""Gather OpenConfig platform component inventory."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.ansible.netcommon.plugins.module_utils.network.netconf.netconf import (
    get,
)


PLATFORM_NAMESPACE = "http://openconfig.net/yang/platform"


def _local_name(tag):
    return tag.rsplit("}", 1)[-1].replace("-", "_")


def _element_value(element):
    children = list(element)
    if not children:
        text = (element.text or "").strip()
        return text or None

    result = {}
    for child in children:
        key = _local_name(child.tag)
        value = _element_value(child)
        if key in result:
            if not isinstance(result[key], list):
                result[key] = [result[key]]
            result[key].append(value)
        else:
            result[key] = value
    return result


def _component_elements(root):
    for element in root.iter():
        if _local_name(element.tag) == "components":
            return [child for child in element if _local_name(child.tag) == "component"]
    return []


class InventoryFacts(object):
    """Collect the device's OpenConfig platform components."""

    def __init__(self, module):
        self._module = module

    def get_inventory(self, data=None):
        if data is None:
            platform_filter = '<components xmlns="%s"/>' % PLATFORM_NAMESPACE
            data = get(self._module, filter=("subtree", platform_filter))

        return [_element_value(item) for item in _component_elements(data)]

    def populate_facts(self, connection, ansible_facts, data=None):
        ansible_facts["ansible_network_resources"]["inventory"] = self.get_inventory(data)
        return ansible_facts

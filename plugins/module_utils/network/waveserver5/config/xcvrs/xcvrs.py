#
# -*- coding: utf-8 -*-
# Copyright 2023 Ciena
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The waveserver5_xcvrs class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type

try:
    from lxml import etree

    HAS_LXML = True
except ImportError:
    HAS_LXML = False


from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)

from ansible_collections.ciena.waveserver5.plugins.module_utils.network.waveserver5.waveserver5 import (
    tostring,
)

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.ciena.waveserver5.plugins.module_utils.network.waveserver5.facts.facts import (
    Facts,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.netconf import (
    build_root_xml_node,
    build_child_xml_node,
)

from ansible_collections.ciena.waveserver5.plugins.module_utils.network.waveserver5.utils.utils import (
    config_is_diff,
)


class Xcvrs(ConfigBase):
    """
    The waveserver5_xcvrs class
    """

    gather_subset = ["!all", "!min"]
    gather_network_resources = ["xcvrs"]

    def __init__(self, module):
        super(Xcvrs, self).__init__(module)

    def get_xcvrs_facts(self):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset, self.gather_network_resources
        )
        xcvrs_facts = facts["ansible_network_resources"].get("xcvrs")
        if not xcvrs_facts:
            return []
        return xcvrs_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        existing_xcvrs_facts = self.get_xcvrs_facts()
        config_xmls = self.set_config(existing_xcvrs_facts)

        if config_xmls and self.state in self.ACTION_STATES:
            for config_xml in to_list(config_xmls):
                config = f"<config>{config_xml}</config>"
                kwargs = {
                    "config": config,
                    "target": "running",
                    "default_operation": "merge",
                    "format": "xml",
                }
                self._module._connection.edit_config(**kwargs)
            result["changed"] = True
            result["xml"] = config_xmls

        changed_xcvrs_facts = self.get_xcvrs_facts()

        result["changed"] = config_is_diff(existing_xcvrs_facts, changed_xcvrs_facts)

        result["before"] = existing_xcvrs_facts
        if self.state in self.ACTION_STATES:
            result["before"] = existing_xcvrs_facts
            if result["changed"]:
                result["after"] = changed_xcvrs_facts

        elif self.state == "gathered":
            result["gathered"] = existing_xcvrs_facts

        return result

    def set_config(self, existing_xcvrs_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_xcvrs_facts
        resp = self.set_state(want, have)
        return to_list(resp)

    def set_state(self, want, have):
        """Select the appropriate function based on the state provided

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        key = "waveserver-xcvr"
        namespace = "urn:ciena:params:xml:ns:yang:ciena-ws:ciena-waveserver-xcvr"
        nsmap = {None: namespace}
        root = etree.Element("{%s}%s" % (namespace, key), nsmap=nsmap)
        state = self._module.params["state"]
        state_methods = {
            "overridden": self._state_overridden,
            "deleted": self._state_deleted,
            "merged": self._state_merged,
            "replaced": self._state_replaced,
        }
        config_xmls = []
        if state in state_methods:
            config_xmls = state_methods.get(state)(want, have)
        for xml in config_xmls:
            root.append(xml)

        return tostring(root)

    def _state_replaced(self, want, have):
        """The command generator when state is replaced

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        xcvrs_xml = []
        xcvrs_xml.extend(self._state_deleted(want, have))
        xcvrs_xml.extend(self._state_merged(want, have))
        return xcvrs_xml

    def _state_overridden(self, want, have):
        """The command generator when state is overridden

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        xcvrs_xml = []
        xcvrs_xml.extend(self._state_deleted(have, have))
        xcvrs_xml.extend(self._state_merged(want, have))
        return xcvrs_xml

    def _state_deleted(self, want, have):
        """The command generator when state is deleted

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        xcvrs_xml = []
        if not want:
            want = have
        for config in want:
            xcvr_root = build_root_xml_node("xcvr")
            build_child_xml_node(xcvr_root, "xcvr_id", config["xcvr_id"])
            xcvr_root.attrib["operation"] = "remove"
            xcvrs_xml.append(xcvr_root)
        return xcvrs_xml

    def _state_merged(self, want, have):
        """The command generator when state is merged

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        # Create an empty list to hold the XML elements
        xml_elements = []

        # Iterate over the 'want' dictionary
        for key, value in want.items():
            key = key.replace("_", "-")
            if isinstance(value, dict):
                # If the value is a dictionary, create a new element and recursively add its children
                element = etree.Element(key)
                if isinstance(want.get(key), dict):
                    element.extend(self._state_merged(value, want.get(key)))
                else:
                    element.extend(self._state_merged(value, {}))
            else:
                # If the value is not a dictionary, create a new element and set its text
                element = etree.Element(key)
                element.text = str(value)

            # Add the element to the list
            xml_elements.append(element)

        return xml_elements

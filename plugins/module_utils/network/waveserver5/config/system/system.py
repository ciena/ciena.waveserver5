#
# -*- coding: utf-8 -*-
# Copyright 2023 Ciena
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The waveserver5_system class
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


class System(ConfigBase):
    """
    The waveserver5_system class
    """

    gather_subset = ["!all", "!min"]
    gather_network_resources = ["system"]

    def __init__(self, module):
        super(System, self).__init__(module)

    def get_system_facts(self):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset, self.gather_network_resources
        )
        system_facts = facts["ansible_network_resources"].get("system")
        if not system_facts:
            return []
        return system_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        existing_system_facts = self.get_system_facts()
        config_xmls = self.set_config(existing_system_facts)

        for config_xml in to_list(config_xmls):
            config = f"<config>{config_xml}</config>"
            kwargs = {
                "config": config,
                "target": "running",
                "default_operation": "merge",
                "format": "xml",
            }

            self._module._connection.edit_config(**kwargs)

        result["xml"] = config_xmls
        changed_system_facts = self.get_system_facts()

        result["changed"] = config_is_diff(existing_system_facts, changed_system_facts)

        result["before"] = existing_system_facts
        if result["changed"]:
            result["after"] = changed_system_facts

        return result

    def set_config(self, existing_system_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_system_facts
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
        key = "waveserver-system"
        namespace = "urn:ciena:params:xml:ns:yang:ciena-ws:ciena-waveserver-system"
        nsmap = {None: namespace}
        root = etree.Element("{%s}%s" % (namespace, key), nsmap=nsmap)
        state = self._module.params["state"]
        if state == "overridden":
            config_xmls = self._state_overridden(want, have)
        elif state == "deleted":
            config_xmls = self._state_deleted(want, have)
        elif state == "merged":
            config_xmls = self._state_merged(want, have)
        elif state == "replaced":
            config_xmls = self._state_replaced(want, have)

        for xml in config_xmls:
            root.append(xml)
        response = tostring(root)
        return response

    def _state_replaced(self, want, have):
        """The command generator when state is replaced

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        system_xml = []
        system_xml.extend(self._state_deleted(want, have))
        system_xml.extend(self._state_merged(want, have))
        return system_xml

    def _state_overridden(self, want, have):
        """The command generator when state is overridden

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        system_xml = []
        system_xml.extend(self._state_deleted(have, have))
        system_xml.extend(self._state_merged(want, have))
        return system_xml

    def _state_deleted(self, want, have):
        """The command generator when state is deleted

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        system_xml = []
        if not want:
            want = have
        for config in want:
            system_root = build_root_xml_node("system")
            build_child_xml_node(system_root, "name", config["name"])
            system_root.attrib["operation"] = "remove"
            system_xml.append(system_root)
        return system_xml

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

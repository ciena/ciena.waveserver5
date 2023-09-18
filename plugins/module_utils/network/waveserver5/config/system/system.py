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
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
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
        have = self.get_system_facts()
        config_dict = self.set_config(have)

        if config_dict:
            config_xml = self.create_xml_config(config_dict)
            if not self.validate_xml(config_xml):
                raise ValueError("Generated XML is not valid.")

            kwargs = {"config": f"<config>{config_xml}</config>", "target": "running"}
            try:
                self._module._connection.edit_config(**kwargs)
            except Exception as e:
                return {"failed": True, "msg": str(e)}

            result["changed"] = True
            result["xml"] = config_xml
        changed_system_facts = self.get_system_facts()

        result["changed"] = config_is_diff(have, changed_system_facts)

        result["before"] = have
        if self.state in self.ACTION_STATES:
            if result["changed"]:
                result["after"] = changed_system_facts

        elif self.state == "gathered":
            result["gathered"] = have

        return result

    def set_config(self, have):
        want = self._module.params["config"]
        state = self._module.params["state"]
        state_methods = {
            "overridden": self._state_overridden,
            "merged": self._state_merged,
            "replaced": self._state_replaced,
        }

        config_dict = state_methods[state](want, have) if state in self.ACTION_STATES else {}
        return config_dict

    def create_element(self, key, value, parent):
        sanitized_key = key.replace("_", "-")
        subelem = etree.Element(sanitized_key)
        if isinstance(value, dict):
            for subkey, subvalue in value.items():
                self.create_element(subkey, subvalue, subelem)
        else:
            subelem.text = str(value)
        if value is not None:
            parent.append(subelem)

    def create_xml_config(self, config_dict):
        key = "waveserver-system"
        namespace = "urn:ciena:params:xml:ns:yang:ciena-ws:ciena-waveserver-system"
        nsmap = {None: namespace}
        root = etree.Element(f"{{{namespace}}}{key}", nsmap=nsmap)
        for key, value in config_dict.items():
            self.create_element(key, value, root)
        return etree.tostring(root).decode()

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

    def _state_merged(self, want, have):
        merged_dict = {}
        for key, value in want.items():
            if key in have and have[key] == value:
                continue
            merged_dict[key] = value
        return merged_dict

    def validate_xml(self, xml_str):
        try:
            etree.fromstring(xml_str.encode())
        except etree.XMLSyntaxError:
            return False
        return True

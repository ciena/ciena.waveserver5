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
from ansible_collections.ciena.waveserver5.plugins.module_utils.network.waveserver5.facts.facts import (
    Facts,
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
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
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
        have = self.get_xcvrs_facts()
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

        changed_xcvrs_facts = self.get_xcvrs_facts()

        result["changed"] = config_is_diff(have, changed_xcvrs_facts)

        result["before"] = have
        if self.state in self.ACTION_STATES:
            if result["changed"]:
                result["after"] = changed_xcvrs_facts

        elif self.state == "gathered":
            result["gathered"] = have

        return result

    def set_config(self, have):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        state = self._module.params["state"]
        state_methods = {
            "merged": self._state_merged,
        }
        config_dict = state_methods[state](want, have) if state in self.ACTION_STATES else {}
        return config_dict

    def create_element(self, key, value, parent):
        sanitized_key = key.replace("_", "-")
        if isinstance(value, dict):
            subelem = etree.Element(sanitized_key)
            for subkey, subvalue in value.items():
                self.create_element(subkey, subvalue, subelem)
            if value:
                parent.append(subelem)
        elif isinstance(value, list):
            for list_item in value:
                subelem = etree.Element(sanitized_key)
                for subkey, subvalue in list_item.items():
                    self.create_element(subkey, subvalue, subelem)
                parent.append(subelem)
        else:
            subelem = etree.Element(sanitized_key)
            subelem.text = str(value)
            if value is not None:
                parent.append(subelem)

    def create_xml_config(self, config_dict_or_list):
        key = "waveserver-xcvrs"
        namespace = "urn:ciena:params:xml:ns:yang:ciena-ws:ciena-waveserver-xcvr"
        nsmap = {None: namespace}
        root = etree.Element("{%s}%s" % (namespace, key), nsmap=nsmap)

        if isinstance(config_dict_or_list, dict):
            for key, value in config_dict_or_list.items():
                self.create_element(key, value, root)
        elif isinstance(config_dict_or_list, list):
            for list_item in config_dict_or_list:
                if not isinstance(list_item, dict):
                    raise ValueError("List items must be dictionaries.")
                parent_for_list_item = etree.Element("xcvrs")
                for key, value in list_item.items():
                    self.create_element(key, value, parent_for_list_item)
                root.append(parent_for_list_item)
        else:
            raise TypeError("Expected a dictionary or a list, got a {}".format(type(config_dict_or_list)))

        return etree.tostring(root).decode()

    def _state_merged(self, want, have):
        if isinstance(want, list):
            return self._state_merged_list(want, have)
        elif isinstance(want, dict):
            return self._state_merged_dict(want, have)

    def _state_merged_dict(self, want, have):
        response = {}
        for key, value in want.items():
            if key in have and have[key] == value:
                continue
            response[key] = value
        return response

    def _state_merged_list(self, want, have):
        merged_list = []
        for w_item in want:
            if w_item in have:
                continue
            merged_list.append(w_item)
        return merged_list

    def validate_xml(self, xml_str):
        try:
            etree.fromstring(xml_str.encode())
        except etree.XMLSyntaxError:
            return False
        return True

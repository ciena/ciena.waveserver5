#
# (c) 2017 Red Hat Inc.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
author: Ansible Networking Team (@ansible-network)
name: waveserver5
short_description: Use ciena netconf plugin to run netconf commands on Ciena Waveserver5
  platform
description:
- This waveserver5 plugin provides low level abstraction apis for sending and receiving
  netconf commands from Ciena Waveserver5 network devices.
version_added: 1.0.0
options:
  ncclient_device_handler:
    type: str
    default: default
    description:
    - Specifies the ncclient device handler name for Juniper waveserver5 network os. To
      identify the ncclient device handler name refer ncclient library documentation.
"""

import json
import re


from ansible.errors import AnsibleConnectionFailure
from lxml.etree import XMLSyntaxError
from ansible.module_utils._text import to_native
from ansible_collections.ansible.netcommon.plugins.plugin_utils.netconf_base import (
    NetconfBase,
    ensure_ncclient,
)
from ansible_collections.ciena.waveserver5.plugins.module_utils.network.waveserver5.waveserver5 import (
    remove_ns,
)


try:
    from ncclient import manager
    from ncclient.operations import RPCError
    from ncclient.transport.errors import SSHUnknownHostError
    from ncclient.xml_ import new_ele, sub_ele, to_ele, to_xml

    HAS_NCCLIENT = True
except (
    ImportError,
    AttributeError,
):  # paramiko and gssapi are incompatible and raise AttributeError not ImportError
    HAS_NCCLIENT = False


class Netconf(NetconfBase):
    def get_capabilities(self):
        result = dict()
        result["rpc"] = self.get_base_rpc() + [
            "kill_session",
            "close_session",
        ]
        result["network_api"] = "netconf"
        result["device_info"] = self.get_device_info()
        result["server_capabilities"] = list(self.m.server_capabilities)
        result["client_capabilities"] = list(self.m.client_capabilities)
        result["session_id"] = self.m.session_id
        result["device_operations"] = self.get_device_operations(
            result["server_capabilities"],
        )
        return json.dumps(result)

    @ensure_ncclient
    def get_device_info(self):
        device_info = {
            "network_os": "waveserver5",
        }

        # Combine filters for components and system information
        combined_filter = '''
        <filter>
            <components xmlns="http://openconfig.net/yang/platform"/>
            <system xmlns="http://openconfig.net/yang/system">
                <config>
                    <hostname/>
                </config>
            </system>
        </filter>
        '''
        root = self._fetch_data(combined_filter)

        # Extract data from components
        model = self._extract_xpath(root, "//component[name='Waveserver']/state/description")
        network_os_version = self._extract_xpath(root, "//component[name='CM-1']/state/software-version")

        device_info["network_os_version"] = network_os_version
        device_info["network_os_model"] = model

        # Extract hostname from system data
        hostname = self._extract_xpath(root, "/data/system/config/hostname")
        device_info["network_os_hostname"] = hostname

        return device_info

    def _extract_xpath(self, root, xpath_str, default=None):
        """Extract data using XPath and return text or default."""
        result = root.xpath(xpath_str)
        return result[0].text if result else default

    def _fetch_data(self, filter_str):
        """Fetch data from device using given filter."""
        filter_ele = to_ele(filter_str)
        reply = self.m.get(filter=("subtree", filter_ele))
        try:
            response = remove_ns(reply.data_ele)
        except Exception as e:
            # Handle the XML parsing error
            raise ValueError("Received an invalid XML response from the device. %s" % e)
        return response

    @staticmethod
    @ensure_ncclient
    def guess_network_os(obj):
        """
        Guess the remote network os name
        :param obj: Netconf connection class object
        :return: Network OS name
        """
        try:
            m = manager.connect(
                host=obj._play_context.remote_addr,
                port=obj._play_context.port or 830,
                username=obj._play_context.remote_user,
                password=obj._play_context.password,
                key_filename=obj.key_filename,
                hostkey_verify=obj.get_option("host_key_checking"),
                look_for_keys=obj.get_option("look_for_keys"),
                allow_agent=obj._play_context.allow_agent,
                timeout=obj.get_option("persistent_connect_timeout"),
                # We need to pass in the path to the ssh_config file when guessing
                # the network_os so that a jumphost is correctly used if defined
                ssh_config=obj._ssh_config,
            )
        except SSHUnknownHostError as exc:
            raise AnsibleConnectionFailure(to_native(exc))

        guessed_os = None
        for c in m.server_capabilities:
            if re.search("waveserver", c):
                guessed_os = "waveserver5"

        m.close_session()
        return guessed_os
    
    def execute_rpc(self, name):
        """
        RPC to be execute on remote device
        :param name: Name of rpc in string format
        :return: Received rpc response from remote host
        """
        return self.rpc(name)

    @ensure_ncclient
    def edit_config(
        self,
        config=None,
        format="xml",
        target="candidate",
        default_operation=None,
        test_option=None,
        error_option=None,
    ):
        """
        Loads all or part of the specified *config* to the *target* configuration datastore.
        :param config: Is the configuration, which must be rooted in the `config` element.
                       It can be specified either as a string or an :class:`~xml.etree.ElementTree.Element`.
        :param format: The format of configuration eg. xml, text
        :param target: Is the name of the configuration datastore being edited
        :param default_operation: If specified must be one of { `"merge"`, `"replace"`, or `"none"` }
        :param test_option: If specified must be one of { `"test_then_set"`, `"set"` }
        :param error_option: If specified must be one of { `"stop-on-error"`, `"continue-on-error"`, `"rollback-on-error"` }
                             The `"rollback-on-error"` *error_option* depends on the `:rollback-on-error` capability.
        :return: Returns xml string containing the RPC response received from remote host
        """
        if config is None:
            raise ValueError("config value must be provided")
        resp = self.m.edit_config(
            config,
            format=format,
            target=target,
            default_operation=default_operation,
            test_option=test_option,
            error_option=error_option,
        )

        return resp.data_xml if hasattr(resp, "data_xml") else resp.xml

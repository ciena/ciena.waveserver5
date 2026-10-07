#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: waveserver5_inventory
version_added: 1.2.0
short_description: Gather chassis and component inventory from Waveserver 5.
description:
  - Reads OpenConfig platform component inventory over NETCONF.
  - This read-only module returns the chassis and installed components exposed by
    the device's platform model.
options:
  state:
    description:
      - The operation to perform. This module only gathers the current inventory.
    type: str
    choices:
      - gathered
    default: gathered
"""

EXAMPLES = """
- name: Gather chassis and component inventory
  ciena.waveserver5.waveserver5_inventory:
    state: gathered
  register: chassis_inventory

- name: Display inventory
  ansible.builtin.debug:
    var: chassis_inventory.gathered
"""

RETURN = """
gathered:
  description: Chassis and platform component data returned by the device.
  returned: always
  type: list
  elements: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ciena.waveserver5.plugins.module_utils.network.waveserver5.facts.inventory.inventory import (
    InventoryFacts,
)


def main():
    module = AnsibleModule(
        argument_spec={"state": {"type": "str", "default": "gathered", "choices": ["gathered"]}},
        supports_check_mode=True,
    )
    gathered = InventoryFacts(module).get_inventory()
    module.exit_json(changed=False, gathered=gathered)


if __name__ == "__main__":
    main()
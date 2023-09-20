#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2023 Ciena
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for waveserver5_xcvrs
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {"metadata_version": "1.1", "status": ["preview"], "supported_by": "network"}

DOCUMENTATION = """
---
module: waveserver5_xcvr
version_added: 1.1.0
short_description: Waveserver Transceiver configuration data and operational data.
description: Waveserver Transceiver configuration data and operational data.
author:
  - Jeff Groom (@jgroom33)
  - Galo Ertola (@perrary)
requirements:
  - ncclient (>=v0.6.4)
  - xmltodict (>=0.12.0)
options:
  config:
    description: Waveserver transceiver (XCVR) list.
    elements: dict
    suboptions:
      properties:
        description: All the Configurable and operational data of this XCVR instance.
        suboptions:
          mode:
            choices:
              - blank
              - OCH
              - OTM
              - OSC
              - OSC-Add-Drop
              - 10GE
              - 4x10GE
              - 40GE
              - 100GE
              - 400GE
              - 4x100GE
              - 4x100GE-ZR
              - OTL4.4
              - OTLC.4
              - FOIC1.4
              - FOIC4.8
              - 35-100
              - 35-150
              - 35-200
              - 35-250
              - 56-100
              - 56-150
              - 56-200
              - 56-250
              - 56-300
              - 56-350
              - 56-400
              - 95-200-O
              - 95-250-O
              - 95-300-O
              - 95-350-O
              - 95-400-O
              - 95-450-O
              - 95-500-O
              - 95-550-O
              - 95-600-O
              - 95-650-O
              - 95-700-O
              - 95-750-O
              - 95-800-O
              - 95-200-E
              - 95-250-E
              - 95-300-E
              - 95-350-E
              - 95-400-E
              - 95-450-E
              - 95-500-E
              - 95-550-E
              - 95-600-E
              - 95-650-E
              - 95-700-E
              - 95-750-E
              - 95-800-E
              - 91.6-200-O
              - 91.6-250-O
              - 91.6-300-O
              - 91.6-350-O
              - 91.6-400-O
              - 91.6-450-O
              - 91.6-500-O
              - 91.6-550-O
              - 91.6-600-O
              - 91.6-650-O
              - 91.6-700-O
              - 91.6-750-O
              - 91.6-800-O
              - 91.6-200-E
              - 91.6-250-E
              - 91.6-300-E
              - 91.6-350-E
              - 91.6-400-E
              - 91.6-450-E
              - 91.6-500-E
              - 91.6-550-E
              - 91.6-600-E
              - 91.6-650-E
              - 91.6-700-E
              - 91.6-750-E
              - 91.6-800-E
              - 89.3-200-O
              - 89.3-250-O
              - 89.3-300-O
              - 89.3-350-O
              - 89.3-400-O
              - 89.3-450-O
              - 89.3-500-O
              - 89.3-550-O
              - 89.3-600-O
              - 89.3-650-O
              - 89.3-700-O
              - 89.3-750-O
              - 89.3-800-O
              - 89.3-200-E
              - 89.3-250-E
              - 89.3-300-E
              - 89.3-350-E
              - 89.3-400-E
              - 89.3-450-E
              - 89.3-500-E
              - 89.3-550-E
              - 89.3-600-E
              - 89.3-650-E
              - 89.3-700-E
              - 89.3-750-E
              - 89.3-800-E
              - 71.3-200-O
              - 71.3-250-O
              - 71.3-300-O
              - 71.3-350-O
              - 71.3-400-O
              - 71.3-450-O
              - 71.3-500-O
              - 71.3-550-O
              - 71.3-600-O
              - 71.3-200-E
              - 71.3-250-E
              - 71.3-300-E
              - 71.3-350-E
              - 71.3-400-E
              - 71.3-450-E
              - 71.3-500-E
              - 71.3-550-E
              - 71.3-600-E
              - 69.5-200-O
              - 69.5-250-O
              - 69.5-300-O
              - 69.5-350-O
              - 69.5-400-O
              - 69.5-450-O
              - 69.5-500-O
              - 69.5-550-O
              - 69.5-600-O
              - 69.5-200-E
              - 69.5-250-E
              - 69.5-300-E
              - 69.5-350-E
              - 69.5-400-E
              - 69.5-450-E
              - 69.5-500-E
              - 69.5-550-E
              - 69.5-600-E
              - 93.3-200-O
              - 93.3-250-O
              - 93.3-300-O
              - 93.3-350-O
              - 93.3-400-O
              - 93.3-450-O
              - 93.3-500-O
              - 93.3-550-O
              - 93.3-600-O
              - 93.3-650-O
              - 93.3-700-O
              - 93.3-750-O
              - 93.3-800-O
              - 93.3-200-E
              - 93.3-250-E
              - 93.3-300-E
              - 93.3-350-E
              - 93.3-400-E
              - 93.3-450-E
              - 93.3-500-E
              - 93.3-550-E
              - 93.3-600-E
              - 93.3-650-E
              - 93.3-700-E
              - 93.3-750-E
              - 93.3-800-E
              - 90-200-O
              - 90-250-O
              - 90-300-O
              - 90-350-O
              - 90-400-O
              - 90-450-O
              - 90-500-O
              - 90-550-O
              - 90-600-O
              - 90-650-O
              - 90-700-O
              - 90-750-O
              - 90-800-O
              - 90-200-E
              - 90-250-E
              - 90-300-E
              - 90-350-E
              - 90-400-E
              - 90-450-E
              - 90-500-E
              - 90-550-E
              - 90-600-E
              - 90-650-E
              - 90-700-E
              - 90-750-E
              - 90-800-E
              - 85-200-O
              - 85-250-O
              - 85-300-O
              - 85-350-O
              - 85-400-O
              - 85-450-O
              - 85-500-O
              - 85-550-O
              - 85-600-O
              - 85-650-O
              - 85-700-O
              - 85-750-O
              - 85-800-O
              - 85-200-E
              - 85-250-E
              - 85-300-E
              - 85-350-E
              - 85-400-E
              - 85-450-E
              - 85-500-E
              - 85-550-E
              - 85-600-E
              - 85-650-E
              - 85-700-E
              - 85-750-E
              - 85-800-E
              - 82-200-O
              - 82-250-O
              - 82-300-O
              - 82-350-O
              - 82-400-O
              - 82-450-O
              - 82-500-O
              - 82-550-O
              - 82-600-O
              - 82-650-O
              - 82-700-O
              - 82-750-O
              - 82-800-O
              - 82-200-E
              - 82-250-E
              - 82-300-E
              - 82-350-E
              - 82-400-E
              - 82-450-E
              - 82-500-E
              - 82-550-E
              - 82-600-E
              - 82-650-E
              - 82-700-E
              - 82-750-E
              - 82-800-E
            description: Mode of the XCVR.
            required: true
            type: str
        type: dict
      state:
        description: State information of this XCVR instance.
        suboptions:
          admin_state:
            choices:
              - disabled
              - enabled
            description:
              Whether Admin State is enabled or disabled for this XCVR's
              PTP.
            required: true
            type: str
        type: dict
      xcvr_id:
        description:
          Unique, access identifier string of the XCVR (e.g. '1-1').
          Key value for the XCVR List.
        required: true
        type: str
    type: list
  state:
    choices:
      - gathered
      - merged
      - overridden
    default: merged
    description:
      - The state the configuration should be left in
    type: str
"""
EXAMPLES = """
# Using merged

- name: Configure xcvr
  ciena.waveserver5.waveserver5_xcvr:
    config:
      host-name:
        config-host-name: foo
    state: merged


# Using overridden

- name: Configure Transceiver enable
  ciena.waveserver5.waveserver5_xcvr:
    config:
      host-name:
        config-host-name: foo
    state: overridden


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
xml:
  description: The set of xml commands pushed to the remote device.
  returned: always
  type: list
  sample: ['<system xmlns="http://openconfig.net/yang/system"><config><hostname>foo</hostname></config></system>']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ciena.waveserver5.plugins.module_utils.network.waveserver5.argspec.xcvrs.xcvrs import (
    XcvrsArgs,
)
from ansible_collections.ciena.waveserver5.plugins.module_utils.network.waveserver5.config.xcvrs.xcvrs import (
    Xcvrs,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=XcvrsArgs.argument_spec, supports_check_mode=True)

    result = Xcvrs(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()

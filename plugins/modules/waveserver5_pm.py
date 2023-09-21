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
The module file for waveserver5_pm
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {"metadata_version": "1.1", "status": ["preview"], "supported_by": "network"}

DOCUMENTATION = """
---
module: waveserver5_pm
version_added: 0.0.1
short_description: Waveserver System configuration data and operational data.
description: Waveserver System configuration data and operational data.
author:
  - Jeff Groom (@jgroom33)
  - Galo Ertola (@perrary)
requirements:
  - ncclient (>=v0.6.4)
  - xmltodict (>=0.12.0)
options:
  config:
    description: Waveserver performance monitoring configuration and operational data.
    type: dict
    suboptions:
      encryption_gcm_performance_instances:
        description: Channel Encryption-GCM PM instances.
        elements: dict
        suboptions:
          instance_name:
            description: Unique name for PM instance.
            required: true
            type: str
          properties:
            description: PM instance properties.
            suboptions:
              tca_profile_15_min:
                description: TCA profile name that is attached to the current 15 minute
                  bin
                required: true
                type: str
              tca_profile_24_hr:
                description: TCA profile name that is attached to the current 24 hour
                  bin
                required: true
                type: str
              tca_profile_untimed:
                description: TCA profile name that is attached to the untimed bin
                required: true
                type: str
            type: dict
          state:
            description: PM instance state.
            suboptions:
              admin_state:
                choices:
                  - disabled
                  - enabled
                description: The configured administrative state of the port.
                required: true
                type: str
              tca_admin_state:
                choices:
                  - disabled
                  - enabled
                description: The configured TCA administrative state for this PM instance.
                required: true
                type: str
            type: dict
        type: list
      ethernet_performance_instances:
        description: Ethernet port PM instances.
        elements: dict
        suboptions:
          instance_name:
            description: Unique name for PM instance.
            required: true
            type: str
          properties:
            description: PM instance properties.
            suboptions:
              tca_profile_15_min:
                description: TCA profile name that is attached to the current 15 minute
                  bin
                required: true
                type: str
              tca_profile_24_hr:
                description: TCA profile name that is attached to the current 24 hour
                  bin
                required: true
                type: str
              tca_profile_untimed:
                description: TCA profile name that is attached to the untimed bin
                required: true
                type: str
            type: dict
          state:
            description: PM instance state.
            suboptions:
              admin_state:
                choices:
                  - disabled
                  - enabled
                description: The configured administrative state of the port.
                required: true
                type: str
              tca_admin_state:
                choices:
                  - disabled
                  - enabled
                description: The configured TCA administrative state for this PM instance.
                required: true
                type: str
            type: dict
        type: list
      global_config:
        description: Performance monitoring global configuration on the Waveserver.
        suboptions:
          admin_state:
            choices:
              - disabled
              - enabled
            description: Global admin state.
            required: true
            type: str
          tca_admin_state:
            choices:
              - disabled
              - enabled
            description: Global TCA administrative state.
            required: true
            type: str
          tca_notification_type:
            choices:
              - summary-event
              - summary-alarm
              - event
              - alarm
            description: Global TCA notification type.
            required: true
            type: str
          untimed_read_and_clear:
            choices:
              - disabled
              - enabled
            description: Global configuration for clearing untimed bin stats on a
              get request.
            required: true
            type: str
        type: dict
      modem_performance_instances:
        description: PTP Modem PM instances.
        elements: dict
        suboptions:
          instance_name:
            description: Unique name for PM instance.
            required: true
            type: str
          properties:
            description: PM instance properties.
            suboptions:
              tca_profile_15_min:
                description: TCA profile name that is attached to the current 15 minute
                  bin
                required: true
                type: str
              tca_profile_24_hr:
                description: TCA profile name that is attached to the current 24 hour
                  bin
                required: true
                type: str
              tca_profile_untimed:
                description: TCA profile name that is attached to the untimed bin
                required: true
                type: str
            type: dict
          state:
            description: PM instance state.
            suboptions:
              admin_state:
                choices:
                  - disabled
                  - enabled
                description: The configured administrative state of the port.
                required: true
                type: str
              tca_admin_state:
                choices:
                  - disabled
                  - enabled
                description: The configured TCA administrative state for this PM instance.
                required: true
                type: str
            type: dict
        type: list
      odu_performance_instances:
        description: Port/channel ODU PM instances.
        elements: dict
        suboptions:
          instance_name:
            description: Unique name for PM instance.
            required: true
            type: str
          properties:
            description: PM instance properties.
            suboptions:
              tca_profile_15_min:
                description: TCA profile name that is attached to the current 15 minute
                  bin
                required: true
                type: str
              tca_profile_24_hr:
                description: TCA profile name that is attached to the current 24 hour
                  bin
                required: true
                type: str
              tca_profile_untimed:
                description: TCA profile name that is attached to the untimed bin
                required: true
                type: str
            type: dict
          state:
            description: PM instance state.
            suboptions:
              admin_state:
                choices:
                  - disabled
                  - enabled
                description: The configured administrative state of the port.
                required: true
                type: str
              tca_admin_state:
                choices:
                  - disabled
                  - enabled
                description: The configured TCA administrative state for this PM instance.
                required: true
                type: str
            type: dict
        type: list
      optical_power_instances:
        description: PTP Optical Power PM instances.
        elements: dict
        suboptions:
          instance_name:
            description: Unique name for PM instance.
            required: true
            type: str
          properties:
            description: PM instance properties.
            suboptions:
              tca_profile_15_min:
                description: TCA profile name that is attached to the current 15 minute
                  bin
                required: true
                type: str
              tca_profile_24_hr:
                description: TCA profile name that is attached to the current 24 hour
                  bin
                required: true
                type: str
              tca_profile_untimed:
                description: TCA profile name that is attached to the untimed bin
                required: true
                type: str
            type: dict
          state:
            description: PM instance state.
            suboptions:
              admin_state:
                choices:
                  - disabled
                  - enabled
                description: The configured administrative state of the port.
                required: true
                type: str
              tca_admin_state:
                choices:
                  - disabled
                  - enabled
                description: The configured TCA administrative state for this PM instance.
                required: true
                type: str
            type: dict
        type: list
      otu_performance_instances:
        description: Port OTU PM instances.
        elements: dict
        suboptions:
          instance_name:
            description: Unique name for PM instance.
            required: true
            type: str
          properties:
            description: PM instance properties.
            suboptions:
              tca_profile_15_min:
                description: TCA profile name that is attached to the current 15 minute
                  bin
                required: true
                type: str
              tca_profile_24_hr:
                description: TCA profile name that is attached to the current 24 hour
                  bin
                required: true
                type: str
              tca_profile_untimed:
                description: TCA profile name that is attached to the untimed bin
                required: true
                type: str
            type: dict
          state:
            description: PM instance state.
            suboptions:
              admin_state:
                choices:
                  - disabled
                  - enabled
                description: The configured administrative state of the port.
                required: true
                type: str
              tca_admin_state:
                choices:
                  - disabled
                  - enabled
                description: The configured TCA administrative state for this PM instance.
                required: true
                type: str
            type: dict
        type: list
      photonics_instances:
        description: PTP Photonics PM instances.
        elements: dict
        suboptions:
          instance_name:
            description: Unique name for PM instance.
            required: true
            type: str
          properties:
            description: PM instance properties.
            suboptions:
              tca_profile_15_min:
                description: TCA profile name that is attached to the current 15 minute
                  bin
                required: true
                type: str
              tca_profile_24_hr:
                description: TCA profile name that is attached to the current 24 hour
                  bin
                required: true
                type: str
              tca_profile_untimed:
                description: TCA profile name that is attached to the untimed bin
                required: true
                type: str
            type: dict
          state:
            description: PM instance state.
            suboptions:
              admin_state:
                choices:
                  - disabled
                  - enabled
                description: The configured administrative state of the port.
                required: true
                type: str
              tca_admin_state:
                choices:
                  - disabled
                  - enabled
                description: The configured TCA administrative state for this PM instance.
                required: true
                type: str
            type: dict
        type: list
  state:
    choices:
      - merged
      - overridden
      - gathered
    default: merged
    description:
      - The state the configuration should be left in
    type: str
"""
EXAMPLES = """
# Using merged

- name: Configure pm
  ciena.waveserver5.waveserver5_pm:
    config:
      encryption_gcm_performance_instances:
        instance_name: foo
    state: merged


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
from ansible_collections.ciena.waveserver5.plugins.module_utils.network.waveserver5.argspec.pm.pm import (
    PmArgs,
)
from ansible_collections.ciena.waveserver5.plugins.module_utils.network.waveserver5.config.pm.pm import (
    Pm,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=PmArgs.argument_spec, supports_check_mode=True)

    result = Pm(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()

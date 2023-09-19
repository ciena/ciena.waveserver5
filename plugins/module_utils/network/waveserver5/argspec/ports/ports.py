#
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
The arg spec for the waveserver5_ports module
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type


class PortsArgs(object):  # pylint: disable=R0903
    """The arg spec for the waveserver5_ports module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "options": {
                "channels": {
                    "options": {
                        "channel_id": {"required": True, "type": "int"},
                        "id": {"options": {"label": {"required": True, "type": "str"}}, "type": "dict"},
                        "properties": {
                            "options": {
                                "odu_sd_threshold": {"required": True, "type": "str"},
                                "trace": {
                                    "options": {
                                        "exp_dapi": {"required": True, "type": "str"},
                                        "exp_oper": {"required": True, "type": "str"},
                                        "exp_sapi": {"required": True, "type": "str"},
                                        "mismatch_fail_mode": {
                                            "choices": ["none", "alarm-only", "squelch-traffic"],
                                            "required": True,
                                            "type": "str",
                                        },
                                        "mismatch_mode": {
                                            "choices": ["operator-only", "sapi", "dapi", "sapi-and-dapi"],
                                            "required": True,
                                            "type": "str",
                                        },
                                        "tx_dapi": {"required": True, "type": "str"},
                                        "tx_oper": {"required": True, "type": "str"},
                                        "tx_oper_mode": {
                                            "choices": ["manual", "automatic"],
                                            "required": True,
                                            "type": "str",
                                        },
                                        "tx_sapi": {"required": True, "type": "str"},
                                    },
                                    "type": "dict",
                                },
                            },
                            "type": "dict",
                        },
                        "state": {
                            "options": {
                                "admin_state": {"choices": ["disabled", "enabled"], "required": True, "type": "str"}
                            },
                            "type": "dict",
                        },
                    },
                    "type": "list",
                },
                "id": {
                    "options": {
                        "label": {"required": True, "type": "str"},
                        "type": {
                            "choices": ["unknown", "ethernet", "otn", "OTUk", "OTUCn", "OTUCn-Flex"],
                            "required": True,
                            "type": "str",
                        },
                    },
                    "type": "dict",
                },
                "port_id": {"required": True, "type": "str"},
                "properties": {
                    "options": {
                        "connection_peer": {"options": {"peer_id": {"required": True, "type": "str"}}, "type": "list"},
                        "connection_state": {"choices": ["disabled", "enabled"], "required": True, "type": "str"},
                        "ethernet": {
                            "options": {
                                "conditioning_holdoff": {"required": True, "type": "int"},
                                "conditioning_type": {
                                    "choices": ["none", "laser-off", "ethernet", "otn", "protocol-specific"],
                                    "required": True,
                                    "type": "str",
                                },
                            },
                            "type": "dict",
                        },
                        "loopback": {"choices": ["disabled", "rx", "tx"], "required": True, "type": "str"},
                        "otn": {
                            "options": {
                                "conditioning_type": {
                                    "choices": ["none", "laser-off", "ethernet", "otn", "protocol-specific"],
                                    "required": True,
                                    "type": "str",
                                },
                                "odu_sd_threshold": {"required": True, "type": "str"},
                                "odu_termination": {
                                    "choices": ["terminated", "passthrough"],
                                    "required": True,
                                    "type": "str",
                                },
                                "otu_sd_threshold": {"required": True, "type": "str"},
                                "trace": {
                                    "options": {
                                        "path": {
                                            "options": {
                                                "exp_dapi": {"required": True, "type": "str"},
                                                "exp_oper": {"required": True, "type": "str"},
                                                "exp_sapi": {"required": True, "type": "str"},
                                                "mismatch_fail_mode": {
                                                    "choices": ["none", "alarm-only", "squelch-traffic"],
                                                    "required": True,
                                                    "type": "str",
                                                },
                                                "mismatch_mode": {
                                                    "choices": ["operator-only", "sapi", "dapi", "sapi-and-dapi"],
                                                    "required": True,
                                                    "type": "str",
                                                },
                                                "tx_dapi": {"required": True, "type": "str"},
                                                "tx_oper": {"required": True, "type": "str"},
                                                "tx_oper_mode": {
                                                    "choices": ["manual", "automatic"],
                                                    "required": True,
                                                    "type": "str",
                                                },
                                                "tx_sapi": {"required": True, "type": "str"},
                                            },
                                            "type": "dict",
                                        },
                                        "section": {
                                            "options": {
                                                "exp_dapi": {"required": True, "type": "str"},
                                                "exp_oper": {"required": True, "type": "str"},
                                                "exp_sapi": {"required": True, "type": "str"},
                                                "mismatch_fail_mode": {
                                                    "choices": ["none", "alarm-only", "squelch-traffic"],
                                                    "required": True,
                                                    "type": "str",
                                                },
                                                "mismatch_mode": {
                                                    "choices": ["operator-only", "sapi", "dapi", "sapi-and-dapi"],
                                                    "required": True,
                                                    "type": "str",
                                                },
                                                "tx_dapi": {"required": True, "type": "str"},
                                                "tx_oper": {"required": True, "type": "str"},
                                                "tx_oper_mode": {
                                                    "choices": ["manual", "automatic"],
                                                    "required": True,
                                                    "type": "str",
                                                },
                                                "tx_sapi": {"required": True, "type": "str"},
                                            },
                                            "type": "dict",
                                        },
                                    },
                                    "type": "dict",
                                },
                            },
                            "type": "dict",
                        },
                    },
                    "type": "dict",
                },
                "state": {
                    "options": {"admin_state": {"choices": ["enabled", "disabled"], "required": True, "type": "str"}},
                    "type": "dict",
                },
            },
            "type": "list",
        },
        "state": {"choices": ["gathered", "merged", "overridden"], "default": "merged", "type": "str"},
    }  # pylint: disable=C0301
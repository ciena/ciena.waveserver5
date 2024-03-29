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
            "type": "list",
            "elements": "dict",
            "options": {
                "port_id": {"type": "str"},
                "id": {
                    "type": "dict",
                    "options": {
                        "type": {
                            "type": "str",
                            "choices": ["unknown", "ethernet", "otn", "OTUk", "OTUCn", "OTUCn-Flex"],
                        },
                        "label": {"type": "str"},
                    },
                },
                "state": {
                    "type": "dict",
                    "options": {"admin_state": {"type": "str", "choices": ["enabled", "disabled"]}},
                },
                "properties": {
                    "type": "dict",
                    "options": {
                        "loopback": {"type": "str", "choices": ["disabled", "rx", "tx"]},
                        "connection_state": {"type": "str", "choices": ["disabled", "enabled"]},
                        "connection_peer": {
                            "type": "list",
                            "elements": "dict",
                            "options": {"peer_id": {"type": "str"}},
                        },
                        "ethernet": {
                            "type": "dict",
                            "options": {
                                "conditioning_type": {
                                    "type": "str",
                                    "choices": ["none", "laser-off", "ethernet", "otn", "protocol-specific"],
                                },
                                "conditioning_holdoff": {"type": "int"},
                            },
                        },
                        "otn": {
                            "type": "dict",
                            "options": {
                                "odu_termination": {"type": "str", "choices": ["terminated", "passthrough"]},
                                "otu_sd_threshold": {"type": "str"},
                                "odu_sd_threshold": {"type": "str"},
                                "conditioning_type": {
                                    "type": "str",
                                    "choices": ["none", "laser-off", "ethernet", "otn", "protocol-specific"],
                                },
                                "trace": {
                                    "type": "dict",
                                    "options": {
                                        "section": {
                                            "type": "dict",
                                            "options": {
                                                "mismatch_mode": {
                                                    "type": "str",
                                                    "choices": ["operator-only", "sapi", "dapi", "sapi-and-dapi"],
                                                },
                                                "mismatch_fail_mode": {
                                                    "type": "str",
                                                    "choices": ["none", "alarm-only", "squelch-traffic"],
                                                },
                                                "tx_sapi": {"type": "str"},
                                                "tx_dapi": {"type": "str"},
                                                "tx_oper": {"type": "str"},
                                                "tx_oper_mode": {"type": "str", "choices": ["manual", "automatic"]},
                                                "exp_sapi": {"type": "str"},
                                                "exp_dapi": {"type": "str"},
                                                "exp_oper": {"type": "str"},
                                            },
                                        },
                                        "path": {
                                            "type": "dict",
                                            "options": {
                                                "mismatch_mode": {
                                                    "type": "str",
                                                    "choices": ["operator-only", "sapi", "dapi", "sapi-and-dapi"],
                                                },
                                                "mismatch_fail_mode": {
                                                    "type": "str",
                                                    "choices": ["none", "alarm-only", "squelch-traffic"],
                                                },
                                                "tx_sapi": {"type": "str"},
                                                "tx_dapi": {"type": "str"},
                                                "tx_oper": {"type": "str"},
                                                "tx_oper_mode": {"type": "str", "choices": ["manual", "automatic"]},
                                                "exp_sapi": {"type": "str"},
                                                "exp_dapi": {"type": "str"},
                                                "exp_oper": {"type": "str"},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
                "channels": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "channel_id": {"type": "int"},
                        "id": {"type": "dict", "options": {"label": {"type": "str"}}},
                        "state": {
                            "type": "dict",
                            "options": {"admin_state": {"type": "str", "choices": ["disabled", "enabled"]}},
                        },
                        "properties": {
                            "type": "dict",
                            "options": {
                                "odu_sd_threshold": {"type": "str"},
                                "trace": {
                                    "type": "dict",
                                    "options": {
                                        "mismatch_mode": {
                                            "type": "str",
                                            "choices": ["operator-only", "sapi", "dapi", "sapi-and-dapi"],
                                        },
                                        "mismatch_fail_mode": {
                                            "type": "str",
                                            "choices": ["none", "alarm-only", "squelch-traffic"],
                                        },
                                        "tx_sapi": {"type": "str"},
                                        "tx_dapi": {"type": "str"},
                                        "tx_oper": {"type": "str"},
                                        "tx_oper_mode": {"type": "str", "choices": ["manual", "automatic"]},
                                        "exp_sapi": {"type": "str"},
                                        "exp_dapi": {"type": "str"},
                                        "exp_oper": {"type": "str"},
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        "state": {"type": "str", "default": "merged", "choices": ["gathered", "merged", "overridden"]},
    }  # pylint: disable=C0301

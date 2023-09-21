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
The arg spec for the waveserver5_ptps module
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type


class PtpsArgs(object):  # pylint: disable=R0903
    """The arg spec for the waveserver5_ptps module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "type": "list",
            "elements": "dict",
            "options": {
                "ptp_id": {"type": "str", "required": True},
                "state": {
                    "type": "dict",
                    "options": {
                        "admin_state": {"type": "str", "choices": ["disabled", "enabled"]},
                        "spli_management": {"type": "str", "choices": ["disabled", "enabled"]},
                    },
                },
                "properties": {
                    "type": "dict",
                    "options": {
                        "type": {
                            "type": "str",
                            "choices": [
                                "unknown",
                                "WLAi",
                                "WLAi-iOPS",
                                "4x25G",
                                "10G",
                                "OCH",
                                "OSC",
                                "OSC-Add-Drop",
                                "OTM",
                                "WL5e",
                                "WL5n",
                                "100G",
                                "4x100G",
                                "8x50G",
                                "2x50G",
                                "400ZR",
                            ],
                        },
                        "xcvr_type": {
                            "type": "str",
                            "choices": [
                                "not-available",
                                "unsupported",
                                "QSFPplus",
                                "QSFP28",
                                "WaveLogic 3 Extreme",
                                "WaveLogic Ai",
                                "SFP",
                                "none",
                                "QSFP-DD",
                                "WaveLogic 5e",
                            ],
                        },
                        "is_coherent": {"type": "bool"},
                        "forward_error_correction": {"type": "str", "choices": ["disabled", "enabled"]},
                        "thresholds": {
                            "type": "dict",
                            "options": {
                                "pre_fec_sf_db": {"type": "float"},
                                "pre_fec_sd_db": {"type": "float"},
                                "hccs_db": {"type": "float"},
                            },
                        },
                        "transmitter": {
                            "type": "dict",
                            "options": {"state": {"type": "str", "choices": ["disabled", "enabled", "not-applicable"]}},
                        },
                    },
                },
            },
        },
        "state": {"type": "str", "default": "merged", "choices": ["gathered", "merged", "overridden"]},
    }  # pylint: disable=C0301

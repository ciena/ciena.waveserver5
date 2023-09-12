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
The arg spec for the waveserver5_system module
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type


class SystemArgs(object):  # pylint: disable=R0903
    """The arg spec for the waveserver5_system module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "options": {
                "host_name": {"options": {"config_host_name": {"required": True, "type": "str"}}, "type": "dict"}
            },
            "type": "dict",
        },
        "state": {"choices": ["merged", "overridden", "gathered"], "default": "merged", "type": "str"},
    }  # pylint: disable=C0301

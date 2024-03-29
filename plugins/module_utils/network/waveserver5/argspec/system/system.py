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
            "type": "dict",
            "options": {
                "id": {
                    "type": "dict",
                    "options": {
                        "network": {
                            "type": "dict",
                            "options": {"description": {"type": "str"}, "id": {"type": "int"}, "name": {"type": "str"}},
                        },
                        "site": {
                            "type": "dict",
                            "options": {
                                "description": {"type": "str"},
                                "id": {"type": "int"},
                                "name": {"type": "str"},
                                "latitude": {"type": "float"},
                                "longitude": {"type": "float"},
                                "address": {"type": "str"},
                            },
                        },
                        "group": {
                            "type": "dict",
                            "options": {"description": {"type": "str"}, "id": {"type": "int"}, "name": {"type": "str"}},
                        },
                        "member": {
                            "type": "dict",
                            "options": {
                                "description": {"type": "str"},
                                "id": {"type": "int"},
                                "name": {"type": "str"},
                                "frame_identification": {"type": "str"},
                                "rack_unit_number": {"type": "int"},
                                "cluster_enrollment": {"type": "str", "choices": ["disabled", "enabled"]},
                            },
                        },
                    },
                },
                "host_name": {"type": "dict", "options": {"config_host_name": {"type": "str"}}},
                "domain_name": {"type": "dict", "options": {"config_domain_name": {"type": "str"}}},
                "time_config": {
                    "type": "dict",
                    "options": {
                        "time_offset": {"type": "int"},
                        "time_stamp": {"type": "str", "choices": ["utc", "local"]},
                    },
                },
                "server_config": {
                    "type": "dict",
                    "options": {
                        "sftp_server_state": {"type": "str", "choices": ["disabled", "enabled"]},
                        "scp_server_state": {"type": "str", "choices": ["disabled", "enabled"]},
                        "netconf_server_state": {"type": "str", "choices": ["disabled", "enabled"]},
                        "global_inactivity_timer": {"type": "str", "choices": ["disabled", "enabled"]},
                        "global_inactivity_timeout": {"type": "int"},
                        "https": {
                            "type": "dict",
                            "options": {
                                "admin_state": {"type": "str", "choices": ["disabled", "enabled"]},
                                "web_ui_file_transfer_admin_state": {"type": "str", "choices": ["disabled", "enabled"]},
                                "inactivity_timeout": {"type": "int"},
                                "certificate_verification": {
                                    "type": "dict",
                                    "options": {
                                        "certificate_name": {"type": "str"},
                                        "trusted_dns": {"type": "str"},
                                        "mutual_authentication": {
                                            "type": "dict",
                                            "options": {
                                                "admin_state": {"type": "str", "choices": ["disabled", "enabled"]}
                                            },
                                        },
                                        "ocsp": {
                                            "type": "dict",
                                            "options": {
                                                "admin_state": {"type": "str", "choices": ["disabled", "enabled"]},
                                                "responder_preference": {
                                                    "type": "str",
                                                    "choices": ["aia", "default-responder"],
                                                },
                                                "default_responder": {"type": "str"},
                                                "nonce": {"type": "str", "choices": ["off", "on"]},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        "grpc": {
                            "type": "dict",
                            "options": {
                                "admin_state": {"type": "str", "choices": ["disabled", "enabled"]},
                                "certificate_verification": {
                                    "type": "dict",
                                    "options": {
                                        "certificate_name": {"type": "str"},
                                        "mutual_authentication": {
                                            "type": "dict",
                                            "options": {
                                                "admin_state": {"type": "str", "choices": ["disabled", "enabled"]}
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        "ssh": {
                            "type": "dict",
                            "options": {
                                "authentication_retries": {"type": "int"},
                                "listener_port": {"type": "int"},
                                "allowed_clients": {
                                    "type": "list",
                                    "elements": "dict",
                                    "options": {"ip_address": {"type": "str"}},
                                },
                                "algorithms": {
                                    "type": "dict",
                                    "options": {
                                        "key_exchange": {
                                            "type": "list",
                                            "elements": "dict",
                                            "no_log": True,
                                            "options": {
                                                "algorithm_name": {"type": "str"},
                                                "admin_state": {"type": "str", "choices": ["disabled", "enabled"]},
                                            },
                                        },
                                        "encryption": {
                                            "type": "list",
                                            "elements": "dict",
                                            "options": {
                                                "algorithm_name": {"type": "str"},
                                                "admin_state": {"type": "str", "choices": ["disabled", "enabled"]},
                                            },
                                        },
                                        "message_authentication_code": {
                                            "type": "list",
                                            "elements": "dict",
                                            "options": {
                                                "algorithm_name": {"type": "str"},
                                                "admin_state": {"type": "str", "choices": ["disabled", "enabled"]},
                                            },
                                        },
                                        "public_key_authentication": {
                                            "type": "list",
                                            "elements": "dict",
                                            "options": {
                                                "algorithm_name": {"type": "str"},
                                                "admin_state": {"type": "str", "choices": ["disabled", "enabled"]},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
                "client_config": {
                    "type": "dict",
                    "options": {
                        "dhcp": {
                            "type": "dict",
                            "options": {
                                "admin_state": {"type": "str", "choices": ["disabled", "enabled"]},
                                "interface_type": {"type": "str", "choices": ["remote", "active"]},
                                "discovery_interval": {"type": "int"},
                                "requested_lease_time": {"type": "int"},
                                "options": {
                                    "type": "dict",
                                    "options": {
                                        "subnet_mask": {"type": "bool"},
                                        "time_offset": {"type": "bool"},
                                        "router": {"type": "bool"},
                                        "domain_server": {"type": "bool"},
                                        "log_server": {"type": "bool"},
                                        "host_name": {"type": "bool"},
                                        "domain_name": {"type": "bool"},
                                        "ntp_servers": {"type": "bool"},
                                        "lease_time": {"type": "bool"},
                                        "tftp_server_name": {"type": "bool"},
                                        "bootfile_name": {"type": "bool"},
                                    },
                                },
                            },
                        },
                        "ntp": {
                            "type": "dict",
                            "options": {
                                "admin_state": {"type": "str", "choices": ["disabled", "enabled"]},
                                "authentication_state": {"type": "str", "choices": ["disabled", "enabled"]},
                                "autokey_authentication_state": {"type": "str", "choices": ["disabled", "enabled"]},
                                "mode": {"type": "str", "choices": ["polling", "broadcast", "multicast"]},
                                "polling_interval": {"type": "int"},
                                "ntp_key": {
                                    "type": "list",
                                    "elements": "dict",
                                    "no_log": True,
                                    "options": {
                                        "key_id": {"type": "int", "required": True},
                                        "key_value": {"type": "str", "no_log": True},
                                    },
                                },
                                "server": {
                                    "type": "list",
                                    "elements": "dict",
                                    "options": {
                                        "address": {"type": "str", "required": True},
                                        "autokey_authentication": {"type": "str", "choices": ["disabled", "enabled"]},
                                        "admin_state": {"type": "str", "choices": ["disabled", "enabled"]},
                                        "key_id": {"type": "str"},
                                    },
                                },
                                "multicast_server": {
                                    "type": "list",
                                    "elements": "dict",
                                    "options": {"ip_address": {"type": "str"}},
                                },
                            },
                        },
                        "dns": {
                            "type": "dict",
                            "options": {
                                "admin_state": {"type": "str", "choices": ["disabled", "enabled"]},
                                "server": {
                                    "type": "list",
                                    "elements": "dict",
                                    "options": {
                                        "ip_address": {"type": "str"},
                                        "admin_state": {"type": "str", "choices": ["disabled", "enabled"]},
                                        "user_priority": {"type": "int"},
                                    },
                                },
                            },
                        },
                    },
                },
                "xftp_config": {
                    "type": "dict",
                    "options": {
                        "mode": {"type": "str", "choices": ["none", "tftp", "ftp", "sftp", "scp"]},
                        "tftp": {"type": "dict", "options": {"config_host_name": {"type": "str"}}},
                        "ftp": {
                            "type": "dict",
                            "options": {
                                "host_name": {"type": "str"},
                                "user_name": {"type": "str"},
                                "password": {"type": "str", "no_log": True},
                                "secret": {"type": "str", "no_log": True},
                            },
                        },
                        "sftp": {
                            "type": "dict",
                            "options": {
                                "host_name": {"type": "str"},
                                "user_name": {"type": "str"},
                                "password": {"type": "str", "no_log": True},
                                "secret": {"type": "str", "no_log": True},
                            },
                        },
                        "scp": {
                            "type": "dict",
                            "options": {
                                "host_name": {"type": "str"},
                                "user_name": {"type": "str"},
                                "password": {"type": "str", "no_log": True},
                                "secret": {"type": "str", "no_log": True},
                            },
                        },
                    },
                },
                "global_provisioning": {
                    "type": "dict",
                    "options": {
                        "line_config": {
                            "type": "dict",
                            "options": {"line_protection": {"type": "str", "choices": ["unprotected", "trunk-ops"]}},
                        }
                    },
                },
                "lamp_test": {
                    "type": "dict",
                    "options": {
                        "admin_state": {"type": "str", "choices": ["disabled", "enabled"]},
                        "target_type": {"type": "str", "choices": ["chassis", "slot", "port"]},
                        "target_id": {"type": "str"},
                        "timeout": {"type": "int"},
                    },
                },
                "management": {
                    "type": "dict",
                    "options": {
                        "query_limits": {
                            "type": "dict",
                            "options": {
                                "netconf": {"type": "dict", "options": {"pm_history_bins": {"type": "int"}}},
                                "rest": {"type": "dict", "options": {"pm_history_bins": {"type": "int"}}},
                                "gnmi": {"type": "dict", "options": {"pm_history_bins": {"type": "int"}}},
                            },
                        },
                        "root_scope": {
                            "type": "dict",
                            "options": {
                                "netconf": {
                                    "type": "dict",
                                    "options": {
                                        "get": {"type": "str", "choices": ["native", "openconfig", "all"]},
                                        "replace": {"type": "str", "choices": ["native", "openconfig", "all"]},
                                    },
                                },
                                "rest": {
                                    "type": "dict",
                                    "options": {
                                        "get": {"type": "str", "choices": ["native", "openconfig", "all"]},
                                        "replace": {"type": "str", "choices": ["native", "openconfig", "all"]},
                                    },
                                },
                                "gnmi": {
                                    "type": "dict",
                                    "options": {
                                        "get": {"type": "str", "choices": ["native", "openconfig", "all"]},
                                        "replace": {"type": "str", "choices": ["native", "openconfig", "all"]},
                                    },
                                },
                            },
                        },
                    },
                },
                "environment": {
                    "type": "dict",
                    "options": {
                        "root": {
                            "type": "dict",
                            "options": {
                                "password": {"type": "str", "no_log": True},
                                "secret": {"type": "str", "no_log": True},
                            },
                        },
                        "diag": {
                            "type": "dict",
                            "options": {
                                "shell": {"type": "str", "choices": ["cli", "system"]},
                                "sudo": {"type": "bool"},
                            },
                        },
                    },
                },
                "auto_config_recovery": {
                    "type": "dict",
                    "options": {
                        "config_mismatch_detection_state": {"type": "str", "choices": ["disabled", "enabled"]},
                        "admin_state": {"type": "str", "choices": ["disabled", "enabled"]},
                        "passphrase": {"type": "str", "no_log": True},
                        "audit_interval": {"type": "int"},
                    },
                },
                "ssl": {
                    "type": "dict",
                    "options": {
                        "tls_cipher_suite_algorithms": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "algorithm_name": {"type": "str"},
                                "admin_state": {"type": "str", "choices": ["disabled", "enabled"]},
                            },
                        }
                    },
                },
                "shell": {
                    "type": "dict",
                    "options": {
                        "more": {"type": "str", "choices": ["disabled", "enabled"]},
                        "more_lines": {"type": "int"},
                        "login_authentication_message": {"type": "str", "choices": ["disabled", "enabled"]},
                        "login_banner_file": {"type": "str"},
                        "welcome_banner_file": {"type": "str"},
                    },
                },
                "default_settings": {
                    "type": "dict",
                    "options": {
                        "conditioning": {
                            "type": "dict",
                            "options": {
                                "type": {
                                    "type": "str",
                                    "choices": ["none", "laser-off", "ethernet", "otn", "protocol-specific"],
                                },
                                "holdoff": {"type": "int"},
                            },
                        },
                        "terrestrial_reach_limit": {"type": "int"},
                    },
                },
            },
        },
        "state": {"type": "str", "default": "merged", "choices": ["merged", "overridden", "gathered"]},
    }  # pylint: disable=C0301

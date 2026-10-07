# Ciena Waveserver5 Collection for Ansible

[![CI](https://github.com/ciena/ciena.waveserver5/workflows/Test%20collection/badge.svg?event=push)](https://github.com/ciena/ciena.waveserver5/actions)
The Ansible Ciena Waveserver 5 collection includes a variety of Ansible content to help automate the management of Ciena Waveserver 5 network appliances.

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.12.0**.

For collections that support Ansible 2.9, please ensure you update your `network_os` to use the
fully qualified collection name (for example, `cisco.ios.ios`).
Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.
<!--end requires_ansible-->

### Supported connections

The Ciena Waveserver5 collection supports `netconf` connections.

## Included content

<!--start collection content-->
### Netconf plugins
Name | Description
--- | ---
[ciena.waveserver5.waveserver5](https://github.com/ciena/ciena.waveserver5/blob/master/docs/ciena.waveserver5.waveserver5_netconf.rst)|Use ciena netconf plugin to run netconf commands on Ciena Waveserver5 platform

### Modules
Name | Description
--- | ---
[ciena.waveserver5.waveserver5_aaa](https://github.com/ciena/ciena.waveserver5/blob/master/docs/ciena.waveserver5.waveserver5_aaa_module.rst)|Waveserver AAA configuration data and operational data.
[ciena.waveserver5.waveserver5_facts](https://github.com/ciena/ciena.waveserver5/blob/master/docs/ciena.waveserver5.waveserver5_facts_module.rst)|Get facts about waveserver5 devices.
[ciena.waveserver5.waveserver5_inventory](https://github.com/ciena/ciena.waveserver5/blob/master/docs/ciena.waveserver5.waveserver5_inventory_module.rst)|Gather chassis and component inventory from Waveserver 5.
[ciena.waveserver5.waveserver5_pm](https://github.com/ciena/ciena.waveserver5/blob/master/docs/ciena.waveserver5.waveserver5_pm_module.rst)|Waveserver System configuration data and operational data.
[ciena.waveserver5.waveserver5_ports](https://github.com/ciena/ciena.waveserver5/blob/master/docs/ciena.waveserver5.waveserver5_ports_module.rst)|Waveserver Port configuration data and operational data.
[ciena.waveserver5.waveserver5_ptps](https://github.com/ciena/ciena.waveserver5/blob/master/docs/ciena.waveserver5.waveserver5_ptps_module.rst)|Waveserver PTP configuration data and operational data.
[ciena.waveserver5.waveserver5_system](https://github.com/ciena/ciena.waveserver5/blob/master/docs/ciena.waveserver5.waveserver5_system_module.rst)|Waveserver System configuration data and operational data.
[ciena.waveserver5.waveserver5_xcvrs](https://github.com/ciena/ciena.waveserver5/blob/master/docs/ciena.waveserver5.waveserver5_xcvrs_module.rst)|Waveserver Transceiver configuration data and operational data.

<!--end collection content-->

## Installing this collection

Install the Ciena Waveserver 5 collection with the Ansible Galaxy CLI:

```bash
ansible-galaxy collection install ciena.waveserver5
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: ciena.waveserver5
```

## Using this collection

The collection communicates with Waveserver 5 over NETCONF; it does not execute device CLI commands. Resource reads use NETCONF `get` operations, and configuration changes use `edit-config` against the running configuration.

### Connection setup

Install the collection and its declared `ansible.netcommon` dependency:

```bash
ansible-galaxy collection install ciena.waveserver5
```

Configure the device in inventory. Keep credentials in Ansible Vault instead of clear text:

```yaml
all:
  hosts:
    waveserver5:
      ansible_host: 192.0.2.10
      ansible_port: 830
      ansible_user: automation
      ansible_password: "{{ vault_waveserver5_password }}"
      ansible_connection: ansible.netcommon.netconf
      ansible_network_os: ciena.waveserver5.waveserver5
```

The collection is tested with Ansible 2.12 or newer. The controller also needs the `ncclient` Python package required by the NETCONF modules.

### Supported modules and data models

The table summarizes the resource models implemented by this collection. Each module reference documents its full nested schema, field types, accepted values, examples, and return data.

| FQCN | Supported model/data | Module reference |
| --- | --- | --- |
| `ciena.waveserver5.waveserver5_facts` | Base device facts and selectable legacy and network-resource subsets. | [Facts](docs/ciena.waveserver5.waveserver5_facts_module.rst) |
| `ciena.waveserver5.waveserver5_inventory` | Read-only chassis and installed-component inventory from OpenConfig platform components. | [Inventory](docs/ciena.waveserver5.waveserver5_inventory_module.rst) |
| `ciena.waveserver5.waveserver5_aaa` | Authentication methods and users; TACACS+, RADIUS, and RADSec configuration and servers. | [AAA](docs/ciena.waveserver5.waveserver5_aaa_module.rst) |
| `ciena.waveserver5.waveserver5_pm` | Global performance-monitoring configuration, PM instances, and threshold-crossing alert settings. | [PM](docs/ciena.waveserver5.waveserver5_pm_module.rst) |
| `ciena.waveserver5.waveserver5_ports` | Port identity and state, Ethernet/OTN properties, connection peers, and channels. | [Ports](docs/ciena.waveserver5.waveserver5_ports_module.rst) |
| `ciena.waveserver5.waveserver5_ptps` | PTP identity and state; type, transceiver, FEC, thresholds, and transmitter properties. | [PTPs](docs/ciena.waveserver5.waveserver5_ptps_module.rst) |
| `ciena.waveserver5.waveserver5_system` | Device/network/site/member identity, hostname, time, management services, and system settings. | [System](docs/ciena.waveserver5.waveserver5_system_module.rst) |
| `ciena.waveserver5.waveserver5_xcvrs` | Transceiver identity and state, operating mode, and supported transceiver properties. | [XCVRs](docs/ciena.waveserver5.waveserver5_xcvrs_module.rst) |

The facts module accepts `gather_network_resources` values `aaa`, `inventory`, `pm`, `ports`, `ptps`, `system`, and `xcvrs`; `all` gathers every supported resource subset. Base facts include model, serial number, software version, platform, and hostname. `gather_subset` controls the legacy `default` and `config` subsets. For a direct inventory read, use `ciena.waveserver5.waveserver5_inventory` with `state: gathered`; the facts subset remains available when collecting inventory together with other network facts.

This is the collection's supported model coverage, not an exhaustive implementation of every Waveserver 5 YANG model or RPC. In particular, inventory returns the platform component data exposed by the device.

### Gather facts and show current data

Gather chassis inventory and ports with the facts module:

```yaml
- name: Gather chassis inventory and ports
  ciena.waveserver5.waveserver5_facts:
    gather_network_resources:
      - inventory
      - ports
  register: waveserver_data

- name: Display chassis components
  ansible.builtin.debug:
    var: waveserver_data.ansible_facts.ansible_network_resources.inventory

- name: Display ports
  ansible.builtin.debug:
    var: waveserver_data.ansible_facts.ansible_network_resources.ports
```

For a system-specific read, use the module with `state: gathered`. This is the collection equivalent of **system show**:

```yaml
- name: Show current system data
  ciena.waveserver5.waveserver5_system:
    state: gathered
  register: system_data

- ansible.builtin.debug:
    var: system_data.gathered
```

The system resource includes the fields defined by the [system model](docs/ciena.waveserver5.waveserver5_system_module.rst). Other resource modules use the same `gathered` pattern to return current data for their respective models.

### Configure a resource

Use `config` to provide fields from the module's model and `state: merged` to apply the supplied values while leaving unrelated settings unchanged. For example:

```yaml
- name: Disable a port
  ciena.waveserver5.waveserver5_ports:
    config:
      - port_id: 5-1
        state:
          admin_state: disabled
    state: merged
```

System configuration is nested under the module's `config` model:

```yaml
- name: Set the device hostname
  ciena.waveserver5.waveserver5_system:
    config:
      host_name:
        config_host_name: waveserver-a
    state: merged
```

Review each module reference for other advertised states and the exact impact of applying them before changing a device.

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please [open an issue](https://github.com/ciena/ciena.waveserver5/issues) or create a PR against the [Ciena SAOS 10 collection repository](https://github.com/ciena/ciena.waveserver5).

Release is done automatically using Github Actions as part of merging to master.

### Resource Module Builder

The modules in this project were built using the [resource module builder hosted by Ciena](https://github.com/ciena/resource_module_builder).

## Changelogs

[CHANGELOG](CHANGELOG.md)

## Licensing

See [LICENSE](LICENSE) to see the full text.


# Ciena Waveserver5 Collection for Ansible

<!-- Add CI and code coverage badges here. Samples included below. -->

[![CI](https://github.com/ciena/ciena.waveserver5/workflows/CI/badge.svg?event=push)](https://github.com/ciena/ciena.waveserver5/actions) [![Codecov](https://img.shields.io/codecov/c/github/ciena/ciena.waveserver5)](https://codecov.io/gh/ciena/ciena.waveserver5)

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
### Modules
Name | Description
--- | ---
[ciena.waveserver5.waveserver5_facts](https://github.com/ciena/ciena.waveserver5/blob/master/docs/ciena.waveserver5.waveserver5_facts_module.rst)|Get facts about waveserver5 devices.
[ciena.waveserver5.waveserver5_system](https://github.com/ciena/ciena.waveserver5/blob/master/docs/ciena.waveserver5.waveserver5_system_module.rst)|Waveserver System configuration data and operational data.

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

This collection includes [network resource modules](https://docs.ansible.com/ansible/latest/network/user_guide/network_resource_modules.html).

### Using modules from the Ciena Waveserver 5 collection in your playbooks

You can call modules by their Fully Qualified Collection Namespace (FQCN), such as `ciena.waveserver5.waveserver5_system`.
The following example task replaces configuration changes in the existing configuration on a Ciena Waveserver 5 network device, using the FQCN:

```yaml
---
- hosts: all
  collections:
    - ciena.waveserver5
  gather_facts: false
  name: Gather facts for ciena device Saos 10
  tasks:
    - name: get device facts for Saos 10
      ciena.waveserver5.waveserver5_facts:
        gather_subset:
          - all
      connection: netconf
    - name: Configure system hostname
      ciena.waveserver5.waveserver5_system:
        config:
          config:
            hostname: foo
        state: merged
```

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please [open an issue](https://github.com/ciena/ciena.waveserver5/issues) or create a PR against the [Ciena SAOS 10 collection repository](https://github.com/ciena/ciena.waveserver5).

Release is done automatically using Github Actions as part of merging to master.

### Resource Module Builder

The modules in this project were built using the [resource module builder hosted by Ciena](https://github.com/ciena/resource_module_builder).

## Changelogs

[CHANGELOG](CHANGELOG.md)

## Licensing

See [LICENSE](LICENSE) to see the full text.

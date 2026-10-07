.. _ciena.waveserver5.waveserver5_inventory_module:


***************************************
ciena.waveserver5.waveserver5_inventory
***************************************

**Gather chassis and component inventory from Waveserver 5.**


Synopsis
--------
- Reads OpenConfig platform component inventory over NETCONF.
- This read-only module returns the chassis and installed components exposed by the device's platform model.


Parameters
----------

state
    The operation to perform. This module only gathers the current inventory.
    Choices: ``gathered``. Default: ``gathered``.


Examples
--------

.. code-block:: yaml

    - name: Gather chassis and component inventory
      ciena.waveserver5.waveserver5_inventory:
        state: gathered
      register: chassis_inventory

    - name: Display inventory
      ansible.builtin.debug:
        var: chassis_inventory.gathered


Return Values
-------------

gathered
    Chassis and platform component data returned by the device. A list of dictionaries;
    available component fields depend on the device's OpenConfig platform response.
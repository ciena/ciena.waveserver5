.. _ciena.waveserver5.waveserver5_xcvr_module:


**********************************
ciena.waveserver5.waveserver5_xcvr
**********************************

**Waveserver Transceiver configuration data and operational data.**


Version added: 1.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Waveserver Transceiver configuration data and operational data.



Requirements
------------
The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="3">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Waveserver transceiver (XCVR) list.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>properties</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>All the Configurable and operational data of this XCVR instance.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>blank</li>
                                    <li>OCH</li>
                                    <li>OTM</li>
                                    <li>OSC</li>
                                    <li>OSC-Add-Drop</li>
                                    <li>10GE</li>
                                    <li>4x10GE</li>
                                    <li>40GE</li>
                                    <li>100GE</li>
                                    <li>400GE</li>
                                    <li>4x100GE</li>
                                    <li>4x100GE-ZR</li>
                                    <li>OTL4.4</li>
                                    <li>OTLC.4</li>
                                    <li>FOIC1.4</li>
                                    <li>FOIC4.8</li>
                                    <li>35-100</li>
                                    <li>35-150</li>
                                    <li>35-200</li>
                                    <li>35-250</li>
                                    <li>56-100</li>
                                    <li>56-150</li>
                                    <li>56-200</li>
                                    <li>56-250</li>
                                    <li>56-300</li>
                                    <li>56-350</li>
                                    <li>56-400</li>
                                    <li>95-200-O</li>
                                    <li>95-250-O</li>
                                    <li>95-300-O</li>
                                    <li>95-350-O</li>
                                    <li>95-400-O</li>
                                    <li>95-450-O</li>
                                    <li>95-500-O</li>
                                    <li>95-550-O</li>
                                    <li>95-600-O</li>
                                    <li>95-650-O</li>
                                    <li>95-700-O</li>
                                    <li>95-750-O</li>
                                    <li>95-800-O</li>
                                    <li>95-200-E</li>
                                    <li>95-250-E</li>
                                    <li>95-300-E</li>
                                    <li>95-350-E</li>
                                    <li>95-400-E</li>
                                    <li>95-450-E</li>
                                    <li>95-500-E</li>
                                    <li>95-550-E</li>
                                    <li>95-600-E</li>
                                    <li>95-650-E</li>
                                    <li>95-700-E</li>
                                    <li>95-750-E</li>
                                    <li>95-800-E</li>
                                    <li>91.6-200-O</li>
                                    <li>91.6-250-O</li>
                                    <li>91.6-300-O</li>
                                    <li>91.6-350-O</li>
                                    <li>91.6-400-O</li>
                                    <li>91.6-450-O</li>
                                    <li>91.6-500-O</li>
                                    <li>91.6-550-O</li>
                                    <li>91.6-600-O</li>
                                    <li>91.6-650-O</li>
                                    <li>91.6-700-O</li>
                                    <li>91.6-750-O</li>
                                    <li>91.6-800-O</li>
                                    <li>91.6-200-E</li>
                                    <li>91.6-250-E</li>
                                    <li>91.6-300-E</li>
                                    <li>91.6-350-E</li>
                                    <li>91.6-400-E</li>
                                    <li>91.6-450-E</li>
                                    <li>91.6-500-E</li>
                                    <li>91.6-550-E</li>
                                    <li>91.6-600-E</li>
                                    <li>91.6-650-E</li>
                                    <li>91.6-700-E</li>
                                    <li>91.6-750-E</li>
                                    <li>91.6-800-E</li>
                                    <li>89.3-200-O</li>
                                    <li>89.3-250-O</li>
                                    <li>89.3-300-O</li>
                                    <li>89.3-350-O</li>
                                    <li>89.3-400-O</li>
                                    <li>89.3-450-O</li>
                                    <li>89.3-500-O</li>
                                    <li>89.3-550-O</li>
                                    <li>89.3-600-O</li>
                                    <li>89.3-650-O</li>
                                    <li>89.3-700-O</li>
                                    <li>89.3-750-O</li>
                                    <li>89.3-800-O</li>
                                    <li>89.3-200-E</li>
                                    <li>89.3-250-E</li>
                                    <li>89.3-300-E</li>
                                    <li>89.3-350-E</li>
                                    <li>89.3-400-E</li>
                                    <li>89.3-450-E</li>
                                    <li>89.3-500-E</li>
                                    <li>89.3-550-E</li>
                                    <li>89.3-600-E</li>
                                    <li>89.3-650-E</li>
                                    <li>89.3-700-E</li>
                                    <li>89.3-750-E</li>
                                    <li>89.3-800-E</li>
                                    <li>71.3-200-O</li>
                                    <li>71.3-250-O</li>
                                    <li>71.3-300-O</li>
                                    <li>71.3-350-O</li>
                                    <li>71.3-400-O</li>
                                    <li>71.3-450-O</li>
                                    <li>71.3-500-O</li>
                                    <li>71.3-550-O</li>
                                    <li>71.3-600-O</li>
                                    <li>71.3-200-E</li>
                                    <li>71.3-250-E</li>
                                    <li>71.3-300-E</li>
                                    <li>71.3-350-E</li>
                                    <li>71.3-400-E</li>
                                    <li>71.3-450-E</li>
                                    <li>71.3-500-E</li>
                                    <li>71.3-550-E</li>
                                    <li>71.3-600-E</li>
                                    <li>69.5-200-O</li>
                                    <li>69.5-250-O</li>
                                    <li>69.5-300-O</li>
                                    <li>69.5-350-O</li>
                                    <li>69.5-400-O</li>
                                    <li>69.5-450-O</li>
                                    <li>69.5-500-O</li>
                                    <li>69.5-550-O</li>
                                    <li>69.5-600-O</li>
                                    <li>69.5-200-E</li>
                                    <li>69.5-250-E</li>
                                    <li>69.5-300-E</li>
                                    <li>69.5-350-E</li>
                                    <li>69.5-400-E</li>
                                    <li>69.5-450-E</li>
                                    <li>69.5-500-E</li>
                                    <li>69.5-550-E</li>
                                    <li>69.5-600-E</li>
                                    <li>93.3-200-O</li>
                                    <li>93.3-250-O</li>
                                    <li>93.3-300-O</li>
                                    <li>93.3-350-O</li>
                                    <li>93.3-400-O</li>
                                    <li>93.3-450-O</li>
                                    <li>93.3-500-O</li>
                                    <li>93.3-550-O</li>
                                    <li>93.3-600-O</li>
                                    <li>93.3-650-O</li>
                                    <li>93.3-700-O</li>
                                    <li>93.3-750-O</li>
                                    <li>93.3-800-O</li>
                                    <li>93.3-200-E</li>
                                    <li>93.3-250-E</li>
                                    <li>93.3-300-E</li>
                                    <li>93.3-350-E</li>
                                    <li>93.3-400-E</li>
                                    <li>93.3-450-E</li>
                                    <li>93.3-500-E</li>
                                    <li>93.3-550-E</li>
                                    <li>93.3-600-E</li>
                                    <li>93.3-650-E</li>
                                    <li>93.3-700-E</li>
                                    <li>93.3-750-E</li>
                                    <li>93.3-800-E</li>
                                    <li>90-200-O</li>
                                    <li>90-250-O</li>
                                    <li>90-300-O</li>
                                    <li>90-350-O</li>
                                    <li>90-400-O</li>
                                    <li>90-450-O</li>
                                    <li>90-500-O</li>
                                    <li>90-550-O</li>
                                    <li>90-600-O</li>
                                    <li>90-650-O</li>
                                    <li>90-700-O</li>
                                    <li>90-750-O</li>
                                    <li>90-800-O</li>
                                    <li>90-200-E</li>
                                    <li>90-250-E</li>
                                    <li>90-300-E</li>
                                    <li>90-350-E</li>
                                    <li>90-400-E</li>
                                    <li>90-450-E</li>
                                    <li>90-500-E</li>
                                    <li>90-550-E</li>
                                    <li>90-600-E</li>
                                    <li>90-650-E</li>
                                    <li>90-700-E</li>
                                    <li>90-750-E</li>
                                    <li>90-800-E</li>
                                    <li>85-200-O</li>
                                    <li>85-250-O</li>
                                    <li>85-300-O</li>
                                    <li>85-350-O</li>
                                    <li>85-400-O</li>
                                    <li>85-450-O</li>
                                    <li>85-500-O</li>
                                    <li>85-550-O</li>
                                    <li>85-600-O</li>
                                    <li>85-650-O</li>
                                    <li>85-700-O</li>
                                    <li>85-750-O</li>
                                    <li>85-800-O</li>
                                    <li>85-200-E</li>
                                    <li>85-250-E</li>
                                    <li>85-300-E</li>
                                    <li>85-350-E</li>
                                    <li>85-400-E</li>
                                    <li>85-450-E</li>
                                    <li>85-500-E</li>
                                    <li>85-550-E</li>
                                    <li>85-600-E</li>
                                    <li>85-650-E</li>
                                    <li>85-700-E</li>
                                    <li>85-750-E</li>
                                    <li>85-800-E</li>
                                    <li>82-200-O</li>
                                    <li>82-250-O</li>
                                    <li>82-300-O</li>
                                    <li>82-350-O</li>
                                    <li>82-400-O</li>
                                    <li>82-450-O</li>
                                    <li>82-500-O</li>
                                    <li>82-550-O</li>
                                    <li>82-600-O</li>
                                    <li>82-650-O</li>
                                    <li>82-700-O</li>
                                    <li>82-750-O</li>
                                    <li>82-800-O</li>
                                    <li>82-200-E</li>
                                    <li>82-250-E</li>
                                    <li>82-300-E</li>
                                    <li>82-350-E</li>
                                    <li>82-400-E</li>
                                    <li>82-450-E</li>
                                    <li>82-500-E</li>
                                    <li>82-550-E</li>
                                    <li>82-600-E</li>
                                    <li>82-650-E</li>
                                    <li>82-700-E</li>
                                    <li>82-750-E</li>
                                    <li>82-800-E</li>
                        </ul>
                </td>
                <td>
                        <div>Mode of the XCVR.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>State information of this XCVR instance.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>admin_state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>disabled</li>
                                    <li>enabled</li>
                        </ul>
                </td>
                <td>
                        <div>Whether Admin State is enabled or disabled for this XCVR&#x27;s PTP.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>xcvr_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Unique, access identifier string of the XCVR (e.g. &#x27;1-1&#x27;). Key value for the XCVR List.</div>
                </td>
            </tr>

            <tr>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>gathered</li>
                                    <li><div style="color: blue"><b>merged</b>&nbsp;&larr;</div></li>
                                    <li>overridden</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

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



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>after</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The resulting configuration model invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     of the parameters above.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>before</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The configuration prior to the model invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     of the parameters above.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>xml</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The set of xml commands pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;system xmlns=&quot;http://openconfig.net/yang/system&quot;&gt;&lt;config&gt;&lt;hostname&gt;foo&lt;/hostname&gt;&lt;/config&gt;&lt;/system&gt;&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Jeff Groom (@jgroom33)
- Galo Ertola (@perrary)

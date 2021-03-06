.. _nunsgateway:

nunsgateway
===========================================

.. class:: nunsgateway.NUNSGateway(bambou.nurest_object.NUMetaRESTObject,):

Represents a Network Service Gateway.


Attributes
----------


- ``mac_address``: MAC Address of the NSG

- ``nat_traversal_enabled``: This attribute is deprecated in version 4.0.

- ``tcpmss_enabled``: Boolean flag to indicate whether MSS on TCP is enabled or not

- ``tcp_maximum_segment_size``: Maximum Segment Size for TCP(min = 576, max = 7812).

- ``bios_version``: NSG BIOS Version

- ``sku``: The part number of the NSG

- ``tpm_status``: TPM Status of the NSG based on the information received by the device during bootstrapping or upgrade.

- ``cpu_type``: The NSG Processor Type

- ``nsg_version``: The NSG Version

- ``ssh_service``: Indicates if SSH Service is enabled/disabled on a NSG. The value configured for this attribute is used only when instanceSSHOverride is allowed on the associated Gateway Template.

- ``uuid``: The Redhat UUID of the NSG

- ``name`` (**Mandatory**): Name of the Gateway

- ``family``: The NSG Type

- ``last_configuration_reload_timestamp``: Time stamp of the last known configuration update of the NSG.  This timestamp gets updated when a bootstrap is successful or when a configuration reload request triggered by VSD is successful.

- ``last_updated_by``: ID of the user who last updated the object.

- ``datapath_id``: Identifier of the Gateway, based on the systemId

- ``redundancy_group_id``: The Redundancy Gateway Group associated with this Gateway Instance. This is a read only attribute

- ``template_id`` (**Mandatory**): The ID of the template that this Gateway was created from. This should be set when instantiating a Gateway

- ``pending``: Indicates that this gateway is pending state or state. When in pending state it cannot be modified from REST.

- ``serial_number``: The NSG's serial number

- ``derived_ssh_service_state``: Indicates the SSH Service state on a NSG. This value is derived based on the SSHService configuration on the NSG and the associated Gateway Template.

- ``permitted_action``: The permitted  action to USE/EXTEND  this Gateway.

- ``personality``: Personality of the Gateway - NSG, cannot be changed after creation.

- ``description``: A description of the Gateway

- ``network_acceleration``: Network Acceleration type to be used when network acceleration is enabled

- ``libraries``: Transient representation of the same property on NSGInfo.

- ``inherited_ssh_service_state``: Indicates the SSH Service state which is configured on the associated template instance.

- ``enterprise_id``: The enterprise associated with this Gateway. This is a read only attribute

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``location_id``: The NSGateway's Location. NOTE: this is a read only property, it can only be set through the location object

- ``configuration_reload_state``: Status resulting from a manually triggered configuration reload operation on an NSG.  This value only reflects the state for a manual action requested by the operator, not the automatic periodic configuration reload triggered by the NSG itself.

- ``configuration_status``: NSG Configuration status represents the NSG update state following a query by the NSG to get the latest version of the infraconfig.json file.  This status will be updated following a Bootstrap request or a Configuration Reload.  Success means that the NSG was able to apply the changes included in the latest infraconfig.json file.  A Failure response will be returned if the NSG was unable to apply the changes; this is normally accompanied with a rollback of the NSG to the previous configuration.

- ``control_traffic_cos_value``: COS Value for Self Generated Traffic (Control Traffic). Min is 0 and Max is 7

- ``control_traffic_dscp_value``: DSCP Value for Self Generated Traffic (Control Traffic). Min is 0 and Max is 63

- ``bootstrap_id``: The bootstrap details associated with this NSGateway. NOTE: this is a read only property, it can only be set during creation of an NSG

- ``bootstrap_status``: The bootstrap status of this NSGateway. NOTE: this is a read only property

- ``operation_mode``: Operation mode of NSGateway

- ``operation_status``: Operation Status of NSGateway

- ``product_name``: NSG Product Name

- ``associated_gateway_security_id``: Readonly Id of the associated gateway security object

- ``associated_gateway_security_profile_id``: Readonly Id of the associated gateway security profile object

- ``associated_nsg_info_id``: Readonly Id of the associated nsg info object

- ``associated_nsg_upgrade_profile_id``: The UUID of the NSG Upgrade Profile associated to this NSG instance.

- ``auto_disc_gateway_id``: The Auto Discovered Gateway associated with this Gateway Instance

- ``external_id``: External object ID. Used for integration with third party systems

- ``system_id``: Identifier of the Gateway, cannot be modified after creation




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nugatewaysecurity.NUGatewaySecurity<nugatewaysecurity>`                                                                                                    ``gateway_securities`` 
:ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`                                                                                                                   ``patnat_pools`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuwirelessport.NUWirelessPort<nuwirelessport>`                                                                                                             ``wireless_ports`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuinfrastructureconfig.NUInfrastructureConfig<nuinfrastructureconfig>`                                                                                     ``infrastructure_configs`` 
:ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`                                                                                     ``enterprise_permissions`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nulocation.NULocation<nulocation>`                                                                                                                         ``locations`` 
:ref:`nucommand.NUCommand<nucommand>`                                                                                                                            ``commands`` 
:ref:`numonitorscope.NUMonitorscope<numonitorscope>`                                                                                                             ``monitorscopes`` 
:ref:`nubootstrap.NUBootstrap<nubootstrap>`                                                                                                                      ``bootstraps`` 
:ref:`nubootstrapactivation.NUBootstrapActivation<nubootstrapactivation>`                                                                                        ``bootstrap_activations`` 
:ref:`nuuplinkconnection.NUUplinkConnection<nuuplinkconnection>`                                                                                                 ``uplink_connections`` 
:ref:`nunsginfo.NUNSGInfo<nunsginfo>`                                                                                                                            ``nsg_infos`` 
:ref:`nunsport.NUNSPort<nunsport>`                                                                                                                               ``ns_ports`` 
:ref:`nusubnet.NUSubnet<nusubnet>`                                                                                                                               ``subnets`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuducgroup.NUDUCGroup<nuducgroup>`

- :ref:`nupolicyobjectgroup.NUPolicyObjectGroup<nupolicyobjectgroup>`

- :ref:`nuperformancemonitor.NUPerformanceMonitor<nuperformancemonitor>`

- :ref:`nume.NUMe<nume>`

- :ref:`nunsggroup.NUNSGGroup<nunsggroup>`

- :ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`


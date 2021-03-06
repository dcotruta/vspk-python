# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from bambou import NURESTObject


class NUVNFInterface(NURESTObject):
    """ Represents a VNFInterface in the VSD

        Notes:
            Represent VNF interface, This can not be created directly, it will be generated from VNF Interface Descriptor when VNF instance is created.
    """

    __rest_name__ = "vnfinterface"
    __resource_name__ = "vnfinterfaces"

    
    ## Constants
    
    CONST_ATTACHED_NETWORK_TYPE_SUBNET = "SUBNET"
    
    CONST_ATTACHED_NETWORK_TYPE_L2DOMAIN = "L2DOMAIN"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VNFInterface instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vnfinterface = NUVNFInterface(id=u'xxxx-xxx-xxx-xxx', name=u'VNFInterface')
                >>> vnfinterface = NUVNFInterface(data=my_dict)
        """

        super(NUVNFInterface, self).__init__()

        # Read/Write Attributes
        
        self._mac = None
        self._vnfuuid = None
        self._ip_address = None
        self._vport_id = None
        self._vport_name = None
        self._name = None
        self._gateway = None
        self._netmask = None
        self._network_name = None
        self._policy_decision_id = None
        self._domain_id = None
        self._domain_name = None
        self._zone_id = None
        self._zone_name = None
        self._is_management_interface = None
        self._attached_network_id = None
        self._attached_network_type = None
        
        self.expose_attribute(local_name="mac", remote_name="MAC", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vnfuuid", remote_name="VNFUUID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ip_address", remote_name="IPAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vport_id", remote_name="VPortID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vport_name", remote_name="VPortName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway", remote_name="gateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="netmask", remote_name="netmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="network_name", remote_name="networkName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="policy_decision_id", remote_name="policyDecisionID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="domain_id", remote_name="domainID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="domain_name", remote_name="domainName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zone_id", remote_name="zoneID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zone_name", remote_name="zoneName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="is_management_interface", remote_name="isManagementInterface", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="attached_network_id", remote_name="attachedNetworkID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="attached_network_type", remote_name="attachedNetworkType", attribute_type=str, is_required=False, is_unique=False, choices=[u'L2DOMAIN', u'SUBNET'])
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def mac(self):
        """ Get mac value.

            Notes:
                MAC address of the  interface

                
                This attribute is named `MAC` in VSD API.
                
        """
        return self._mac

    @mac.setter
    def mac(self, value):
        """ Set mac value.

            Notes:
                MAC address of the  interface

                
                This attribute is named `MAC` in VSD API.
                
        """
        self._mac = value

    
    @property
    def vnfuuid(self):
        """ Get vnfuuid value.

            Notes:
                UUID of the associated VNF

                
                This attribute is named `VNFUUID` in VSD API.
                
        """
        return self._vnfuuid

    @vnfuuid.setter
    def vnfuuid(self, value):
        """ Set vnfuuid value.

            Notes:
                UUID of the associated VNF

                
                This attribute is named `VNFUUID` in VSD API.
                
        """
        self._vnfuuid = value

    
    @property
    def ip_address(self):
        """ Get ip_address value.

            Notes:
                IP address of the  interface

                
                This attribute is named `IPAddress` in VSD API.
                
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        """ Set ip_address value.

            Notes:
                IP address of the  interface

                
                This attribute is named `IPAddress` in VSD API.
                
        """
        self._ip_address = value

    
    @property
    def vport_id(self):
        """ Get vport_id value.

            Notes:
                ID of the vport that the interface is attached to

                
                This attribute is named `VPortID` in VSD API.
                
        """
        return self._vport_id

    @vport_id.setter
    def vport_id(self, value):
        """ Set vport_id value.

            Notes:
                ID of the vport that the interface is attached to

                
                This attribute is named `VPortID` in VSD API.
                
        """
        self._vport_id = value

    
    @property
    def vport_name(self):
        """ Get vport_name value.

            Notes:
                Name of the vport that the interface is attached to

                
                This attribute is named `VPortName` in VSD API.
                
        """
        return self._vport_name

    @vport_name.setter
    def vport_name(self, value):
        """ Set vport_name value.

            Notes:
                Name of the vport that the interface is attached to

                
                This attribute is named `VPortName` in VSD API.
                
        """
        self._vport_name = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Device name associated with this interface

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Device name associated with this interface

                
        """
        self._name = value

    
    @property
    def gateway(self):
        """ Get gateway value.

            Notes:
                Gateway of the subnet that the interface is connected to

                
        """
        return self._gateway

    @gateway.setter
    def gateway(self, value):
        """ Set gateway value.

            Notes:
                Gateway of the subnet that the interface is connected to

                
        """
        self._gateway = value

    
    @property
    def netmask(self):
        """ Get netmask value.

            Notes:
                Netmask of the subnet that the interface is attached to

                
        """
        return self._netmask

    @netmask.setter
    def netmask(self, value):
        """ Set netmask value.

            Notes:
                Netmask of the subnet that the interface is attached to

                
        """
        self._netmask = value

    
    @property
    def network_name(self):
        """ Get network_name value.

            Notes:
                Name of the network that the interface is attached to

                
                This attribute is named `networkName` in VSD API.
                
        """
        return self._network_name

    @network_name.setter
    def network_name(self, value):
        """ Set network_name value.

            Notes:
                Name of the network that the interface is attached to

                
                This attribute is named `networkName` in VSD API.
                
        """
        self._network_name = value

    
    @property
    def policy_decision_id(self):
        """ Get policy_decision_id value.

            Notes:
                The policy decision ID for this particular interface

                
                This attribute is named `policyDecisionID` in VSD API.
                
        """
        return self._policy_decision_id

    @policy_decision_id.setter
    def policy_decision_id(self, value):
        """ Set policy_decision_id value.

            Notes:
                The policy decision ID for this particular interface

                
                This attribute is named `policyDecisionID` in VSD API.
                
        """
        self._policy_decision_id = value

    
    @property
    def domain_id(self):
        """ Get domain_id value.

            Notes:
                ID of the domain that the interface is attached to

                
                This attribute is named `domainID` in VSD API.
                
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, value):
        """ Set domain_id value.

            Notes:
                ID of the domain that the interface is attached to

                
                This attribute is named `domainID` in VSD API.
                
        """
        self._domain_id = value

    
    @property
    def domain_name(self):
        """ Get domain_name value.

            Notes:
                Name of the domain that the interface is attached to

                
                This attribute is named `domainName` in VSD API.
                
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, value):
        """ Set domain_name value.

            Notes:
                Name of the domain that the interface is attached to

                
                This attribute is named `domainName` in VSD API.
                
        """
        self._domain_name = value

    
    @property
    def zone_id(self):
        """ Get zone_id value.

            Notes:
                ID of the zone that the interface is attached to

                
                This attribute is named `zoneID` in VSD API.
                
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, value):
        """ Set zone_id value.

            Notes:
                ID of the zone that the interface is attached to

                
                This attribute is named `zoneID` in VSD API.
                
        """
        self._zone_id = value

    
    @property
    def zone_name(self):
        """ Get zone_name value.

            Notes:
                Name of the zone that the VM is attached to

                
                This attribute is named `zoneName` in VSD API.
                
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, value):
        """ Set zone_name value.

            Notes:
                Name of the zone that the VM is attached to

                
                This attribute is named `zoneName` in VSD API.
                
        """
        self._zone_name = value

    
    @property
    def is_management_interface(self):
        """ Get is_management_interface value.

            Notes:
                Indicates if this is a management interface

                
                This attribute is named `isManagementInterface` in VSD API.
                
        """
        return self._is_management_interface

    @is_management_interface.setter
    def is_management_interface(self, value):
        """ Set is_management_interface value.

            Notes:
                Indicates if this is a management interface

                
                This attribute is named `isManagementInterface` in VSD API.
                
        """
        self._is_management_interface = value

    
    @property
    def attached_network_id(self):
        """ Get attached_network_id value.

            Notes:
                ID of the Subnet that the interface is attached to

                
                This attribute is named `attachedNetworkID` in VSD API.
                
        """
        return self._attached_network_id

    @attached_network_id.setter
    def attached_network_id(self, value):
        """ Set attached_network_id value.

            Notes:
                ID of the Subnet that the interface is attached to

                
                This attribute is named `attachedNetworkID` in VSD API.
                
        """
        self._attached_network_id = value

    
    @property
    def attached_network_type(self):
        """ Get attached_network_type value.

            Notes:
                network type that the interface is attached to

                
                This attribute is named `attachedNetworkType` in VSD API.
                
        """
        return self._attached_network_type

    @attached_network_type.setter
    def attached_network_type(self, value):
        """ Set attached_network_type value.

            Notes:
                network type that the interface is attached to

                
                This attribute is named `attachedNetworkType` in VSD API.
                
        """
        self._attached_network_type = value

    

    
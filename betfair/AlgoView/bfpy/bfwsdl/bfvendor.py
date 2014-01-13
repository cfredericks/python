#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
# This file is part of BfPy
#
# BfPy is a Python library to communicate with the Betfair Betting Exchange
# Copyright (C) 2010 Daniel Rodriguez (aka Daniel Rodriksson)
# Copyright (C) 2011 Sensible Odds Ltd.
#
# You can learn more and contact the author at:
#
#    http://code.google.com/p/bfpy/
#
# BfPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BfPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BfPy. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
'''
BfPy wsdsl variables holding the Betfair WSDL definitions
'''

#
# Variables containing the Betfair WSDL files
#
BFVendorService = '''
<?xml version="1.0" encoding="UTF-8"?>

<!--

Copyright 2003-2004 The Sporting Exchange Limited. All rights reserved. 
The presentation, distribution or other dissemination of the information contained herein by The Sporting Exchange Limited (Betfair) is not a license, either expressly or impliedly, to any intellectual property owned or controlled by Betfair.
Save as provided by statute and to the fullest extent permitted by law, the following provisions set out the entire liability of Betfair (including any liability for the acts and omissions of its employees, agents and sub-contractors) to the User in respect of the use of its WSDL file whether in contract, tort, statute, equity or otherwise: 
(a)     The User acknowledges and agrees that (except as expressly provided in this Agreement) the WSDL is provided "AS IS" without warranties of any kind (whether express or implied);
(b)    All conditions, warranties, terms and undertakings (whether express or implied, statutory or otherwise relating to the delivery, performance, quality, uninterrupted use, fitness for purpose, occurrence or reliability of the WSDL are hereby excluded to the fullest extent permitted by law; and 
(c)     Betfair shall not be liable to the User for loss of profit (whether direct or indirect), loss of contracts or goodwill, lost advertising, loss of data or any type of special, indirect, consequential or economic loss (including loss or damage suffered by the User as a result of an action brought by a third party) even if such loss was reasonably foreseeable or Betfair had been advised of the possibility of the User incurring such loss.
No exclusion or limitation set out in this Agreement shall apply in the case of fraud or fraudulent concealment, death or personal injury resulting from the negligence of either party or any of its employees, agents or sub-contractors; and/or any breach of the obligations implied by (as appropriate) section 12 of the Sale of Goods Act 1979, section 2 of the Supply of Goods and Services Act 1982 or section 8 of the Supply of Goods (Implied Terms) Act 1973.

-->

<wsdl:definitions name="VendorService"
	xmlns:http="http://schemas.xmlsoap.org/wsdl/http/" 
	xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" 
	xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
	xmlns:types="http://www.betfair.com/adminapi/types/v2/"
	xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" 
	xmlns:tns="http://www.betfair.com/adminapi/v2/VendorService/" 
	xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/" 
	xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/" 
	targetNamespace="http://www.betfair.com/adminapi/v2/VendorService/" 
	xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
  <wsdl:types>
    <xsd:schema targetNamespace="http://www.betfair.com/adminapi/types/v2/">
      <xsd:import namespace="http://schemas.xmlsoap.org/soap/encoding/"/>


      <xsd:complexType name="SetAccessRequestReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
          <xsd:sequence>
            <xsd:element name="accessRequestToken" nillable="false" type="xsd:string"/>
          </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="SetAccessRequestResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
                <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
                <xsd:element name="vendorClientId" nillable="false" type="xsd:int"/>
                <xsd:element name="vendorSoftwareName" nillable="false" type="xsd:string"/>
                <xsd:element name="expiryDate" nillable="false" type="xsd:dateTime"/>
                <xsd:element name="errorCode" type="types:SetAccessRequestErrorEnum"/>
                <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="SetAccessRequestErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_ACCESS_REQUEST_TOKEN"/>
          <xsd:enumeration value="REQUEST_ALREADY_DONE"/>
          <xsd:enumeration value="REQUEST_EXPIRED"/>
          <xsd:enumeration value="REQUEST_CANCELLED"/>
          <xsd:enumeration value='VENDOR_SOFTWARE_INVALID'/>
          <xsd:enumeration value='VENDOR_SOFTWARE_INACTIVE'/>
          <xsd:enumeration value='USER_ALREADY_SUBSCRIBED'/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>


      <xsd:complexType name="CancelVendorAccessRequestReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
          <xsd:sequence>
            <xsd:element name="accessRequestToken" nillable="false" type="xsd:string"/>
            <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
          </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="CancelVendorAccessRequestResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
                <xsd:element name="errorCode" type="types:CancelVendorAccessRequestErrorEnum"/>
                <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="CancelVendorAccessRequestErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_VENDOR_SOFTWARE_ID"/>
          <xsd:enumeration value="INVALID_VENDOR_SESSION" />
          <xsd:enumeration value="OPERATOR_NOT_VENDORSOFTWARE_OWNER" />
          <xsd:enumeration value='INVALID_ACCESS_REQUEST_TOKEN'/>
          <xsd:enumeration value='INVALID_VENDOR_CLIENT_ACCESS_REQUEST_STATUS'/>
          <xsd:enumeration value='VENDOR_SOFTWARE_INVALID'/>
          <xsd:enumeration value='VENDOR_SOFTWARE_INACTIVE'/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="GetVendorAccessRequestsReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
          <xsd:sequence>
            <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
            <xsd:element name="status" type="types:VendorClientAccessRequestStatusEnum"/>
            <xsd:element name="requestDateFrom" nillable="true" type="xsd:dateTime"/>
            <xsd:element name="requestDateTo" nillable="true" type="xsd:dateTime"/>
          </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetVendorAccessRequestsResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
                <xsd:element name="vendorAccessRequests" nillable="true" type="types:ArrayOfVendorAccessRequest"/>
                <xsd:element name="errorCode" type="types:GetVendorAccessRequestsErrorEnum"/>
                <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfVendorAccessRequest">
        <xsd:sequence>
          <xsd:element name="vendorAccessRequest" form="qualified" maxOccurs="unbounded"
            nillable="true" type="types:VendorAccessRequest"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="VendorAccessRequest">
        <xsd:sequence>
        <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
        <xsd:element name="vendorCustomField" nillable="false" type="xsd:string"/>
        <xsd:element name="vendorClientId" nillable="false" type="xsd:int"/>
        <xsd:element name="accessRequestToken" nillable="false" type="xsd:string"/>
        <xsd:element name="expiryDate" nillable="false" type="xsd:dateTime"/>
        <xsd:element name="status" nillable="true" type="types:VendorClientAccessRequestStatusEnum"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="GetVendorAccessRequestsErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_VENDOR_SOFTWARE_ID"/>
          <xsd:enumeration value="INVALID_VENDOR_SESSION" />
          <xsd:enumeration value="OPERATOR_NOT_VENDORSOFTWARE_OWNER" />
          <xsd:enumeration value='VENDOR_SOFTWARE_INACTIVE'/>
          <xsd:enumeration value='INVALID_STATUS'/>
          <xsd:enumeration value='NO_RESULTS'/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:simpleType name="VendorClientAccessRequestStatusEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="ACTIVE"/>
          <xsd:enumeration value="CANCELLED"/>
          <xsd:enumeration value="EXPIRED"/>
          <xsd:enumeration value="DONE"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="CreateVendorAccessRequestReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
          <xsd:sequence>
            <xsd:element name="vendorCustomField" nillable="false" type="xsd:string"/>
            <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
            <xsd:element name="expiryDate" nillable="true" type="xsd:dateTime"/>
          </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="CreateVendorAccessRequestResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
                <xsd:element name="errorCode" type="types:CreateVendorAccessRequestErrorEnum"/>
                <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
                <xsd:element name="accessRequestToken" nillable="true" type="xsd:string"/>
                <xsd:element name="validUntil" type="xsd:dateTime"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="CreateVendorAccessRequestErrorEnum">
        <xsd:restriction base="xsd:string">
	        <xsd:enumeration value='OK'/>
	        <xsd:enumeration value='INVALID_VENDOR_SOFTWARE_ID'/>
	        <xsd:enumeration value='INVALID_VENDOR_SESSION'/>
	        <xsd:enumeration value='OPERATOR_NOT_VENDORSOFTWARE_OWNER'/>
	        <xsd:enumeration value='LOGIN_RESTRICTED_LOCATION'/>
	        <xsd:enumeration value='VENDOR_SOFTWARE_INVALID'/>
	        <xsd:enumeration value='VENDOR_SOFTWARE_INACTIVE'/>
	        <xsd:enumeration value='INVALID_VENDOR_CUSTOM_FIELD'/>
	        <xsd:enumeration value='INVALID_EXPIRY_DATE'/>
	        <xsd:enumeration value='API_ERROR'/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="VendorSubscriptionReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
	        <xsd:sequence>
		        <xsd:element name="username" nillable="false" type="xsd:string"/>
		        <xsd:element name="vendorCustomField" nillable="false" type="xsd:string"/>
		        <xsd:element name="vendorClientId" nillable="false" type="xsd:int"/>
		        <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
		        <xsd:element name="expiryDate" nillable="true" type="xsd:dateTime"/>
	        </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="VendorSubscriptionResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              	<xsd:element name="errorCode" type="types:VendorSubscriptionErrorEnum"/>
              	<xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              	<xsd:element name="validUntil" type="xsd:dateTime"/>
              	<xsd:element name="vendorClientId" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="VendorSubscriptionErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_USERNAME"/>
          <xsd:enumeration value="USER_NOT_ACCOUNT_OWNER"/>
          <xsd:enumeration value="INVALID_VENDOR_SOFTWARE_ID"/>
          <xsd:enumeration value="LOGIN_FAILED_ACCOUNT_LOCKED"/>
          <xsd:enumeration value="ACCOUNT_SUSPENDED"/>
          <xsd:enumeration value="ACCOUNT_CLOSED"/>
          <xsd:enumeration value="INVALID_VENDOR_SESSION" />
          <xsd:enumeration value="OPERATOR_NOT_VENDORSOFTWARE_OWNER" />
          <xsd:enumeration value="LOGIN_RESTRICTED_LOCATION"/>
          <xsd:enumeration value="USER_ALREADY_SUBSCRIBED"/>
          <xsd:enumeration value="INVALID_VENDOR_CLIENT_ID"/>
          <xsd:enumeration value="INVALID_VENDOR_CUSTOM_FIELD"/>
          <xsd:enumeration value="INVALID_INPUT_PARAMETERS"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
	  
      <xsd:complexType name="CancelVendorSubscriptionReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
	        <xsd:sequence>
		      <xsd:element name="username" nillable="false" type="xsd:string"/>
	          <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
	          <xsd:element name="vendorClientId" nillable="false" type="xsd:int"/>
			</xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="CancelVendorSubscriptionResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              	<xsd:element name="errorCode" type="types:VendorSubscriptionErrorEnum"/>
              	<xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
	  
      <xsd:complexType name="GetSubscriptionInfoReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
	        <xsd:sequence>
		      <xsd:element name="username" nillable="false" type="xsd:string"/>
		      <xsd:element name="vendorClientId" nillable="false" type="xsd:int"/>
		      <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
			</xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetSubscriptionInfoResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              	<xsd:element name="vendorSoftware" nillable="true" type="xsd:int"/>
              	<xsd:element name="expiryDate" nillable="true" type="xsd:dateTime"/>
              	<xsd:element name="errorCode" type="types:VendorSubscriptionErrorEnum"/>
              	<xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              	<xsd:element name="status" nillable="true" type="types:VendorSoftwareClientStatusEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
	  
      <xsd:complexType name="GetVendorInfoReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest"/>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetVendorInfoResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
				<xsd:element name="vendorInfo" nillable="true" type="types:ArrayOfVendorSoftwareInfos"/>
              	<xsd:element name="errorCode" type="types:VendorSubscriptionErrorEnum"/>
              	<xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfVendorSoftwareInfos">
        <xsd:sequence>
          <xsd:element name="vsInfo" form="qualified" maxOccurs="unbounded"
            nillable="true" type="types:VendorSoftwareInfo"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="VendorSoftwareInfo">
        <xsd:sequence>
          <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
          <xsd:element name="vendorSoftwareName" nillable="false" type="xsd:string"/>
          <xsd:element name="activeClientsNo" type="xsd:long"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="GetVendorUsersReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
	        <xsd:sequence>
	          <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
	          <xsd:element name="username" nillable="true" type="xsd:string"/>
	          <xsd:element name="usernameSearchModifier" type="types:SearchModifierEnum"/>
	          <xsd:element name="vendorCustomField" nillable="true" type="xsd:string"/>
	          <xsd:element name="customFieldSearchModifier" type="types:SearchModifierEnum"/>
	          <xsd:element name="expiryDateFrom" nillable="true" type="xsd:dateTime"/>
	          <xsd:element name="expiryDateTo" nillable="true" type="xsd:dateTime"/>
	          <xsd:element name="status" type="types:VendorSoftwareClientStatusEnum"/>
			</xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="SearchModifierEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="STARTS_WITH"/>
          <xsd:enumeration value="EXACT"/>
          <xsd:enumeration value="ENDS_WITH"/>
          <xsd:enumeration value="CONTAINS"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="GetVendorUsersResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
				<xsd:element name="vendorUsers" nillable="true" type="types:ArrayOfVendorUser"/>
              	<xsd:element name="errorCode" type="types:VendorSubscriptionErrorEnum"/>
              	<xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfVendorUser">
        <xsd:sequence>
          <xsd:element name="vendorUser" form="qualified" maxOccurs="unbounded"
            nillable="true" type="types:VendorUser"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="VendorUser">
        <xsd:sequence>
	      <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
	      <xsd:element name="username" nillable="false" type="xsd:string"/>
	      <xsd:element name="expiryDate" nillable="true" type="xsd:dateTime"/>
	      <xsd:element name="status" nillable="true" type="types:VendorSoftwareClientStatusEnum"/>
	      <xsd:element name="vendorClientId" nillable="false" type="xsd:int"/>
	      <xsd:element name="vendorCustomField" nillable="false" type="xsd:string"/>
	      <xsd:element name="createDate" nillable="true" type="xsd:dateTime"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="VendorSoftwareClientStatusEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="ACTIVE"/>
          <xsd:enumeration value="CANCELLED"/>
          <xsd:enumeration value="EXPIRED"/>
        </xsd:restriction>
      </xsd:simpleType>
	  
	  
	  <!-- base types copied from BFService wsdl-->
      <xsd:complexType abstract="true" name="APIRequest">
        <xsd:sequence>
          <xsd:element name="header" nillable="true" type="types:APIRequestHeader"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="APIRequestHeader">
        <xsd:sequence>
          <xsd:element name="clientStamp" type="xsd:long"/>
          <xsd:element name="sessionToken" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType abstract="true" name="APIResponse">
        <xsd:sequence>
          <xsd:element name="header" nillable="true" type="types:APIResponseHeader"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="APIResponseHeader">
        <xsd:sequence>
          <xsd:element name="errorCode" type="types:APIErrorEnum"/>
          <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
          <xsd:element name="sessionToken" nillable="true" type="xsd:string"/>
          <xsd:element name="timestamp" type="xsd:dateTime"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="APIErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INTERNAL_ERROR"/>
          <xsd:enumeration value="EXCEEDED_THROTTLE"/>
          <xsd:enumeration value="USER_NOT_SUBSCRIBED_TO_PRODUCT"/>
          <xsd:enumeration value="SUBSCRIPTION_INACTIVE_OR_SUSPENDED"/>
          <xsd:enumeration value="VENDOR_SOFTWARE_INACTIVE"/>
          <xsd:enumeration value="VENDOR_SOFTWARE_INVALID"/>
          <xsd:enumeration value="SERVICE_NOT_AVAILABLE_IN_PRODUCT"/>
          <xsd:enumeration value="NO_SESSION"/>
          <xsd:enumeration value="TOO_MANY_REQUESTS"/>
          <xsd:enumeration value="PRODUCT_REQUIRES_FUNDED_ACCOUNT"/>
          <xsd:enumeration value="SERVICE_NOT_AVAILABLE_FOR_LOGIN_STATUS"/>
        </xsd:restriction>
      </xsd:simpleType>
	  
    </xsd:schema>
    
    <xsd:schema elementFormDefault="qualified" targetNamespace="http://www.betfair.com/adminapi/v2/VendorService/">
      <xsd:import namespace="http://www.betfair.com/adminapi/types/v2/"/>

      <xsd:element name="setAccessRequest">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:SetAccessRequestReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="setAccessRequestResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:SetAccessRequestResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="cancelVendorAccessRequest">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:CancelVendorAccessRequestReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="cancelVendorAccessRequestResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:CancelVendorAccessRequestResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getVendorAccessRequests">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetVendorAccessRequestsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getVendorAccessRequestsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetVendorAccessRequestsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="createVendorAccessRequest">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:CreateVendorAccessRequestReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="createVendorAccessRequestResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:CreateVendorAccessRequestResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="addVendorSubscription">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:VendorSubscriptionReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="addVendorSubscriptionResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:VendorSubscriptionResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="updateVendorSubscription">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:VendorSubscriptionReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="updateVendorSubscriptionResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:VendorSubscriptionResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="cancelVendorSubscription">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:CancelVendorSubscriptionReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="cancelVendorSubscriptionResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:CancelVendorSubscriptionResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getSubscriptionInfo">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetSubscriptionInfoReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getSubscriptionInfoResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetSubscriptionInfoResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getVendorInfo">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetVendorInfoReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getVendorInfoResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetVendorInfoResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getVendorUsers">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetVendorUsersReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getVendorUsersResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetVendorUsersResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

    </xsd:schema>

  </wsdl:types>

  <wsdl:message name="setAccessRequestIn">
    <wsdl:part element="tns:setAccessRequest" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="setAccessRequestOut">
    <wsdl:part element="tns:setAccessRequestResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="cancelVendorAccessRequestIn">
    <wsdl:part element="tns:cancelVendorAccessRequest" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="cancelVendorAccessRequestOut">
    <wsdl:part element="tns:cancelVendorAccessRequestResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getVendorAccessRequestsIn">
    <wsdl:part element="tns:getVendorAccessRequests" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getVendorAccessRequestsOut">
    <wsdl:part element="tns:getVendorAccessRequestsResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="createVendorAccessRequestIn">
    <wsdl:part element="tns:createVendorAccessRequest" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="createVendorAccessRequestOut">
    <wsdl:part element="tns:createVendorAccessRequestResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="addVendorSubscriptionIn">
    <wsdl:part element="tns:addVendorSubscription" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="addVendorSubscriptionOut">
    <wsdl:part element="tns:addVendorSubscriptionResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="updateVendorSubscriptionIn">
    <wsdl:part element="tns:updateVendorSubscription" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="updateVendorSubscriptionOut">
    <wsdl:part element="tns:updateVendorSubscriptionResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="cancelVendorSubscriptionIn">
    <wsdl:part element="tns:cancelVendorSubscription" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="cancelVendorSubscriptionOut">
    <wsdl:part element="tns:cancelVendorSubscriptionResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getSubscriptionInfoIn">
    <wsdl:part element="tns:getSubscriptionInfo" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getSubscriptionInfoOut">
    <wsdl:part element="tns:getSubscriptionInfoResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getVendorInfoIn">
    <wsdl:part element="tns:getVendorInfo" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getVendorInfoOut">
    <wsdl:part element="tns:getVendorInfoResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getVendorUsersIn">
    <wsdl:part element="tns:getVendorUsers" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getVendorUsersOut">
    <wsdl:part element="tns:getVendorUsersResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:portType name="VendorService">

    <wsdl:operation name="setAccessRequest">
      <wsdl:input message="tns:setAccessRequestIn" name="setAccessRequestIn"/>
      <wsdl:output message="tns:setAccessRequestOut" name="setAccessRequestOut"/>
    </wsdl:operation>

    <wsdl:operation name="cancelVendorAccessRequest">
      <wsdl:input message="tns:cancelVendorAccessRequestIn" name="cancelVendorAccessRequestIn"/>
      <wsdl:output message="tns:cancelVendorAccessRequestOut" name="cancelVendorAccessRequestOut"/>
    </wsdl:operation>

    <wsdl:operation name="getVendorAccessRequests">
      <wsdl:input message="tns:getVendorAccessRequestsIn" name="getVendorAccessRequestsIn"/>
      <wsdl:output message="tns:getVendorAccessRequestsOut" name="getVendorAccessRequestsOut"/>
    </wsdl:operation>

    <wsdl:operation name="createVendorAccessRequest">
      <wsdl:input message="tns:createVendorAccessRequestIn" name="createVendorAccessRequestIn"/>
      <wsdl:output message="tns:createVendorAccessRequestOut" name="createVendorAccessRequestOut"/>
    </wsdl:operation>

    <wsdl:operation name="addVendorSubscription">
      <wsdl:input message="tns:addVendorSubscriptionIn" name="addVendorSubscriptionIn"/>
      <wsdl:output message="tns:addVendorSubscriptionOut" name="addVendorSubscriptionOut"/>
    </wsdl:operation>

    <wsdl:operation name="updateVendorSubscription">
      <wsdl:input message="tns:updateVendorSubscriptionIn" name="updateVendorSubscriptionIn"/>
      <wsdl:output message="tns:updateVendorSubscriptionOut" name="updateVendorSubscriptionOut"/>
    </wsdl:operation>

    <wsdl:operation name="cancelVendorSubscription">
      <wsdl:input message="tns:cancelVendorSubscriptionIn" name="cancelVendorSubscriptionIn"/>
      <wsdl:output message="tns:cancelVendorSubscriptionOut" name="cancelVendorSubscriptionOut"/>
    </wsdl:operation>

    <wsdl:operation name="getSubscriptionInfo">
      <wsdl:input message="tns:getSubscriptionInfoIn" name="getSubscriptionInfoIn"/>
      <wsdl:output message="tns:getSubscriptionInfoOut" name="getSubscriptionInfoOut"/>
    </wsdl:operation>

    <wsdl:operation name="getVendorInfo">
      <wsdl:input message="tns:getVendorInfoIn" name="getVendorInfoIn"/>
      <wsdl:output message="tns:getVendorInfoOut" name="getVendorInfoOut"/>
    </wsdl:operation>

    <wsdl:operation name="getVendorUsers">
      <wsdl:input message="tns:getVendorUsersIn" name="getVendorUsersIn"/>
      <wsdl:output message="tns:getVendorUsersOut" name="getVendorUsersOut"/>
    </wsdl:operation>

  </wsdl:portType>


  <wsdl:binding name="VendorService" type="tns:VendorService">
    <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>

    <wsdl:operation name="setAccessRequest">
      <soap:operation soapAction="setAccessRequest" style="document"/>
      <wsdl:input name="setAccessRequestIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="setAccessRequestOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="cancelVendorAccessRequest">
      <soap:operation soapAction="cancelVendorAccessRequest" style="document"/>
      <wsdl:input name="cancelVendorAccessRequestIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="cancelVendorAccessRequestOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getVendorAccessRequests">
      <soap:operation soapAction="getVendorAccessRequests" style="document"/>
      <wsdl:input name="getVendorAccessRequestsIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getVendorAccessRequestsOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="createVendorAccessRequest">
      <soap:operation soapAction="createVendorAccessRequest" style="document"/>
      <wsdl:input name="createVendorAccessRequestIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="createVendorAccessRequestOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="addVendorSubscription">
      <soap:operation soapAction="addVendorSubscription" style="document"/>
      <wsdl:input name="addVendorSubscriptionIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="addVendorSubscriptionOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="updateVendorSubscription">
      <soap:operation soapAction="updateVendorSubscription" style="document"/>
      <wsdl:input name="updateVendorSubscriptionIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="updateVendorSubscriptionOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="cancelVendorSubscription">
      <soap:operation soapAction="cancelVendorSubscription" style="document"/>
      <wsdl:input name="cancelVendorSubscriptionIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="cancelVendorSubscriptionOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getSubscriptionInfo">
      <soap:operation soapAction="getSubscriptionInfo" style="document"/>
      <wsdl:input name="getSubscriptionInfoIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getSubscriptionInfoOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getVendorInfo">
      <soap:operation soapAction="getVendorInfo" style="document"/>
      <wsdl:input name="getVendorInfoIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getVendorInfoOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getVendorUsers">
      <soap:operation soapAction="getVendorUsers" style="document"/>
      <wsdl:input name="getVendorUsersIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getVendorUsersOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

  </wsdl:binding>
  <wsdl:service name="VendorService">
    <wsdl:port binding="tns:VendorService" name="VendorService">
      <soap:address location="https://api.betfair.com/admin-api/v2/VendorService"/>
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>
'''

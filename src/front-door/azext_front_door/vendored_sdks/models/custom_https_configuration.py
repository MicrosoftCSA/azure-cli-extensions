# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CustomHttpsConfiguration(Model):
    """Https settings for a domain.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param certificate_source: Required. Defines the source of the SSL
     certificate. Possible values include: 'AzureKeyVault', 'FrontDoor'
    :type certificate_source: str or
     ~azure.mgmt.frontdoor.models.FrontDoorCertificateSource
    :ivar protocol_type: Required. Defines the TLS extension protocol that is
     used for secure delivery. Default value: "ServerNameIndication" .
    :vartype protocol_type: str
    :param minimum_tls_version: Required. The minimum TLS version required
     from the clients to establish an SSL handshake with Front Door. Possible
     values include: '1.0', '1.2'
    :type minimum_tls_version: str or
     ~azure.mgmt.frontdoor.models.MinimumTLSVersion
    :param vault: The Key Vault containing the SSL certificate
    :type vault:
     ~azure.mgmt.frontdoor.models.KeyVaultCertificateSourceParametersVault
    :param secret_name: The name of the Key Vault secret representing the full
     certificate PFX
    :type secret_name: str
    :param secret_version: The version of the Key Vault secret representing
     the full certificate PFX
    :type secret_version: str
    :param certificate_type: Defines the type of the certificate used for
     secure connections to a frontendEndpoint. Possible values include:
     'Dedicated'
    :type certificate_type: str or
     ~azure.mgmt.frontdoor.models.FrontDoorCertificateType
    """

    _validation = {
        'certificate_source': {'required': True},
        'protocol_type': {'required': True, 'constant': True},
        'minimum_tls_version': {'required': True},
    }

    _attribute_map = {
        'certificate_source': {'key': 'certificateSource', 'type': 'str'},
        'protocol_type': {'key': 'protocolType', 'type': 'str'},
        'minimum_tls_version': {'key': 'minimumTlsVersion', 'type': 'str'},
        'vault': {'key': 'keyVaultCertificateSourceParameters.vault', 'type': 'KeyVaultCertificateSourceParametersVault'},
        'secret_name': {'key': 'keyVaultCertificateSourceParameters.secretName', 'type': 'str'},
        'secret_version': {'key': 'keyVaultCertificateSourceParameters.secretVersion', 'type': 'str'},
        'certificate_type': {'key': 'frontDoorCertificateSourceParameters.certificateType', 'type': 'str'},
    }

    protocol_type = "ServerNameIndication"

    def __init__(self, **kwargs):
        super(CustomHttpsConfiguration, self).__init__(**kwargs)
        self.certificate_source = kwargs.get('certificate_source', None)
        self.minimum_tls_version = kwargs.get('minimum_tls_version', None)
        self.vault = kwargs.get('vault', None)
        self.secret_name = kwargs.get('secret_name', None)
        self.secret_version = kwargs.get('secret_version', None)
        self.certificate_type = kwargs.get('certificate_type', None)

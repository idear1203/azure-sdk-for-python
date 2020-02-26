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

from .proxy_resource_py3 import ProxyResource


class ManagedIdentitySqlControlSettingsModel(ProxyResource):
    """Managed Identity Sql Control Settings.

    Sql Control Settings for workspace managed identity.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param grant_sql_control_to_managed_identity: Grant sql control to managed
     identity
    :type grant_sql_control_to_managed_identity:
     ~azure.mgmt.synapse.models.ManagedIdentitySqlControlSettingsModelPropertiesGrantSqlControlToManagedIdentity
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'grant_sql_control_to_managed_identity': {'key': 'properties.grantSqlControlToManagedIdentity', 'type': 'ManagedIdentitySqlControlSettingsModelPropertiesGrantSqlControlToManagedIdentity'},
    }

    def __init__(self, *, grant_sql_control_to_managed_identity=None, **kwargs) -> None:
        super(ManagedIdentitySqlControlSettingsModel, self).__init__(**kwargs)
        self.grant_sql_control_to_managed_identity = grant_sql_control_to_managed_identity

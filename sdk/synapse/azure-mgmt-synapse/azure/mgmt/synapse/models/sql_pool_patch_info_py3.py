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


class SqlPoolPatchInfo(Model):
    """SQL pool patch info.

    A SQL Analytics pool patch info.

    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: The geo-location where the resource lives
    :type location: str
    :param sku: SQL pool SKU
    :type sku: ~azure.mgmt.synapse.models.Sku
    :param max_size_bytes: Maximum size in bytes
    :type max_size_bytes: long
    :param collation: Collation mode
    :type collation: str
    :param source_database_id: Source database to create from
    :type source_database_id: str
    :param recoverable_database_id: Backup database to restore from
    :type recoverable_database_id: str
    :param provisioning_state: Resource state
    :type provisioning_state: str
    :param status: Resource status
    :type status: str
    :param restore_point_in_time: Snapshot time to restore
    :type restore_point_in_time: datetime
    :param create_mode: What is this?
    :type create_mode: str
    :param creation_date: Date the SQL pool was created
    :type creation_date: datetime
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'max_size_bytes': {'key': 'properties.maxSizeBytes', 'type': 'long'},
        'collation': {'key': 'properties.collation', 'type': 'str'},
        'source_database_id': {'key': 'properties.sourceDatabaseId', 'type': 'str'},
        'recoverable_database_id': {'key': 'properties.recoverableDatabaseId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'restore_point_in_time': {'key': 'properties.restorePointInTime', 'type': 'iso-8601'},
        'create_mode': {'key': 'properties.createMode', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
    }

    def __init__(self, *, tags=None, location: str=None, sku=None, max_size_bytes: int=None, collation: str=None, source_database_id: str=None, recoverable_database_id: str=None, provisioning_state: str=None, status: str=None, restore_point_in_time=None, create_mode: str=None, creation_date=None, **kwargs) -> None:
        super(SqlPoolPatchInfo, self).__init__(**kwargs)
        self.tags = tags
        self.location = location
        self.sku = sku
        self.max_size_bytes = max_size_bytes
        self.collation = collation
        self.source_database_id = source_database_id
        self.recoverable_database_id = recoverable_database_id
        self.provisioning_state = provisioning_state
        self.status = status
        self.restore_point_in_time = restore_point_in_time
        self.create_mode = create_mode
        self.creation_date = creation_date

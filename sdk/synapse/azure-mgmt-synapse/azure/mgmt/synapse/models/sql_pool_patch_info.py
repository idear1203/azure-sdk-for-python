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

    def __init__(self, **kwargs):
        super(SqlPoolPatchInfo, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.location = kwargs.get('location', None)
        self.sku = kwargs.get('sku', None)
        self.max_size_bytes = kwargs.get('max_size_bytes', None)
        self.collation = kwargs.get('collation', None)
        self.source_database_id = kwargs.get('source_database_id', None)
        self.recoverable_database_id = kwargs.get('recoverable_database_id', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.status = kwargs.get('status', None)
        self.restore_point_in_time = kwargs.get('restore_point_in_time', None)
        self.create_mode = kwargs.get('create_mode', None)
        self.creation_date = kwargs.get('creation_date', None)

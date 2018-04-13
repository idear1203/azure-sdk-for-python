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


class PerformanceTierProperties(Model):
    """Performance tier properties.

    :param id: ID of the performance tier.
    :type id: str
    :param backup_retention_days: Backup retention in days for the performance
     tier edition
    :type backup_retention_days: int
    :param service_level_objectives: Service level objectives associated with
     the performance tier
    :type service_level_objectives:
     list[~azure.mgmt.rdbms.postgres.models.PerformanceTierServiceLevelObjectives]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'backup_retention_days': {'key': 'backupRetentionDays', 'type': 'int'},
        'service_level_objectives': {'key': 'serviceLevelObjectives', 'type': '[PerformanceTierServiceLevelObjectives]'},
    }

    def __init__(self, **kwargs):
        super(PerformanceTierProperties, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.backup_retention_days = kwargs.get('backup_retention_days', None)
        self.service_level_objectives = kwargs.get('service_level_objectives', None)

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


class PerformanceTierServiceLevelObjectives(Model):
    """Service level objectives for performance tier.

    :param id: ID for the service level objective.
    :type id: str
    :param edition: Edition of the performance tier.
    :type edition: str
    :param dtu: Database throughput unit associated with the service level
     objective
    :type dtu: int
    :param storage_mb: Maximum storage in MB associated with the service level
     objective
    :type storage_mb: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'edition': {'key': 'edition', 'type': 'str'},
        'dtu': {'key': 'dtu', 'type': 'int'},
        'storage_mb': {'key': 'storageMB', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(PerformanceTierServiceLevelObjectives, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.edition = kwargs.get('edition', None)
        self.dtu = kwargs.get('dtu', None)
        self.storage_mb = kwargs.get('storage_mb', None)

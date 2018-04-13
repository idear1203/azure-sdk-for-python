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


class Operation(Model):
    """REST API operation definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the operation being performed on this particular
     object.
    :vartype name: str
    :ivar display: The localized display information for this particular
     operation or action.
    :vartype display: ~azure.mgmt.rdbms.postgres.models.OperationDisplay
    :ivar origin: The intended executor of the operation. Possible values
     include: 'NotSpecified', 'user', 'system'
    :vartype origin: str or ~azure.mgmt.rdbms.postgres.models.OperationOrigin
    :ivar properties: Additional descriptions for the operation.
    :vartype properties: dict[str, object]
    """

    _validation = {
        'name': {'readonly': True},
        'display': {'readonly': True},
        'origin': {'readonly': True},
        'properties': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{object}'},
    }

    def __init__(self, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = None
        self.origin = None
        self.properties = None

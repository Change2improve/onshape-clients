# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.113
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import
import re  # noqa: F401
import sys  # noqa: F401

import six  # noqa: F401
import nulltype  # noqa: F401

from onshape_client.oas.model_utils import (  # noqa: F401
    ModelComposed,
    ModelNormal,
    ModelSimple,
    date,
    datetime,
    file_type,
    int,
    none_type,
    str,
    validate_get_composed_info,
)
try:
    from onshape_client.oas.models import bt_diff_info
except ImportError:
    bt_diff_info = sys.modules[
        'onshape_client.oas.models.bt_diff_info']


class BTRootDiffInfo(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('entity_type',): {
            'PARTS': "PARTS",
            'SKETCHES': "SKETCHES",
            'POINTS': "POINTS",
            'MATE_CONNECTORS': "MATE_CONNECTORS",
            'PLANES': "PLANES",
            'CURVES': "CURVES",
            'SURFACES': "SURFACES",
        },
        ('type',): {
            'NONE': "NONE",
            'MOVED': "MOVED",
            'MODIFIED': "MODIFIED",
            'MOVED_AND_MODIFIED': "MOVED_AND_MODIFIED",
            'ADDED': "ADDED",
            'DELETED': "DELETED",
            'UNKNOWN': "UNKNOWN",
        },
    }

    validations = {
    }

    additional_properties_type = None

    @staticmethod
    def openapi_types():
        """
        This must be a class method so a model may have properties that are
        of type self, this ensures that we don't create a cyclic import

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'changes': ({str: (bt_diff_info.BTDiffInfo,)},),  # noqa: E501
            'collection_changes': ({str: ([bt_diff_info.BTDiffInfo],)},),  # noqa: E501
            'entity_type': (str,),  # noqa: E501
            'geometry_change_messages': ([str],),  # noqa: E501
            'source_configuration': (str,),  # noqa: E501
            'source_id': (str,),  # noqa: E501
            'source_microversion_id': (str,),  # noqa: E501
            'source_value': (str,),  # noqa: E501
            'source_version_id': (str,),  # noqa: E501
            'source_workspace_id': (str,),  # noqa: E501
            'target_configuration': (str,),  # noqa: E501
            'target_id': (str,),  # noqa: E501
            'target_microversion_id': (str,),  # noqa: E501
            'target_value': (str,),  # noqa: E501
            'target_version_id': (str,),  # noqa: E501
            'target_workspace_id': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        'changes': 'changes',  # noqa: E501
        'collection_changes': 'collectionChanges',  # noqa: E501
        'entity_type': 'entityType',  # noqa: E501
        'geometry_change_messages': 'geometryChangeMessages',  # noqa: E501
        'source_configuration': 'sourceConfiguration',  # noqa: E501
        'source_id': 'sourceId',  # noqa: E501
        'source_microversion_id': 'sourceMicroversionId',  # noqa: E501
        'source_value': 'sourceValue',  # noqa: E501
        'source_version_id': 'sourceVersionId',  # noqa: E501
        'source_workspace_id': 'sourceWorkspaceId',  # noqa: E501
        'target_configuration': 'targetConfiguration',  # noqa: E501
        'target_id': 'targetId',  # noqa: E501
        'target_microversion_id': 'targetMicroversionId',  # noqa: E501
        'target_value': 'targetValue',  # noqa: E501
        'target_version_id': 'targetVersionId',  # noqa: E501
        'target_workspace_id': 'targetWorkspaceId',  # noqa: E501
        'type': 'type',  # noqa: E501
    }

    @staticmethod
    def _composed_schemas():
        return None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_from_server',
        '_path_to_item',
        '_configuration',
    ])

    def __init__(self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs):  # noqa: E501
        """bt_root_diff_info.BTRootDiffInfo - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _from_server (bool): True if the data is from the server
                                False if the data is from the client (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            changes ({str: (bt_diff_info.BTDiffInfo,)}): [optional]  # noqa: E501
            collection_changes ({str: ([bt_diff_info.BTDiffInfo],)}): [optional]  # noqa: E501
            entity_type (str): [optional]  # noqa: E501
            geometry_change_messages ([str]): [optional]  # noqa: E501
            source_configuration (str): [optional]  # noqa: E501
            source_id (str): [optional]  # noqa: E501
            source_microversion_id (str): [optional]  # noqa: E501
            source_value (str): [optional]  # noqa: E501
            source_version_id (str): [optional]  # noqa: E501
            source_workspace_id (str): [optional]  # noqa: E501
            target_configuration (str): [optional]  # noqa: E501
            target_id (str): [optional]  # noqa: E501
            target_microversion_id (str): [optional]  # noqa: E501
            target_value (str): [optional]  # noqa: E501
            target_version_id (str): [optional]  # noqa: E501
            target_workspace_id (str): [optional]  # noqa: E501
            type (str): [optional]  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration

        for var_name, var_value in six.iteritems(kwargs):
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

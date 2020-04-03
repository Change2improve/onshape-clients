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
    from onshape_client.oas.models import header
except ImportError:
    header = sys.modules[
        'onshape_client.oas.models.header']
try:
    from onshape_client.oas.models import server
except ImportError:
    server = sys.modules[
        'onshape_client.oas.models.server']


class Link(ModelNormal):
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
            'description': (str,),  # noqa: E501
            'extensions': ({str: (bool, date, datetime, dict, float, int, list, str,)},),  # noqa: E501
            'getref': (str,),  # noqa: E501
            'headers': ({str: (header.Header,)},),  # noqa: E501
            'operation_id': (str,),  # noqa: E501
            'operation_ref': (str,),  # noqa: E501
            'parameters': ({str: (str,)},),  # noqa: E501
            'request_body': (bool, date, datetime, dict, float, int, list, str,),  # noqa: E501
            'server': (server.Server,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        'description': 'description',  # noqa: E501
        'extensions': 'extensions',  # noqa: E501
        'getref': 'get$ref',  # noqa: E501
        'headers': 'headers',  # noqa: E501
        'operation_id': 'operationId',  # noqa: E501
        'operation_ref': 'operationRef',  # noqa: E501
        'parameters': 'parameters',  # noqa: E501
        'request_body': 'requestBody',  # noqa: E501
        'server': 'server',  # noqa: E501
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
        """link.Link - a model defined in OpenAPI


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
            description (str): [optional]  # noqa: E501
            extensions ({str: (bool, date, datetime, dict, float, int, list, str,)}): [optional]  # noqa: E501
            getref (str): [optional]  # noqa: E501
            headers ({str: (header.Header,)}): [optional]  # noqa: E501
            operation_id (str): [optional]  # noqa: E501
            operation_ref (str): [optional]  # noqa: E501
            parameters ({str: (str,)}): [optional]  # noqa: E501
            request_body (bool, date, datetime, dict, float, int, list, str): [optional]  # noqa: E501
            server (server.Server): [optional]  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration

        for var_name, var_value in six.iteritems(kwargs):
            setattr(self, var_name, var_value)

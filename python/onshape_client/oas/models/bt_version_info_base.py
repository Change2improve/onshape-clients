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
    from onshape_client.oas.models import bt_base_info
except ImportError:
    bt_base_info = sys.modules[
        'onshape_client.oas.models.bt_base_info']
try:
    from onshape_client.oas.models import bt_thumbnail_info
except ImportError:
    bt_thumbnail_info = sys.modules[
        'onshape_client.oas.models.bt_thumbnail_info']
try:
    from onshape_client.oas.models import bt_user_basic_summary_info
except ImportError:
    bt_user_basic_summary_info = sys.modules[
        'onshape_client.oas.models.bt_user_basic_summary_info']
try:
    from onshape_client.oas.models import bt_version_info
except ImportError:
    bt_version_info = sys.modules[
        'onshape_client.oas.models.bt_version_info']
try:
    from onshape_client.oas.models import bt_version_info_base_all_of
except ImportError:
    bt_version_info_base_all_of = sys.modules[
        'onshape_client.oas.models.bt_version_info_base_all_of']
try:
    from onshape_client.oas.models import bt_workspace_info
except ImportError:
    bt_workspace_info = sys.modules[
        'onshape_client.oas.models.bt_workspace_info']


class BTVersionInfoBase(ModelComposed):
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
            'type': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'modified_at': (datetime,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'last_modifier': (bt_user_basic_summary_info.BTUserBasicSummaryInfo,),  # noqa: E501
            'document_id': (str,),  # noqa: E501
            'creator': (bt_user_basic_summary_info.BTUserBasicSummaryInfo,),  # noqa: E501
            'thumbnail': (bt_thumbnail_info.BTThumbnailInfo,),  # noqa: E501
            'microversion': (str,),  # noqa: E501
            'parents': ([bt_version_info.BTVersionInfo],),  # noqa: E501
            'override_date': (datetime,),  # noqa: E501
            'parent': (str,),  # noqa: E501
            'href': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'json_type': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'view_ref': (str,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return {
            'type': {
                'BTWorkspaceInfo': bt_workspace_info.BTWorkspaceInfo,
                'BTVersionInfo': bt_version_info.BTVersionInfo,
            },
        }

    attribute_map = {
        'type': 'type',  # noqa: E501
        'description': 'description',  # noqa: E501
        'modified_at': 'modifiedAt',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'last_modifier': 'lastModifier',  # noqa: E501
        'document_id': 'documentId',  # noqa: E501
        'creator': 'creator',  # noqa: E501
        'thumbnail': 'thumbnail',  # noqa: E501
        'microversion': 'microversion',  # noqa: E501
        'parents': 'parents',  # noqa: E501
        'override_date': 'overrideDate',  # noqa: E501
        'parent': 'parent',  # noqa: E501
        'href': 'href',  # noqa: E501
        'id': 'id',  # noqa: E501
        'json_type': 'jsonType',  # noqa: E501
        'name': 'name',  # noqa: E501
        'view_ref': 'viewRef',  # noqa: E501
    }

    required_properties = set([
        '_data_store',
        '_check_type',
        '_from_server',
        '_path_to_item',
        '_configuration',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    def __init__(self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs):  # noqa: E501
        """bt_version_info_base.BTVersionInfoBase - a model defined in OpenAPI

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
            type (str): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            modified_at (datetime): [optional]  # noqa: E501
            created_at (datetime): [optional]  # noqa: E501
            last_modifier (bt_user_basic_summary_info.BTUserBasicSummaryInfo): [optional]  # noqa: E501
            document_id (str): [optional]  # noqa: E501
            creator (bt_user_basic_summary_info.BTUserBasicSummaryInfo): [optional]  # noqa: E501
            thumbnail (bt_thumbnail_info.BTThumbnailInfo): [optional]  # noqa: E501
            microversion (str): [optional]  # noqa: E501
            parents ([bt_version_info.BTVersionInfo]): [optional]  # noqa: E501
            override_date (datetime): [optional]  # noqa: E501
            parent (str): [optional]  # noqa: E501
            href (str): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            json_type (str): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            view_ref (str): [optional]  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_from_server': _from_server,
            '_configuration': _configuration,
        }
        required_args = {
        }
        # remove args whose value is Null because they are unset
        required_arg_names = list(required_args.keys())
        for required_arg_name in required_arg_names:
            if required_args[required_arg_name] is nulltype.Null:
                del required_args[required_arg_name]
        model_args = {}
        model_args.update(required_args)
        model_args.update(kwargs)
        composed_info = validate_get_composed_info(
            constant_args, model_args, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        unused_args = composed_info[3]

        for var_name, var_value in required_args.items():
            setattr(self, var_name, var_value)
        for var_name, var_value in six.iteritems(kwargs):
            if var_name in unused_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        not self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

    @staticmethod
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error beause the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        return {
          'anyOf': [
          ],
          'allOf': [
              bt_base_info.BTBaseInfo,
              bt_version_info_base_all_of.BTVersionInfoBaseAllOf,
          ],
          'oneOf': [
          ],
        }

    @classmethod
    def get_discriminator_class(cls, from_server, data):
        """Returns the child class specified by the discriminator"""
        discriminator = cls.discriminator()
        discr_propertyname_py = list(discriminator.keys())[0]
        discr_propertyname_js = cls.attribute_map[discr_propertyname_py]
        if from_server:
            class_name = data[discr_propertyname_js]
        else:
            class_name = data[discr_propertyname_py]
        class_name_to_discr_class = discriminator[discr_propertyname_py]
        return class_name_to_discr_class.get(class_name)

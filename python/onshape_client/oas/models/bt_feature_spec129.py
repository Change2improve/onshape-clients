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
    from onshape_client.oas.models import bt_editing_logic2350
except ImportError:
    bt_editing_logic2350 = sys.modules[
        'onshape_client.oas.models.bt_editing_logic2350']
try:
    from onshape_client.oas.models import bt_location_info226
except ImportError:
    bt_location_info226 = sys.modules[
        'onshape_client.oas.models.bt_location_info226']
try:
    from onshape_client.oas.models import bt_parameter_group_spec3469
except ImportError:
    bt_parameter_group_spec3469 = sys.modules[
        'onshape_client.oas.models.bt_parameter_group_spec3469']
try:
    from onshape_client.oas.models import bt_parameter_spec6
except ImportError:
    bt_parameter_spec6 = sys.modules[
        'onshape_client.oas.models.bt_parameter_spec6']
try:
    from onshape_client.oas.models import bt_table_spec915
except ImportError:
    bt_table_spec915 = sys.modules[
        'onshape_client.oas.models.bt_table_spec915']


class BTFeatureSpec129(ModelNormal):
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
        ('ui_hints',): {
            'OPPOSITE_DIRECTION': "OPPOSITE_DIRECTION",
            'ALWAYS_HIDDEN': "ALWAYS_HIDDEN",
            'SHOW_CREATE_SELECTION': "SHOW_CREATE_SELECTION",
            'CONTROL_VISIBILITY': "CONTROL_VISIBILITY",
            'NO_PREVIEW_PROVIDED': "NO_PREVIEW_PROVIDED",
            'REMEMBER_PREVIOUS_VALUE': "REMEMBER_PREVIOUS_VALUE",
            'DISPLAY_SHORT': "DISPLAY_SHORT",
            'ALLOW_FEATURE_SELECTION': "ALLOW_FEATURE_SELECTION",
            'MATE_CONNECTOR_AXIS_TYPE': "MATE_CONNECTOR_AXIS_TYPE",
            'PRIMARY_AXIS': "PRIMARY_AXIS",
            'SHOW_EXPRESSION': "SHOW_EXPRESSION",
            'OPPOSITE_DIRECTION_CIRCULAR': "OPPOSITE_DIRECTION_CIRCULAR",
            'SHOW_LABEL': "SHOW_LABEL",
            'HORIZONTAL_ENUM': "HORIZONTAL_ENUM",
            'UNCONFIGURABLE': "UNCONFIGURABLE",
            'MATCH_LAST_ARRAY_ITEM': "MATCH_LAST_ARRAY_ITEM",
            'COLLAPSE_ARRAY_ITEMS': "COLLAPSE_ARRAY_ITEMS",
            'INITIAL_FOCUS_ON_EDIT': "INITIAL_FOCUS_ON_EDIT",
            'INITIAL_FOCUS': "INITIAL_FOCUS",
            'DISPLAY_CURRENT_VALUE_ONLY': "DISPLAY_CURRENT_VALUE_ONLY",
            'READ_ONLY': "READ_ONLY",
            'PREVENT_CREATING_NEW_MATE_CONNECTORS': "PREVENT_CREATING_NEW_MATE_CONNECTORS",
            'FIRST_IN_ROW': "FIRST_IN_ROW",
            'ALLOW_QUERY_ORDER': "ALLOW_QUERY_ORDER",
            'PREVENT_ARRAY_REORDER': "PREVENT_ARRAY_REORDER",
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
            'additional_localized_strings': (int,),  # noqa: E501
            'all_parameters': ([bt_parameter_spec6.BTParameterSpec6],),  # noqa: E501
            'bt_type': (str,),  # noqa: E501
            'editing_logic': (bt_editing_logic2350.BTEditingLogic2350,),  # noqa: E501
            'feature_name_template': (str,),  # noqa: E501
            'feature_type': (str,),  # noqa: E501
            'feature_type_name': (str,),  # noqa: E501
            'filter_selectors': ([str],),  # noqa: E501
            'full_feature_type': (str,),  # noqa: E501
            'groups': ([bt_parameter_group_spec3469.BTParameterGroupSpec3469],),  # noqa: E501
            'icon_uri': (str,),  # noqa: E501
            'language_version': (int,),  # noqa: E501
            'linked_location_name': (str,),  # noqa: E501
            'localizable_name': (str,),  # noqa: E501
            'localized_name': (str,),  # noqa: E501
            'location_infos': ([bt_location_info226.BTLocationInfo226],),  # noqa: E501
            'manipulator_change_function': (str,),  # noqa: E501
            'namespace': (str,),  # noqa: E501
            'namespace_including_enums': (str,),  # noqa: E501
            'namespace_the_source': (bool,),  # noqa: E501
            'parameters': ([bt_parameter_spec6.BTParameterSpec6],),  # noqa: E501
            'signature': (str,),  # noqa: E501
            'source_location': (bt_location_info226.BTLocationInfo226,),  # noqa: E501
            'source_microversion_id': (str,),  # noqa: E501
            'strings_to_localize': ([str],),  # noqa: E501
            'table_spec': (bool,),  # noqa: E501
            'ui_hints': ([str],),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return {
            'bt_type': {
                'BTTableSpec-915': bt_table_spec915.BTTableSpec915,
            },
        }

    attribute_map = {
        'additional_localized_strings': 'additionalLocalizedStrings',  # noqa: E501
        'all_parameters': 'allParameters',  # noqa: E501
        'bt_type': 'btType',  # noqa: E501
        'editing_logic': 'editingLogic',  # noqa: E501
        'feature_name_template': 'featureNameTemplate',  # noqa: E501
        'feature_type': 'featureType',  # noqa: E501
        'feature_type_name': 'featureTypeName',  # noqa: E501
        'filter_selectors': 'filterSelectors',  # noqa: E501
        'full_feature_type': 'fullFeatureType',  # noqa: E501
        'groups': 'groups',  # noqa: E501
        'icon_uri': 'iconUri',  # noqa: E501
        'language_version': 'languageVersion',  # noqa: E501
        'linked_location_name': 'linkedLocationName',  # noqa: E501
        'localizable_name': 'localizableName',  # noqa: E501
        'localized_name': 'localizedName',  # noqa: E501
        'location_infos': 'locationInfos',  # noqa: E501
        'manipulator_change_function': 'manipulatorChangeFunction',  # noqa: E501
        'namespace': 'namespace',  # noqa: E501
        'namespace_including_enums': 'namespaceIncludingEnums',  # noqa: E501
        'namespace_the_source': 'namespaceTheSource',  # noqa: E501
        'parameters': 'parameters',  # noqa: E501
        'signature': 'signature',  # noqa: E501
        'source_location': 'sourceLocation',  # noqa: E501
        'source_microversion_id': 'sourceMicroversionId',  # noqa: E501
        'strings_to_localize': 'stringsToLocalize',  # noqa: E501
        'table_spec': 'tableSpec',  # noqa: E501
        'ui_hints': 'uiHints',  # noqa: E501
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
        """bt_feature_spec129.BTFeatureSpec129 - a model defined in OpenAPI

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
            additional_localized_strings (int): [optional]  # noqa: E501
            all_parameters ([bt_parameter_spec6.BTParameterSpec6]): [optional]  # noqa: E501
            bt_type (str): [optional]  # noqa: E501
            editing_logic (bt_editing_logic2350.BTEditingLogic2350): [optional]  # noqa: E501
            feature_name_template (str): [optional]  # noqa: E501
            feature_type (str): [optional]  # noqa: E501
            feature_type_name (str): [optional]  # noqa: E501
            filter_selectors ([str]): [optional]  # noqa: E501
            full_feature_type (str): [optional]  # noqa: E501
            groups ([bt_parameter_group_spec3469.BTParameterGroupSpec3469]): [optional]  # noqa: E501
            icon_uri (str): [optional]  # noqa: E501
            language_version (int): [optional]  # noqa: E501
            linked_location_name (str): [optional]  # noqa: E501
            localizable_name (str): [optional]  # noqa: E501
            localized_name (str): [optional]  # noqa: E501
            location_infos ([bt_location_info226.BTLocationInfo226]): [optional]  # noqa: E501
            manipulator_change_function (str): [optional]  # noqa: E501
            namespace (str): [optional]  # noqa: E501
            namespace_including_enums (str): [optional]  # noqa: E501
            namespace_the_source (bool): [optional]  # noqa: E501
            parameters ([bt_parameter_spec6.BTParameterSpec6]): [optional]  # noqa: E501
            signature (str): [optional]  # noqa: E501
            source_location (bt_location_info226.BTLocationInfo226): [optional]  # noqa: E501
            source_microversion_id (str): [optional]  # noqa: E501
            strings_to_localize ([str]): [optional]  # noqa: E501
            table_spec (bool): [optional]  # noqa: E501
            ui_hints ([str]): [optional]  # noqa: E501
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

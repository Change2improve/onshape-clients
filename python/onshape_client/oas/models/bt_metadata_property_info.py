# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.104
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTMetadataPropertyInfo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'required': 'bool',
        'validator': 'BTMetadataPropertyValidatorInfo',
        'property_source': 'int',
        'property_id': 'str',
        'editable': 'bool',
        'value_type': 'str',
        'schema_id': 'str',
        'enum_values': 'list[BTMetadataEnumValueInfo]',
        'initial_value': 'object',
        'editable_in_ui': 'bool',
        'ui_hints': 'BTMetadataPropertyUiHintsInfo',
        'dirty': 'bool',
        'name': 'str',
        'default_value': 'object'
    }

    attribute_map = {
        'required': 'required',
        'validator': 'validator',
        'property_source': 'propertySource',
        'property_id': 'propertyId',
        'editable': 'editable',
        'value_type': 'valueType',
        'schema_id': 'schemaId',
        'enum_values': 'enumValues',
        'initial_value': 'initialValue',
        'editable_in_ui': 'editableInUi',
        'ui_hints': 'uiHints',
        'dirty': 'dirty',
        'name': 'name',
        'default_value': 'defaultValue'
    }

    def __init__(self, required=None, validator=None, property_source=None, property_id=None, editable=None, value_type=None, schema_id=None, enum_values=None, initial_value=None, editable_in_ui=None, ui_hints=None, dirty=None, name=None, default_value=None):  # noqa: E501
        """BTMetadataPropertyInfo - a model defined in OpenAPI"""  # noqa: E501

        self._required = None
        self._validator = None
        self._property_source = None
        self._property_id = None
        self._editable = None
        self._value_type = None
        self._schema_id = None
        self._enum_values = None
        self._initial_value = None
        self._editable_in_ui = None
        self._ui_hints = None
        self._dirty = None
        self._name = None
        self._default_value = None
        self.discriminator = None

        if required is not None:
            self.required = required
        if validator is not None:
            self.validator = validator
        if property_source is not None:
            self.property_source = property_source
        if property_id is not None:
            self.property_id = property_id
        if editable is not None:
            self.editable = editable
        if value_type is not None:
            self.value_type = value_type
        if schema_id is not None:
            self.schema_id = schema_id
        if enum_values is not None:
            self.enum_values = enum_values
        if initial_value is not None:
            self.initial_value = initial_value
        if editable_in_ui is not None:
            self.editable_in_ui = editable_in_ui
        if ui_hints is not None:
            self.ui_hints = ui_hints
        if dirty is not None:
            self.dirty = dirty
        if name is not None:
            self.name = name
        if default_value is not None:
            self.default_value = default_value

    @property
    def required(self):
        """Gets the required of this BTMetadataPropertyInfo.  # noqa: E501


        :return: The required of this BTMetadataPropertyInfo.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this BTMetadataPropertyInfo.


        :param required: The required of this BTMetadataPropertyInfo.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def validator(self):
        """Gets the validator of this BTMetadataPropertyInfo.  # noqa: E501


        :return: The validator of this BTMetadataPropertyInfo.  # noqa: E501
        :rtype: BTMetadataPropertyValidatorInfo
        """
        return self._validator

    @validator.setter
    def validator(self, validator):
        """Sets the validator of this BTMetadataPropertyInfo.


        :param validator: The validator of this BTMetadataPropertyInfo.  # noqa: E501
        :type: BTMetadataPropertyValidatorInfo
        """

        self._validator = validator

    @property
    def property_source(self):
        """Gets the property_source of this BTMetadataPropertyInfo.  # noqa: E501


        :return: The property_source of this BTMetadataPropertyInfo.  # noqa: E501
        :rtype: int
        """
        return self._property_source

    @property_source.setter
    def property_source(self, property_source):
        """Sets the property_source of this BTMetadataPropertyInfo.


        :param property_source: The property_source of this BTMetadataPropertyInfo.  # noqa: E501
        :type: int
        """

        self._property_source = property_source

    @property
    def property_id(self):
        """Gets the property_id of this BTMetadataPropertyInfo.  # noqa: E501


        :return: The property_id of this BTMetadataPropertyInfo.  # noqa: E501
        :rtype: str
        """
        return self._property_id

    @property_id.setter
    def property_id(self, property_id):
        """Sets the property_id of this BTMetadataPropertyInfo.


        :param property_id: The property_id of this BTMetadataPropertyInfo.  # noqa: E501
        :type: str
        """

        self._property_id = property_id

    @property
    def editable(self):
        """Gets the editable of this BTMetadataPropertyInfo.  # noqa: E501


        :return: The editable of this BTMetadataPropertyInfo.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this BTMetadataPropertyInfo.


        :param editable: The editable of this BTMetadataPropertyInfo.  # noqa: E501
        :type: bool
        """

        self._editable = editable

    @property
    def value_type(self):
        """Gets the value_type of this BTMetadataPropertyInfo.  # noqa: E501


        :return: The value_type of this BTMetadataPropertyInfo.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this BTMetadataPropertyInfo.


        :param value_type: The value_type of this BTMetadataPropertyInfo.  # noqa: E501
        :type: str
        """

        self._value_type = value_type

    @property
    def schema_id(self):
        """Gets the schema_id of this BTMetadataPropertyInfo.  # noqa: E501


        :return: The schema_id of this BTMetadataPropertyInfo.  # noqa: E501
        :rtype: str
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        """Sets the schema_id of this BTMetadataPropertyInfo.


        :param schema_id: The schema_id of this BTMetadataPropertyInfo.  # noqa: E501
        :type: str
        """

        self._schema_id = schema_id

    @property
    def enum_values(self):
        """Gets the enum_values of this BTMetadataPropertyInfo.  # noqa: E501


        :return: The enum_values of this BTMetadataPropertyInfo.  # noqa: E501
        :rtype: list[BTMetadataEnumValueInfo]
        """
        return self._enum_values

    @enum_values.setter
    def enum_values(self, enum_values):
        """Sets the enum_values of this BTMetadataPropertyInfo.


        :param enum_values: The enum_values of this BTMetadataPropertyInfo.  # noqa: E501
        :type: list[BTMetadataEnumValueInfo]
        """

        self._enum_values = enum_values

    @property
    def initial_value(self):
        """Gets the initial_value of this BTMetadataPropertyInfo.  # noqa: E501


        :return: The initial_value of this BTMetadataPropertyInfo.  # noqa: E501
        :rtype: object
        """
        return self._initial_value

    @initial_value.setter
    def initial_value(self, initial_value):
        """Sets the initial_value of this BTMetadataPropertyInfo.


        :param initial_value: The initial_value of this BTMetadataPropertyInfo.  # noqa: E501
        :type: object
        """

        self._initial_value = initial_value

    @property
    def editable_in_ui(self):
        """Gets the editable_in_ui of this BTMetadataPropertyInfo.  # noqa: E501


        :return: The editable_in_ui of this BTMetadataPropertyInfo.  # noqa: E501
        :rtype: bool
        """
        return self._editable_in_ui

    @editable_in_ui.setter
    def editable_in_ui(self, editable_in_ui):
        """Sets the editable_in_ui of this BTMetadataPropertyInfo.


        :param editable_in_ui: The editable_in_ui of this BTMetadataPropertyInfo.  # noqa: E501
        :type: bool
        """

        self._editable_in_ui = editable_in_ui

    @property
    def ui_hints(self):
        """Gets the ui_hints of this BTMetadataPropertyInfo.  # noqa: E501


        :return: The ui_hints of this BTMetadataPropertyInfo.  # noqa: E501
        :rtype: BTMetadataPropertyUiHintsInfo
        """
        return self._ui_hints

    @ui_hints.setter
    def ui_hints(self, ui_hints):
        """Sets the ui_hints of this BTMetadataPropertyInfo.


        :param ui_hints: The ui_hints of this BTMetadataPropertyInfo.  # noqa: E501
        :type: BTMetadataPropertyUiHintsInfo
        """

        self._ui_hints = ui_hints

    @property
    def dirty(self):
        """Gets the dirty of this BTMetadataPropertyInfo.  # noqa: E501


        :return: The dirty of this BTMetadataPropertyInfo.  # noqa: E501
        :rtype: bool
        """
        return self._dirty

    @dirty.setter
    def dirty(self, dirty):
        """Sets the dirty of this BTMetadataPropertyInfo.


        :param dirty: The dirty of this BTMetadataPropertyInfo.  # noqa: E501
        :type: bool
        """

        self._dirty = dirty

    @property
    def name(self):
        """Gets the name of this BTMetadataPropertyInfo.  # noqa: E501


        :return: The name of this BTMetadataPropertyInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTMetadataPropertyInfo.


        :param name: The name of this BTMetadataPropertyInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def default_value(self):
        """Gets the default_value of this BTMetadataPropertyInfo.  # noqa: E501


        :return: The default_value of this BTMetadataPropertyInfo.  # noqa: E501
        :rtype: object
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this BTMetadataPropertyInfo.


        :param default_value: The default_value of this BTMetadataPropertyInfo.  # noqa: E501
        :type: object
        """

        self._default_value = default_value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BTMetadataPropertyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

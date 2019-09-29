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


class BTStandardContentHierarchyParams(object):
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
        'types': 'str',
        'component_document_id': 'str',
        'disable_production': 'bool',
        'production_version_id': 'str',
        'test_version_id': 'str',
        'category': 'str',
        'standard': 'str',
        'type': 'str'
    }

    attribute_map = {
        'types': 'types',
        'component_document_id': 'componentDocumentId',
        'disable_production': 'disableProduction',
        'production_version_id': 'productionVersionId',
        'test_version_id': 'testVersionId',
        'category': 'category',
        'standard': 'standard',
        'type': 'type'
    }

    def __init__(self, types=None, component_document_id=None, disable_production=None, production_version_id=None, test_version_id=None, category=None, standard=None, type=None):  # noqa: E501
        """BTStandardContentHierarchyParams - a model defined in OpenAPI"""  # noqa: E501

        self._types = None
        self._component_document_id = None
        self._disable_production = None
        self._production_version_id = None
        self._test_version_id = None
        self._category = None
        self._standard = None
        self._type = None
        self.discriminator = None

        if types is not None:
            self.types = types
        if component_document_id is not None:
            self.component_document_id = component_document_id
        if disable_production is not None:
            self.disable_production = disable_production
        if production_version_id is not None:
            self.production_version_id = production_version_id
        if test_version_id is not None:
            self.test_version_id = test_version_id
        if category is not None:
            self.category = category
        if standard is not None:
            self.standard = standard
        if type is not None:
            self.type = type

    @property
    def types(self):
        """Gets the types of this BTStandardContentHierarchyParams.  # noqa: E501


        :return: The types of this BTStandardContentHierarchyParams.  # noqa: E501
        :rtype: str
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this BTStandardContentHierarchyParams.


        :param types: The types of this BTStandardContentHierarchyParams.  # noqa: E501
        :type: str
        """

        self._types = types

    @property
    def component_document_id(self):
        """Gets the component_document_id of this BTStandardContentHierarchyParams.  # noqa: E501


        :return: The component_document_id of this BTStandardContentHierarchyParams.  # noqa: E501
        :rtype: str
        """
        return self._component_document_id

    @component_document_id.setter
    def component_document_id(self, component_document_id):
        """Sets the component_document_id of this BTStandardContentHierarchyParams.


        :param component_document_id: The component_document_id of this BTStandardContentHierarchyParams.  # noqa: E501
        :type: str
        """

        self._component_document_id = component_document_id

    @property
    def disable_production(self):
        """Gets the disable_production of this BTStandardContentHierarchyParams.  # noqa: E501


        :return: The disable_production of this BTStandardContentHierarchyParams.  # noqa: E501
        :rtype: bool
        """
        return self._disable_production

    @disable_production.setter
    def disable_production(self, disable_production):
        """Sets the disable_production of this BTStandardContentHierarchyParams.


        :param disable_production: The disable_production of this BTStandardContentHierarchyParams.  # noqa: E501
        :type: bool
        """

        self._disable_production = disable_production

    @property
    def production_version_id(self):
        """Gets the production_version_id of this BTStandardContentHierarchyParams.  # noqa: E501


        :return: The production_version_id of this BTStandardContentHierarchyParams.  # noqa: E501
        :rtype: str
        """
        return self._production_version_id

    @production_version_id.setter
    def production_version_id(self, production_version_id):
        """Sets the production_version_id of this BTStandardContentHierarchyParams.


        :param production_version_id: The production_version_id of this BTStandardContentHierarchyParams.  # noqa: E501
        :type: str
        """

        self._production_version_id = production_version_id

    @property
    def test_version_id(self):
        """Gets the test_version_id of this BTStandardContentHierarchyParams.  # noqa: E501


        :return: The test_version_id of this BTStandardContentHierarchyParams.  # noqa: E501
        :rtype: str
        """
        return self._test_version_id

    @test_version_id.setter
    def test_version_id(self, test_version_id):
        """Sets the test_version_id of this BTStandardContentHierarchyParams.


        :param test_version_id: The test_version_id of this BTStandardContentHierarchyParams.  # noqa: E501
        :type: str
        """

        self._test_version_id = test_version_id

    @property
    def category(self):
        """Gets the category of this BTStandardContentHierarchyParams.  # noqa: E501


        :return: The category of this BTStandardContentHierarchyParams.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this BTStandardContentHierarchyParams.


        :param category: The category of this BTStandardContentHierarchyParams.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def standard(self):
        """Gets the standard of this BTStandardContentHierarchyParams.  # noqa: E501


        :return: The standard of this BTStandardContentHierarchyParams.  # noqa: E501
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        """Sets the standard of this BTStandardContentHierarchyParams.


        :param standard: The standard of this BTStandardContentHierarchyParams.  # noqa: E501
        :type: str
        """

        self._standard = standard

    @property
    def type(self):
        """Gets the type of this BTStandardContentHierarchyParams.  # noqa: E501


        :return: The type of this BTStandardContentHierarchyParams.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BTStandardContentHierarchyParams.


        :param type: The type of this BTStandardContentHierarchyParams.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, BTStandardContentHierarchyParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

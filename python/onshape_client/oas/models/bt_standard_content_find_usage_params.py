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


class BTStandardContentFindUsageParams(object):
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
        'component_document_id': 'str',
        'used_from_in_days': 'str',
        'company_id': 'str',
        'parameters': 'list[BTStandardContentParameterDefinition]',
        'user_id': 'str'
    }

    attribute_map = {
        'component_document_id': 'componentDocumentId',
        'used_from_in_days': 'usedFromInDays',
        'company_id': 'companyId',
        'parameters': 'parameters',
        'user_id': 'userId'
    }

    def __init__(self, component_document_id=None, used_from_in_days=None, company_id=None, parameters=None, user_id=None):  # noqa: E501
        """BTStandardContentFindUsageParams - a model defined in OpenAPI"""  # noqa: E501

        self._component_document_id = None
        self._used_from_in_days = None
        self._company_id = None
        self._parameters = None
        self._user_id = None
        self.discriminator = None

        if component_document_id is not None:
            self.component_document_id = component_document_id
        if used_from_in_days is not None:
            self.used_from_in_days = used_from_in_days
        if company_id is not None:
            self.company_id = company_id
        if parameters is not None:
            self.parameters = parameters
        if user_id is not None:
            self.user_id = user_id

    @property
    def component_document_id(self):
        """Gets the component_document_id of this BTStandardContentFindUsageParams.  # noqa: E501


        :return: The component_document_id of this BTStandardContentFindUsageParams.  # noqa: E501
        :rtype: str
        """
        return self._component_document_id

    @component_document_id.setter
    def component_document_id(self, component_document_id):
        """Sets the component_document_id of this BTStandardContentFindUsageParams.


        :param component_document_id: The component_document_id of this BTStandardContentFindUsageParams.  # noqa: E501
        :type: str
        """

        self._component_document_id = component_document_id

    @property
    def used_from_in_days(self):
        """Gets the used_from_in_days of this BTStandardContentFindUsageParams.  # noqa: E501


        :return: The used_from_in_days of this BTStandardContentFindUsageParams.  # noqa: E501
        :rtype: str
        """
        return self._used_from_in_days

    @used_from_in_days.setter
    def used_from_in_days(self, used_from_in_days):
        """Sets the used_from_in_days of this BTStandardContentFindUsageParams.


        :param used_from_in_days: The used_from_in_days of this BTStandardContentFindUsageParams.  # noqa: E501
        :type: str
        """

        self._used_from_in_days = used_from_in_days

    @property
    def company_id(self):
        """Gets the company_id of this BTStandardContentFindUsageParams.  # noqa: E501


        :return: The company_id of this BTStandardContentFindUsageParams.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this BTStandardContentFindUsageParams.


        :param company_id: The company_id of this BTStandardContentFindUsageParams.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def parameters(self):
        """Gets the parameters of this BTStandardContentFindUsageParams.  # noqa: E501


        :return: The parameters of this BTStandardContentFindUsageParams.  # noqa: E501
        :rtype: list[BTStandardContentParameterDefinition]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this BTStandardContentFindUsageParams.


        :param parameters: The parameters of this BTStandardContentFindUsageParams.  # noqa: E501
        :type: list[BTStandardContentParameterDefinition]
        """

        self._parameters = parameters

    @property
    def user_id(self):
        """Gets the user_id of this BTStandardContentFindUsageParams.  # noqa: E501


        :return: The user_id of this BTStandardContentFindUsageParams.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BTStandardContentFindUsageParams.


        :param user_id: The user_id of this BTStandardContentFindUsageParams.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if not isinstance(other, BTStandardContentFindUsageParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

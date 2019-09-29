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


class UpdateParams(object):
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
        'to_reference': 'BTUniqueDocumentItemParams',
        'from_reference': 'BTUniqueDocumentItemParams',
        'ids_to_update': 'list[str]'
    }

    attribute_map = {
        'to_reference': 'toReference',
        'from_reference': 'fromReference',
        'ids_to_update': 'idsToUpdate'
    }

    def __init__(self, to_reference=None, from_reference=None, ids_to_update=None):  # noqa: E501
        """UpdateParams - a model defined in OpenAPI"""  # noqa: E501

        self._to_reference = None
        self._from_reference = None
        self._ids_to_update = None
        self.discriminator = None

        if to_reference is not None:
            self.to_reference = to_reference
        if from_reference is not None:
            self.from_reference = from_reference
        if ids_to_update is not None:
            self.ids_to_update = ids_to_update

    @property
    def to_reference(self):
        """Gets the to_reference of this UpdateParams.  # noqa: E501


        :return: The to_reference of this UpdateParams.  # noqa: E501
        :rtype: BTUniqueDocumentItemParams
        """
        return self._to_reference

    @to_reference.setter
    def to_reference(self, to_reference):
        """Sets the to_reference of this UpdateParams.


        :param to_reference: The to_reference of this UpdateParams.  # noqa: E501
        :type: BTUniqueDocumentItemParams
        """

        self._to_reference = to_reference

    @property
    def from_reference(self):
        """Gets the from_reference of this UpdateParams.  # noqa: E501


        :return: The from_reference of this UpdateParams.  # noqa: E501
        :rtype: BTUniqueDocumentItemParams
        """
        return self._from_reference

    @from_reference.setter
    def from_reference(self, from_reference):
        """Sets the from_reference of this UpdateParams.


        :param from_reference: The from_reference of this UpdateParams.  # noqa: E501
        :type: BTUniqueDocumentItemParams
        """

        self._from_reference = from_reference

    @property
    def ids_to_update(self):
        """Gets the ids_to_update of this UpdateParams.  # noqa: E501


        :return: The ids_to_update of this UpdateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids_to_update

    @ids_to_update.setter
    def ids_to_update(self, ids_to_update):
        """Sets the ids_to_update of this UpdateParams.


        :param ids_to_update: The ids_to_update of this UpdateParams.  # noqa: E501
        :type: list[str]
        """

        self._ids_to_update = ids_to_update

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
        if not isinstance(other, UpdateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

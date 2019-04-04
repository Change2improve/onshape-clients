# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.96
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTAppElementStartTransactionParams(object):
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
        'return_error': 'bool',
        'parent_change_id': 'str'
    }

    attribute_map = {
        'return_error': 'returnError',
        'parent_change_id': 'parentChangeId'
    }

    def __init__(self, return_error=None, parent_change_id=None):  # noqa: E501
        """BTAppElementStartTransactionParams - a model defined in OpenAPI"""  # noqa: E501

        self._return_error = None
        self._parent_change_id = None
        self.discriminator = None

        if return_error is not None:
            self.return_error = return_error
        if parent_change_id is not None:
            self.parent_change_id = parent_change_id

    @property
    def return_error(self):
        """Gets the return_error of this BTAppElementStartTransactionParams.  # noqa: E501


        :return: The return_error of this BTAppElementStartTransactionParams.  # noqa: E501
        :rtype: bool
        """
        return self._return_error

    @return_error.setter
    def return_error(self, return_error):
        """Sets the return_error of this BTAppElementStartTransactionParams.


        :param return_error: The return_error of this BTAppElementStartTransactionParams.  # noqa: E501
        :type: bool
        """

        self._return_error = return_error

    @property
    def parent_change_id(self):
        """Gets the parent_change_id of this BTAppElementStartTransactionParams.  # noqa: E501


        :return: The parent_change_id of this BTAppElementStartTransactionParams.  # noqa: E501
        :rtype: str
        """
        return self._parent_change_id

    @parent_change_id.setter
    def parent_change_id(self, parent_change_id):
        """Sets the parent_change_id of this BTAppElementStartTransactionParams.


        :param parent_change_id: The parent_change_id of this BTAppElementStartTransactionParams.  # noqa: E501
        :type: str
        """

        self._parent_change_id = parent_change_id

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
        if not isinstance(other, BTAppElementStartTransactionParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

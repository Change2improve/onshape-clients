# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.94
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTUserEmailParams(object):
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
        'password': 'str',
        'primary': 'bool',
        'email': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'password': 'password',
        'primary': 'primary',
        'email': 'email',
        'user_id': 'userId'
    }

    def __init__(self, password=None, primary=None, email=None, user_id=None):  # noqa: E501
        """BTUserEmailParams - a model defined in OpenAPI"""  # noqa: E501

        self._password = None
        self._primary = None
        self._email = None
        self._user_id = None
        self.discriminator = None

        if password is not None:
            self.password = password
        if primary is not None:
            self.primary = primary
        if email is not None:
            self.email = email
        if user_id is not None:
            self.user_id = user_id

    @property
    def password(self):
        """Gets the password of this BTUserEmailParams.  # noqa: E501


        :return: The password of this BTUserEmailParams.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this BTUserEmailParams.


        :param password: The password of this BTUserEmailParams.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def primary(self):
        """Gets the primary of this BTUserEmailParams.  # noqa: E501


        :return: The primary of this BTUserEmailParams.  # noqa: E501
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this BTUserEmailParams.


        :param primary: The primary of this BTUserEmailParams.  # noqa: E501
        :type: bool
        """

        self._primary = primary

    @property
    def email(self):
        """Gets the email of this BTUserEmailParams.  # noqa: E501


        :return: The email of this BTUserEmailParams.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BTUserEmailParams.


        :param email: The email of this BTUserEmailParams.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def user_id(self):
        """Gets the user_id of this BTUserEmailParams.  # noqa: E501


        :return: The user_id of this BTUserEmailParams.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BTUserEmailParams.


        :param user_id: The user_id of this BTUserEmailParams.  # noqa: E501
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
        if not isinstance(other, BTUserEmailParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

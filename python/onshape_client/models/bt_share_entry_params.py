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


class BTShareEntryParams(object):
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
        'team_id': 'str',
        'application_id': 'str',
        'entry_type': 'int',
        'email': 'str',
        'company_id': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'team_id': 'teamId',
        'application_id': 'applicationId',
        'entry_type': 'entryType',
        'email': 'email',
        'company_id': 'companyId',
        'user_id': 'userId'
    }

    def __init__(self, team_id=None, application_id=None, entry_type=None, email=None, company_id=None, user_id=None):  # noqa: E501
        """BTShareEntryParams - a model defined in OpenAPI"""  # noqa: E501

        self._team_id = None
        self._application_id = None
        self._entry_type = None
        self._email = None
        self._company_id = None
        self._user_id = None
        self.discriminator = None

        if team_id is not None:
            self.team_id = team_id
        if application_id is not None:
            self.application_id = application_id
        if entry_type is not None:
            self.entry_type = entry_type
        if email is not None:
            self.email = email
        if company_id is not None:
            self.company_id = company_id
        if user_id is not None:
            self.user_id = user_id

    @property
    def team_id(self):
        """Gets the team_id of this BTShareEntryParams.  # noqa: E501


        :return: The team_id of this BTShareEntryParams.  # noqa: E501
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this BTShareEntryParams.


        :param team_id: The team_id of this BTShareEntryParams.  # noqa: E501
        :type: str
        """

        self._team_id = team_id

    @property
    def application_id(self):
        """Gets the application_id of this BTShareEntryParams.  # noqa: E501


        :return: The application_id of this BTShareEntryParams.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this BTShareEntryParams.


        :param application_id: The application_id of this BTShareEntryParams.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def entry_type(self):
        """Gets the entry_type of this BTShareEntryParams.  # noqa: E501


        :return: The entry_type of this BTShareEntryParams.  # noqa: E501
        :rtype: int
        """
        return self._entry_type

    @entry_type.setter
    def entry_type(self, entry_type):
        """Sets the entry_type of this BTShareEntryParams.


        :param entry_type: The entry_type of this BTShareEntryParams.  # noqa: E501
        :type: int
        """

        self._entry_type = entry_type

    @property
    def email(self):
        """Gets the email of this BTShareEntryParams.  # noqa: E501


        :return: The email of this BTShareEntryParams.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BTShareEntryParams.


        :param email: The email of this BTShareEntryParams.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def company_id(self):
        """Gets the company_id of this BTShareEntryParams.  # noqa: E501


        :return: The company_id of this BTShareEntryParams.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this BTShareEntryParams.


        :param company_id: The company_id of this BTShareEntryParams.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def user_id(self):
        """Gets the user_id of this BTShareEntryParams.  # noqa: E501


        :return: The user_id of this BTShareEntryParams.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BTShareEntryParams.


        :param user_id: The user_id of this BTShareEntryParams.  # noqa: E501
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
        if not isinstance(other, BTShareEntryParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

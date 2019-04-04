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


class BTAddressInfo(object):
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
        'id': 'str',
        'state': 'str',
        'address': 'str',
        'country': 'str',
        'city': 'str',
        'state_code': 'str',
        'country_code': 'str',
        'zip': 'str'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'address': 'address',
        'country': 'country',
        'city': 'city',
        'state_code': 'stateCode',
        'country_code': 'countryCode',
        'zip': 'zip'
    }

    def __init__(self, id=None, state=None, address=None, country=None, city=None, state_code=None, country_code=None, zip=None):  # noqa: E501
        """BTAddressInfo - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._state = None
        self._address = None
        self._country = None
        self._city = None
        self._state_code = None
        self._country_code = None
        self._zip = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if address is not None:
            self.address = address
        if country is not None:
            self.country = country
        if city is not None:
            self.city = city
        if state_code is not None:
            self.state_code = state_code
        if country_code is not None:
            self.country_code = country_code
        if zip is not None:
            self.zip = zip

    @property
    def id(self):
        """Gets the id of this BTAddressInfo.  # noqa: E501


        :return: The id of this BTAddressInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTAddressInfo.


        :param id: The id of this BTAddressInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this BTAddressInfo.  # noqa: E501


        :return: The state of this BTAddressInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BTAddressInfo.


        :param state: The state of this BTAddressInfo.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def address(self):
        """Gets the address of this BTAddressInfo.  # noqa: E501


        :return: The address of this BTAddressInfo.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this BTAddressInfo.


        :param address: The address of this BTAddressInfo.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def country(self):
        """Gets the country of this BTAddressInfo.  # noqa: E501


        :return: The country of this BTAddressInfo.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this BTAddressInfo.


        :param country: The country of this BTAddressInfo.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def city(self):
        """Gets the city of this BTAddressInfo.  # noqa: E501


        :return: The city of this BTAddressInfo.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this BTAddressInfo.


        :param city: The city of this BTAddressInfo.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state_code(self):
        """Gets the state_code of this BTAddressInfo.  # noqa: E501


        :return: The state_code of this BTAddressInfo.  # noqa: E501
        :rtype: str
        """
        return self._state_code

    @state_code.setter
    def state_code(self, state_code):
        """Sets the state_code of this BTAddressInfo.


        :param state_code: The state_code of this BTAddressInfo.  # noqa: E501
        :type: str
        """

        self._state_code = state_code

    @property
    def country_code(self):
        """Gets the country_code of this BTAddressInfo.  # noqa: E501


        :return: The country_code of this BTAddressInfo.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this BTAddressInfo.


        :param country_code: The country_code of this BTAddressInfo.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def zip(self):
        """Gets the zip of this BTAddressInfo.  # noqa: E501


        :return: The zip of this BTAddressInfo.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this BTAddressInfo.


        :param zip: The zip of this BTAddressInfo.  # noqa: E501
        :type: str
        """

        self._zip = zip

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
        if not isinstance(other, BTAddressInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

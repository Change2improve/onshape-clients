# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.107
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from onshape_client.oas.configuration import Configuration


class BTSphereDescription1263(object):
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
        'radius': 'float',
        'origin': 'BTVector3d389',
        'bt_type': 'str'
    }

    attribute_map = {
        'radius': 'radius',
        'origin': 'origin',
        'bt_type': 'btType'
    }

    def __init__(self, radius=None, origin=None, bt_type=None, local_vars_configuration=None):  # noqa: E501
        """BTSphereDescription1263 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._radius = None
        self._origin = None
        self._bt_type = None
        self.discriminator = None

        if radius is not None:
            self.radius = radius
        if origin is not None:
            self.origin = origin
        if bt_type is not None:
            self.bt_type = bt_type

    @property
    def radius(self):
        """Gets the radius of this BTSphereDescription1263.  # noqa: E501


        :return: The radius of this BTSphereDescription1263.  # noqa: E501
        :rtype: float
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Sets the radius of this BTSphereDescription1263.


        :param radius: The radius of this BTSphereDescription1263.  # noqa: E501
        :type: float
        """

        self._radius = radius

    @property
    def origin(self):
        """Gets the origin of this BTSphereDescription1263.  # noqa: E501


        :return: The origin of this BTSphereDescription1263.  # noqa: E501
        :rtype: BTVector3d389
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this BTSphereDescription1263.


        :param origin: The origin of this BTSphereDescription1263.  # noqa: E501
        :type: BTVector3d389
        """

        self._origin = origin

    @property
    def bt_type(self):
        """Gets the bt_type of this BTSphereDescription1263.  # noqa: E501


        :return: The bt_type of this BTSphereDescription1263.  # noqa: E501
        :rtype: str
        """
        return self._bt_type

    @bt_type.setter
    def bt_type(self, bt_type):
        """Sets the bt_type of this BTSphereDescription1263.


        :param bt_type: The bt_type of this BTSphereDescription1263.  # noqa: E501
        :type: str
        """

        self._bt_type = bt_type

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
        if not isinstance(other, BTSphereDescription1263):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTSphereDescription1263):
            return True

        return self.to_dict() != other.to_dict()
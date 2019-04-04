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


class TransformGroup(object):
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
        'instances': 'list[BTAssemblyInstanceDefinitionParams]',
        'transform': 'list[float]'
    }

    attribute_map = {
        'instances': 'instances',
        'transform': 'transform'
    }

    def __init__(self, instances=None, transform=None):  # noqa: E501
        """TransformGroup - a model defined in OpenAPI"""  # noqa: E501

        self._instances = None
        self._transform = None
        self.discriminator = None

        if instances is not None:
            self.instances = instances
        if transform is not None:
            self.transform = transform

    @property
    def instances(self):
        """Gets the instances of this TransformGroup.  # noqa: E501


        :return: The instances of this TransformGroup.  # noqa: E501
        :rtype: list[BTAssemblyInstanceDefinitionParams]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this TransformGroup.


        :param instances: The instances of this TransformGroup.  # noqa: E501
        :type: list[BTAssemblyInstanceDefinitionParams]
        """

        self._instances = instances

    @property
    def transform(self):
        """Gets the transform of this TransformGroup.  # noqa: E501


        :return: The transform of this TransformGroup.  # noqa: E501
        :rtype: list[float]
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        """Sets the transform of this TransformGroup.


        :param transform: The transform of this TransformGroup.  # noqa: E501
        :type: list[float]
        """

        self._transform = transform

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
        if not isinstance(other, TransformGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

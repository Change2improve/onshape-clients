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


class BTMParameterReference2434(object):
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
        'element_id': 'str',
        'feature_script_type': 'str',
        'namespace': 'str',
        'bt_type': 'str'
    }

    attribute_map = {
        'element_id': 'elementId',
        'feature_script_type': 'featureScriptType',
        'namespace': 'namespace',
        'bt_type': 'btType'
    }

    discriminator_value_class_map = {
        'BTMParameterReferenceWithConfiguration-3028': 'BTMParameterReferenceWithConfiguration3028',
        'BTMParameterReferenceBlob-3281': 'BTMParameterReferenceBlob3281'
    }

    def __init__(self, element_id=None, feature_script_type=None, namespace=None, bt_type=None, local_vars_configuration=None):  # noqa: E501
        """BTMParameterReference2434 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._element_id = None
        self._feature_script_type = None
        self._namespace = None
        self._bt_type = None
        self.discriminator = 'bt_type'

        if element_id is not None:
            self.element_id = element_id
        if feature_script_type is not None:
            self.feature_script_type = feature_script_type
        if namespace is not None:
            self.namespace = namespace
        if bt_type is not None:
            self.bt_type = bt_type

    @property
    def element_id(self):
        """Gets the element_id of this BTMParameterReference2434.  # noqa: E501


        :return: The element_id of this BTMParameterReference2434.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTMParameterReference2434.


        :param element_id: The element_id of this BTMParameterReference2434.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def feature_script_type(self):
        """Gets the feature_script_type of this BTMParameterReference2434.  # noqa: E501


        :return: The feature_script_type of this BTMParameterReference2434.  # noqa: E501
        :rtype: str
        """
        return self._feature_script_type

    @feature_script_type.setter
    def feature_script_type(self, feature_script_type):
        """Sets the feature_script_type of this BTMParameterReference2434.


        :param feature_script_type: The feature_script_type of this BTMParameterReference2434.  # noqa: E501
        :type: str
        """

        self._feature_script_type = feature_script_type

    @property
    def namespace(self):
        """Gets the namespace of this BTMParameterReference2434.  # noqa: E501


        :return: The namespace of this BTMParameterReference2434.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this BTMParameterReference2434.


        :param namespace: The namespace of this BTMParameterReference2434.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def bt_type(self):
        """Gets the bt_type of this BTMParameterReference2434.  # noqa: E501


        :return: The bt_type of this BTMParameterReference2434.  # noqa: E501
        :rtype: str
        """
        return self._bt_type

    @bt_type.setter
    def bt_type(self, bt_type):
        """Sets the bt_type of this BTMParameterReference2434.


        :param bt_type: The bt_type of this BTMParameterReference2434.  # noqa: E501
        :type: str
        """

        self._bt_type = bt_type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, BTMParameterReference2434):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTMParameterReference2434):
            return True

        return self.to_dict() != other.to_dict()
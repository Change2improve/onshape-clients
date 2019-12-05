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


class BTMSketchTextEntity1761(object):
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
        'font_name': 'str',
        'text': 'str',
        'ascent': 'float',
        'baseline_start_x': 'float',
        'baseline_start_y': 'float',
        'baseline_direction_x': 'float',
        'baseline_direction_y': 'float',
        'bt_type': 'str'
    }

    attribute_map = {
        'font_name': 'fontName',
        'text': 'text',
        'ascent': 'ascent',
        'baseline_start_x': 'baselineStartX',
        'baseline_start_y': 'baselineStartY',
        'baseline_direction_x': 'baselineDirectionX',
        'baseline_direction_y': 'baselineDirectionY',
        'bt_type': 'btType'
    }

    def __init__(self, font_name=None, text=None, ascent=None, baseline_start_x=None, baseline_start_y=None, baseline_direction_x=None, baseline_direction_y=None, bt_type=None, local_vars_configuration=None):  # noqa: E501
        """BTMSketchTextEntity1761 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._font_name = None
        self._text = None
        self._ascent = None
        self._baseline_start_x = None
        self._baseline_start_y = None
        self._baseline_direction_x = None
        self._baseline_direction_y = None
        self._bt_type = None
        self.discriminator = None

        if font_name is not None:
            self.font_name = font_name
        if text is not None:
            self.text = text
        if ascent is not None:
            self.ascent = ascent
        if baseline_start_x is not None:
            self.baseline_start_x = baseline_start_x
        if baseline_start_y is not None:
            self.baseline_start_y = baseline_start_y
        if baseline_direction_x is not None:
            self.baseline_direction_x = baseline_direction_x
        if baseline_direction_y is not None:
            self.baseline_direction_y = baseline_direction_y
        if bt_type is not None:
            self.bt_type = bt_type

    @property
    def font_name(self):
        """Gets the font_name of this BTMSketchTextEntity1761.  # noqa: E501


        :return: The font_name of this BTMSketchTextEntity1761.  # noqa: E501
        :rtype: str
        """
        return self._font_name

    @font_name.setter
    def font_name(self, font_name):
        """Sets the font_name of this BTMSketchTextEntity1761.


        :param font_name: The font_name of this BTMSketchTextEntity1761.  # noqa: E501
        :type: str
        """

        self._font_name = font_name

    @property
    def text(self):
        """Gets the text of this BTMSketchTextEntity1761.  # noqa: E501


        :return: The text of this BTMSketchTextEntity1761.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this BTMSketchTextEntity1761.


        :param text: The text of this BTMSketchTextEntity1761.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def ascent(self):
        """Gets the ascent of this BTMSketchTextEntity1761.  # noqa: E501


        :return: The ascent of this BTMSketchTextEntity1761.  # noqa: E501
        :rtype: float
        """
        return self._ascent

    @ascent.setter
    def ascent(self, ascent):
        """Sets the ascent of this BTMSketchTextEntity1761.


        :param ascent: The ascent of this BTMSketchTextEntity1761.  # noqa: E501
        :type: float
        """

        self._ascent = ascent

    @property
    def baseline_start_x(self):
        """Gets the baseline_start_x of this BTMSketchTextEntity1761.  # noqa: E501


        :return: The baseline_start_x of this BTMSketchTextEntity1761.  # noqa: E501
        :rtype: float
        """
        return self._baseline_start_x

    @baseline_start_x.setter
    def baseline_start_x(self, baseline_start_x):
        """Sets the baseline_start_x of this BTMSketchTextEntity1761.


        :param baseline_start_x: The baseline_start_x of this BTMSketchTextEntity1761.  # noqa: E501
        :type: float
        """

        self._baseline_start_x = baseline_start_x

    @property
    def baseline_start_y(self):
        """Gets the baseline_start_y of this BTMSketchTextEntity1761.  # noqa: E501


        :return: The baseline_start_y of this BTMSketchTextEntity1761.  # noqa: E501
        :rtype: float
        """
        return self._baseline_start_y

    @baseline_start_y.setter
    def baseline_start_y(self, baseline_start_y):
        """Sets the baseline_start_y of this BTMSketchTextEntity1761.


        :param baseline_start_y: The baseline_start_y of this BTMSketchTextEntity1761.  # noqa: E501
        :type: float
        """

        self._baseline_start_y = baseline_start_y

    @property
    def baseline_direction_x(self):
        """Gets the baseline_direction_x of this BTMSketchTextEntity1761.  # noqa: E501


        :return: The baseline_direction_x of this BTMSketchTextEntity1761.  # noqa: E501
        :rtype: float
        """
        return self._baseline_direction_x

    @baseline_direction_x.setter
    def baseline_direction_x(self, baseline_direction_x):
        """Sets the baseline_direction_x of this BTMSketchTextEntity1761.


        :param baseline_direction_x: The baseline_direction_x of this BTMSketchTextEntity1761.  # noqa: E501
        :type: float
        """

        self._baseline_direction_x = baseline_direction_x

    @property
    def baseline_direction_y(self):
        """Gets the baseline_direction_y of this BTMSketchTextEntity1761.  # noqa: E501


        :return: The baseline_direction_y of this BTMSketchTextEntity1761.  # noqa: E501
        :rtype: float
        """
        return self._baseline_direction_y

    @baseline_direction_y.setter
    def baseline_direction_y(self, baseline_direction_y):
        """Sets the baseline_direction_y of this BTMSketchTextEntity1761.


        :param baseline_direction_y: The baseline_direction_y of this BTMSketchTextEntity1761.  # noqa: E501
        :type: float
        """

        self._baseline_direction_y = baseline_direction_y

    @property
    def bt_type(self):
        """Gets the bt_type of this BTMSketchTextEntity1761.  # noqa: E501


        :return: The bt_type of this BTMSketchTextEntity1761.  # noqa: E501
        :rtype: str
        """
        return self._bt_type

    @bt_type.setter
    def bt_type(self, bt_type):
        """Sets the bt_type of this BTMSketchTextEntity1761.


        :param bt_type: The bt_type of this BTMSketchTextEntity1761.  # noqa: E501
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
        if not isinstance(other, BTMSketchTextEntity1761):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTMSketchTextEntity1761):
            return True

        return self.to_dict() != other.to_dict()
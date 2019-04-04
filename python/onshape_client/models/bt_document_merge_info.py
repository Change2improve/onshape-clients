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


class BTDocumentMergeInfo(object):
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
        'overwritten_elements': 'list[BTDocumentElementInfo]',
        'library_version_mismatch': 'bool'
    }

    attribute_map = {
        'overwritten_elements': 'overwrittenElements',
        'library_version_mismatch': 'libraryVersionMismatch'
    }

    def __init__(self, overwritten_elements=None, library_version_mismatch=None):  # noqa: E501
        """BTDocumentMergeInfo - a model defined in OpenAPI"""  # noqa: E501

        self._overwritten_elements = None
        self._library_version_mismatch = None
        self.discriminator = None

        if overwritten_elements is not None:
            self.overwritten_elements = overwritten_elements
        if library_version_mismatch is not None:
            self.library_version_mismatch = library_version_mismatch

    @property
    def overwritten_elements(self):
        """Gets the overwritten_elements of this BTDocumentMergeInfo.  # noqa: E501


        :return: The overwritten_elements of this BTDocumentMergeInfo.  # noqa: E501
        :rtype: list[BTDocumentElementInfo]
        """
        return self._overwritten_elements

    @overwritten_elements.setter
    def overwritten_elements(self, overwritten_elements):
        """Sets the overwritten_elements of this BTDocumentMergeInfo.


        :param overwritten_elements: The overwritten_elements of this BTDocumentMergeInfo.  # noqa: E501
        :type: list[BTDocumentElementInfo]
        """

        self._overwritten_elements = overwritten_elements

    @property
    def library_version_mismatch(self):
        """Gets the library_version_mismatch of this BTDocumentMergeInfo.  # noqa: E501


        :return: The library_version_mismatch of this BTDocumentMergeInfo.  # noqa: E501
        :rtype: bool
        """
        return self._library_version_mismatch

    @library_version_mismatch.setter
    def library_version_mismatch(self, library_version_mismatch):
        """Sets the library_version_mismatch of this BTDocumentMergeInfo.


        :param library_version_mismatch: The library_version_mismatch of this BTDocumentMergeInfo.  # noqa: E501
        :type: bool
        """

        self._library_version_mismatch = library_version_mismatch

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
        if not isinstance(other, BTDocumentMergeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

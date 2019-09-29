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


class BTAclParams(object):
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
        'document_id': 'str',
        'anonymous_access_allowed': 'bool',
        'anonymous_allows_export': 'bool',
        'public': 'bool'
    }

    attribute_map = {
        'document_id': 'documentId',
        'anonymous_access_allowed': 'anonymousAccessAllowed',
        'anonymous_allows_export': 'anonymousAllowsExport',
        'public': 'public'
    }

    def __init__(self, document_id=None, anonymous_access_allowed=None, anonymous_allows_export=None, public=None):  # noqa: E501
        """BTAclParams - a model defined in OpenAPI"""  # noqa: E501

        self._document_id = None
        self._anonymous_access_allowed = None
        self._anonymous_allows_export = None
        self._public = None
        self.discriminator = None

        if document_id is not None:
            self.document_id = document_id
        if anonymous_access_allowed is not None:
            self.anonymous_access_allowed = anonymous_access_allowed
        if anonymous_allows_export is not None:
            self.anonymous_allows_export = anonymous_allows_export
        if public is not None:
            self.public = public

    @property
    def document_id(self):
        """Gets the document_id of this BTAclParams.  # noqa: E501


        :return: The document_id of this BTAclParams.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTAclParams.


        :param document_id: The document_id of this BTAclParams.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def anonymous_access_allowed(self):
        """Gets the anonymous_access_allowed of this BTAclParams.  # noqa: E501


        :return: The anonymous_access_allowed of this BTAclParams.  # noqa: E501
        :rtype: bool
        """
        return self._anonymous_access_allowed

    @anonymous_access_allowed.setter
    def anonymous_access_allowed(self, anonymous_access_allowed):
        """Sets the anonymous_access_allowed of this BTAclParams.


        :param anonymous_access_allowed: The anonymous_access_allowed of this BTAclParams.  # noqa: E501
        :type: bool
        """

        self._anonymous_access_allowed = anonymous_access_allowed

    @property
    def anonymous_allows_export(self):
        """Gets the anonymous_allows_export of this BTAclParams.  # noqa: E501


        :return: The anonymous_allows_export of this BTAclParams.  # noqa: E501
        :rtype: bool
        """
        return self._anonymous_allows_export

    @anonymous_allows_export.setter
    def anonymous_allows_export(self, anonymous_allows_export):
        """Sets the anonymous_allows_export of this BTAclParams.


        :param anonymous_allows_export: The anonymous_allows_export of this BTAclParams.  # noqa: E501
        :type: bool
        """

        self._anonymous_allows_export = anonymous_allows_export

    @property
    def public(self):
        """Gets the public of this BTAclParams.  # noqa: E501


        :return: The public of this BTAclParams.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this BTAclParams.


        :param public: The public of this BTAclParams.  # noqa: E501
        :type: bool
        """

        self._public = public

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
        if not isinstance(other, BTAclParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class BTDocumentOptionsParams(object):
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
        'cpp_server_memory': 'int',
        'enable_cpp_server_memory_diagnostics': 'bool',
        'skip_retrieval_test': 'bool',
        'document_memory': 'int',
        'extended_display_check': 'bool',
        'cpp_server_limit': 'int',
        'thumbnail_cpp_server_limit': 'int',
        'linked_cpp_server_limit': 'int',
        'drawing_server_memory': 'int',
        'cpp_server_default_element_limit': 'int'
    }

    attribute_map = {
        'cpp_server_memory': 'cppServerMemory',
        'enable_cpp_server_memory_diagnostics': 'enableCppServerMemoryDiagnostics',
        'skip_retrieval_test': 'skipRetrievalTest',
        'document_memory': 'documentMemory',
        'extended_display_check': 'extendedDisplayCheck',
        'cpp_server_limit': 'cppServerLimit',
        'thumbnail_cpp_server_limit': 'thumbnailCppServerLimit',
        'linked_cpp_server_limit': 'linkedCppServerLimit',
        'drawing_server_memory': 'drawingServerMemory',
        'cpp_server_default_element_limit': 'cppServerDefaultElementLimit'
    }

    def __init__(self, cpp_server_memory=None, enable_cpp_server_memory_diagnostics=None, skip_retrieval_test=None, document_memory=None, extended_display_check=None, cpp_server_limit=None, thumbnail_cpp_server_limit=None, linked_cpp_server_limit=None, drawing_server_memory=None, cpp_server_default_element_limit=None):  # noqa: E501
        """BTDocumentOptionsParams - a model defined in OpenAPI"""  # noqa: E501

        self._cpp_server_memory = None
        self._enable_cpp_server_memory_diagnostics = None
        self._skip_retrieval_test = None
        self._document_memory = None
        self._extended_display_check = None
        self._cpp_server_limit = None
        self._thumbnail_cpp_server_limit = None
        self._linked_cpp_server_limit = None
        self._drawing_server_memory = None
        self._cpp_server_default_element_limit = None
        self.discriminator = None

        if cpp_server_memory is not None:
            self.cpp_server_memory = cpp_server_memory
        if enable_cpp_server_memory_diagnostics is not None:
            self.enable_cpp_server_memory_diagnostics = enable_cpp_server_memory_diagnostics
        if skip_retrieval_test is not None:
            self.skip_retrieval_test = skip_retrieval_test
        if document_memory is not None:
            self.document_memory = document_memory
        if extended_display_check is not None:
            self.extended_display_check = extended_display_check
        if cpp_server_limit is not None:
            self.cpp_server_limit = cpp_server_limit
        if thumbnail_cpp_server_limit is not None:
            self.thumbnail_cpp_server_limit = thumbnail_cpp_server_limit
        if linked_cpp_server_limit is not None:
            self.linked_cpp_server_limit = linked_cpp_server_limit
        if drawing_server_memory is not None:
            self.drawing_server_memory = drawing_server_memory
        if cpp_server_default_element_limit is not None:
            self.cpp_server_default_element_limit = cpp_server_default_element_limit

    @property
    def cpp_server_memory(self):
        """Gets the cpp_server_memory of this BTDocumentOptionsParams.  # noqa: E501


        :return: The cpp_server_memory of this BTDocumentOptionsParams.  # noqa: E501
        :rtype: int
        """
        return self._cpp_server_memory

    @cpp_server_memory.setter
    def cpp_server_memory(self, cpp_server_memory):
        """Sets the cpp_server_memory of this BTDocumentOptionsParams.


        :param cpp_server_memory: The cpp_server_memory of this BTDocumentOptionsParams.  # noqa: E501
        :type: int
        """

        self._cpp_server_memory = cpp_server_memory

    @property
    def enable_cpp_server_memory_diagnostics(self):
        """Gets the enable_cpp_server_memory_diagnostics of this BTDocumentOptionsParams.  # noqa: E501


        :return: The enable_cpp_server_memory_diagnostics of this BTDocumentOptionsParams.  # noqa: E501
        :rtype: bool
        """
        return self._enable_cpp_server_memory_diagnostics

    @enable_cpp_server_memory_diagnostics.setter
    def enable_cpp_server_memory_diagnostics(self, enable_cpp_server_memory_diagnostics):
        """Sets the enable_cpp_server_memory_diagnostics of this BTDocumentOptionsParams.


        :param enable_cpp_server_memory_diagnostics: The enable_cpp_server_memory_diagnostics of this BTDocumentOptionsParams.  # noqa: E501
        :type: bool
        """

        self._enable_cpp_server_memory_diagnostics = enable_cpp_server_memory_diagnostics

    @property
    def skip_retrieval_test(self):
        """Gets the skip_retrieval_test of this BTDocumentOptionsParams.  # noqa: E501


        :return: The skip_retrieval_test of this BTDocumentOptionsParams.  # noqa: E501
        :rtype: bool
        """
        return self._skip_retrieval_test

    @skip_retrieval_test.setter
    def skip_retrieval_test(self, skip_retrieval_test):
        """Sets the skip_retrieval_test of this BTDocumentOptionsParams.


        :param skip_retrieval_test: The skip_retrieval_test of this BTDocumentOptionsParams.  # noqa: E501
        :type: bool
        """

        self._skip_retrieval_test = skip_retrieval_test

    @property
    def document_memory(self):
        """Gets the document_memory of this BTDocumentOptionsParams.  # noqa: E501


        :return: The document_memory of this BTDocumentOptionsParams.  # noqa: E501
        :rtype: int
        """
        return self._document_memory

    @document_memory.setter
    def document_memory(self, document_memory):
        """Sets the document_memory of this BTDocumentOptionsParams.


        :param document_memory: The document_memory of this BTDocumentOptionsParams.  # noqa: E501
        :type: int
        """

        self._document_memory = document_memory

    @property
    def extended_display_check(self):
        """Gets the extended_display_check of this BTDocumentOptionsParams.  # noqa: E501


        :return: The extended_display_check of this BTDocumentOptionsParams.  # noqa: E501
        :rtype: bool
        """
        return self._extended_display_check

    @extended_display_check.setter
    def extended_display_check(self, extended_display_check):
        """Sets the extended_display_check of this BTDocumentOptionsParams.


        :param extended_display_check: The extended_display_check of this BTDocumentOptionsParams.  # noqa: E501
        :type: bool
        """

        self._extended_display_check = extended_display_check

    @property
    def cpp_server_limit(self):
        """Gets the cpp_server_limit of this BTDocumentOptionsParams.  # noqa: E501


        :return: The cpp_server_limit of this BTDocumentOptionsParams.  # noqa: E501
        :rtype: int
        """
        return self._cpp_server_limit

    @cpp_server_limit.setter
    def cpp_server_limit(self, cpp_server_limit):
        """Sets the cpp_server_limit of this BTDocumentOptionsParams.


        :param cpp_server_limit: The cpp_server_limit of this BTDocumentOptionsParams.  # noqa: E501
        :type: int
        """

        self._cpp_server_limit = cpp_server_limit

    @property
    def thumbnail_cpp_server_limit(self):
        """Gets the thumbnail_cpp_server_limit of this BTDocumentOptionsParams.  # noqa: E501


        :return: The thumbnail_cpp_server_limit of this BTDocumentOptionsParams.  # noqa: E501
        :rtype: int
        """
        return self._thumbnail_cpp_server_limit

    @thumbnail_cpp_server_limit.setter
    def thumbnail_cpp_server_limit(self, thumbnail_cpp_server_limit):
        """Sets the thumbnail_cpp_server_limit of this BTDocumentOptionsParams.


        :param thumbnail_cpp_server_limit: The thumbnail_cpp_server_limit of this BTDocumentOptionsParams.  # noqa: E501
        :type: int
        """

        self._thumbnail_cpp_server_limit = thumbnail_cpp_server_limit

    @property
    def linked_cpp_server_limit(self):
        """Gets the linked_cpp_server_limit of this BTDocumentOptionsParams.  # noqa: E501


        :return: The linked_cpp_server_limit of this BTDocumentOptionsParams.  # noqa: E501
        :rtype: int
        """
        return self._linked_cpp_server_limit

    @linked_cpp_server_limit.setter
    def linked_cpp_server_limit(self, linked_cpp_server_limit):
        """Sets the linked_cpp_server_limit of this BTDocumentOptionsParams.


        :param linked_cpp_server_limit: The linked_cpp_server_limit of this BTDocumentOptionsParams.  # noqa: E501
        :type: int
        """

        self._linked_cpp_server_limit = linked_cpp_server_limit

    @property
    def drawing_server_memory(self):
        """Gets the drawing_server_memory of this BTDocumentOptionsParams.  # noqa: E501


        :return: The drawing_server_memory of this BTDocumentOptionsParams.  # noqa: E501
        :rtype: int
        """
        return self._drawing_server_memory

    @drawing_server_memory.setter
    def drawing_server_memory(self, drawing_server_memory):
        """Sets the drawing_server_memory of this BTDocumentOptionsParams.


        :param drawing_server_memory: The drawing_server_memory of this BTDocumentOptionsParams.  # noqa: E501
        :type: int
        """

        self._drawing_server_memory = drawing_server_memory

    @property
    def cpp_server_default_element_limit(self):
        """Gets the cpp_server_default_element_limit of this BTDocumentOptionsParams.  # noqa: E501


        :return: The cpp_server_default_element_limit of this BTDocumentOptionsParams.  # noqa: E501
        :rtype: int
        """
        return self._cpp_server_default_element_limit

    @cpp_server_default_element_limit.setter
    def cpp_server_default_element_limit(self, cpp_server_default_element_limit):
        """Sets the cpp_server_default_element_limit of this BTDocumentOptionsParams.


        :param cpp_server_default_element_limit: The cpp_server_default_element_limit of this BTDocumentOptionsParams.  # noqa: E501
        :type: int
        """

        self._cpp_server_default_element_limit = cpp_server_default_element_limit

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
        if not isinstance(other, BTDocumentOptionsParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

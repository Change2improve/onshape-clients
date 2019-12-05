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


class BTPModule234(object):
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
        'is_internal_module': 'bool',
        'imports': 'list[BTPTopLevelImport285]',
        'version_number': 'int',
        'deep_imports': 'dict(str, list[BTImport])',
        'path_map': 'dict(str, BTMicroversionId366)',
        'version': 'BTPLiteralNumber258',
        'top_level': 'list[BTPTopLevelNode286]',
        'is_blob': 'bool',
        'path_to_cache': 'BTCacheDataPath191',
        'may_have_implicit_imports': 'bool',
        'bt_type': 'str'
    }

    attribute_map = {
        'is_internal_module': 'isInternalModule',
        'imports': 'imports',
        'version_number': 'versionNumber',
        'deep_imports': 'deepImports',
        'path_map': 'pathMap',
        'version': 'version',
        'top_level': 'topLevel',
        'is_blob': 'isBlob',
        'path_to_cache': 'pathToCache',
        'may_have_implicit_imports': 'mayHaveImplicitImports',
        'bt_type': 'btType'
    }

    def __init__(self, is_internal_module=None, imports=None, version_number=None, deep_imports=None, path_map=None, version=None, top_level=None, is_blob=None, path_to_cache=None, may_have_implicit_imports=None, bt_type=None, local_vars_configuration=None):  # noqa: E501
        """BTPModule234 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_internal_module = None
        self._imports = None
        self._version_number = None
        self._deep_imports = None
        self._path_map = None
        self._version = None
        self._top_level = None
        self._is_blob = None
        self._path_to_cache = None
        self._may_have_implicit_imports = None
        self._bt_type = None
        self.discriminator = None

        if is_internal_module is not None:
            self.is_internal_module = is_internal_module
        if imports is not None:
            self.imports = imports
        if version_number is not None:
            self.version_number = version_number
        if deep_imports is not None:
            self.deep_imports = deep_imports
        if path_map is not None:
            self.path_map = path_map
        if version is not None:
            self.version = version
        if top_level is not None:
            self.top_level = top_level
        if is_blob is not None:
            self.is_blob = is_blob
        if path_to_cache is not None:
            self.path_to_cache = path_to_cache
        if may_have_implicit_imports is not None:
            self.may_have_implicit_imports = may_have_implicit_imports
        if bt_type is not None:
            self.bt_type = bt_type

    @property
    def is_internal_module(self):
        """Gets the is_internal_module of this BTPModule234.  # noqa: E501


        :return: The is_internal_module of this BTPModule234.  # noqa: E501
        :rtype: bool
        """
        return self._is_internal_module

    @is_internal_module.setter
    def is_internal_module(self, is_internal_module):
        """Sets the is_internal_module of this BTPModule234.


        :param is_internal_module: The is_internal_module of this BTPModule234.  # noqa: E501
        :type: bool
        """

        self._is_internal_module = is_internal_module

    @property
    def imports(self):
        """Gets the imports of this BTPModule234.  # noqa: E501


        :return: The imports of this BTPModule234.  # noqa: E501
        :rtype: list[BTPTopLevelImport285]
        """
        return self._imports

    @imports.setter
    def imports(self, imports):
        """Sets the imports of this BTPModule234.


        :param imports: The imports of this BTPModule234.  # noqa: E501
        :type: list[BTPTopLevelImport285]
        """

        self._imports = imports

    @property
    def version_number(self):
        """Gets the version_number of this BTPModule234.  # noqa: E501


        :return: The version_number of this BTPModule234.  # noqa: E501
        :rtype: int
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this BTPModule234.


        :param version_number: The version_number of this BTPModule234.  # noqa: E501
        :type: int
        """

        self._version_number = version_number

    @property
    def deep_imports(self):
        """Gets the deep_imports of this BTPModule234.  # noqa: E501


        :return: The deep_imports of this BTPModule234.  # noqa: E501
        :rtype: dict(str, list[BTImport])
        """
        return self._deep_imports

    @deep_imports.setter
    def deep_imports(self, deep_imports):
        """Sets the deep_imports of this BTPModule234.


        :param deep_imports: The deep_imports of this BTPModule234.  # noqa: E501
        :type: dict(str, list[BTImport])
        """

        self._deep_imports = deep_imports

    @property
    def path_map(self):
        """Gets the path_map of this BTPModule234.  # noqa: E501


        :return: The path_map of this BTPModule234.  # noqa: E501
        :rtype: dict(str, BTMicroversionId366)
        """
        return self._path_map

    @path_map.setter
    def path_map(self, path_map):
        """Sets the path_map of this BTPModule234.


        :param path_map: The path_map of this BTPModule234.  # noqa: E501
        :type: dict(str, BTMicroversionId366)
        """

        self._path_map = path_map

    @property
    def version(self):
        """Gets the version of this BTPModule234.  # noqa: E501


        :return: The version of this BTPModule234.  # noqa: E501
        :rtype: BTPLiteralNumber258
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this BTPModule234.


        :param version: The version of this BTPModule234.  # noqa: E501
        :type: BTPLiteralNumber258
        """

        self._version = version

    @property
    def top_level(self):
        """Gets the top_level of this BTPModule234.  # noqa: E501


        :return: The top_level of this BTPModule234.  # noqa: E501
        :rtype: list[BTPTopLevelNode286]
        """
        return self._top_level

    @top_level.setter
    def top_level(self, top_level):
        """Sets the top_level of this BTPModule234.


        :param top_level: The top_level of this BTPModule234.  # noqa: E501
        :type: list[BTPTopLevelNode286]
        """

        self._top_level = top_level

    @property
    def is_blob(self):
        """Gets the is_blob of this BTPModule234.  # noqa: E501


        :return: The is_blob of this BTPModule234.  # noqa: E501
        :rtype: bool
        """
        return self._is_blob

    @is_blob.setter
    def is_blob(self, is_blob):
        """Sets the is_blob of this BTPModule234.


        :param is_blob: The is_blob of this BTPModule234.  # noqa: E501
        :type: bool
        """

        self._is_blob = is_blob

    @property
    def path_to_cache(self):
        """Gets the path_to_cache of this BTPModule234.  # noqa: E501


        :return: The path_to_cache of this BTPModule234.  # noqa: E501
        :rtype: BTCacheDataPath191
        """
        return self._path_to_cache

    @path_to_cache.setter
    def path_to_cache(self, path_to_cache):
        """Sets the path_to_cache of this BTPModule234.


        :param path_to_cache: The path_to_cache of this BTPModule234.  # noqa: E501
        :type: BTCacheDataPath191
        """

        self._path_to_cache = path_to_cache

    @property
    def may_have_implicit_imports(self):
        """Gets the may_have_implicit_imports of this BTPModule234.  # noqa: E501


        :return: The may_have_implicit_imports of this BTPModule234.  # noqa: E501
        :rtype: bool
        """
        return self._may_have_implicit_imports

    @may_have_implicit_imports.setter
    def may_have_implicit_imports(self, may_have_implicit_imports):
        """Sets the may_have_implicit_imports of this BTPModule234.


        :param may_have_implicit_imports: The may_have_implicit_imports of this BTPModule234.  # noqa: E501
        :type: bool
        """

        self._may_have_implicit_imports = may_have_implicit_imports

    @property
    def bt_type(self):
        """Gets the bt_type of this BTPModule234.  # noqa: E501


        :return: The bt_type of this BTPModule234.  # noqa: E501
        :rtype: str
        """
        return self._bt_type

    @bt_type.setter
    def bt_type(self, bt_type):
        """Sets the bt_type of this BTPModule234.


        :param bt_type: The bt_type of this BTPModule234.  # noqa: E501
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
        if not isinstance(other, BTPModule234):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTPModule234):
            return True

        return self.to_dict() != other.to_dict()
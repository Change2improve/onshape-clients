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


class BTLocationInfo(object):
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
        'from_node': 'BTPNode',
        'version': 'str',
        'line': 'int',
        'document': 'str',
        'top_level': 'str',
        'element_microversion': 'str',
        'language_version': 'int',
        'module_ids': 'BTDocumentVersionElementIds',
        'column': 'int',
        'end_line': 'int',
        'changeable_child_field_indices': 'list[int]',
        'end_column': 'int',
        'character': 'int',
        'parse_node_id': 'str',
        'end_character': 'int',
        'parse_node_id_raw': 'BTObjectId',
        'node_id': 'str',
        'child_map_indices': 'list[int]',
        'atomic_child_indices': 'list[int]',
        'node_id_raw': 'BTObjectId',
        'first_child_field': 'int',
        'child_list_indices': 'list[int]',
        'type_id': 'int',
        'connection_source': 'BTConnection',
        'export_type_name': 'str',
        'unknown_class': 'bool'
    }

    attribute_map = {
        'from_node': 'fromNode',
        'version': 'version',
        'line': 'line',
        'document': 'document',
        'top_level': 'topLevel',
        'element_microversion': 'elementMicroversion',
        'language_version': 'languageVersion',
        'module_ids': 'moduleIds',
        'column': 'column',
        'end_line': 'endLine',
        'changeable_child_field_indices': 'changeableChildFieldIndices',
        'end_column': 'endColumn',
        'character': 'character',
        'parse_node_id': 'parseNodeId',
        'end_character': 'endCharacter',
        'parse_node_id_raw': 'parseNodeIdRaw',
        'node_id': 'nodeId',
        'child_map_indices': 'childMapIndices',
        'atomic_child_indices': 'atomicChildIndices',
        'node_id_raw': 'nodeIdRaw',
        'first_child_field': 'firstChildField',
        'child_list_indices': 'childListIndices',
        'type_id': 'typeId',
        'connection_source': 'connectionSource',
        'export_type_name': 'exportTypeName',
        'unknown_class': 'unknownClass'
    }

    def __init__(self, from_node=None, version=None, line=None, document=None, top_level=None, element_microversion=None, language_version=None, module_ids=None, column=None, end_line=None, changeable_child_field_indices=None, end_column=None, character=None, parse_node_id=None, end_character=None, parse_node_id_raw=None, node_id=None, child_map_indices=None, atomic_child_indices=None, node_id_raw=None, first_child_field=None, child_list_indices=None, type_id=None, connection_source=None, export_type_name=None, unknown_class=None):  # noqa: E501
        """BTLocationInfo - a model defined in OpenAPI"""  # noqa: E501

        self._from_node = None
        self._version = None
        self._line = None
        self._document = None
        self._top_level = None
        self._element_microversion = None
        self._language_version = None
        self._module_ids = None
        self._column = None
        self._end_line = None
        self._changeable_child_field_indices = None
        self._end_column = None
        self._character = None
        self._parse_node_id = None
        self._end_character = None
        self._parse_node_id_raw = None
        self._node_id = None
        self._child_map_indices = None
        self._atomic_child_indices = None
        self._node_id_raw = None
        self._first_child_field = None
        self._child_list_indices = None
        self._type_id = None
        self._connection_source = None
        self._export_type_name = None
        self._unknown_class = None
        self.discriminator = None

        if from_node is not None:
            self.from_node = from_node
        if version is not None:
            self.version = version
        if line is not None:
            self.line = line
        if document is not None:
            self.document = document
        if top_level is not None:
            self.top_level = top_level
        if element_microversion is not None:
            self.element_microversion = element_microversion
        if language_version is not None:
            self.language_version = language_version
        if module_ids is not None:
            self.module_ids = module_ids
        if column is not None:
            self.column = column
        if end_line is not None:
            self.end_line = end_line
        if changeable_child_field_indices is not None:
            self.changeable_child_field_indices = changeable_child_field_indices
        if end_column is not None:
            self.end_column = end_column
        if character is not None:
            self.character = character
        if parse_node_id is not None:
            self.parse_node_id = parse_node_id
        if end_character is not None:
            self.end_character = end_character
        if parse_node_id_raw is not None:
            self.parse_node_id_raw = parse_node_id_raw
        if node_id is not None:
            self.node_id = node_id
        if child_map_indices is not None:
            self.child_map_indices = child_map_indices
        if atomic_child_indices is not None:
            self.atomic_child_indices = atomic_child_indices
        if node_id_raw is not None:
            self.node_id_raw = node_id_raw
        if first_child_field is not None:
            self.first_child_field = first_child_field
        if child_list_indices is not None:
            self.child_list_indices = child_list_indices
        if type_id is not None:
            self.type_id = type_id
        if connection_source is not None:
            self.connection_source = connection_source
        if export_type_name is not None:
            self.export_type_name = export_type_name
        if unknown_class is not None:
            self.unknown_class = unknown_class

    @property
    def from_node(self):
        """Gets the from_node of this BTLocationInfo.  # noqa: E501


        :return: The from_node of this BTLocationInfo.  # noqa: E501
        :rtype: BTPNode
        """
        return self._from_node

    @from_node.setter
    def from_node(self, from_node):
        """Sets the from_node of this BTLocationInfo.


        :param from_node: The from_node of this BTLocationInfo.  # noqa: E501
        :type: BTPNode
        """

        self._from_node = from_node

    @property
    def version(self):
        """Gets the version of this BTLocationInfo.  # noqa: E501


        :return: The version of this BTLocationInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this BTLocationInfo.


        :param version: The version of this BTLocationInfo.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def line(self):
        """Gets the line of this BTLocationInfo.  # noqa: E501


        :return: The line of this BTLocationInfo.  # noqa: E501
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this BTLocationInfo.


        :param line: The line of this BTLocationInfo.  # noqa: E501
        :type: int
        """

        self._line = line

    @property
    def document(self):
        """Gets the document of this BTLocationInfo.  # noqa: E501


        :return: The document of this BTLocationInfo.  # noqa: E501
        :rtype: str
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this BTLocationInfo.


        :param document: The document of this BTLocationInfo.  # noqa: E501
        :type: str
        """

        self._document = document

    @property
    def top_level(self):
        """Gets the top_level of this BTLocationInfo.  # noqa: E501


        :return: The top_level of this BTLocationInfo.  # noqa: E501
        :rtype: str
        """
        return self._top_level

    @top_level.setter
    def top_level(self, top_level):
        """Sets the top_level of this BTLocationInfo.


        :param top_level: The top_level of this BTLocationInfo.  # noqa: E501
        :type: str
        """

        self._top_level = top_level

    @property
    def element_microversion(self):
        """Gets the element_microversion of this BTLocationInfo.  # noqa: E501


        :return: The element_microversion of this BTLocationInfo.  # noqa: E501
        :rtype: str
        """
        return self._element_microversion

    @element_microversion.setter
    def element_microversion(self, element_microversion):
        """Sets the element_microversion of this BTLocationInfo.


        :param element_microversion: The element_microversion of this BTLocationInfo.  # noqa: E501
        :type: str
        """

        self._element_microversion = element_microversion

    @property
    def language_version(self):
        """Gets the language_version of this BTLocationInfo.  # noqa: E501


        :return: The language_version of this BTLocationInfo.  # noqa: E501
        :rtype: int
        """
        return self._language_version

    @language_version.setter
    def language_version(self, language_version):
        """Sets the language_version of this BTLocationInfo.


        :param language_version: The language_version of this BTLocationInfo.  # noqa: E501
        :type: int
        """

        self._language_version = language_version

    @property
    def module_ids(self):
        """Gets the module_ids of this BTLocationInfo.  # noqa: E501


        :return: The module_ids of this BTLocationInfo.  # noqa: E501
        :rtype: BTDocumentVersionElementIds
        """
        return self._module_ids

    @module_ids.setter
    def module_ids(self, module_ids):
        """Sets the module_ids of this BTLocationInfo.


        :param module_ids: The module_ids of this BTLocationInfo.  # noqa: E501
        :type: BTDocumentVersionElementIds
        """

        self._module_ids = module_ids

    @property
    def column(self):
        """Gets the column of this BTLocationInfo.  # noqa: E501


        :return: The column of this BTLocationInfo.  # noqa: E501
        :rtype: int
        """
        return self._column

    @column.setter
    def column(self, column):
        """Sets the column of this BTLocationInfo.


        :param column: The column of this BTLocationInfo.  # noqa: E501
        :type: int
        """

        self._column = column

    @property
    def end_line(self):
        """Gets the end_line of this BTLocationInfo.  # noqa: E501


        :return: The end_line of this BTLocationInfo.  # noqa: E501
        :rtype: int
        """
        return self._end_line

    @end_line.setter
    def end_line(self, end_line):
        """Sets the end_line of this BTLocationInfo.


        :param end_line: The end_line of this BTLocationInfo.  # noqa: E501
        :type: int
        """

        self._end_line = end_line

    @property
    def changeable_child_field_indices(self):
        """Gets the changeable_child_field_indices of this BTLocationInfo.  # noqa: E501


        :return: The changeable_child_field_indices of this BTLocationInfo.  # noqa: E501
        :rtype: list[int]
        """
        return self._changeable_child_field_indices

    @changeable_child_field_indices.setter
    def changeable_child_field_indices(self, changeable_child_field_indices):
        """Sets the changeable_child_field_indices of this BTLocationInfo.


        :param changeable_child_field_indices: The changeable_child_field_indices of this BTLocationInfo.  # noqa: E501
        :type: list[int]
        """

        self._changeable_child_field_indices = changeable_child_field_indices

    @property
    def end_column(self):
        """Gets the end_column of this BTLocationInfo.  # noqa: E501


        :return: The end_column of this BTLocationInfo.  # noqa: E501
        :rtype: int
        """
        return self._end_column

    @end_column.setter
    def end_column(self, end_column):
        """Sets the end_column of this BTLocationInfo.


        :param end_column: The end_column of this BTLocationInfo.  # noqa: E501
        :type: int
        """

        self._end_column = end_column

    @property
    def character(self):
        """Gets the character of this BTLocationInfo.  # noqa: E501


        :return: The character of this BTLocationInfo.  # noqa: E501
        :rtype: int
        """
        return self._character

    @character.setter
    def character(self, character):
        """Sets the character of this BTLocationInfo.


        :param character: The character of this BTLocationInfo.  # noqa: E501
        :type: int
        """

        self._character = character

    @property
    def parse_node_id(self):
        """Gets the parse_node_id of this BTLocationInfo.  # noqa: E501


        :return: The parse_node_id of this BTLocationInfo.  # noqa: E501
        :rtype: str
        """
        return self._parse_node_id

    @parse_node_id.setter
    def parse_node_id(self, parse_node_id):
        """Sets the parse_node_id of this BTLocationInfo.


        :param parse_node_id: The parse_node_id of this BTLocationInfo.  # noqa: E501
        :type: str
        """

        self._parse_node_id = parse_node_id

    @property
    def end_character(self):
        """Gets the end_character of this BTLocationInfo.  # noqa: E501


        :return: The end_character of this BTLocationInfo.  # noqa: E501
        :rtype: int
        """
        return self._end_character

    @end_character.setter
    def end_character(self, end_character):
        """Sets the end_character of this BTLocationInfo.


        :param end_character: The end_character of this BTLocationInfo.  # noqa: E501
        :type: int
        """

        self._end_character = end_character

    @property
    def parse_node_id_raw(self):
        """Gets the parse_node_id_raw of this BTLocationInfo.  # noqa: E501


        :return: The parse_node_id_raw of this BTLocationInfo.  # noqa: E501
        :rtype: BTObjectId
        """
        return self._parse_node_id_raw

    @parse_node_id_raw.setter
    def parse_node_id_raw(self, parse_node_id_raw):
        """Sets the parse_node_id_raw of this BTLocationInfo.


        :param parse_node_id_raw: The parse_node_id_raw of this BTLocationInfo.  # noqa: E501
        :type: BTObjectId
        """

        self._parse_node_id_raw = parse_node_id_raw

    @property
    def node_id(self):
        """Gets the node_id of this BTLocationInfo.  # noqa: E501


        :return: The node_id of this BTLocationInfo.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this BTLocationInfo.


        :param node_id: The node_id of this BTLocationInfo.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def child_map_indices(self):
        """Gets the child_map_indices of this BTLocationInfo.  # noqa: E501


        :return: The child_map_indices of this BTLocationInfo.  # noqa: E501
        :rtype: list[int]
        """
        return self._child_map_indices

    @child_map_indices.setter
    def child_map_indices(self, child_map_indices):
        """Sets the child_map_indices of this BTLocationInfo.


        :param child_map_indices: The child_map_indices of this BTLocationInfo.  # noqa: E501
        :type: list[int]
        """

        self._child_map_indices = child_map_indices

    @property
    def atomic_child_indices(self):
        """Gets the atomic_child_indices of this BTLocationInfo.  # noqa: E501


        :return: The atomic_child_indices of this BTLocationInfo.  # noqa: E501
        :rtype: list[int]
        """
        return self._atomic_child_indices

    @atomic_child_indices.setter
    def atomic_child_indices(self, atomic_child_indices):
        """Sets the atomic_child_indices of this BTLocationInfo.


        :param atomic_child_indices: The atomic_child_indices of this BTLocationInfo.  # noqa: E501
        :type: list[int]
        """

        self._atomic_child_indices = atomic_child_indices

    @property
    def node_id_raw(self):
        """Gets the node_id_raw of this BTLocationInfo.  # noqa: E501


        :return: The node_id_raw of this BTLocationInfo.  # noqa: E501
        :rtype: BTObjectId
        """
        return self._node_id_raw

    @node_id_raw.setter
    def node_id_raw(self, node_id_raw):
        """Sets the node_id_raw of this BTLocationInfo.


        :param node_id_raw: The node_id_raw of this BTLocationInfo.  # noqa: E501
        :type: BTObjectId
        """

        self._node_id_raw = node_id_raw

    @property
    def first_child_field(self):
        """Gets the first_child_field of this BTLocationInfo.  # noqa: E501


        :return: The first_child_field of this BTLocationInfo.  # noqa: E501
        :rtype: int
        """
        return self._first_child_field

    @first_child_field.setter
    def first_child_field(self, first_child_field):
        """Sets the first_child_field of this BTLocationInfo.


        :param first_child_field: The first_child_field of this BTLocationInfo.  # noqa: E501
        :type: int
        """

        self._first_child_field = first_child_field

    @property
    def child_list_indices(self):
        """Gets the child_list_indices of this BTLocationInfo.  # noqa: E501


        :return: The child_list_indices of this BTLocationInfo.  # noqa: E501
        :rtype: list[int]
        """
        return self._child_list_indices

    @child_list_indices.setter
    def child_list_indices(self, child_list_indices):
        """Sets the child_list_indices of this BTLocationInfo.


        :param child_list_indices: The child_list_indices of this BTLocationInfo.  # noqa: E501
        :type: list[int]
        """

        self._child_list_indices = child_list_indices

    @property
    def type_id(self):
        """Gets the type_id of this BTLocationInfo.  # noqa: E501


        :return: The type_id of this BTLocationInfo.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this BTLocationInfo.


        :param type_id: The type_id of this BTLocationInfo.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

    @property
    def connection_source(self):
        """Gets the connection_source of this BTLocationInfo.  # noqa: E501


        :return: The connection_source of this BTLocationInfo.  # noqa: E501
        :rtype: BTConnection
        """
        return self._connection_source

    @connection_source.setter
    def connection_source(self, connection_source):
        """Sets the connection_source of this BTLocationInfo.


        :param connection_source: The connection_source of this BTLocationInfo.  # noqa: E501
        :type: BTConnection
        """

        self._connection_source = connection_source

    @property
    def export_type_name(self):
        """Gets the export_type_name of this BTLocationInfo.  # noqa: E501


        :return: The export_type_name of this BTLocationInfo.  # noqa: E501
        :rtype: str
        """
        return self._export_type_name

    @export_type_name.setter
    def export_type_name(self, export_type_name):
        """Sets the export_type_name of this BTLocationInfo.


        :param export_type_name: The export_type_name of this BTLocationInfo.  # noqa: E501
        :type: str
        """

        self._export_type_name = export_type_name

    @property
    def unknown_class(self):
        """Gets the unknown_class of this BTLocationInfo.  # noqa: E501


        :return: The unknown_class of this BTLocationInfo.  # noqa: E501
        :rtype: bool
        """
        return self._unknown_class

    @unknown_class.setter
    def unknown_class(self, unknown_class):
        """Sets the unknown_class of this BTLocationInfo.


        :param unknown_class: The unknown_class of this BTLocationInfo.  # noqa: E501
        :type: bool
        """

        self._unknown_class = unknown_class

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
        if not isinstance(other, BTLocationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

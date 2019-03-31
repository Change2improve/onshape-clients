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


class BTMoveElementParams(object):
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
        'name': 'str',
        'generate_unknown_messages': 'bool',
        'is_copy': 'bool',
        'need_new_version': 'bool',
        'is_deep_copy': 'bool',
        'anchor_element_id': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'version_name': 'str',
        'owner_id': 'str',
        'project_id': 'str',
        'parent_id': 'str',
        'is_public': 'bool',
        'target_document_id': 'str',
        'owner_type': 'int',
        'elements': 'list[str]',
        'source_document_id': 'str',
        'source_workspace_id': 'str',
        'is_group_anchor': 'bool',
        'target_workspace_id': 'str',
        'import_data': 'list[str]',
        'element_original_to_new_map': 'dict(str, str)',
        'is_new_document': 'bool',
        'owner_email': 'str'
    }

    attribute_map = {
        'name': 'name',
        'generate_unknown_messages': 'generateUnknownMessages',
        'is_copy': 'isCopy',
        'need_new_version': 'needNewVersion',
        'is_deep_copy': 'isDeepCopy',
        'anchor_element_id': 'anchorElementId',
        'description': 'description',
        'tags': 'tags',
        'version_name': 'versionName',
        'owner_id': 'ownerId',
        'project_id': 'projectId',
        'parent_id': 'parentId',
        'is_public': 'isPublic',
        'target_document_id': 'targetDocumentId',
        'owner_type': 'ownerType',
        'elements': 'elements',
        'source_document_id': 'sourceDocumentId',
        'source_workspace_id': 'sourceWorkspaceId',
        'is_group_anchor': 'isGroupAnchor',
        'target_workspace_id': 'targetWorkspaceId',
        'import_data': 'importData',
        'element_original_to_new_map': 'elementOriginalToNewMap',
        'is_new_document': 'isNewDocument',
        'owner_email': 'ownerEmail'
    }

    def __init__(self, name=None, generate_unknown_messages=None, is_copy=None, need_new_version=None, is_deep_copy=None, anchor_element_id=None, description=None, tags=None, version_name=None, owner_id=None, project_id=None, parent_id=None, is_public=None, target_document_id=None, owner_type=None, elements=None, source_document_id=None, source_workspace_id=None, is_group_anchor=None, target_workspace_id=None, import_data=None, element_original_to_new_map=None, is_new_document=None, owner_email=None):  # noqa: E501
        """BTMoveElementParams - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._generate_unknown_messages = None
        self._is_copy = None
        self._need_new_version = None
        self._is_deep_copy = None
        self._anchor_element_id = None
        self._description = None
        self._tags = None
        self._version_name = None
        self._owner_id = None
        self._project_id = None
        self._parent_id = None
        self._is_public = None
        self._target_document_id = None
        self._owner_type = None
        self._elements = None
        self._source_document_id = None
        self._source_workspace_id = None
        self._is_group_anchor = None
        self._target_workspace_id = None
        self._import_data = None
        self._element_original_to_new_map = None
        self._is_new_document = None
        self._owner_email = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if generate_unknown_messages is not None:
            self.generate_unknown_messages = generate_unknown_messages
        if is_copy is not None:
            self.is_copy = is_copy
        if need_new_version is not None:
            self.need_new_version = need_new_version
        if is_deep_copy is not None:
            self.is_deep_copy = is_deep_copy
        if anchor_element_id is not None:
            self.anchor_element_id = anchor_element_id
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if version_name is not None:
            self.version_name = version_name
        if owner_id is not None:
            self.owner_id = owner_id
        if project_id is not None:
            self.project_id = project_id
        if parent_id is not None:
            self.parent_id = parent_id
        if is_public is not None:
            self.is_public = is_public
        if target_document_id is not None:
            self.target_document_id = target_document_id
        if owner_type is not None:
            self.owner_type = owner_type
        if elements is not None:
            self.elements = elements
        if source_document_id is not None:
            self.source_document_id = source_document_id
        if source_workspace_id is not None:
            self.source_workspace_id = source_workspace_id
        if is_group_anchor is not None:
            self.is_group_anchor = is_group_anchor
        if target_workspace_id is not None:
            self.target_workspace_id = target_workspace_id
        if import_data is not None:
            self.import_data = import_data
        if element_original_to_new_map is not None:
            self.element_original_to_new_map = element_original_to_new_map
        if is_new_document is not None:
            self.is_new_document = is_new_document
        if owner_email is not None:
            self.owner_email = owner_email

    @property
    def name(self):
        """Gets the name of this BTMoveElementParams.  # noqa: E501


        :return: The name of this BTMoveElementParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTMoveElementParams.


        :param name: The name of this BTMoveElementParams.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def generate_unknown_messages(self):
        """Gets the generate_unknown_messages of this BTMoveElementParams.  # noqa: E501


        :return: The generate_unknown_messages of this BTMoveElementParams.  # noqa: E501
        :rtype: bool
        """
        return self._generate_unknown_messages

    @generate_unknown_messages.setter
    def generate_unknown_messages(self, generate_unknown_messages):
        """Sets the generate_unknown_messages of this BTMoveElementParams.


        :param generate_unknown_messages: The generate_unknown_messages of this BTMoveElementParams.  # noqa: E501
        :type: bool
        """

        self._generate_unknown_messages = generate_unknown_messages

    @property
    def is_copy(self):
        """Gets the is_copy of this BTMoveElementParams.  # noqa: E501


        :return: The is_copy of this BTMoveElementParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_copy

    @is_copy.setter
    def is_copy(self, is_copy):
        """Sets the is_copy of this BTMoveElementParams.


        :param is_copy: The is_copy of this BTMoveElementParams.  # noqa: E501
        :type: bool
        """

        self._is_copy = is_copy

    @property
    def need_new_version(self):
        """Gets the need_new_version of this BTMoveElementParams.  # noqa: E501


        :return: The need_new_version of this BTMoveElementParams.  # noqa: E501
        :rtype: bool
        """
        return self._need_new_version

    @need_new_version.setter
    def need_new_version(self, need_new_version):
        """Sets the need_new_version of this BTMoveElementParams.


        :param need_new_version: The need_new_version of this BTMoveElementParams.  # noqa: E501
        :type: bool
        """

        self._need_new_version = need_new_version

    @property
    def is_deep_copy(self):
        """Gets the is_deep_copy of this BTMoveElementParams.  # noqa: E501


        :return: The is_deep_copy of this BTMoveElementParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_deep_copy

    @is_deep_copy.setter
    def is_deep_copy(self, is_deep_copy):
        """Sets the is_deep_copy of this BTMoveElementParams.


        :param is_deep_copy: The is_deep_copy of this BTMoveElementParams.  # noqa: E501
        :type: bool
        """

        self._is_deep_copy = is_deep_copy

    @property
    def anchor_element_id(self):
        """Gets the anchor_element_id of this BTMoveElementParams.  # noqa: E501


        :return: The anchor_element_id of this BTMoveElementParams.  # noqa: E501
        :rtype: str
        """
        return self._anchor_element_id

    @anchor_element_id.setter
    def anchor_element_id(self, anchor_element_id):
        """Sets the anchor_element_id of this BTMoveElementParams.


        :param anchor_element_id: The anchor_element_id of this BTMoveElementParams.  # noqa: E501
        :type: str
        """

        self._anchor_element_id = anchor_element_id

    @property
    def description(self):
        """Gets the description of this BTMoveElementParams.  # noqa: E501


        :return: The description of this BTMoveElementParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTMoveElementParams.


        :param description: The description of this BTMoveElementParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this BTMoveElementParams.  # noqa: E501


        :return: The tags of this BTMoveElementParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BTMoveElementParams.


        :param tags: The tags of this BTMoveElementParams.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def version_name(self):
        """Gets the version_name of this BTMoveElementParams.  # noqa: E501


        :return: The version_name of this BTMoveElementParams.  # noqa: E501
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this BTMoveElementParams.


        :param version_name: The version_name of this BTMoveElementParams.  # noqa: E501
        :type: str
        """

        self._version_name = version_name

    @property
    def owner_id(self):
        """Gets the owner_id of this BTMoveElementParams.  # noqa: E501


        :return: The owner_id of this BTMoveElementParams.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this BTMoveElementParams.


        :param owner_id: The owner_id of this BTMoveElementParams.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def project_id(self):
        """Gets the project_id of this BTMoveElementParams.  # noqa: E501


        :return: The project_id of this BTMoveElementParams.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BTMoveElementParams.


        :param project_id: The project_id of this BTMoveElementParams.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def parent_id(self):
        """Gets the parent_id of this BTMoveElementParams.  # noqa: E501


        :return: The parent_id of this BTMoveElementParams.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this BTMoveElementParams.


        :param parent_id: The parent_id of this BTMoveElementParams.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def is_public(self):
        """Gets the is_public of this BTMoveElementParams.  # noqa: E501


        :return: The is_public of this BTMoveElementParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this BTMoveElementParams.


        :param is_public: The is_public of this BTMoveElementParams.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def target_document_id(self):
        """Gets the target_document_id of this BTMoveElementParams.  # noqa: E501


        :return: The target_document_id of this BTMoveElementParams.  # noqa: E501
        :rtype: str
        """
        return self._target_document_id

    @target_document_id.setter
    def target_document_id(self, target_document_id):
        """Sets the target_document_id of this BTMoveElementParams.


        :param target_document_id: The target_document_id of this BTMoveElementParams.  # noqa: E501
        :type: str
        """

        self._target_document_id = target_document_id

    @property
    def owner_type(self):
        """Gets the owner_type of this BTMoveElementParams.  # noqa: E501


        :return: The owner_type of this BTMoveElementParams.  # noqa: E501
        :rtype: int
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        """Sets the owner_type of this BTMoveElementParams.


        :param owner_type: The owner_type of this BTMoveElementParams.  # noqa: E501
        :type: int
        """

        self._owner_type = owner_type

    @property
    def elements(self):
        """Gets the elements of this BTMoveElementParams.  # noqa: E501


        :return: The elements of this BTMoveElementParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this BTMoveElementParams.


        :param elements: The elements of this BTMoveElementParams.  # noqa: E501
        :type: list[str]
        """

        self._elements = elements

    @property
    def source_document_id(self):
        """Gets the source_document_id of this BTMoveElementParams.  # noqa: E501


        :return: The source_document_id of this BTMoveElementParams.  # noqa: E501
        :rtype: str
        """
        return self._source_document_id

    @source_document_id.setter
    def source_document_id(self, source_document_id):
        """Sets the source_document_id of this BTMoveElementParams.


        :param source_document_id: The source_document_id of this BTMoveElementParams.  # noqa: E501
        :type: str
        """

        self._source_document_id = source_document_id

    @property
    def source_workspace_id(self):
        """Gets the source_workspace_id of this BTMoveElementParams.  # noqa: E501


        :return: The source_workspace_id of this BTMoveElementParams.  # noqa: E501
        :rtype: str
        """
        return self._source_workspace_id

    @source_workspace_id.setter
    def source_workspace_id(self, source_workspace_id):
        """Sets the source_workspace_id of this BTMoveElementParams.


        :param source_workspace_id: The source_workspace_id of this BTMoveElementParams.  # noqa: E501
        :type: str
        """

        self._source_workspace_id = source_workspace_id

    @property
    def is_group_anchor(self):
        """Gets the is_group_anchor of this BTMoveElementParams.  # noqa: E501


        :return: The is_group_anchor of this BTMoveElementParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_group_anchor

    @is_group_anchor.setter
    def is_group_anchor(self, is_group_anchor):
        """Sets the is_group_anchor of this BTMoveElementParams.


        :param is_group_anchor: The is_group_anchor of this BTMoveElementParams.  # noqa: E501
        :type: bool
        """

        self._is_group_anchor = is_group_anchor

    @property
    def target_workspace_id(self):
        """Gets the target_workspace_id of this BTMoveElementParams.  # noqa: E501


        :return: The target_workspace_id of this BTMoveElementParams.  # noqa: E501
        :rtype: str
        """
        return self._target_workspace_id

    @target_workspace_id.setter
    def target_workspace_id(self, target_workspace_id):
        """Sets the target_workspace_id of this BTMoveElementParams.


        :param target_workspace_id: The target_workspace_id of this BTMoveElementParams.  # noqa: E501
        :type: str
        """

        self._target_workspace_id = target_workspace_id

    @property
    def import_data(self):
        """Gets the import_data of this BTMoveElementParams.  # noqa: E501


        :return: The import_data of this BTMoveElementParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._import_data

    @import_data.setter
    def import_data(self, import_data):
        """Sets the import_data of this BTMoveElementParams.


        :param import_data: The import_data of this BTMoveElementParams.  # noqa: E501
        :type: list[str]
        """

        self._import_data = import_data

    @property
    def element_original_to_new_map(self):
        """Gets the element_original_to_new_map of this BTMoveElementParams.  # noqa: E501


        :return: The element_original_to_new_map of this BTMoveElementParams.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._element_original_to_new_map

    @element_original_to_new_map.setter
    def element_original_to_new_map(self, element_original_to_new_map):
        """Sets the element_original_to_new_map of this BTMoveElementParams.


        :param element_original_to_new_map: The element_original_to_new_map of this BTMoveElementParams.  # noqa: E501
        :type: dict(str, str)
        """

        self._element_original_to_new_map = element_original_to_new_map

    @property
    def is_new_document(self):
        """Gets the is_new_document of this BTMoveElementParams.  # noqa: E501


        :return: The is_new_document of this BTMoveElementParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_new_document

    @is_new_document.setter
    def is_new_document(self, is_new_document):
        """Sets the is_new_document of this BTMoveElementParams.


        :param is_new_document: The is_new_document of this BTMoveElementParams.  # noqa: E501
        :type: bool
        """

        self._is_new_document = is_new_document

    @property
    def owner_email(self):
        """Gets the owner_email of this BTMoveElementParams.  # noqa: E501


        :return: The owner_email of this BTMoveElementParams.  # noqa: E501
        :rtype: str
        """
        return self._owner_email

    @owner_email.setter
    def owner_email(self, owner_email):
        """Sets the owner_email of this BTMoveElementParams.


        :param owner_email: The owner_email of this BTMoveElementParams.  # noqa: E501
        :type: str
        """

        self._owner_email = owner_email

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
        if not isinstance(other, BTMoveElementParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

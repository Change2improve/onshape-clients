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


class BTProjectInfo(object):
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
        'permission_set': 'BTPermissionSet',
        'permission_scheme': 'BTRbacPermissionSchemeInfo',
        'role_map_entries': 'list[RoleMapEntry]',
        'trash': 'bool',
        'owner': 'BTOwnerInfo',
        'description': 'str',
        'tree_href': 'str',
        'is_mutable': 'bool',
        'resource_type': 'str',
        'created_at': 'datetime',
        'created_by': 'BTUserBasicSummaryInfo',
        'modified_by': 'BTUserBasicSummaryInfo',
        'modified_at': 'datetime',
        'project_id': 'str',
        'can_move': 'bool',
        'is_container': 'bool',
        'is_enterprise_owned': 'bool',
        'has_pending_owner': 'bool',
        'name': 'str',
        'id': 'str',
        'href': 'str',
        'view_ref': 'str'
    }

    attribute_map = {
        'permission_set': 'permissionSet',
        'permission_scheme': 'permissionScheme',
        'role_map_entries': 'roleMapEntries',
        'trash': 'trash',
        'owner': 'owner',
        'description': 'description',
        'tree_href': 'treeHref',
        'is_mutable': 'isMutable',
        'resource_type': 'resourceType',
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'modified_by': 'modifiedBy',
        'modified_at': 'modifiedAt',
        'project_id': 'projectId',
        'can_move': 'canMove',
        'is_container': 'isContainer',
        'is_enterprise_owned': 'isEnterpriseOwned',
        'has_pending_owner': 'hasPendingOwner',
        'name': 'name',
        'id': 'id',
        'href': 'href',
        'view_ref': 'viewRef'
    }

    def __init__(self, permission_set=None, permission_scheme=None, role_map_entries=None, trash=None, owner=None, description=None, tree_href=None, is_mutable=None, resource_type=None, created_at=None, created_by=None, modified_by=None, modified_at=None, project_id=None, can_move=None, is_container=None, is_enterprise_owned=None, has_pending_owner=None, name=None, id=None, href=None, view_ref=None):  # noqa: E501
        """BTProjectInfo - a model defined in OpenAPI"""  # noqa: E501

        self._permission_set = None
        self._permission_scheme = None
        self._role_map_entries = None
        self._trash = None
        self._owner = None
        self._description = None
        self._tree_href = None
        self._is_mutable = None
        self._resource_type = None
        self._created_at = None
        self._created_by = None
        self._modified_by = None
        self._modified_at = None
        self._project_id = None
        self._can_move = None
        self._is_container = None
        self._is_enterprise_owned = None
        self._has_pending_owner = None
        self._name = None
        self._id = None
        self._href = None
        self._view_ref = None
        self.discriminator = None

        if permission_set is not None:
            self.permission_set = permission_set
        if permission_scheme is not None:
            self.permission_scheme = permission_scheme
        if role_map_entries is not None:
            self.role_map_entries = role_map_entries
        if trash is not None:
            self.trash = trash
        if owner is not None:
            self.owner = owner
        if description is not None:
            self.description = description
        if tree_href is not None:
            self.tree_href = tree_href
        if is_mutable is not None:
            self.is_mutable = is_mutable
        if resource_type is not None:
            self.resource_type = resource_type
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_at is not None:
            self.modified_at = modified_at
        if project_id is not None:
            self.project_id = project_id
        if can_move is not None:
            self.can_move = can_move
        if is_container is not None:
            self.is_container = is_container
        if is_enterprise_owned is not None:
            self.is_enterprise_owned = is_enterprise_owned
        if has_pending_owner is not None:
            self.has_pending_owner = has_pending_owner
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref

    @property
    def permission_set(self):
        """Gets the permission_set of this BTProjectInfo.  # noqa: E501


        :return: The permission_set of this BTProjectInfo.  # noqa: E501
        :rtype: BTPermissionSet
        """
        return self._permission_set

    @permission_set.setter
    def permission_set(self, permission_set):
        """Sets the permission_set of this BTProjectInfo.


        :param permission_set: The permission_set of this BTProjectInfo.  # noqa: E501
        :type: BTPermissionSet
        """

        self._permission_set = permission_set

    @property
    def permission_scheme(self):
        """Gets the permission_scheme of this BTProjectInfo.  # noqa: E501


        :return: The permission_scheme of this BTProjectInfo.  # noqa: E501
        :rtype: BTRbacPermissionSchemeInfo
        """
        return self._permission_scheme

    @permission_scheme.setter
    def permission_scheme(self, permission_scheme):
        """Sets the permission_scheme of this BTProjectInfo.


        :param permission_scheme: The permission_scheme of this BTProjectInfo.  # noqa: E501
        :type: BTRbacPermissionSchemeInfo
        """

        self._permission_scheme = permission_scheme

    @property
    def role_map_entries(self):
        """Gets the role_map_entries of this BTProjectInfo.  # noqa: E501


        :return: The role_map_entries of this BTProjectInfo.  # noqa: E501
        :rtype: list[RoleMapEntry]
        """
        return self._role_map_entries

    @role_map_entries.setter
    def role_map_entries(self, role_map_entries):
        """Sets the role_map_entries of this BTProjectInfo.


        :param role_map_entries: The role_map_entries of this BTProjectInfo.  # noqa: E501
        :type: list[RoleMapEntry]
        """

        self._role_map_entries = role_map_entries

    @property
    def trash(self):
        """Gets the trash of this BTProjectInfo.  # noqa: E501


        :return: The trash of this BTProjectInfo.  # noqa: E501
        :rtype: bool
        """
        return self._trash

    @trash.setter
    def trash(self, trash):
        """Sets the trash of this BTProjectInfo.


        :param trash: The trash of this BTProjectInfo.  # noqa: E501
        :type: bool
        """

        self._trash = trash

    @property
    def owner(self):
        """Gets the owner of this BTProjectInfo.  # noqa: E501


        :return: The owner of this BTProjectInfo.  # noqa: E501
        :rtype: BTOwnerInfo
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this BTProjectInfo.


        :param owner: The owner of this BTProjectInfo.  # noqa: E501
        :type: BTOwnerInfo
        """

        self._owner = owner

    @property
    def description(self):
        """Gets the description of this BTProjectInfo.  # noqa: E501


        :return: The description of this BTProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTProjectInfo.


        :param description: The description of this BTProjectInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tree_href(self):
        """Gets the tree_href of this BTProjectInfo.  # noqa: E501


        :return: The tree_href of this BTProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._tree_href

    @tree_href.setter
    def tree_href(self, tree_href):
        """Sets the tree_href of this BTProjectInfo.


        :param tree_href: The tree_href of this BTProjectInfo.  # noqa: E501
        :type: str
        """

        self._tree_href = tree_href

    @property
    def is_mutable(self):
        """Gets the is_mutable of this BTProjectInfo.  # noqa: E501


        :return: The is_mutable of this BTProjectInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_mutable

    @is_mutable.setter
    def is_mutable(self, is_mutable):
        """Sets the is_mutable of this BTProjectInfo.


        :param is_mutable: The is_mutable of this BTProjectInfo.  # noqa: E501
        :type: bool
        """

        self._is_mutable = is_mutable

    @property
    def resource_type(self):
        """Gets the resource_type of this BTProjectInfo.  # noqa: E501


        :return: The resource_type of this BTProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this BTProjectInfo.


        :param resource_type: The resource_type of this BTProjectInfo.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def created_at(self):
        """Gets the created_at of this BTProjectInfo.  # noqa: E501


        :return: The created_at of this BTProjectInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BTProjectInfo.


        :param created_at: The created_at of this BTProjectInfo.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this BTProjectInfo.  # noqa: E501


        :return: The created_by of this BTProjectInfo.  # noqa: E501
        :rtype: BTUserBasicSummaryInfo
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this BTProjectInfo.


        :param created_by: The created_by of this BTProjectInfo.  # noqa: E501
        :type: BTUserBasicSummaryInfo
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this BTProjectInfo.  # noqa: E501


        :return: The modified_by of this BTProjectInfo.  # noqa: E501
        :rtype: BTUserBasicSummaryInfo
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this BTProjectInfo.


        :param modified_by: The modified_by of this BTProjectInfo.  # noqa: E501
        :type: BTUserBasicSummaryInfo
        """

        self._modified_by = modified_by

    @property
    def modified_at(self):
        """Gets the modified_at of this BTProjectInfo.  # noqa: E501


        :return: The modified_at of this BTProjectInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this BTProjectInfo.


        :param modified_at: The modified_at of this BTProjectInfo.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def project_id(self):
        """Gets the project_id of this BTProjectInfo.  # noqa: E501


        :return: The project_id of this BTProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BTProjectInfo.


        :param project_id: The project_id of this BTProjectInfo.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def can_move(self):
        """Gets the can_move of this BTProjectInfo.  # noqa: E501


        :return: The can_move of this BTProjectInfo.  # noqa: E501
        :rtype: bool
        """
        return self._can_move

    @can_move.setter
    def can_move(self, can_move):
        """Sets the can_move of this BTProjectInfo.


        :param can_move: The can_move of this BTProjectInfo.  # noqa: E501
        :type: bool
        """

        self._can_move = can_move

    @property
    def is_container(self):
        """Gets the is_container of this BTProjectInfo.  # noqa: E501


        :return: The is_container of this BTProjectInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_container

    @is_container.setter
    def is_container(self, is_container):
        """Sets the is_container of this BTProjectInfo.


        :param is_container: The is_container of this BTProjectInfo.  # noqa: E501
        :type: bool
        """

        self._is_container = is_container

    @property
    def is_enterprise_owned(self):
        """Gets the is_enterprise_owned of this BTProjectInfo.  # noqa: E501


        :return: The is_enterprise_owned of this BTProjectInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_enterprise_owned

    @is_enterprise_owned.setter
    def is_enterprise_owned(self, is_enterprise_owned):
        """Sets the is_enterprise_owned of this BTProjectInfo.


        :param is_enterprise_owned: The is_enterprise_owned of this BTProjectInfo.  # noqa: E501
        :type: bool
        """

        self._is_enterprise_owned = is_enterprise_owned

    @property
    def has_pending_owner(self):
        """Gets the has_pending_owner of this BTProjectInfo.  # noqa: E501


        :return: The has_pending_owner of this BTProjectInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_pending_owner

    @has_pending_owner.setter
    def has_pending_owner(self, has_pending_owner):
        """Sets the has_pending_owner of this BTProjectInfo.


        :param has_pending_owner: The has_pending_owner of this BTProjectInfo.  # noqa: E501
        :type: bool
        """

        self._has_pending_owner = has_pending_owner

    @property
    def name(self):
        """Gets the name of this BTProjectInfo.  # noqa: E501


        :return: The name of this BTProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTProjectInfo.


        :param name: The name of this BTProjectInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTProjectInfo.  # noqa: E501


        :return: The id of this BTProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTProjectInfo.


        :param id: The id of this BTProjectInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this BTProjectInfo.  # noqa: E501


        :return: The href of this BTProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTProjectInfo.


        :param href: The href of this BTProjectInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTProjectInfo.  # noqa: E501


        :return: The view_ref of this BTProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTProjectInfo.


        :param view_ref: The view_ref of this BTProjectInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

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
        if not isinstance(other, BTProjectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

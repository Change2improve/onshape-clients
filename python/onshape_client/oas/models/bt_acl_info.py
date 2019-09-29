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


class BTAclInfo(object):
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
        'admin': 'bool',
        'inherited_acls': 'list[BTInheritedAclInfo]',
        'shared_with_support': 'bool',
        'entries': 'list[BTAclEntryInfo]',
        'object_id': 'str',
        'object_type': 'int',
        'visibility': 'str',
        'public': 'bool',
        'owner': 'BTOwnerInfo',
        'href': 'str',
        'view_ref': 'str',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'admin': 'admin',
        'inherited_acls': 'inheritedAcls',
        'shared_with_support': 'sharedWithSupport',
        'entries': 'entries',
        'object_id': 'objectId',
        'object_type': 'objectType',
        'visibility': 'visibility',
        'public': 'public',
        'owner': 'owner',
        'href': 'href',
        'view_ref': 'viewRef',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, admin=None, inherited_acls=None, shared_with_support=None, entries=None, object_id=None, object_type=None, visibility=None, public=None, owner=None, href=None, view_ref=None, name=None, id=None):  # noqa: E501
        """BTAclInfo - a model defined in OpenAPI"""  # noqa: E501

        self._admin = None
        self._inherited_acls = None
        self._shared_with_support = None
        self._entries = None
        self._object_id = None
        self._object_type = None
        self._visibility = None
        self._public = None
        self._owner = None
        self._href = None
        self._view_ref = None
        self._name = None
        self._id = None
        self.discriminator = None

        if admin is not None:
            self.admin = admin
        if inherited_acls is not None:
            self.inherited_acls = inherited_acls
        if shared_with_support is not None:
            self.shared_with_support = shared_with_support
        if entries is not None:
            self.entries = entries
        if object_id is not None:
            self.object_id = object_id
        if object_type is not None:
            self.object_type = object_type
        if visibility is not None:
            self.visibility = visibility
        if public is not None:
            self.public = public
        if owner is not None:
            self.owner = owner
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def admin(self):
        """Gets the admin of this BTAclInfo.  # noqa: E501


        :return: The admin of this BTAclInfo.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this BTAclInfo.


        :param admin: The admin of this BTAclInfo.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def inherited_acls(self):
        """Gets the inherited_acls of this BTAclInfo.  # noqa: E501


        :return: The inherited_acls of this BTAclInfo.  # noqa: E501
        :rtype: list[BTInheritedAclInfo]
        """
        return self._inherited_acls

    @inherited_acls.setter
    def inherited_acls(self, inherited_acls):
        """Sets the inherited_acls of this BTAclInfo.


        :param inherited_acls: The inherited_acls of this BTAclInfo.  # noqa: E501
        :type: list[BTInheritedAclInfo]
        """

        self._inherited_acls = inherited_acls

    @property
    def shared_with_support(self):
        """Gets the shared_with_support of this BTAclInfo.  # noqa: E501


        :return: The shared_with_support of this BTAclInfo.  # noqa: E501
        :rtype: bool
        """
        return self._shared_with_support

    @shared_with_support.setter
    def shared_with_support(self, shared_with_support):
        """Sets the shared_with_support of this BTAclInfo.


        :param shared_with_support: The shared_with_support of this BTAclInfo.  # noqa: E501
        :type: bool
        """

        self._shared_with_support = shared_with_support

    @property
    def entries(self):
        """Gets the entries of this BTAclInfo.  # noqa: E501


        :return: The entries of this BTAclInfo.  # noqa: E501
        :rtype: list[BTAclEntryInfo]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this BTAclInfo.


        :param entries: The entries of this BTAclInfo.  # noqa: E501
        :type: list[BTAclEntryInfo]
        """

        self._entries = entries

    @property
    def object_id(self):
        """Gets the object_id of this BTAclInfo.  # noqa: E501


        :return: The object_id of this BTAclInfo.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this BTAclInfo.


        :param object_id: The object_id of this BTAclInfo.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def object_type(self):
        """Gets the object_type of this BTAclInfo.  # noqa: E501


        :return: The object_type of this BTAclInfo.  # noqa: E501
        :rtype: int
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this BTAclInfo.


        :param object_type: The object_type of this BTAclInfo.  # noqa: E501
        :type: int
        """

        self._object_type = object_type

    @property
    def visibility(self):
        """Gets the visibility of this BTAclInfo.  # noqa: E501


        :return: The visibility of this BTAclInfo.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this BTAclInfo.


        :param visibility: The visibility of this BTAclInfo.  # noqa: E501
        :type: str
        """

        self._visibility = visibility

    @property
    def public(self):
        """Gets the public of this BTAclInfo.  # noqa: E501


        :return: The public of this BTAclInfo.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this BTAclInfo.


        :param public: The public of this BTAclInfo.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def owner(self):
        """Gets the owner of this BTAclInfo.  # noqa: E501


        :return: The owner of this BTAclInfo.  # noqa: E501
        :rtype: BTOwnerInfo
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this BTAclInfo.


        :param owner: The owner of this BTAclInfo.  # noqa: E501
        :type: BTOwnerInfo
        """

        self._owner = owner

    @property
    def href(self):
        """Gets the href of this BTAclInfo.  # noqa: E501


        :return: The href of this BTAclInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTAclInfo.


        :param href: The href of this BTAclInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTAclInfo.  # noqa: E501


        :return: The view_ref of this BTAclInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTAclInfo.


        :param view_ref: The view_ref of this BTAclInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

    @property
    def name(self):
        """Gets the name of this BTAclInfo.  # noqa: E501


        :return: The name of this BTAclInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTAclInfo.


        :param name: The name of this BTAclInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTAclInfo.  # noqa: E501


        :return: The id of this BTAclInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTAclInfo.


        :param id: The id of this BTAclInfo.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, BTAclInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

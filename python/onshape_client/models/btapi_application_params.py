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


class BTAPIApplicationParams(object):
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
        'hidden_from_plus_menu_': 'bool',
        'name': 'str',
        'state': 'int',
        'description': 'str',
        'scope_names': 'list[str]',
        'primary_format': 'str',
        'internal_grant_on_demand': 'bool',
        'client_id': 'str',
        'base_href': 'str',
        'supports_collaboration': 'bool',
        'developer_id': 'str',
        'redirect_ur_ls': 'list[str]',
        'ui_spec': 'str',
        'supports_merge': 'bool',
        'admin_team_id': 'str',
        'hidden_from_plus_menu': 'bool',
        'store_entry_is_public': 'bool',
        'developer_email': 'str'
    }

    attribute_map = {
        'hidden_from_plus_menu_': 'hiddenFromPlusMenu_',
        'name': 'name',
        'state': 'state',
        'description': 'description',
        'scope_names': 'scopeNames',
        'primary_format': 'primaryFormat',
        'internal_grant_on_demand': 'internalGrantOnDemand',
        'client_id': 'clientId',
        'base_href': 'baseHref',
        'supports_collaboration': 'supportsCollaboration',
        'developer_id': 'developerId',
        'redirect_ur_ls': 'redirectURLs',
        'ui_spec': 'uiSpec',
        'supports_merge': 'supportsMerge',
        'admin_team_id': 'adminTeamId',
        'hidden_from_plus_menu': 'hiddenFromPlusMenu',
        'store_entry_is_public': 'storeEntryIsPublic',
        'developer_email': 'developerEmail'
    }

    def __init__(self, hidden_from_plus_menu_=None, name=None, state=None, description=None, scope_names=None, primary_format=None, internal_grant_on_demand=None, client_id=None, base_href=None, supports_collaboration=None, developer_id=None, redirect_ur_ls=None, ui_spec=None, supports_merge=None, admin_team_id=None, hidden_from_plus_menu=None, store_entry_is_public=None, developer_email=None):  # noqa: E501
        """BTAPIApplicationParams - a model defined in OpenAPI"""  # noqa: E501

        self._hidden_from_plus_menu_ = None
        self._name = None
        self._state = None
        self._description = None
        self._scope_names = None
        self._primary_format = None
        self._internal_grant_on_demand = None
        self._client_id = None
        self._base_href = None
        self._supports_collaboration = None
        self._developer_id = None
        self._redirect_ur_ls = None
        self._ui_spec = None
        self._supports_merge = None
        self._admin_team_id = None
        self._hidden_from_plus_menu = None
        self._store_entry_is_public = None
        self._developer_email = None
        self.discriminator = None

        if hidden_from_plus_menu_ is not None:
            self.hidden_from_plus_menu_ = hidden_from_plus_menu_
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if description is not None:
            self.description = description
        if scope_names is not None:
            self.scope_names = scope_names
        if primary_format is not None:
            self.primary_format = primary_format
        if internal_grant_on_demand is not None:
            self.internal_grant_on_demand = internal_grant_on_demand
        if client_id is not None:
            self.client_id = client_id
        if base_href is not None:
            self.base_href = base_href
        if supports_collaboration is not None:
            self.supports_collaboration = supports_collaboration
        if developer_id is not None:
            self.developer_id = developer_id
        if redirect_ur_ls is not None:
            self.redirect_ur_ls = redirect_ur_ls
        if ui_spec is not None:
            self.ui_spec = ui_spec
        if supports_merge is not None:
            self.supports_merge = supports_merge
        if admin_team_id is not None:
            self.admin_team_id = admin_team_id
        if hidden_from_plus_menu is not None:
            self.hidden_from_plus_menu = hidden_from_plus_menu
        if store_entry_is_public is not None:
            self.store_entry_is_public = store_entry_is_public
        if developer_email is not None:
            self.developer_email = developer_email

    @property
    def hidden_from_plus_menu_(self):
        """Gets the hidden_from_plus_menu_ of this BTAPIApplicationParams.  # noqa: E501


        :return: The hidden_from_plus_menu_ of this BTAPIApplicationParams.  # noqa: E501
        :rtype: bool
        """
        return self._hidden_from_plus_menu_

    @hidden_from_plus_menu_.setter
    def hidden_from_plus_menu_(self, hidden_from_plus_menu_):
        """Sets the hidden_from_plus_menu_ of this BTAPIApplicationParams.


        :param hidden_from_plus_menu_: The hidden_from_plus_menu_ of this BTAPIApplicationParams.  # noqa: E501
        :type: bool
        """

        self._hidden_from_plus_menu_ = hidden_from_plus_menu_

    @property
    def name(self):
        """Gets the name of this BTAPIApplicationParams.  # noqa: E501


        :return: The name of this BTAPIApplicationParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTAPIApplicationParams.


        :param name: The name of this BTAPIApplicationParams.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def state(self):
        """Gets the state of this BTAPIApplicationParams.  # noqa: E501


        :return: The state of this BTAPIApplicationParams.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BTAPIApplicationParams.


        :param state: The state of this BTAPIApplicationParams.  # noqa: E501
        :type: int
        """

        self._state = state

    @property
    def description(self):
        """Gets the description of this BTAPIApplicationParams.  # noqa: E501


        :return: The description of this BTAPIApplicationParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTAPIApplicationParams.


        :param description: The description of this BTAPIApplicationParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def scope_names(self):
        """Gets the scope_names of this BTAPIApplicationParams.  # noqa: E501


        :return: The scope_names of this BTAPIApplicationParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._scope_names

    @scope_names.setter
    def scope_names(self, scope_names):
        """Sets the scope_names of this BTAPIApplicationParams.


        :param scope_names: The scope_names of this BTAPIApplicationParams.  # noqa: E501
        :type: list[str]
        """

        self._scope_names = scope_names

    @property
    def primary_format(self):
        """Gets the primary_format of this BTAPIApplicationParams.  # noqa: E501


        :return: The primary_format of this BTAPIApplicationParams.  # noqa: E501
        :rtype: str
        """
        return self._primary_format

    @primary_format.setter
    def primary_format(self, primary_format):
        """Sets the primary_format of this BTAPIApplicationParams.


        :param primary_format: The primary_format of this BTAPIApplicationParams.  # noqa: E501
        :type: str
        """

        self._primary_format = primary_format

    @property
    def internal_grant_on_demand(self):
        """Gets the internal_grant_on_demand of this BTAPIApplicationParams.  # noqa: E501


        :return: The internal_grant_on_demand of this BTAPIApplicationParams.  # noqa: E501
        :rtype: bool
        """
        return self._internal_grant_on_demand

    @internal_grant_on_demand.setter
    def internal_grant_on_demand(self, internal_grant_on_demand):
        """Sets the internal_grant_on_demand of this BTAPIApplicationParams.


        :param internal_grant_on_demand: The internal_grant_on_demand of this BTAPIApplicationParams.  # noqa: E501
        :type: bool
        """

        self._internal_grant_on_demand = internal_grant_on_demand

    @property
    def client_id(self):
        """Gets the client_id of this BTAPIApplicationParams.  # noqa: E501


        :return: The client_id of this BTAPIApplicationParams.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this BTAPIApplicationParams.


        :param client_id: The client_id of this BTAPIApplicationParams.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def base_href(self):
        """Gets the base_href of this BTAPIApplicationParams.  # noqa: E501


        :return: The base_href of this BTAPIApplicationParams.  # noqa: E501
        :rtype: str
        """
        return self._base_href

    @base_href.setter
    def base_href(self, base_href):
        """Sets the base_href of this BTAPIApplicationParams.


        :param base_href: The base_href of this BTAPIApplicationParams.  # noqa: E501
        :type: str
        """

        self._base_href = base_href

    @property
    def supports_collaboration(self):
        """Gets the supports_collaboration of this BTAPIApplicationParams.  # noqa: E501


        :return: The supports_collaboration of this BTAPIApplicationParams.  # noqa: E501
        :rtype: bool
        """
        return self._supports_collaboration

    @supports_collaboration.setter
    def supports_collaboration(self, supports_collaboration):
        """Sets the supports_collaboration of this BTAPIApplicationParams.


        :param supports_collaboration: The supports_collaboration of this BTAPIApplicationParams.  # noqa: E501
        :type: bool
        """

        self._supports_collaboration = supports_collaboration

    @property
    def developer_id(self):
        """Gets the developer_id of this BTAPIApplicationParams.  # noqa: E501


        :return: The developer_id of this BTAPIApplicationParams.  # noqa: E501
        :rtype: str
        """
        return self._developer_id

    @developer_id.setter
    def developer_id(self, developer_id):
        """Sets the developer_id of this BTAPIApplicationParams.


        :param developer_id: The developer_id of this BTAPIApplicationParams.  # noqa: E501
        :type: str
        """

        self._developer_id = developer_id

    @property
    def redirect_ur_ls(self):
        """Gets the redirect_ur_ls of this BTAPIApplicationParams.  # noqa: E501


        :return: The redirect_ur_ls of this BTAPIApplicationParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._redirect_ur_ls

    @redirect_ur_ls.setter
    def redirect_ur_ls(self, redirect_ur_ls):
        """Sets the redirect_ur_ls of this BTAPIApplicationParams.


        :param redirect_ur_ls: The redirect_ur_ls of this BTAPIApplicationParams.  # noqa: E501
        :type: list[str]
        """

        self._redirect_ur_ls = redirect_ur_ls

    @property
    def ui_spec(self):
        """Gets the ui_spec of this BTAPIApplicationParams.  # noqa: E501


        :return: The ui_spec of this BTAPIApplicationParams.  # noqa: E501
        :rtype: str
        """
        return self._ui_spec

    @ui_spec.setter
    def ui_spec(self, ui_spec):
        """Sets the ui_spec of this BTAPIApplicationParams.


        :param ui_spec: The ui_spec of this BTAPIApplicationParams.  # noqa: E501
        :type: str
        """

        self._ui_spec = ui_spec

    @property
    def supports_merge(self):
        """Gets the supports_merge of this BTAPIApplicationParams.  # noqa: E501


        :return: The supports_merge of this BTAPIApplicationParams.  # noqa: E501
        :rtype: bool
        """
        return self._supports_merge

    @supports_merge.setter
    def supports_merge(self, supports_merge):
        """Sets the supports_merge of this BTAPIApplicationParams.


        :param supports_merge: The supports_merge of this BTAPIApplicationParams.  # noqa: E501
        :type: bool
        """

        self._supports_merge = supports_merge

    @property
    def admin_team_id(self):
        """Gets the admin_team_id of this BTAPIApplicationParams.  # noqa: E501


        :return: The admin_team_id of this BTAPIApplicationParams.  # noqa: E501
        :rtype: str
        """
        return self._admin_team_id

    @admin_team_id.setter
    def admin_team_id(self, admin_team_id):
        """Sets the admin_team_id of this BTAPIApplicationParams.


        :param admin_team_id: The admin_team_id of this BTAPIApplicationParams.  # noqa: E501
        :type: str
        """

        self._admin_team_id = admin_team_id

    @property
    def hidden_from_plus_menu(self):
        """Gets the hidden_from_plus_menu of this BTAPIApplicationParams.  # noqa: E501


        :return: The hidden_from_plus_menu of this BTAPIApplicationParams.  # noqa: E501
        :rtype: bool
        """
        return self._hidden_from_plus_menu

    @hidden_from_plus_menu.setter
    def hidden_from_plus_menu(self, hidden_from_plus_menu):
        """Sets the hidden_from_plus_menu of this BTAPIApplicationParams.


        :param hidden_from_plus_menu: The hidden_from_plus_menu of this BTAPIApplicationParams.  # noqa: E501
        :type: bool
        """

        self._hidden_from_plus_menu = hidden_from_plus_menu

    @property
    def store_entry_is_public(self):
        """Gets the store_entry_is_public of this BTAPIApplicationParams.  # noqa: E501


        :return: The store_entry_is_public of this BTAPIApplicationParams.  # noqa: E501
        :rtype: bool
        """
        return self._store_entry_is_public

    @store_entry_is_public.setter
    def store_entry_is_public(self, store_entry_is_public):
        """Sets the store_entry_is_public of this BTAPIApplicationParams.


        :param store_entry_is_public: The store_entry_is_public of this BTAPIApplicationParams.  # noqa: E501
        :type: bool
        """

        self._store_entry_is_public = store_entry_is_public

    @property
    def developer_email(self):
        """Gets the developer_email of this BTAPIApplicationParams.  # noqa: E501


        :return: The developer_email of this BTAPIApplicationParams.  # noqa: E501
        :rtype: str
        """
        return self._developer_email

    @developer_email.setter
    def developer_email(self, developer_email):
        """Sets the developer_email of this BTAPIApplicationParams.


        :param developer_email: The developer_email of this BTAPIApplicationParams.  # noqa: E501
        :type: str
        """

        self._developer_email = developer_email

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
        if not isinstance(other, BTAPIApplicationParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

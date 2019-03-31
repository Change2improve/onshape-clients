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


class BTInAppMessageInfo(object):
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
        'context': 'int',
        'content': 'list[BTInAppMessageContent]',
        'description': 'str',
        'content_type': 'int',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'rule_id': 'str',
        'looker_query': 'int',
        'population_task_id': 'str',
        'billing_plan_ids': 'list[str]',
        'domain_type': 'int',
        'show_once': 'bool',
        'display_order': 'int',
        'content_index': 'int',
        'name': 'str',
        'id': 'str',
        'href': 'str',
        'view_ref': 'str'
    }

    attribute_map = {
        'context': 'context',
        'content': 'content',
        'description': 'description',
        'content_type': 'contentType',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'rule_id': 'ruleId',
        'looker_query': 'lookerQuery',
        'population_task_id': 'populationTaskId',
        'billing_plan_ids': 'billingPlanIds',
        'domain_type': 'domainType',
        'show_once': 'showOnce',
        'display_order': 'displayOrder',
        'content_index': 'contentIndex',
        'name': 'name',
        'id': 'id',
        'href': 'href',
        'view_ref': 'viewRef'
    }

    def __init__(self, context=None, content=None, description=None, content_type=None, start_date=None, end_date=None, rule_id=None, looker_query=None, population_task_id=None, billing_plan_ids=None, domain_type=None, show_once=None, display_order=None, content_index=None, name=None, id=None, href=None, view_ref=None):  # noqa: E501
        """BTInAppMessageInfo - a model defined in OpenAPI"""  # noqa: E501

        self._context = None
        self._content = None
        self._description = None
        self._content_type = None
        self._start_date = None
        self._end_date = None
        self._rule_id = None
        self._looker_query = None
        self._population_task_id = None
        self._billing_plan_ids = None
        self._domain_type = None
        self._show_once = None
        self._display_order = None
        self._content_index = None
        self._name = None
        self._id = None
        self._href = None
        self._view_ref = None
        self.discriminator = None

        if context is not None:
            self.context = context
        if content is not None:
            self.content = content
        if description is not None:
            self.description = description
        if content_type is not None:
            self.content_type = content_type
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if rule_id is not None:
            self.rule_id = rule_id
        if looker_query is not None:
            self.looker_query = looker_query
        if population_task_id is not None:
            self.population_task_id = population_task_id
        if billing_plan_ids is not None:
            self.billing_plan_ids = billing_plan_ids
        if domain_type is not None:
            self.domain_type = domain_type
        if show_once is not None:
            self.show_once = show_once
        if display_order is not None:
            self.display_order = display_order
        if content_index is not None:
            self.content_index = content_index
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref

    @property
    def context(self):
        """Gets the context of this BTInAppMessageInfo.  # noqa: E501


        :return: The context of this BTInAppMessageInfo.  # noqa: E501
        :rtype: int
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this BTInAppMessageInfo.


        :param context: The context of this BTInAppMessageInfo.  # noqa: E501
        :type: int
        """

        self._context = context

    @property
    def content(self):
        """Gets the content of this BTInAppMessageInfo.  # noqa: E501


        :return: The content of this BTInAppMessageInfo.  # noqa: E501
        :rtype: list[BTInAppMessageContent]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this BTInAppMessageInfo.


        :param content: The content of this BTInAppMessageInfo.  # noqa: E501
        :type: list[BTInAppMessageContent]
        """

        self._content = content

    @property
    def description(self):
        """Gets the description of this BTInAppMessageInfo.  # noqa: E501


        :return: The description of this BTInAppMessageInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTInAppMessageInfo.


        :param description: The description of this BTInAppMessageInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def content_type(self):
        """Gets the content_type of this BTInAppMessageInfo.  # noqa: E501


        :return: The content_type of this BTInAppMessageInfo.  # noqa: E501
        :rtype: int
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this BTInAppMessageInfo.


        :param content_type: The content_type of this BTInAppMessageInfo.  # noqa: E501
        :type: int
        """

        self._content_type = content_type

    @property
    def start_date(self):
        """Gets the start_date of this BTInAppMessageInfo.  # noqa: E501


        :return: The start_date of this BTInAppMessageInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this BTInAppMessageInfo.


        :param start_date: The start_date of this BTInAppMessageInfo.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this BTInAppMessageInfo.  # noqa: E501


        :return: The end_date of this BTInAppMessageInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this BTInAppMessageInfo.


        :param end_date: The end_date of this BTInAppMessageInfo.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def rule_id(self):
        """Gets the rule_id of this BTInAppMessageInfo.  # noqa: E501


        :return: The rule_id of this BTInAppMessageInfo.  # noqa: E501
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this BTInAppMessageInfo.


        :param rule_id: The rule_id of this BTInAppMessageInfo.  # noqa: E501
        :type: str
        """

        self._rule_id = rule_id

    @property
    def looker_query(self):
        """Gets the looker_query of this BTInAppMessageInfo.  # noqa: E501


        :return: The looker_query of this BTInAppMessageInfo.  # noqa: E501
        :rtype: int
        """
        return self._looker_query

    @looker_query.setter
    def looker_query(self, looker_query):
        """Sets the looker_query of this BTInAppMessageInfo.


        :param looker_query: The looker_query of this BTInAppMessageInfo.  # noqa: E501
        :type: int
        """

        self._looker_query = looker_query

    @property
    def population_task_id(self):
        """Gets the population_task_id of this BTInAppMessageInfo.  # noqa: E501


        :return: The population_task_id of this BTInAppMessageInfo.  # noqa: E501
        :rtype: str
        """
        return self._population_task_id

    @population_task_id.setter
    def population_task_id(self, population_task_id):
        """Sets the population_task_id of this BTInAppMessageInfo.


        :param population_task_id: The population_task_id of this BTInAppMessageInfo.  # noqa: E501
        :type: str
        """

        self._population_task_id = population_task_id

    @property
    def billing_plan_ids(self):
        """Gets the billing_plan_ids of this BTInAppMessageInfo.  # noqa: E501


        :return: The billing_plan_ids of this BTInAppMessageInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._billing_plan_ids

    @billing_plan_ids.setter
    def billing_plan_ids(self, billing_plan_ids):
        """Sets the billing_plan_ids of this BTInAppMessageInfo.


        :param billing_plan_ids: The billing_plan_ids of this BTInAppMessageInfo.  # noqa: E501
        :type: list[str]
        """

        self._billing_plan_ids = billing_plan_ids

    @property
    def domain_type(self):
        """Gets the domain_type of this BTInAppMessageInfo.  # noqa: E501


        :return: The domain_type of this BTInAppMessageInfo.  # noqa: E501
        :rtype: int
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this BTInAppMessageInfo.


        :param domain_type: The domain_type of this BTInAppMessageInfo.  # noqa: E501
        :type: int
        """

        self._domain_type = domain_type

    @property
    def show_once(self):
        """Gets the show_once of this BTInAppMessageInfo.  # noqa: E501


        :return: The show_once of this BTInAppMessageInfo.  # noqa: E501
        :rtype: bool
        """
        return self._show_once

    @show_once.setter
    def show_once(self, show_once):
        """Sets the show_once of this BTInAppMessageInfo.


        :param show_once: The show_once of this BTInAppMessageInfo.  # noqa: E501
        :type: bool
        """

        self._show_once = show_once

    @property
    def display_order(self):
        """Gets the display_order of this BTInAppMessageInfo.  # noqa: E501


        :return: The display_order of this BTInAppMessageInfo.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this BTInAppMessageInfo.


        :param display_order: The display_order of this BTInAppMessageInfo.  # noqa: E501
        :type: int
        """

        self._display_order = display_order

    @property
    def content_index(self):
        """Gets the content_index of this BTInAppMessageInfo.  # noqa: E501


        :return: The content_index of this BTInAppMessageInfo.  # noqa: E501
        :rtype: int
        """
        return self._content_index

    @content_index.setter
    def content_index(self, content_index):
        """Sets the content_index of this BTInAppMessageInfo.


        :param content_index: The content_index of this BTInAppMessageInfo.  # noqa: E501
        :type: int
        """

        self._content_index = content_index

    @property
    def name(self):
        """Gets the name of this BTInAppMessageInfo.  # noqa: E501


        :return: The name of this BTInAppMessageInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTInAppMessageInfo.


        :param name: The name of this BTInAppMessageInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTInAppMessageInfo.  # noqa: E501


        :return: The id of this BTInAppMessageInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTInAppMessageInfo.


        :param id: The id of this BTInAppMessageInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this BTInAppMessageInfo.  # noqa: E501


        :return: The href of this BTInAppMessageInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTInAppMessageInfo.


        :param href: The href of this BTInAppMessageInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTInAppMessageInfo.  # noqa: E501


        :return: The view_ref of this BTInAppMessageInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTInAppMessageInfo.


        :param view_ref: The view_ref of this BTInAppMessageInfo.  # noqa: E501
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
        if not isinstance(other, BTInAppMessageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class BTBetaCapabilityMetricsInfo(object):
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
        'state_pre_approved': 'int',
        'state_requested': 'int',
        'state_approved': 'int',
        'state_removed': 'int',
        'approved_pre_approved': 'int',
        'approved_requested': 'int',
        'approved_paid': 'int',
        'approved_onshape': 'int',
        'href': 'str',
        'view_ref': 'str',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'state_pre_approved': 'statePreApproved',
        'state_requested': 'stateRequested',
        'state_approved': 'stateApproved',
        'state_removed': 'stateRemoved',
        'approved_pre_approved': 'approvedPreApproved',
        'approved_requested': 'approvedRequested',
        'approved_paid': 'approvedPaid',
        'approved_onshape': 'approvedOnshape',
        'href': 'href',
        'view_ref': 'viewRef',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, state_pre_approved=None, state_requested=None, state_approved=None, state_removed=None, approved_pre_approved=None, approved_requested=None, approved_paid=None, approved_onshape=None, href=None, view_ref=None, name=None, id=None):  # noqa: E501
        """BTBetaCapabilityMetricsInfo - a model defined in OpenAPI"""  # noqa: E501

        self._state_pre_approved = None
        self._state_requested = None
        self._state_approved = None
        self._state_removed = None
        self._approved_pre_approved = None
        self._approved_requested = None
        self._approved_paid = None
        self._approved_onshape = None
        self._href = None
        self._view_ref = None
        self._name = None
        self._id = None
        self.discriminator = None

        if state_pre_approved is not None:
            self.state_pre_approved = state_pre_approved
        if state_requested is not None:
            self.state_requested = state_requested
        if state_approved is not None:
            self.state_approved = state_approved
        if state_removed is not None:
            self.state_removed = state_removed
        if approved_pre_approved is not None:
            self.approved_pre_approved = approved_pre_approved
        if approved_requested is not None:
            self.approved_requested = approved_requested
        if approved_paid is not None:
            self.approved_paid = approved_paid
        if approved_onshape is not None:
            self.approved_onshape = approved_onshape
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def state_pre_approved(self):
        """Gets the state_pre_approved of this BTBetaCapabilityMetricsInfo.  # noqa: E501


        :return: The state_pre_approved of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :rtype: int
        """
        return self._state_pre_approved

    @state_pre_approved.setter
    def state_pre_approved(self, state_pre_approved):
        """Sets the state_pre_approved of this BTBetaCapabilityMetricsInfo.


        :param state_pre_approved: The state_pre_approved of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :type: int
        """

        self._state_pre_approved = state_pre_approved

    @property
    def state_requested(self):
        """Gets the state_requested of this BTBetaCapabilityMetricsInfo.  # noqa: E501


        :return: The state_requested of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :rtype: int
        """
        return self._state_requested

    @state_requested.setter
    def state_requested(self, state_requested):
        """Sets the state_requested of this BTBetaCapabilityMetricsInfo.


        :param state_requested: The state_requested of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :type: int
        """

        self._state_requested = state_requested

    @property
    def state_approved(self):
        """Gets the state_approved of this BTBetaCapabilityMetricsInfo.  # noqa: E501


        :return: The state_approved of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :rtype: int
        """
        return self._state_approved

    @state_approved.setter
    def state_approved(self, state_approved):
        """Sets the state_approved of this BTBetaCapabilityMetricsInfo.


        :param state_approved: The state_approved of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :type: int
        """

        self._state_approved = state_approved

    @property
    def state_removed(self):
        """Gets the state_removed of this BTBetaCapabilityMetricsInfo.  # noqa: E501


        :return: The state_removed of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :rtype: int
        """
        return self._state_removed

    @state_removed.setter
    def state_removed(self, state_removed):
        """Sets the state_removed of this BTBetaCapabilityMetricsInfo.


        :param state_removed: The state_removed of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :type: int
        """

        self._state_removed = state_removed

    @property
    def approved_pre_approved(self):
        """Gets the approved_pre_approved of this BTBetaCapabilityMetricsInfo.  # noqa: E501


        :return: The approved_pre_approved of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :rtype: int
        """
        return self._approved_pre_approved

    @approved_pre_approved.setter
    def approved_pre_approved(self, approved_pre_approved):
        """Sets the approved_pre_approved of this BTBetaCapabilityMetricsInfo.


        :param approved_pre_approved: The approved_pre_approved of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :type: int
        """

        self._approved_pre_approved = approved_pre_approved

    @property
    def approved_requested(self):
        """Gets the approved_requested of this BTBetaCapabilityMetricsInfo.  # noqa: E501


        :return: The approved_requested of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :rtype: int
        """
        return self._approved_requested

    @approved_requested.setter
    def approved_requested(self, approved_requested):
        """Sets the approved_requested of this BTBetaCapabilityMetricsInfo.


        :param approved_requested: The approved_requested of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :type: int
        """

        self._approved_requested = approved_requested

    @property
    def approved_paid(self):
        """Gets the approved_paid of this BTBetaCapabilityMetricsInfo.  # noqa: E501


        :return: The approved_paid of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :rtype: int
        """
        return self._approved_paid

    @approved_paid.setter
    def approved_paid(self, approved_paid):
        """Sets the approved_paid of this BTBetaCapabilityMetricsInfo.


        :param approved_paid: The approved_paid of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :type: int
        """

        self._approved_paid = approved_paid

    @property
    def approved_onshape(self):
        """Gets the approved_onshape of this BTBetaCapabilityMetricsInfo.  # noqa: E501


        :return: The approved_onshape of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :rtype: int
        """
        return self._approved_onshape

    @approved_onshape.setter
    def approved_onshape(self, approved_onshape):
        """Sets the approved_onshape of this BTBetaCapabilityMetricsInfo.


        :param approved_onshape: The approved_onshape of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :type: int
        """

        self._approved_onshape = approved_onshape

    @property
    def href(self):
        """Gets the href of this BTBetaCapabilityMetricsInfo.  # noqa: E501


        :return: The href of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTBetaCapabilityMetricsInfo.


        :param href: The href of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTBetaCapabilityMetricsInfo.  # noqa: E501


        :return: The view_ref of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTBetaCapabilityMetricsInfo.


        :param view_ref: The view_ref of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

    @property
    def name(self):
        """Gets the name of this BTBetaCapabilityMetricsInfo.  # noqa: E501


        :return: The name of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTBetaCapabilityMetricsInfo.


        :param name: The name of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTBetaCapabilityMetricsInfo.  # noqa: E501


        :return: The id of this BTBetaCapabilityMetricsInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTBetaCapabilityMetricsInfo.


        :param id: The id of this BTBetaCapabilityMetricsInfo.  # noqa: E501
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
        if not isinstance(other, BTBetaCapabilityMetricsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class BTPurchaseParams(object):
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
        'password': 'str',
        'email': 'str',
        'plan_id': 'str',
        'seats': 'int',
        'domain_prefix': 'str',
        'light_seats': 'int',
        'allow_deprecated_plan': 'bool',
        'user_id': 'str',
        'payment_type': 'int',
        'trial_period_days': 'int',
        'reseller_name': 'str'
    }

    attribute_map = {
        'password': 'password',
        'email': 'email',
        'plan_id': 'planId',
        'seats': 'seats',
        'domain_prefix': 'domainPrefix',
        'light_seats': 'lightSeats',
        'allow_deprecated_plan': 'allowDeprecatedPlan',
        'user_id': 'userId',
        'payment_type': 'paymentType',
        'trial_period_days': 'trialPeriodDays',
        'reseller_name': 'resellerName'
    }

    def __init__(self, password=None, email=None, plan_id=None, seats=None, domain_prefix=None, light_seats=None, allow_deprecated_plan=None, user_id=None, payment_type=None, trial_period_days=None, reseller_name=None):  # noqa: E501
        """BTPurchaseParams - a model defined in OpenAPI"""  # noqa: E501

        self._password = None
        self._email = None
        self._plan_id = None
        self._seats = None
        self._domain_prefix = None
        self._light_seats = None
        self._allow_deprecated_plan = None
        self._user_id = None
        self._payment_type = None
        self._trial_period_days = None
        self._reseller_name = None
        self.discriminator = None

        if password is not None:
            self.password = password
        if email is not None:
            self.email = email
        if plan_id is not None:
            self.plan_id = plan_id
        if seats is not None:
            self.seats = seats
        if domain_prefix is not None:
            self.domain_prefix = domain_prefix
        if light_seats is not None:
            self.light_seats = light_seats
        if allow_deprecated_plan is not None:
            self.allow_deprecated_plan = allow_deprecated_plan
        if user_id is not None:
            self.user_id = user_id
        if payment_type is not None:
            self.payment_type = payment_type
        if trial_period_days is not None:
            self.trial_period_days = trial_period_days
        if reseller_name is not None:
            self.reseller_name = reseller_name

    @property
    def password(self):
        """Gets the password of this BTPurchaseParams.  # noqa: E501


        :return: The password of this BTPurchaseParams.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this BTPurchaseParams.


        :param password: The password of this BTPurchaseParams.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def email(self):
        """Gets the email of this BTPurchaseParams.  # noqa: E501


        :return: The email of this BTPurchaseParams.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BTPurchaseParams.


        :param email: The email of this BTPurchaseParams.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def plan_id(self):
        """Gets the plan_id of this BTPurchaseParams.  # noqa: E501


        :return: The plan_id of this BTPurchaseParams.  # noqa: E501
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this BTPurchaseParams.


        :param plan_id: The plan_id of this BTPurchaseParams.  # noqa: E501
        :type: str
        """

        self._plan_id = plan_id

    @property
    def seats(self):
        """Gets the seats of this BTPurchaseParams.  # noqa: E501


        :return: The seats of this BTPurchaseParams.  # noqa: E501
        :rtype: int
        """
        return self._seats

    @seats.setter
    def seats(self, seats):
        """Sets the seats of this BTPurchaseParams.


        :param seats: The seats of this BTPurchaseParams.  # noqa: E501
        :type: int
        """

        self._seats = seats

    @property
    def domain_prefix(self):
        """Gets the domain_prefix of this BTPurchaseParams.  # noqa: E501


        :return: The domain_prefix of this BTPurchaseParams.  # noqa: E501
        :rtype: str
        """
        return self._domain_prefix

    @domain_prefix.setter
    def domain_prefix(self, domain_prefix):
        """Sets the domain_prefix of this BTPurchaseParams.


        :param domain_prefix: The domain_prefix of this BTPurchaseParams.  # noqa: E501
        :type: str
        """

        self._domain_prefix = domain_prefix

    @property
    def light_seats(self):
        """Gets the light_seats of this BTPurchaseParams.  # noqa: E501


        :return: The light_seats of this BTPurchaseParams.  # noqa: E501
        :rtype: int
        """
        return self._light_seats

    @light_seats.setter
    def light_seats(self, light_seats):
        """Sets the light_seats of this BTPurchaseParams.


        :param light_seats: The light_seats of this BTPurchaseParams.  # noqa: E501
        :type: int
        """

        self._light_seats = light_seats

    @property
    def allow_deprecated_plan(self):
        """Gets the allow_deprecated_plan of this BTPurchaseParams.  # noqa: E501


        :return: The allow_deprecated_plan of this BTPurchaseParams.  # noqa: E501
        :rtype: bool
        """
        return self._allow_deprecated_plan

    @allow_deprecated_plan.setter
    def allow_deprecated_plan(self, allow_deprecated_plan):
        """Sets the allow_deprecated_plan of this BTPurchaseParams.


        :param allow_deprecated_plan: The allow_deprecated_plan of this BTPurchaseParams.  # noqa: E501
        :type: bool
        """

        self._allow_deprecated_plan = allow_deprecated_plan

    @property
    def user_id(self):
        """Gets the user_id of this BTPurchaseParams.  # noqa: E501


        :return: The user_id of this BTPurchaseParams.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BTPurchaseParams.


        :param user_id: The user_id of this BTPurchaseParams.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def payment_type(self):
        """Gets the payment_type of this BTPurchaseParams.  # noqa: E501


        :return: The payment_type of this BTPurchaseParams.  # noqa: E501
        :rtype: int
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this BTPurchaseParams.


        :param payment_type: The payment_type of this BTPurchaseParams.  # noqa: E501
        :type: int
        """

        self._payment_type = payment_type

    @property
    def trial_period_days(self):
        """Gets the trial_period_days of this BTPurchaseParams.  # noqa: E501


        :return: The trial_period_days of this BTPurchaseParams.  # noqa: E501
        :rtype: int
        """
        return self._trial_period_days

    @trial_period_days.setter
    def trial_period_days(self, trial_period_days):
        """Sets the trial_period_days of this BTPurchaseParams.


        :param trial_period_days: The trial_period_days of this BTPurchaseParams.  # noqa: E501
        :type: int
        """

        self._trial_period_days = trial_period_days

    @property
    def reseller_name(self):
        """Gets the reseller_name of this BTPurchaseParams.  # noqa: E501


        :return: The reseller_name of this BTPurchaseParams.  # noqa: E501
        :rtype: str
        """
        return self._reseller_name

    @reseller_name.setter
    def reseller_name(self, reseller_name):
        """Sets the reseller_name of this BTPurchaseParams.


        :param reseller_name: The reseller_name of this BTPurchaseParams.  # noqa: E501
        :type: str
        """

        self._reseller_name = reseller_name

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
        if not isinstance(other, BTPurchaseParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

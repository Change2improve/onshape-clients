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


class BTReleasePackageItem(object):
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
        'id': 'str',
        'state': 'int',
        'revision': 'str',
        'part_id': 'str',
        'mime_type': 'str',
        'created_at': 'datetime',
        'document_id': 'str',
        'version_id': 'str',
        'element_id': 'str',
        'part_number': 'str',
        'company_id': 'str',
        'element_type': 'int',
        'workspace_id': 'str',
        'modified_at': 'datetime',
        'microversion_id': 'str',
        'children': 'list[BTReleasePackageItem]',
        'configuration': 'str',
        'created_by': 'str',
        'modified_by': 'str',
        'configuration_key': 'str',
        'revision_rule_id': 'str',
        'is_included': 'bool',
        'remote_state': 'int',
        'diff_thumbnail_configuration_key': 'str',
        'small_thumbnail_href': 'str',
        'initial_revision': 'str',
        'is_revision_managed': 'bool',
        'errors': 'list[BTReleasePackageItemError]',
        'rpid': 'str',
        'obsoletion_revision_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'state': 'state',
        'revision': 'revision',
        'part_id': 'partId',
        'mime_type': 'mimeType',
        'created_at': 'createdAt',
        'document_id': 'documentId',
        'version_id': 'versionId',
        'element_id': 'elementId',
        'part_number': 'partNumber',
        'company_id': 'companyId',
        'element_type': 'elementType',
        'workspace_id': 'workspaceId',
        'modified_at': 'modifiedAt',
        'microversion_id': 'microversionId',
        'children': 'children',
        'configuration': 'configuration',
        'created_by': 'createdBy',
        'modified_by': 'modifiedBy',
        'configuration_key': 'configurationKey',
        'revision_rule_id': 'revisionRuleId',
        'is_included': 'isIncluded',
        'remote_state': 'remoteState',
        'diff_thumbnail_configuration_key': 'diffThumbnailConfigurationKey',
        'small_thumbnail_href': 'smallThumbnailHref',
        'initial_revision': 'initialRevision',
        'is_revision_managed': 'isRevisionManaged',
        'errors': 'errors',
        'rpid': 'rpid',
        'obsoletion_revision_id': 'obsoletionRevisionId'
    }

    def __init__(self, name=None, id=None, state=None, revision=None, part_id=None, mime_type=None, created_at=None, document_id=None, version_id=None, element_id=None, part_number=None, company_id=None, element_type=None, workspace_id=None, modified_at=None, microversion_id=None, children=None, configuration=None, created_by=None, modified_by=None, configuration_key=None, revision_rule_id=None, is_included=None, remote_state=None, diff_thumbnail_configuration_key=None, small_thumbnail_href=None, initial_revision=None, is_revision_managed=None, errors=None, rpid=None, obsoletion_revision_id=None):  # noqa: E501
        """BTReleasePackageItem - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._id = None
        self._state = None
        self._revision = None
        self._part_id = None
        self._mime_type = None
        self._created_at = None
        self._document_id = None
        self._version_id = None
        self._element_id = None
        self._part_number = None
        self._company_id = None
        self._element_type = None
        self._workspace_id = None
        self._modified_at = None
        self._microversion_id = None
        self._children = None
        self._configuration = None
        self._created_by = None
        self._modified_by = None
        self._configuration_key = None
        self._revision_rule_id = None
        self._is_included = None
        self._remote_state = None
        self._diff_thumbnail_configuration_key = None
        self._small_thumbnail_href = None
        self._initial_revision = None
        self._is_revision_managed = None
        self._errors = None
        self._rpid = None
        self._obsoletion_revision_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if revision is not None:
            self.revision = revision
        if part_id is not None:
            self.part_id = part_id
        if mime_type is not None:
            self.mime_type = mime_type
        if created_at is not None:
            self.created_at = created_at
        if document_id is not None:
            self.document_id = document_id
        if version_id is not None:
            self.version_id = version_id
        if element_id is not None:
            self.element_id = element_id
        if part_number is not None:
            self.part_number = part_number
        if company_id is not None:
            self.company_id = company_id
        if element_type is not None:
            self.element_type = element_type
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if modified_at is not None:
            self.modified_at = modified_at
        if microversion_id is not None:
            self.microversion_id = microversion_id
        if children is not None:
            self.children = children
        if configuration is not None:
            self.configuration = configuration
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by
        if configuration_key is not None:
            self.configuration_key = configuration_key
        if revision_rule_id is not None:
            self.revision_rule_id = revision_rule_id
        if is_included is not None:
            self.is_included = is_included
        if remote_state is not None:
            self.remote_state = remote_state
        if diff_thumbnail_configuration_key is not None:
            self.diff_thumbnail_configuration_key = diff_thumbnail_configuration_key
        if small_thumbnail_href is not None:
            self.small_thumbnail_href = small_thumbnail_href
        if initial_revision is not None:
            self.initial_revision = initial_revision
        if is_revision_managed is not None:
            self.is_revision_managed = is_revision_managed
        if errors is not None:
            self.errors = errors
        if rpid is not None:
            self.rpid = rpid
        if obsoletion_revision_id is not None:
            self.obsoletion_revision_id = obsoletion_revision_id

    @property
    def name(self):
        """Gets the name of this BTReleasePackageItem.  # noqa: E501


        :return: The name of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTReleasePackageItem.


        :param name: The name of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTReleasePackageItem.  # noqa: E501


        :return: The id of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTReleasePackageItem.


        :param id: The id of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this BTReleasePackageItem.  # noqa: E501


        :return: The state of this BTReleasePackageItem.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BTReleasePackageItem.


        :param state: The state of this BTReleasePackageItem.  # noqa: E501
        :type: int
        """

        self._state = state

    @property
    def revision(self):
        """Gets the revision of this BTReleasePackageItem.  # noqa: E501


        :return: The revision of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this BTReleasePackageItem.


        :param revision: The revision of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def part_id(self):
        """Gets the part_id of this BTReleasePackageItem.  # noqa: E501


        :return: The part_id of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """Sets the part_id of this BTReleasePackageItem.


        :param part_id: The part_id of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._part_id = part_id

    @property
    def mime_type(self):
        """Gets the mime_type of this BTReleasePackageItem.  # noqa: E501


        :return: The mime_type of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this BTReleasePackageItem.


        :param mime_type: The mime_type of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def created_at(self):
        """Gets the created_at of this BTReleasePackageItem.  # noqa: E501


        :return: The created_at of this BTReleasePackageItem.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BTReleasePackageItem.


        :param created_at: The created_at of this BTReleasePackageItem.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def document_id(self):
        """Gets the document_id of this BTReleasePackageItem.  # noqa: E501


        :return: The document_id of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTReleasePackageItem.


        :param document_id: The document_id of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def version_id(self):
        """Gets the version_id of this BTReleasePackageItem.  # noqa: E501


        :return: The version_id of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this BTReleasePackageItem.


        :param version_id: The version_id of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def element_id(self):
        """Gets the element_id of this BTReleasePackageItem.  # noqa: E501


        :return: The element_id of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTReleasePackageItem.


        :param element_id: The element_id of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def part_number(self):
        """Gets the part_number of this BTReleasePackageItem.  # noqa: E501


        :return: The part_number of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this BTReleasePackageItem.


        :param part_number: The part_number of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def company_id(self):
        """Gets the company_id of this BTReleasePackageItem.  # noqa: E501


        :return: The company_id of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this BTReleasePackageItem.


        :param company_id: The company_id of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def element_type(self):
        """Gets the element_type of this BTReleasePackageItem.  # noqa: E501


        :return: The element_type of this BTReleasePackageItem.  # noqa: E501
        :rtype: int
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this BTReleasePackageItem.


        :param element_type: The element_type of this BTReleasePackageItem.  # noqa: E501
        :type: int
        """

        self._element_type = element_type

    @property
    def workspace_id(self):
        """Gets the workspace_id of this BTReleasePackageItem.  # noqa: E501


        :return: The workspace_id of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this BTReleasePackageItem.


        :param workspace_id: The workspace_id of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def modified_at(self):
        """Gets the modified_at of this BTReleasePackageItem.  # noqa: E501


        :return: The modified_at of this BTReleasePackageItem.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this BTReleasePackageItem.


        :param modified_at: The modified_at of this BTReleasePackageItem.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def microversion_id(self):
        """Gets the microversion_id of this BTReleasePackageItem.  # noqa: E501


        :return: The microversion_id of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._microversion_id

    @microversion_id.setter
    def microversion_id(self, microversion_id):
        """Sets the microversion_id of this BTReleasePackageItem.


        :param microversion_id: The microversion_id of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._microversion_id = microversion_id

    @property
    def children(self):
        """Gets the children of this BTReleasePackageItem.  # noqa: E501


        :return: The children of this BTReleasePackageItem.  # noqa: E501
        :rtype: list[BTReleasePackageItem]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this BTReleasePackageItem.


        :param children: The children of this BTReleasePackageItem.  # noqa: E501
        :type: list[BTReleasePackageItem]
        """

        self._children = children

    @property
    def configuration(self):
        """Gets the configuration of this BTReleasePackageItem.  # noqa: E501


        :return: The configuration of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this BTReleasePackageItem.


        :param configuration: The configuration of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def created_by(self):
        """Gets the created_by of this BTReleasePackageItem.  # noqa: E501


        :return: The created_by of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this BTReleasePackageItem.


        :param created_by: The created_by of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this BTReleasePackageItem.  # noqa: E501


        :return: The modified_by of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this BTReleasePackageItem.


        :param modified_by: The modified_by of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def configuration_key(self):
        """Gets the configuration_key of this BTReleasePackageItem.  # noqa: E501


        :return: The configuration_key of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._configuration_key

    @configuration_key.setter
    def configuration_key(self, configuration_key):
        """Sets the configuration_key of this BTReleasePackageItem.


        :param configuration_key: The configuration_key of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._configuration_key = configuration_key

    @property
    def revision_rule_id(self):
        """Gets the revision_rule_id of this BTReleasePackageItem.  # noqa: E501


        :return: The revision_rule_id of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._revision_rule_id

    @revision_rule_id.setter
    def revision_rule_id(self, revision_rule_id):
        """Sets the revision_rule_id of this BTReleasePackageItem.


        :param revision_rule_id: The revision_rule_id of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._revision_rule_id = revision_rule_id

    @property
    def is_included(self):
        """Gets the is_included of this BTReleasePackageItem.  # noqa: E501


        :return: The is_included of this BTReleasePackageItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_included

    @is_included.setter
    def is_included(self, is_included):
        """Sets the is_included of this BTReleasePackageItem.


        :param is_included: The is_included of this BTReleasePackageItem.  # noqa: E501
        :type: bool
        """

        self._is_included = is_included

    @property
    def remote_state(self):
        """Gets the remote_state of this BTReleasePackageItem.  # noqa: E501


        :return: The remote_state of this BTReleasePackageItem.  # noqa: E501
        :rtype: int
        """
        return self._remote_state

    @remote_state.setter
    def remote_state(self, remote_state):
        """Sets the remote_state of this BTReleasePackageItem.


        :param remote_state: The remote_state of this BTReleasePackageItem.  # noqa: E501
        :type: int
        """

        self._remote_state = remote_state

    @property
    def diff_thumbnail_configuration_key(self):
        """Gets the diff_thumbnail_configuration_key of this BTReleasePackageItem.  # noqa: E501


        :return: The diff_thumbnail_configuration_key of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._diff_thumbnail_configuration_key

    @diff_thumbnail_configuration_key.setter
    def diff_thumbnail_configuration_key(self, diff_thumbnail_configuration_key):
        """Sets the diff_thumbnail_configuration_key of this BTReleasePackageItem.


        :param diff_thumbnail_configuration_key: The diff_thumbnail_configuration_key of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._diff_thumbnail_configuration_key = diff_thumbnail_configuration_key

    @property
    def small_thumbnail_href(self):
        """Gets the small_thumbnail_href of this BTReleasePackageItem.  # noqa: E501


        :return: The small_thumbnail_href of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._small_thumbnail_href

    @small_thumbnail_href.setter
    def small_thumbnail_href(self, small_thumbnail_href):
        """Sets the small_thumbnail_href of this BTReleasePackageItem.


        :param small_thumbnail_href: The small_thumbnail_href of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._small_thumbnail_href = small_thumbnail_href

    @property
    def initial_revision(self):
        """Gets the initial_revision of this BTReleasePackageItem.  # noqa: E501


        :return: The initial_revision of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._initial_revision

    @initial_revision.setter
    def initial_revision(self, initial_revision):
        """Sets the initial_revision of this BTReleasePackageItem.


        :param initial_revision: The initial_revision of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._initial_revision = initial_revision

    @property
    def is_revision_managed(self):
        """Gets the is_revision_managed of this BTReleasePackageItem.  # noqa: E501


        :return: The is_revision_managed of this BTReleasePackageItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_revision_managed

    @is_revision_managed.setter
    def is_revision_managed(self, is_revision_managed):
        """Sets the is_revision_managed of this BTReleasePackageItem.


        :param is_revision_managed: The is_revision_managed of this BTReleasePackageItem.  # noqa: E501
        :type: bool
        """

        self._is_revision_managed = is_revision_managed

    @property
    def errors(self):
        """Gets the errors of this BTReleasePackageItem.  # noqa: E501


        :return: The errors of this BTReleasePackageItem.  # noqa: E501
        :rtype: list[BTReleasePackageItemError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this BTReleasePackageItem.


        :param errors: The errors of this BTReleasePackageItem.  # noqa: E501
        :type: list[BTReleasePackageItemError]
        """

        self._errors = errors

    @property
    def rpid(self):
        """Gets the rpid of this BTReleasePackageItem.  # noqa: E501


        :return: The rpid of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._rpid

    @rpid.setter
    def rpid(self, rpid):
        """Sets the rpid of this BTReleasePackageItem.


        :param rpid: The rpid of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._rpid = rpid

    @property
    def obsoletion_revision_id(self):
        """Gets the obsoletion_revision_id of this BTReleasePackageItem.  # noqa: E501


        :return: The obsoletion_revision_id of this BTReleasePackageItem.  # noqa: E501
        :rtype: str
        """
        return self._obsoletion_revision_id

    @obsoletion_revision_id.setter
    def obsoletion_revision_id(self, obsoletion_revision_id):
        """Sets the obsoletion_revision_id of this BTReleasePackageItem.


        :param obsoletion_revision_id: The obsoletion_revision_id of this BTReleasePackageItem.  # noqa: E501
        :type: str
        """

        self._obsoletion_revision_id = obsoletion_revision_id

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
        if not isinstance(other, BTReleasePackageItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

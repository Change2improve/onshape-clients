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


class BTReleasePackageItemInfo(object):
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
        'properties': 'list[BTMetadataPropertyInfo]',
        'element_type': 'int',
        'mime_type': 'str',
        'configuration': 'str',
        'company_id': 'str',
        'configuration_key': 'str',
        'workspace_id': 'str',
        'element_id': 'str',
        'document_id': 'str',
        'version_id': 'str',
        'part_id': 'str',
        'small_thumbnail_href': 'str',
        'is_revision_managed': 'bool',
        'errors': 'list[BTReleasePackageItemError]',
        'is_included_editable': 'bool',
        'diff_thumbnail_configuration_key': 'str',
        'rpid': 'str',
        'obsoletion_revision_id': 'str',
        'name': 'str',
        'id': 'str',
        'href': 'str',
        'view_ref': 'str'
    }

    attribute_map = {
        'properties': 'properties',
        'element_type': 'elementType',
        'mime_type': 'mimeType',
        'configuration': 'configuration',
        'company_id': 'companyId',
        'configuration_key': 'configurationKey',
        'workspace_id': 'workspaceId',
        'element_id': 'elementId',
        'document_id': 'documentId',
        'version_id': 'versionId',
        'part_id': 'partId',
        'small_thumbnail_href': 'smallThumbnailHref',
        'is_revision_managed': 'isRevisionManaged',
        'errors': 'errors',
        'is_included_editable': 'isIncludedEditable',
        'diff_thumbnail_configuration_key': 'diffThumbnailConfigurationKey',
        'rpid': 'rpid',
        'obsoletion_revision_id': 'obsoletionRevisionId',
        'name': 'name',
        'id': 'id',
        'href': 'href',
        'view_ref': 'viewRef'
    }

    def __init__(self, properties=None, element_type=None, mime_type=None, configuration=None, company_id=None, configuration_key=None, workspace_id=None, element_id=None, document_id=None, version_id=None, part_id=None, small_thumbnail_href=None, is_revision_managed=None, errors=None, is_included_editable=None, diff_thumbnail_configuration_key=None, rpid=None, obsoletion_revision_id=None, name=None, id=None, href=None, view_ref=None):  # noqa: E501
        """BTReleasePackageItemInfo - a model defined in OpenAPI"""  # noqa: E501

        self._properties = None
        self._element_type = None
        self._mime_type = None
        self._configuration = None
        self._company_id = None
        self._configuration_key = None
        self._workspace_id = None
        self._element_id = None
        self._document_id = None
        self._version_id = None
        self._part_id = None
        self._small_thumbnail_href = None
        self._is_revision_managed = None
        self._errors = None
        self._is_included_editable = None
        self._diff_thumbnail_configuration_key = None
        self._rpid = None
        self._obsoletion_revision_id = None
        self._name = None
        self._id = None
        self._href = None
        self._view_ref = None
        self.discriminator = None

        if properties is not None:
            self.properties = properties
        if element_type is not None:
            self.element_type = element_type
        if mime_type is not None:
            self.mime_type = mime_type
        if configuration is not None:
            self.configuration = configuration
        if company_id is not None:
            self.company_id = company_id
        if configuration_key is not None:
            self.configuration_key = configuration_key
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if element_id is not None:
            self.element_id = element_id
        if document_id is not None:
            self.document_id = document_id
        if version_id is not None:
            self.version_id = version_id
        if part_id is not None:
            self.part_id = part_id
        if small_thumbnail_href is not None:
            self.small_thumbnail_href = small_thumbnail_href
        if is_revision_managed is not None:
            self.is_revision_managed = is_revision_managed
        if errors is not None:
            self.errors = errors
        if is_included_editable is not None:
            self.is_included_editable = is_included_editable
        if diff_thumbnail_configuration_key is not None:
            self.diff_thumbnail_configuration_key = diff_thumbnail_configuration_key
        if rpid is not None:
            self.rpid = rpid
        if obsoletion_revision_id is not None:
            self.obsoletion_revision_id = obsoletion_revision_id
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref

    @property
    def properties(self):
        """Gets the properties of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The properties of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: list[BTMetadataPropertyInfo]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this BTReleasePackageItemInfo.


        :param properties: The properties of this BTReleasePackageItemInfo.  # noqa: E501
        :type: list[BTMetadataPropertyInfo]
        """

        self._properties = properties

    @property
    def element_type(self):
        """Gets the element_type of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The element_type of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: int
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this BTReleasePackageItemInfo.


        :param element_type: The element_type of this BTReleasePackageItemInfo.  # noqa: E501
        :type: int
        """

        self._element_type = element_type

    @property
    def mime_type(self):
        """Gets the mime_type of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The mime_type of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this BTReleasePackageItemInfo.


        :param mime_type: The mime_type of this BTReleasePackageItemInfo.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def configuration(self):
        """Gets the configuration of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The configuration of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this BTReleasePackageItemInfo.


        :param configuration: The configuration of this BTReleasePackageItemInfo.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def company_id(self):
        """Gets the company_id of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The company_id of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this BTReleasePackageItemInfo.


        :param company_id: The company_id of this BTReleasePackageItemInfo.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def configuration_key(self):
        """Gets the configuration_key of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The configuration_key of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._configuration_key

    @configuration_key.setter
    def configuration_key(self, configuration_key):
        """Sets the configuration_key of this BTReleasePackageItemInfo.


        :param configuration_key: The configuration_key of this BTReleasePackageItemInfo.  # noqa: E501
        :type: str
        """

        self._configuration_key = configuration_key

    @property
    def workspace_id(self):
        """Gets the workspace_id of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The workspace_id of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this BTReleasePackageItemInfo.


        :param workspace_id: The workspace_id of this BTReleasePackageItemInfo.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def element_id(self):
        """Gets the element_id of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The element_id of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTReleasePackageItemInfo.


        :param element_id: The element_id of this BTReleasePackageItemInfo.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def document_id(self):
        """Gets the document_id of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The document_id of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTReleasePackageItemInfo.


        :param document_id: The document_id of this BTReleasePackageItemInfo.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def version_id(self):
        """Gets the version_id of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The version_id of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this BTReleasePackageItemInfo.


        :param version_id: The version_id of this BTReleasePackageItemInfo.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def part_id(self):
        """Gets the part_id of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The part_id of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """Sets the part_id of this BTReleasePackageItemInfo.


        :param part_id: The part_id of this BTReleasePackageItemInfo.  # noqa: E501
        :type: str
        """

        self._part_id = part_id

    @property
    def small_thumbnail_href(self):
        """Gets the small_thumbnail_href of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The small_thumbnail_href of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._small_thumbnail_href

    @small_thumbnail_href.setter
    def small_thumbnail_href(self, small_thumbnail_href):
        """Sets the small_thumbnail_href of this BTReleasePackageItemInfo.


        :param small_thumbnail_href: The small_thumbnail_href of this BTReleasePackageItemInfo.  # noqa: E501
        :type: str
        """

        self._small_thumbnail_href = small_thumbnail_href

    @property
    def is_revision_managed(self):
        """Gets the is_revision_managed of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The is_revision_managed of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_revision_managed

    @is_revision_managed.setter
    def is_revision_managed(self, is_revision_managed):
        """Sets the is_revision_managed of this BTReleasePackageItemInfo.


        :param is_revision_managed: The is_revision_managed of this BTReleasePackageItemInfo.  # noqa: E501
        :type: bool
        """

        self._is_revision_managed = is_revision_managed

    @property
    def errors(self):
        """Gets the errors of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The errors of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: list[BTReleasePackageItemError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this BTReleasePackageItemInfo.


        :param errors: The errors of this BTReleasePackageItemInfo.  # noqa: E501
        :type: list[BTReleasePackageItemError]
        """

        self._errors = errors

    @property
    def is_included_editable(self):
        """Gets the is_included_editable of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The is_included_editable of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_included_editable

    @is_included_editable.setter
    def is_included_editable(self, is_included_editable):
        """Sets the is_included_editable of this BTReleasePackageItemInfo.


        :param is_included_editable: The is_included_editable of this BTReleasePackageItemInfo.  # noqa: E501
        :type: bool
        """

        self._is_included_editable = is_included_editable

    @property
    def diff_thumbnail_configuration_key(self):
        """Gets the diff_thumbnail_configuration_key of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The diff_thumbnail_configuration_key of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._diff_thumbnail_configuration_key

    @diff_thumbnail_configuration_key.setter
    def diff_thumbnail_configuration_key(self, diff_thumbnail_configuration_key):
        """Sets the diff_thumbnail_configuration_key of this BTReleasePackageItemInfo.


        :param diff_thumbnail_configuration_key: The diff_thumbnail_configuration_key of this BTReleasePackageItemInfo.  # noqa: E501
        :type: str
        """

        self._diff_thumbnail_configuration_key = diff_thumbnail_configuration_key

    @property
    def rpid(self):
        """Gets the rpid of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The rpid of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._rpid

    @rpid.setter
    def rpid(self, rpid):
        """Sets the rpid of this BTReleasePackageItemInfo.


        :param rpid: The rpid of this BTReleasePackageItemInfo.  # noqa: E501
        :type: str
        """

        self._rpid = rpid

    @property
    def obsoletion_revision_id(self):
        """Gets the obsoletion_revision_id of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The obsoletion_revision_id of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._obsoletion_revision_id

    @obsoletion_revision_id.setter
    def obsoletion_revision_id(self, obsoletion_revision_id):
        """Sets the obsoletion_revision_id of this BTReleasePackageItemInfo.


        :param obsoletion_revision_id: The obsoletion_revision_id of this BTReleasePackageItemInfo.  # noqa: E501
        :type: str
        """

        self._obsoletion_revision_id = obsoletion_revision_id

    @property
    def name(self):
        """Gets the name of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The name of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTReleasePackageItemInfo.


        :param name: The name of this BTReleasePackageItemInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The id of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTReleasePackageItemInfo.


        :param id: The id of this BTReleasePackageItemInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The href of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTReleasePackageItemInfo.


        :param href: The href of this BTReleasePackageItemInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTReleasePackageItemInfo.  # noqa: E501


        :return: The view_ref of this BTReleasePackageItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTReleasePackageItemInfo.


        :param view_ref: The view_ref of this BTReleasePackageItemInfo.  # noqa: E501
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
        if not isinstance(other, BTReleasePackageItemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

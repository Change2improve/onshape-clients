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


class BTImportCloudObjectParams(object):
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
        'public': 'bool',
        'cloud_storage_account_id': 'str',
        'url': 'str',
        'mime_type': 'str',
        'cloud_storage_provider': 'int',
        'owner_id': 'str',
        'owner_type': 'str',
        'notify_user': 'bool',
        'cloud_object_id': 'str',
        'size_bytes': 'int',
        'access_token': 'str',
        'project_id': 'str',
        'parent_id': 'str',
        'foreign_id': 'str',
        'upload_id': 'str',
        'split_assemblies_into_multiple_documents': 'bool',
        'flatten_assemblies': 'bool',
        'gety_axis_is_up': 'bool',
        'allow_faulty_parts': 'bool',
        'unit': 'str',
        'original_foreign_id': 'str',
        'blob_microversion_id': 'str',
        'blob_element_id': 'str',
        'specify_units': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'public': 'public',
        'cloud_storage_account_id': 'cloudStorageAccountId',
        'url': 'url',
        'mime_type': 'mimeType',
        'cloud_storage_provider': 'cloudStorageProvider',
        'owner_id': 'ownerId',
        'owner_type': 'ownerType',
        'notify_user': 'notifyUser',
        'cloud_object_id': 'cloudObjectId',
        'size_bytes': 'sizeBytes',
        'access_token': 'accessToken',
        'project_id': 'projectId',
        'parent_id': 'parentId',
        'foreign_id': 'foreignId',
        'upload_id': 'uploadId',
        'split_assemblies_into_multiple_documents': 'splitAssembliesIntoMultipleDocuments',
        'flatten_assemblies': 'flattenAssemblies',
        'gety_axis_is_up': 'getyAxisIsUp',
        'allow_faulty_parts': 'allowFaultyParts',
        'unit': 'unit',
        'original_foreign_id': 'originalForeignId',
        'blob_microversion_id': 'blobMicroversionId',
        'blob_element_id': 'blobElementId',
        'specify_units': 'specifyUnits'
    }

    def __init__(self, name=None, public=None, cloud_storage_account_id=None, url=None, mime_type=None, cloud_storage_provider=None, owner_id=None, owner_type=None, notify_user=None, cloud_object_id=None, size_bytes=None, access_token=None, project_id=None, parent_id=None, foreign_id=None, upload_id=None, split_assemblies_into_multiple_documents=None, flatten_assemblies=None, gety_axis_is_up=None, allow_faulty_parts=None, unit=None, original_foreign_id=None, blob_microversion_id=None, blob_element_id=None, specify_units=None):  # noqa: E501
        """BTImportCloudObjectParams - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._public = None
        self._cloud_storage_account_id = None
        self._url = None
        self._mime_type = None
        self._cloud_storage_provider = None
        self._owner_id = None
        self._owner_type = None
        self._notify_user = None
        self._cloud_object_id = None
        self._size_bytes = None
        self._access_token = None
        self._project_id = None
        self._parent_id = None
        self._foreign_id = None
        self._upload_id = None
        self._split_assemblies_into_multiple_documents = None
        self._flatten_assemblies = None
        self._gety_axis_is_up = None
        self._allow_faulty_parts = None
        self._unit = None
        self._original_foreign_id = None
        self._blob_microversion_id = None
        self._blob_element_id = None
        self._specify_units = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if public is not None:
            self.public = public
        if cloud_storage_account_id is not None:
            self.cloud_storage_account_id = cloud_storage_account_id
        if url is not None:
            self.url = url
        if mime_type is not None:
            self.mime_type = mime_type
        if cloud_storage_provider is not None:
            self.cloud_storage_provider = cloud_storage_provider
        if owner_id is not None:
            self.owner_id = owner_id
        if owner_type is not None:
            self.owner_type = owner_type
        if notify_user is not None:
            self.notify_user = notify_user
        if cloud_object_id is not None:
            self.cloud_object_id = cloud_object_id
        if size_bytes is not None:
            self.size_bytes = size_bytes
        if access_token is not None:
            self.access_token = access_token
        if project_id is not None:
            self.project_id = project_id
        if parent_id is not None:
            self.parent_id = parent_id
        if foreign_id is not None:
            self.foreign_id = foreign_id
        if upload_id is not None:
            self.upload_id = upload_id
        if split_assemblies_into_multiple_documents is not None:
            self.split_assemblies_into_multiple_documents = split_assemblies_into_multiple_documents
        if flatten_assemblies is not None:
            self.flatten_assemblies = flatten_assemblies
        if gety_axis_is_up is not None:
            self.gety_axis_is_up = gety_axis_is_up
        if allow_faulty_parts is not None:
            self.allow_faulty_parts = allow_faulty_parts
        if unit is not None:
            self.unit = unit
        if original_foreign_id is not None:
            self.original_foreign_id = original_foreign_id
        if blob_microversion_id is not None:
            self.blob_microversion_id = blob_microversion_id
        if blob_element_id is not None:
            self.blob_element_id = blob_element_id
        if specify_units is not None:
            self.specify_units = specify_units

    @property
    def name(self):
        """Gets the name of this BTImportCloudObjectParams.  # noqa: E501


        :return: The name of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTImportCloudObjectParams.


        :param name: The name of this BTImportCloudObjectParams.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def public(self):
        """Gets the public of this BTImportCloudObjectParams.  # noqa: E501


        :return: The public of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this BTImportCloudObjectParams.


        :param public: The public of this BTImportCloudObjectParams.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def cloud_storage_account_id(self):
        """Gets the cloud_storage_account_id of this BTImportCloudObjectParams.  # noqa: E501


        :return: The cloud_storage_account_id of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: str
        """
        return self._cloud_storage_account_id

    @cloud_storage_account_id.setter
    def cloud_storage_account_id(self, cloud_storage_account_id):
        """Sets the cloud_storage_account_id of this BTImportCloudObjectParams.


        :param cloud_storage_account_id: The cloud_storage_account_id of this BTImportCloudObjectParams.  # noqa: E501
        :type: str
        """

        self._cloud_storage_account_id = cloud_storage_account_id

    @property
    def url(self):
        """Gets the url of this BTImportCloudObjectParams.  # noqa: E501


        :return: The url of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BTImportCloudObjectParams.


        :param url: The url of this BTImportCloudObjectParams.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def mime_type(self):
        """Gets the mime_type of this BTImportCloudObjectParams.  # noqa: E501


        :return: The mime_type of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this BTImportCloudObjectParams.


        :param mime_type: The mime_type of this BTImportCloudObjectParams.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def cloud_storage_provider(self):
        """Gets the cloud_storage_provider of this BTImportCloudObjectParams.  # noqa: E501


        :return: The cloud_storage_provider of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: int
        """
        return self._cloud_storage_provider

    @cloud_storage_provider.setter
    def cloud_storage_provider(self, cloud_storage_provider):
        """Sets the cloud_storage_provider of this BTImportCloudObjectParams.


        :param cloud_storage_provider: The cloud_storage_provider of this BTImportCloudObjectParams.  # noqa: E501
        :type: int
        """

        self._cloud_storage_provider = cloud_storage_provider

    @property
    def owner_id(self):
        """Gets the owner_id of this BTImportCloudObjectParams.  # noqa: E501


        :return: The owner_id of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this BTImportCloudObjectParams.


        :param owner_id: The owner_id of this BTImportCloudObjectParams.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def owner_type(self):
        """Gets the owner_type of this BTImportCloudObjectParams.  # noqa: E501


        :return: The owner_type of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        """Sets the owner_type of this BTImportCloudObjectParams.


        :param owner_type: The owner_type of this BTImportCloudObjectParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["USER", "COMPANY", "ONSHAPE"]  # noqa: E501
        if owner_type not in allowed_values:
            raise ValueError(
                "Invalid value for `owner_type` ({0}), must be one of {1}"  # noqa: E501
                .format(owner_type, allowed_values)
            )

        self._owner_type = owner_type

    @property
    def notify_user(self):
        """Gets the notify_user of this BTImportCloudObjectParams.  # noqa: E501


        :return: The notify_user of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: bool
        """
        return self._notify_user

    @notify_user.setter
    def notify_user(self, notify_user):
        """Sets the notify_user of this BTImportCloudObjectParams.


        :param notify_user: The notify_user of this BTImportCloudObjectParams.  # noqa: E501
        :type: bool
        """

        self._notify_user = notify_user

    @property
    def cloud_object_id(self):
        """Gets the cloud_object_id of this BTImportCloudObjectParams.  # noqa: E501


        :return: The cloud_object_id of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: str
        """
        return self._cloud_object_id

    @cloud_object_id.setter
    def cloud_object_id(self, cloud_object_id):
        """Sets the cloud_object_id of this BTImportCloudObjectParams.


        :param cloud_object_id: The cloud_object_id of this BTImportCloudObjectParams.  # noqa: E501
        :type: str
        """

        self._cloud_object_id = cloud_object_id

    @property
    def size_bytes(self):
        """Gets the size_bytes of this BTImportCloudObjectParams.  # noqa: E501


        :return: The size_bytes of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: int
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this BTImportCloudObjectParams.


        :param size_bytes: The size_bytes of this BTImportCloudObjectParams.  # noqa: E501
        :type: int
        """

        self._size_bytes = size_bytes

    @property
    def access_token(self):
        """Gets the access_token of this BTImportCloudObjectParams.  # noqa: E501


        :return: The access_token of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this BTImportCloudObjectParams.


        :param access_token: The access_token of this BTImportCloudObjectParams.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def project_id(self):
        """Gets the project_id of this BTImportCloudObjectParams.  # noqa: E501


        :return: The project_id of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BTImportCloudObjectParams.


        :param project_id: The project_id of this BTImportCloudObjectParams.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def parent_id(self):
        """Gets the parent_id of this BTImportCloudObjectParams.  # noqa: E501


        :return: The parent_id of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this BTImportCloudObjectParams.


        :param parent_id: The parent_id of this BTImportCloudObjectParams.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def foreign_id(self):
        """Gets the foreign_id of this BTImportCloudObjectParams.  # noqa: E501


        :return: The foreign_id of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: str
        """
        return self._foreign_id

    @foreign_id.setter
    def foreign_id(self, foreign_id):
        """Sets the foreign_id of this BTImportCloudObjectParams.


        :param foreign_id: The foreign_id of this BTImportCloudObjectParams.  # noqa: E501
        :type: str
        """

        self._foreign_id = foreign_id

    @property
    def upload_id(self):
        """Gets the upload_id of this BTImportCloudObjectParams.  # noqa: E501


        :return: The upload_id of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: str
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        """Sets the upload_id of this BTImportCloudObjectParams.


        :param upload_id: The upload_id of this BTImportCloudObjectParams.  # noqa: E501
        :type: str
        """

        self._upload_id = upload_id

    @property
    def split_assemblies_into_multiple_documents(self):
        """Gets the split_assemblies_into_multiple_documents of this BTImportCloudObjectParams.  # noqa: E501


        :return: The split_assemblies_into_multiple_documents of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: bool
        """
        return self._split_assemblies_into_multiple_documents

    @split_assemblies_into_multiple_documents.setter
    def split_assemblies_into_multiple_documents(self, split_assemblies_into_multiple_documents):
        """Sets the split_assemblies_into_multiple_documents of this BTImportCloudObjectParams.


        :param split_assemblies_into_multiple_documents: The split_assemblies_into_multiple_documents of this BTImportCloudObjectParams.  # noqa: E501
        :type: bool
        """

        self._split_assemblies_into_multiple_documents = split_assemblies_into_multiple_documents

    @property
    def flatten_assemblies(self):
        """Gets the flatten_assemblies of this BTImportCloudObjectParams.  # noqa: E501


        :return: The flatten_assemblies of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: bool
        """
        return self._flatten_assemblies

    @flatten_assemblies.setter
    def flatten_assemblies(self, flatten_assemblies):
        """Sets the flatten_assemblies of this BTImportCloudObjectParams.


        :param flatten_assemblies: The flatten_assemblies of this BTImportCloudObjectParams.  # noqa: E501
        :type: bool
        """

        self._flatten_assemblies = flatten_assemblies

    @property
    def gety_axis_is_up(self):
        """Gets the gety_axis_is_up of this BTImportCloudObjectParams.  # noqa: E501


        :return: The gety_axis_is_up of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: bool
        """
        return self._gety_axis_is_up

    @gety_axis_is_up.setter
    def gety_axis_is_up(self, gety_axis_is_up):
        """Sets the gety_axis_is_up of this BTImportCloudObjectParams.


        :param gety_axis_is_up: The gety_axis_is_up of this BTImportCloudObjectParams.  # noqa: E501
        :type: bool
        """

        self._gety_axis_is_up = gety_axis_is_up

    @property
    def allow_faulty_parts(self):
        """Gets the allow_faulty_parts of this BTImportCloudObjectParams.  # noqa: E501


        :return: The allow_faulty_parts of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: bool
        """
        return self._allow_faulty_parts

    @allow_faulty_parts.setter
    def allow_faulty_parts(self, allow_faulty_parts):
        """Sets the allow_faulty_parts of this BTImportCloudObjectParams.


        :param allow_faulty_parts: The allow_faulty_parts of this BTImportCloudObjectParams.  # noqa: E501
        :type: bool
        """

        self._allow_faulty_parts = allow_faulty_parts

    @property
    def unit(self):
        """Gets the unit of this BTImportCloudObjectParams.  # noqa: E501


        :return: The unit of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this BTImportCloudObjectParams.


        :param unit: The unit of this BTImportCloudObjectParams.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def original_foreign_id(self):
        """Gets the original_foreign_id of this BTImportCloudObjectParams.  # noqa: E501


        :return: The original_foreign_id of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: str
        """
        return self._original_foreign_id

    @original_foreign_id.setter
    def original_foreign_id(self, original_foreign_id):
        """Sets the original_foreign_id of this BTImportCloudObjectParams.


        :param original_foreign_id: The original_foreign_id of this BTImportCloudObjectParams.  # noqa: E501
        :type: str
        """

        self._original_foreign_id = original_foreign_id

    @property
    def blob_microversion_id(self):
        """Gets the blob_microversion_id of this BTImportCloudObjectParams.  # noqa: E501


        :return: The blob_microversion_id of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: str
        """
        return self._blob_microversion_id

    @blob_microversion_id.setter
    def blob_microversion_id(self, blob_microversion_id):
        """Sets the blob_microversion_id of this BTImportCloudObjectParams.


        :param blob_microversion_id: The blob_microversion_id of this BTImportCloudObjectParams.  # noqa: E501
        :type: str
        """

        self._blob_microversion_id = blob_microversion_id

    @property
    def blob_element_id(self):
        """Gets the blob_element_id of this BTImportCloudObjectParams.  # noqa: E501


        :return: The blob_element_id of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: str
        """
        return self._blob_element_id

    @blob_element_id.setter
    def blob_element_id(self, blob_element_id):
        """Sets the blob_element_id of this BTImportCloudObjectParams.


        :param blob_element_id: The blob_element_id of this BTImportCloudObjectParams.  # noqa: E501
        :type: str
        """

        self._blob_element_id = blob_element_id

    @property
    def specify_units(self):
        """Gets the specify_units of this BTImportCloudObjectParams.  # noqa: E501


        :return: The specify_units of this BTImportCloudObjectParams.  # noqa: E501
        :rtype: bool
        """
        return self._specify_units

    @specify_units.setter
    def specify_units(self, specify_units):
        """Sets the specify_units of this BTImportCloudObjectParams.


        :param specify_units: The specify_units of this BTImportCloudObjectParams.  # noqa: E501
        :type: bool
        """

        self._specify_units = specify_units

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
        if not isinstance(other, BTImportCloudObjectParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

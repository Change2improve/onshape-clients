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


class BTImportForeignDataParams(object):
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
        'size': 'int',
        'owner_id': 'str',
        'owner_type': 'str',
        'media_type': 'str',
        'filename': 'str',
        'document_id': 'str',
        'file_format': 'str',
        'public_document': 'bool',
        'notify_user': 'bool',
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
        'size': 'size',
        'owner_id': 'ownerId',
        'owner_type': 'ownerType',
        'media_type': 'mediaType',
        'filename': 'filename',
        'document_id': 'documentId',
        'file_format': 'fileFormat',
        'public_document': 'publicDocument',
        'notify_user': 'notifyUser',
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

    def __init__(self, size=None, owner_id=None, owner_type=None, media_type=None, filename=None, document_id=None, file_format=None, public_document=None, notify_user=None, project_id=None, parent_id=None, foreign_id=None, upload_id=None, split_assemblies_into_multiple_documents=None, flatten_assemblies=None, gety_axis_is_up=None, allow_faulty_parts=None, unit=None, original_foreign_id=None, blob_microversion_id=None, blob_element_id=None, specify_units=None):  # noqa: E501
        """BTImportForeignDataParams - a model defined in OpenAPI"""  # noqa: E501

        self._size = None
        self._owner_id = None
        self._owner_type = None
        self._media_type = None
        self._filename = None
        self._document_id = None
        self._file_format = None
        self._public_document = None
        self._notify_user = None
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

        if size is not None:
            self.size = size
        if owner_id is not None:
            self.owner_id = owner_id
        if owner_type is not None:
            self.owner_type = owner_type
        if media_type is not None:
            self.media_type = media_type
        if filename is not None:
            self.filename = filename
        if document_id is not None:
            self.document_id = document_id
        if file_format is not None:
            self.file_format = file_format
        if public_document is not None:
            self.public_document = public_document
        if notify_user is not None:
            self.notify_user = notify_user
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
    def size(self):
        """Gets the size of this BTImportForeignDataParams.  # noqa: E501


        :return: The size of this BTImportForeignDataParams.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BTImportForeignDataParams.


        :param size: The size of this BTImportForeignDataParams.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def owner_id(self):
        """Gets the owner_id of this BTImportForeignDataParams.  # noqa: E501


        :return: The owner_id of this BTImportForeignDataParams.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this BTImportForeignDataParams.


        :param owner_id: The owner_id of this BTImportForeignDataParams.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def owner_type(self):
        """Gets the owner_type of this BTImportForeignDataParams.  # noqa: E501


        :return: The owner_type of this BTImportForeignDataParams.  # noqa: E501
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        """Sets the owner_type of this BTImportForeignDataParams.


        :param owner_type: The owner_type of this BTImportForeignDataParams.  # noqa: E501
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
    def media_type(self):
        """Gets the media_type of this BTImportForeignDataParams.  # noqa: E501


        :return: The media_type of this BTImportForeignDataParams.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this BTImportForeignDataParams.


        :param media_type: The media_type of this BTImportForeignDataParams.  # noqa: E501
        :type: str
        """

        self._media_type = media_type

    @property
    def filename(self):
        """Gets the filename of this BTImportForeignDataParams.  # noqa: E501


        :return: The filename of this BTImportForeignDataParams.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this BTImportForeignDataParams.


        :param filename: The filename of this BTImportForeignDataParams.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def document_id(self):
        """Gets the document_id of this BTImportForeignDataParams.  # noqa: E501


        :return: The document_id of this BTImportForeignDataParams.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTImportForeignDataParams.


        :param document_id: The document_id of this BTImportForeignDataParams.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def file_format(self):
        """Gets the file_format of this BTImportForeignDataParams.  # noqa: E501


        :return: The file_format of this BTImportForeignDataParams.  # noqa: E501
        :rtype: str
        """
        return self._file_format

    @file_format.setter
    def file_format(self, file_format):
        """Sets the file_format of this BTImportForeignDataParams.


        :param file_format: The file_format of this BTImportForeignDataParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["ONSHAPE_ONSHAPE", "PARASOLID_XT", "PARASOLID_XB", "PARASOLID_XMT_TXT", "PARASOLID_XMT_BIN", "ACIS_SAT", "STEP_STEP", "IGES_IGES", "SOLIDWORKS_SLDPRT", "SOLIDWORKS_SLDASM", "SOLIDWORKS_ZIP", "INVENTOR_IPRT", "INVENTOR_IAM", "PROE_PRT_OR_NX", "PROE_ASM", "SOLIDEDGE_PAR", "CATIAV5_CATPART", "CATIAV5_CATPRODUCT", "JT_JT", "COLLADA_DAE", "RHINO_3DM", "STL_STL", "OBJ_OBJ"]  # noqa: E501
        if file_format not in allowed_values:
            raise ValueError(
                "Invalid value for `file_format` ({0}), must be one of {1}"  # noqa: E501
                .format(file_format, allowed_values)
            )

        self._file_format = file_format

    @property
    def public_document(self):
        """Gets the public_document of this BTImportForeignDataParams.  # noqa: E501


        :return: The public_document of this BTImportForeignDataParams.  # noqa: E501
        :rtype: bool
        """
        return self._public_document

    @public_document.setter
    def public_document(self, public_document):
        """Sets the public_document of this BTImportForeignDataParams.


        :param public_document: The public_document of this BTImportForeignDataParams.  # noqa: E501
        :type: bool
        """

        self._public_document = public_document

    @property
    def notify_user(self):
        """Gets the notify_user of this BTImportForeignDataParams.  # noqa: E501


        :return: The notify_user of this BTImportForeignDataParams.  # noqa: E501
        :rtype: bool
        """
        return self._notify_user

    @notify_user.setter
    def notify_user(self, notify_user):
        """Sets the notify_user of this BTImportForeignDataParams.


        :param notify_user: The notify_user of this BTImportForeignDataParams.  # noqa: E501
        :type: bool
        """

        self._notify_user = notify_user

    @property
    def project_id(self):
        """Gets the project_id of this BTImportForeignDataParams.  # noqa: E501


        :return: The project_id of this BTImportForeignDataParams.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BTImportForeignDataParams.


        :param project_id: The project_id of this BTImportForeignDataParams.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def parent_id(self):
        """Gets the parent_id of this BTImportForeignDataParams.  # noqa: E501


        :return: The parent_id of this BTImportForeignDataParams.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this BTImportForeignDataParams.


        :param parent_id: The parent_id of this BTImportForeignDataParams.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def foreign_id(self):
        """Gets the foreign_id of this BTImportForeignDataParams.  # noqa: E501


        :return: The foreign_id of this BTImportForeignDataParams.  # noqa: E501
        :rtype: str
        """
        return self._foreign_id

    @foreign_id.setter
    def foreign_id(self, foreign_id):
        """Sets the foreign_id of this BTImportForeignDataParams.


        :param foreign_id: The foreign_id of this BTImportForeignDataParams.  # noqa: E501
        :type: str
        """

        self._foreign_id = foreign_id

    @property
    def upload_id(self):
        """Gets the upload_id of this BTImportForeignDataParams.  # noqa: E501


        :return: The upload_id of this BTImportForeignDataParams.  # noqa: E501
        :rtype: str
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        """Sets the upload_id of this BTImportForeignDataParams.


        :param upload_id: The upload_id of this BTImportForeignDataParams.  # noqa: E501
        :type: str
        """

        self._upload_id = upload_id

    @property
    def split_assemblies_into_multiple_documents(self):
        """Gets the split_assemblies_into_multiple_documents of this BTImportForeignDataParams.  # noqa: E501


        :return: The split_assemblies_into_multiple_documents of this BTImportForeignDataParams.  # noqa: E501
        :rtype: bool
        """
        return self._split_assemblies_into_multiple_documents

    @split_assemblies_into_multiple_documents.setter
    def split_assemblies_into_multiple_documents(self, split_assemblies_into_multiple_documents):
        """Sets the split_assemblies_into_multiple_documents of this BTImportForeignDataParams.


        :param split_assemblies_into_multiple_documents: The split_assemblies_into_multiple_documents of this BTImportForeignDataParams.  # noqa: E501
        :type: bool
        """

        self._split_assemblies_into_multiple_documents = split_assemblies_into_multiple_documents

    @property
    def flatten_assemblies(self):
        """Gets the flatten_assemblies of this BTImportForeignDataParams.  # noqa: E501


        :return: The flatten_assemblies of this BTImportForeignDataParams.  # noqa: E501
        :rtype: bool
        """
        return self._flatten_assemblies

    @flatten_assemblies.setter
    def flatten_assemblies(self, flatten_assemblies):
        """Sets the flatten_assemblies of this BTImportForeignDataParams.


        :param flatten_assemblies: The flatten_assemblies of this BTImportForeignDataParams.  # noqa: E501
        :type: bool
        """

        self._flatten_assemblies = flatten_assemblies

    @property
    def gety_axis_is_up(self):
        """Gets the gety_axis_is_up of this BTImportForeignDataParams.  # noqa: E501


        :return: The gety_axis_is_up of this BTImportForeignDataParams.  # noqa: E501
        :rtype: bool
        """
        return self._gety_axis_is_up

    @gety_axis_is_up.setter
    def gety_axis_is_up(self, gety_axis_is_up):
        """Sets the gety_axis_is_up of this BTImportForeignDataParams.


        :param gety_axis_is_up: The gety_axis_is_up of this BTImportForeignDataParams.  # noqa: E501
        :type: bool
        """

        self._gety_axis_is_up = gety_axis_is_up

    @property
    def allow_faulty_parts(self):
        """Gets the allow_faulty_parts of this BTImportForeignDataParams.  # noqa: E501


        :return: The allow_faulty_parts of this BTImportForeignDataParams.  # noqa: E501
        :rtype: bool
        """
        return self._allow_faulty_parts

    @allow_faulty_parts.setter
    def allow_faulty_parts(self, allow_faulty_parts):
        """Sets the allow_faulty_parts of this BTImportForeignDataParams.


        :param allow_faulty_parts: The allow_faulty_parts of this BTImportForeignDataParams.  # noqa: E501
        :type: bool
        """

        self._allow_faulty_parts = allow_faulty_parts

    @property
    def unit(self):
        """Gets the unit of this BTImportForeignDataParams.  # noqa: E501


        :return: The unit of this BTImportForeignDataParams.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this BTImportForeignDataParams.


        :param unit: The unit of this BTImportForeignDataParams.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def original_foreign_id(self):
        """Gets the original_foreign_id of this BTImportForeignDataParams.  # noqa: E501


        :return: The original_foreign_id of this BTImportForeignDataParams.  # noqa: E501
        :rtype: str
        """
        return self._original_foreign_id

    @original_foreign_id.setter
    def original_foreign_id(self, original_foreign_id):
        """Sets the original_foreign_id of this BTImportForeignDataParams.


        :param original_foreign_id: The original_foreign_id of this BTImportForeignDataParams.  # noqa: E501
        :type: str
        """

        self._original_foreign_id = original_foreign_id

    @property
    def blob_microversion_id(self):
        """Gets the blob_microversion_id of this BTImportForeignDataParams.  # noqa: E501


        :return: The blob_microversion_id of this BTImportForeignDataParams.  # noqa: E501
        :rtype: str
        """
        return self._blob_microversion_id

    @blob_microversion_id.setter
    def blob_microversion_id(self, blob_microversion_id):
        """Sets the blob_microversion_id of this BTImportForeignDataParams.


        :param blob_microversion_id: The blob_microversion_id of this BTImportForeignDataParams.  # noqa: E501
        :type: str
        """

        self._blob_microversion_id = blob_microversion_id

    @property
    def blob_element_id(self):
        """Gets the blob_element_id of this BTImportForeignDataParams.  # noqa: E501


        :return: The blob_element_id of this BTImportForeignDataParams.  # noqa: E501
        :rtype: str
        """
        return self._blob_element_id

    @blob_element_id.setter
    def blob_element_id(self, blob_element_id):
        """Sets the blob_element_id of this BTImportForeignDataParams.


        :param blob_element_id: The blob_element_id of this BTImportForeignDataParams.  # noqa: E501
        :type: str
        """

        self._blob_element_id = blob_element_id

    @property
    def specify_units(self):
        """Gets the specify_units of this BTImportForeignDataParams.  # noqa: E501


        :return: The specify_units of this BTImportForeignDataParams.  # noqa: E501
        :rtype: bool
        """
        return self._specify_units

    @specify_units.setter
    def specify_units(self, specify_units):
        """Sets the specify_units of this BTImportForeignDataParams.


        :param specify_units: The specify_units of this BTImportForeignDataParams.  # noqa: E501
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
        if not isinstance(other, BTImportForeignDataParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

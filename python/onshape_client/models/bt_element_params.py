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


class BTElementParams(object):
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
        'location': 'BTElementLocationParams',
        'workspace_id': 'str',
        'element_id': 'str',
        'format': 'str',
        'media_type': 'str',
        'filename': 'str',
        'document_id': 'str',
        'source_document_id': 'str',
        'source_workspace_id': 'str',
        'notify_user': 'bool',
        'translate_stored_file': 'bool',
        'create_drawing_if_possible': 'bool',
        'is_initial_upload': 'bool',
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
        'location': 'location',
        'workspace_id': 'workspaceId',
        'element_id': 'elementId',
        'format': 'format',
        'media_type': 'mediaType',
        'filename': 'filename',
        'document_id': 'documentId',
        'source_document_id': 'sourceDocumentId',
        'source_workspace_id': 'sourceWorkspaceId',
        'notify_user': 'notifyUser',
        'translate_stored_file': 'translateStoredFile',
        'create_drawing_if_possible': 'createDrawingIfPossible',
        'is_initial_upload': 'isInitialUpload',
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

    def __init__(self, location=None, workspace_id=None, element_id=None, format=None, media_type=None, filename=None, document_id=None, source_document_id=None, source_workspace_id=None, notify_user=None, translate_stored_file=None, create_drawing_if_possible=None, is_initial_upload=None, project_id=None, parent_id=None, foreign_id=None, upload_id=None, split_assemblies_into_multiple_documents=None, flatten_assemblies=None, gety_axis_is_up=None, allow_faulty_parts=None, unit=None, original_foreign_id=None, blob_microversion_id=None, blob_element_id=None, specify_units=None):  # noqa: E501
        """BTElementParams - a model defined in OpenAPI"""  # noqa: E501

        self._location = None
        self._workspace_id = None
        self._element_id = None
        self._format = None
        self._media_type = None
        self._filename = None
        self._document_id = None
        self._source_document_id = None
        self._source_workspace_id = None
        self._notify_user = None
        self._translate_stored_file = None
        self._create_drawing_if_possible = None
        self._is_initial_upload = None
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

        if location is not None:
            self.location = location
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if element_id is not None:
            self.element_id = element_id
        if format is not None:
            self.format = format
        if media_type is not None:
            self.media_type = media_type
        if filename is not None:
            self.filename = filename
        if document_id is not None:
            self.document_id = document_id
        if source_document_id is not None:
            self.source_document_id = source_document_id
        if source_workspace_id is not None:
            self.source_workspace_id = source_workspace_id
        if notify_user is not None:
            self.notify_user = notify_user
        if translate_stored_file is not None:
            self.translate_stored_file = translate_stored_file
        if create_drawing_if_possible is not None:
            self.create_drawing_if_possible = create_drawing_if_possible
        if is_initial_upload is not None:
            self.is_initial_upload = is_initial_upload
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
    def location(self):
        """Gets the location of this BTElementParams.  # noqa: E501


        :return: The location of this BTElementParams.  # noqa: E501
        :rtype: BTElementLocationParams
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this BTElementParams.


        :param location: The location of this BTElementParams.  # noqa: E501
        :type: BTElementLocationParams
        """

        self._location = location

    @property
    def workspace_id(self):
        """Gets the workspace_id of this BTElementParams.  # noqa: E501


        :return: The workspace_id of this BTElementParams.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this BTElementParams.


        :param workspace_id: The workspace_id of this BTElementParams.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def element_id(self):
        """Gets the element_id of this BTElementParams.  # noqa: E501


        :return: The element_id of this BTElementParams.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTElementParams.


        :param element_id: The element_id of this BTElementParams.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def format(self):
        """Gets the format of this BTElementParams.  # noqa: E501


        :return: The format of this BTElementParams.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this BTElementParams.


        :param format: The format of this BTElementParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["ONSHAPE", "PARASOLID", "ACIS", "STEP", "IGES", "SOLIDWORKS", "SOLIDWORKS_ASSEMBLY", "INVENTOR", "INVENTOR_ASSEMBLY", "PROE_OR_NX", "PROE_ASSEMBLY", "SOLIDEDGE", "CATIAV5", "CATIAV5_ASSEMBLY", "JT", "COLLADA", "RHINO", "ZIP", "STL", "OBJ", "PARASOLID_MESH", "PARASOLID_ZIP", "PDF", "DWG", "DXF", "DWT"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def media_type(self):
        """Gets the media_type of this BTElementParams.  # noqa: E501


        :return: The media_type of this BTElementParams.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this BTElementParams.


        :param media_type: The media_type of this BTElementParams.  # noqa: E501
        :type: str
        """

        self._media_type = media_type

    @property
    def filename(self):
        """Gets the filename of this BTElementParams.  # noqa: E501


        :return: The filename of this BTElementParams.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this BTElementParams.


        :param filename: The filename of this BTElementParams.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def document_id(self):
        """Gets the document_id of this BTElementParams.  # noqa: E501


        :return: The document_id of this BTElementParams.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTElementParams.


        :param document_id: The document_id of this BTElementParams.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def source_document_id(self):
        """Gets the source_document_id of this BTElementParams.  # noqa: E501


        :return: The source_document_id of this BTElementParams.  # noqa: E501
        :rtype: str
        """
        return self._source_document_id

    @source_document_id.setter
    def source_document_id(self, source_document_id):
        """Sets the source_document_id of this BTElementParams.


        :param source_document_id: The source_document_id of this BTElementParams.  # noqa: E501
        :type: str
        """

        self._source_document_id = source_document_id

    @property
    def source_workspace_id(self):
        """Gets the source_workspace_id of this BTElementParams.  # noqa: E501


        :return: The source_workspace_id of this BTElementParams.  # noqa: E501
        :rtype: str
        """
        return self._source_workspace_id

    @source_workspace_id.setter
    def source_workspace_id(self, source_workspace_id):
        """Sets the source_workspace_id of this BTElementParams.


        :param source_workspace_id: The source_workspace_id of this BTElementParams.  # noqa: E501
        :type: str
        """

        self._source_workspace_id = source_workspace_id

    @property
    def notify_user(self):
        """Gets the notify_user of this BTElementParams.  # noqa: E501


        :return: The notify_user of this BTElementParams.  # noqa: E501
        :rtype: bool
        """
        return self._notify_user

    @notify_user.setter
    def notify_user(self, notify_user):
        """Sets the notify_user of this BTElementParams.


        :param notify_user: The notify_user of this BTElementParams.  # noqa: E501
        :type: bool
        """

        self._notify_user = notify_user

    @property
    def translate_stored_file(self):
        """Gets the translate_stored_file of this BTElementParams.  # noqa: E501


        :return: The translate_stored_file of this BTElementParams.  # noqa: E501
        :rtype: bool
        """
        return self._translate_stored_file

    @translate_stored_file.setter
    def translate_stored_file(self, translate_stored_file):
        """Sets the translate_stored_file of this BTElementParams.


        :param translate_stored_file: The translate_stored_file of this BTElementParams.  # noqa: E501
        :type: bool
        """

        self._translate_stored_file = translate_stored_file

    @property
    def create_drawing_if_possible(self):
        """Gets the create_drawing_if_possible of this BTElementParams.  # noqa: E501


        :return: The create_drawing_if_possible of this BTElementParams.  # noqa: E501
        :rtype: bool
        """
        return self._create_drawing_if_possible

    @create_drawing_if_possible.setter
    def create_drawing_if_possible(self, create_drawing_if_possible):
        """Sets the create_drawing_if_possible of this BTElementParams.


        :param create_drawing_if_possible: The create_drawing_if_possible of this BTElementParams.  # noqa: E501
        :type: bool
        """

        self._create_drawing_if_possible = create_drawing_if_possible

    @property
    def is_initial_upload(self):
        """Gets the is_initial_upload of this BTElementParams.  # noqa: E501


        :return: The is_initial_upload of this BTElementParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_initial_upload

    @is_initial_upload.setter
    def is_initial_upload(self, is_initial_upload):
        """Sets the is_initial_upload of this BTElementParams.


        :param is_initial_upload: The is_initial_upload of this BTElementParams.  # noqa: E501
        :type: bool
        """

        self._is_initial_upload = is_initial_upload

    @property
    def project_id(self):
        """Gets the project_id of this BTElementParams.  # noqa: E501


        :return: The project_id of this BTElementParams.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BTElementParams.


        :param project_id: The project_id of this BTElementParams.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def parent_id(self):
        """Gets the parent_id of this BTElementParams.  # noqa: E501


        :return: The parent_id of this BTElementParams.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this BTElementParams.


        :param parent_id: The parent_id of this BTElementParams.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def foreign_id(self):
        """Gets the foreign_id of this BTElementParams.  # noqa: E501


        :return: The foreign_id of this BTElementParams.  # noqa: E501
        :rtype: str
        """
        return self._foreign_id

    @foreign_id.setter
    def foreign_id(self, foreign_id):
        """Sets the foreign_id of this BTElementParams.


        :param foreign_id: The foreign_id of this BTElementParams.  # noqa: E501
        :type: str
        """

        self._foreign_id = foreign_id

    @property
    def upload_id(self):
        """Gets the upload_id of this BTElementParams.  # noqa: E501


        :return: The upload_id of this BTElementParams.  # noqa: E501
        :rtype: str
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        """Sets the upload_id of this BTElementParams.


        :param upload_id: The upload_id of this BTElementParams.  # noqa: E501
        :type: str
        """

        self._upload_id = upload_id

    @property
    def split_assemblies_into_multiple_documents(self):
        """Gets the split_assemblies_into_multiple_documents of this BTElementParams.  # noqa: E501


        :return: The split_assemblies_into_multiple_documents of this BTElementParams.  # noqa: E501
        :rtype: bool
        """
        return self._split_assemblies_into_multiple_documents

    @split_assemblies_into_multiple_documents.setter
    def split_assemblies_into_multiple_documents(self, split_assemblies_into_multiple_documents):
        """Sets the split_assemblies_into_multiple_documents of this BTElementParams.


        :param split_assemblies_into_multiple_documents: The split_assemblies_into_multiple_documents of this BTElementParams.  # noqa: E501
        :type: bool
        """

        self._split_assemblies_into_multiple_documents = split_assemblies_into_multiple_documents

    @property
    def flatten_assemblies(self):
        """Gets the flatten_assemblies of this BTElementParams.  # noqa: E501


        :return: The flatten_assemblies of this BTElementParams.  # noqa: E501
        :rtype: bool
        """
        return self._flatten_assemblies

    @flatten_assemblies.setter
    def flatten_assemblies(self, flatten_assemblies):
        """Sets the flatten_assemblies of this BTElementParams.


        :param flatten_assemblies: The flatten_assemblies of this BTElementParams.  # noqa: E501
        :type: bool
        """

        self._flatten_assemblies = flatten_assemblies

    @property
    def gety_axis_is_up(self):
        """Gets the gety_axis_is_up of this BTElementParams.  # noqa: E501


        :return: The gety_axis_is_up of this BTElementParams.  # noqa: E501
        :rtype: bool
        """
        return self._gety_axis_is_up

    @gety_axis_is_up.setter
    def gety_axis_is_up(self, gety_axis_is_up):
        """Sets the gety_axis_is_up of this BTElementParams.


        :param gety_axis_is_up: The gety_axis_is_up of this BTElementParams.  # noqa: E501
        :type: bool
        """

        self._gety_axis_is_up = gety_axis_is_up

    @property
    def allow_faulty_parts(self):
        """Gets the allow_faulty_parts of this BTElementParams.  # noqa: E501


        :return: The allow_faulty_parts of this BTElementParams.  # noqa: E501
        :rtype: bool
        """
        return self._allow_faulty_parts

    @allow_faulty_parts.setter
    def allow_faulty_parts(self, allow_faulty_parts):
        """Sets the allow_faulty_parts of this BTElementParams.


        :param allow_faulty_parts: The allow_faulty_parts of this BTElementParams.  # noqa: E501
        :type: bool
        """

        self._allow_faulty_parts = allow_faulty_parts

    @property
    def unit(self):
        """Gets the unit of this BTElementParams.  # noqa: E501


        :return: The unit of this BTElementParams.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this BTElementParams.


        :param unit: The unit of this BTElementParams.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def original_foreign_id(self):
        """Gets the original_foreign_id of this BTElementParams.  # noqa: E501


        :return: The original_foreign_id of this BTElementParams.  # noqa: E501
        :rtype: str
        """
        return self._original_foreign_id

    @original_foreign_id.setter
    def original_foreign_id(self, original_foreign_id):
        """Sets the original_foreign_id of this BTElementParams.


        :param original_foreign_id: The original_foreign_id of this BTElementParams.  # noqa: E501
        :type: str
        """

        self._original_foreign_id = original_foreign_id

    @property
    def blob_microversion_id(self):
        """Gets the blob_microversion_id of this BTElementParams.  # noqa: E501


        :return: The blob_microversion_id of this BTElementParams.  # noqa: E501
        :rtype: str
        """
        return self._blob_microversion_id

    @blob_microversion_id.setter
    def blob_microversion_id(self, blob_microversion_id):
        """Sets the blob_microversion_id of this BTElementParams.


        :param blob_microversion_id: The blob_microversion_id of this BTElementParams.  # noqa: E501
        :type: str
        """

        self._blob_microversion_id = blob_microversion_id

    @property
    def blob_element_id(self):
        """Gets the blob_element_id of this BTElementParams.  # noqa: E501


        :return: The blob_element_id of this BTElementParams.  # noqa: E501
        :rtype: str
        """
        return self._blob_element_id

    @blob_element_id.setter
    def blob_element_id(self, blob_element_id):
        """Sets the blob_element_id of this BTElementParams.


        :param blob_element_id: The blob_element_id of this BTElementParams.  # noqa: E501
        :type: str
        """

        self._blob_element_id = blob_element_id

    @property
    def specify_units(self):
        """Gets the specify_units of this BTElementParams.  # noqa: E501


        :return: The specify_units of this BTElementParams.  # noqa: E501
        :rtype: bool
        """
        return self._specify_units

    @specify_units.setter
    def specify_units(self, specify_units):
        """Sets the specify_units of this BTElementParams.


        :param specify_units: The specify_units of this BTElementParams.  # noqa: E501
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
        if not isinstance(other, BTElementParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

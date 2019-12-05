# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.107
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from onshape_client.oas.configuration import Configuration


class BTInsertableInfo(object):
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
        'element_id': 'str',
        'document_id': 'str',
        'class_type': 'int',
        'deterministic_id': 'str',
        'data_type': 'str',
        'microversion_id': 'str',
        'parent_id': 'str',
        'version_name': 'str',
        'version_id': 'str',
        'element_type': 'str',
        'configuration_id': 'str',
        'predictable_id': 'str',
        'configuration_parameters': 'list[str]',
        'feature_name': 'str',
        'feature_spec': 'list[str]',
        'feature_type': 'str',
        'feature_id': 'str',
        'element_name': 'str',
        'thumbnail_uri': 'str',
        'insertable_query': 'str',
        'part_name': 'str',
        'unflattened_part_deterministic_id': 'str',
        'has_faults': 'bool',
        'configuration_parameter_values': 'list[str]',
        'is_flattened_body': 'bool',
        'body_type': 'str',
        'is_mesh': 'bool',
        'href': 'str',
        'view_ref': 'str',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'element_id': 'elementId',
        'document_id': 'documentId',
        'class_type': 'classType',
        'deterministic_id': 'deterministicId',
        'data_type': 'dataType',
        'microversion_id': 'microversionId',
        'parent_id': 'parentId',
        'version_name': 'versionName',
        'version_id': 'versionId',
        'element_type': 'elementType',
        'configuration_id': 'configurationId',
        'predictable_id': 'predictableId',
        'configuration_parameters': 'configurationParameters',
        'feature_name': 'featureName',
        'feature_spec': 'featureSpec',
        'feature_type': 'featureType',
        'feature_id': 'featureId',
        'element_name': 'elementName',
        'thumbnail_uri': 'thumbnailUri',
        'insertable_query': 'insertableQuery',
        'part_name': 'partName',
        'unflattened_part_deterministic_id': 'unflattenedPartDeterministicId',
        'has_faults': 'hasFaults',
        'configuration_parameter_values': 'configurationParameterValues',
        'is_flattened_body': 'isFlattenedBody',
        'body_type': 'bodyType',
        'is_mesh': 'isMesh',
        'href': 'href',
        'view_ref': 'viewRef',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, element_id=None, document_id=None, class_type=None, deterministic_id=None, data_type=None, microversion_id=None, parent_id=None, version_name=None, version_id=None, element_type=None, configuration_id=None, predictable_id=None, configuration_parameters=None, feature_name=None, feature_spec=None, feature_type=None, feature_id=None, element_name=None, thumbnail_uri=None, insertable_query=None, part_name=None, unflattened_part_deterministic_id=None, has_faults=None, configuration_parameter_values=None, is_flattened_body=None, body_type=None, is_mesh=None, href=None, view_ref=None, name=None, id=None, local_vars_configuration=None):  # noqa: E501
        """BTInsertableInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._element_id = None
        self._document_id = None
        self._class_type = None
        self._deterministic_id = None
        self._data_type = None
        self._microversion_id = None
        self._parent_id = None
        self._version_name = None
        self._version_id = None
        self._element_type = None
        self._configuration_id = None
        self._predictable_id = None
        self._configuration_parameters = None
        self._feature_name = None
        self._feature_spec = None
        self._feature_type = None
        self._feature_id = None
        self._element_name = None
        self._thumbnail_uri = None
        self._insertable_query = None
        self._part_name = None
        self._unflattened_part_deterministic_id = None
        self._has_faults = None
        self._configuration_parameter_values = None
        self._is_flattened_body = None
        self._body_type = None
        self._is_mesh = None
        self._href = None
        self._view_ref = None
        self._name = None
        self._id = None
        self.discriminator = None

        if element_id is not None:
            self.element_id = element_id
        if document_id is not None:
            self.document_id = document_id
        if class_type is not None:
            self.class_type = class_type
        if deterministic_id is not None:
            self.deterministic_id = deterministic_id
        if data_type is not None:
            self.data_type = data_type
        if microversion_id is not None:
            self.microversion_id = microversion_id
        if parent_id is not None:
            self.parent_id = parent_id
        if version_name is not None:
            self.version_name = version_name
        if version_id is not None:
            self.version_id = version_id
        if element_type is not None:
            self.element_type = element_type
        if configuration_id is not None:
            self.configuration_id = configuration_id
        if predictable_id is not None:
            self.predictable_id = predictable_id
        if configuration_parameters is not None:
            self.configuration_parameters = configuration_parameters
        if feature_name is not None:
            self.feature_name = feature_name
        if feature_spec is not None:
            self.feature_spec = feature_spec
        if feature_type is not None:
            self.feature_type = feature_type
        if feature_id is not None:
            self.feature_id = feature_id
        if element_name is not None:
            self.element_name = element_name
        if thumbnail_uri is not None:
            self.thumbnail_uri = thumbnail_uri
        if insertable_query is not None:
            self.insertable_query = insertable_query
        if part_name is not None:
            self.part_name = part_name
        if unflattened_part_deterministic_id is not None:
            self.unflattened_part_deterministic_id = unflattened_part_deterministic_id
        if has_faults is not None:
            self.has_faults = has_faults
        if configuration_parameter_values is not None:
            self.configuration_parameter_values = configuration_parameter_values
        if is_flattened_body is not None:
            self.is_flattened_body = is_flattened_body
        if body_type is not None:
            self.body_type = body_type
        if is_mesh is not None:
            self.is_mesh = is_mesh
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def element_id(self):
        """Gets the element_id of this BTInsertableInfo.  # noqa: E501


        :return: The element_id of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTInsertableInfo.


        :param element_id: The element_id of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def document_id(self):
        """Gets the document_id of this BTInsertableInfo.  # noqa: E501


        :return: The document_id of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTInsertableInfo.


        :param document_id: The document_id of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def class_type(self):
        """Gets the class_type of this BTInsertableInfo.  # noqa: E501


        :return: The class_type of this BTInsertableInfo.  # noqa: E501
        :rtype: int
        """
        return self._class_type

    @class_type.setter
    def class_type(self, class_type):
        """Sets the class_type of this BTInsertableInfo.


        :param class_type: The class_type of this BTInsertableInfo.  # noqa: E501
        :type: int
        """

        self._class_type = class_type

    @property
    def deterministic_id(self):
        """Gets the deterministic_id of this BTInsertableInfo.  # noqa: E501


        :return: The deterministic_id of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._deterministic_id

    @deterministic_id.setter
    def deterministic_id(self, deterministic_id):
        """Sets the deterministic_id of this BTInsertableInfo.


        :param deterministic_id: The deterministic_id of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._deterministic_id = deterministic_id

    @property
    def data_type(self):
        """Gets the data_type of this BTInsertableInfo.  # noqa: E501


        :return: The data_type of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this BTInsertableInfo.


        :param data_type: The data_type of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def microversion_id(self):
        """Gets the microversion_id of this BTInsertableInfo.  # noqa: E501


        :return: The microversion_id of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._microversion_id

    @microversion_id.setter
    def microversion_id(self, microversion_id):
        """Sets the microversion_id of this BTInsertableInfo.


        :param microversion_id: The microversion_id of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._microversion_id = microversion_id

    @property
    def parent_id(self):
        """Gets the parent_id of this BTInsertableInfo.  # noqa: E501


        :return: The parent_id of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this BTInsertableInfo.


        :param parent_id: The parent_id of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def version_name(self):
        """Gets the version_name of this BTInsertableInfo.  # noqa: E501


        :return: The version_name of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this BTInsertableInfo.


        :param version_name: The version_name of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._version_name = version_name

    @property
    def version_id(self):
        """Gets the version_id of this BTInsertableInfo.  # noqa: E501


        :return: The version_id of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this BTInsertableInfo.


        :param version_id: The version_id of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def element_type(self):
        """Gets the element_type of this BTInsertableInfo.  # noqa: E501


        :return: The element_type of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this BTInsertableInfo.


        :param element_type: The element_type of this BTInsertableInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["PARTSTUDIO", "ASSEMBLY", "DRAWING", "FEATURESTUDIO", "BLOB", "APPLICATION", "TABLE", "BILLOFMATERIALS", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and element_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `element_type` ({0}), must be one of {1}"  # noqa: E501
                .format(element_type, allowed_values)
            )

        self._element_type = element_type

    @property
    def configuration_id(self):
        """Gets the configuration_id of this BTInsertableInfo.  # noqa: E501


        :return: The configuration_id of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this BTInsertableInfo.


        :param configuration_id: The configuration_id of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._configuration_id = configuration_id

    @property
    def predictable_id(self):
        """Gets the predictable_id of this BTInsertableInfo.  # noqa: E501


        :return: The predictable_id of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._predictable_id

    @predictable_id.setter
    def predictable_id(self, predictable_id):
        """Sets the predictable_id of this BTInsertableInfo.


        :param predictable_id: The predictable_id of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._predictable_id = predictable_id

    @property
    def configuration_parameters(self):
        """Gets the configuration_parameters of this BTInsertableInfo.  # noqa: E501


        :return: The configuration_parameters of this BTInsertableInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._configuration_parameters

    @configuration_parameters.setter
    def configuration_parameters(self, configuration_parameters):
        """Sets the configuration_parameters of this BTInsertableInfo.


        :param configuration_parameters: The configuration_parameters of this BTInsertableInfo.  # noqa: E501
        :type: list[str]
        """

        self._configuration_parameters = configuration_parameters

    @property
    def feature_name(self):
        """Gets the feature_name of this BTInsertableInfo.  # noqa: E501


        :return: The feature_name of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._feature_name

    @feature_name.setter
    def feature_name(self, feature_name):
        """Sets the feature_name of this BTInsertableInfo.


        :param feature_name: The feature_name of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._feature_name = feature_name

    @property
    def feature_spec(self):
        """Gets the feature_spec of this BTInsertableInfo.  # noqa: E501


        :return: The feature_spec of this BTInsertableInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._feature_spec

    @feature_spec.setter
    def feature_spec(self, feature_spec):
        """Sets the feature_spec of this BTInsertableInfo.


        :param feature_spec: The feature_spec of this BTInsertableInfo.  # noqa: E501
        :type: list[str]
        """

        self._feature_spec = feature_spec

    @property
    def feature_type(self):
        """Gets the feature_type of this BTInsertableInfo.  # noqa: E501


        :return: The feature_type of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._feature_type

    @feature_type.setter
    def feature_type(self, feature_type):
        """Sets the feature_type of this BTInsertableInfo.


        :param feature_type: The feature_type of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._feature_type = feature_type

    @property
    def feature_id(self):
        """Gets the feature_id of this BTInsertableInfo.  # noqa: E501


        :return: The feature_id of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._feature_id

    @feature_id.setter
    def feature_id(self, feature_id):
        """Sets the feature_id of this BTInsertableInfo.


        :param feature_id: The feature_id of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._feature_id = feature_id

    @property
    def element_name(self):
        """Gets the element_name of this BTInsertableInfo.  # noqa: E501


        :return: The element_name of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._element_name

    @element_name.setter
    def element_name(self, element_name):
        """Sets the element_name of this BTInsertableInfo.


        :param element_name: The element_name of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._element_name = element_name

    @property
    def thumbnail_uri(self):
        """Gets the thumbnail_uri of this BTInsertableInfo.  # noqa: E501


        :return: The thumbnail_uri of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_uri

    @thumbnail_uri.setter
    def thumbnail_uri(self, thumbnail_uri):
        """Sets the thumbnail_uri of this BTInsertableInfo.


        :param thumbnail_uri: The thumbnail_uri of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._thumbnail_uri = thumbnail_uri

    @property
    def insertable_query(self):
        """Gets the insertable_query of this BTInsertableInfo.  # noqa: E501


        :return: The insertable_query of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._insertable_query

    @insertable_query.setter
    def insertable_query(self, insertable_query):
        """Sets the insertable_query of this BTInsertableInfo.


        :param insertable_query: The insertable_query of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._insertable_query = insertable_query

    @property
    def part_name(self):
        """Gets the part_name of this BTInsertableInfo.  # noqa: E501


        :return: The part_name of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._part_name

    @part_name.setter
    def part_name(self, part_name):
        """Sets the part_name of this BTInsertableInfo.


        :param part_name: The part_name of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._part_name = part_name

    @property
    def unflattened_part_deterministic_id(self):
        """Gets the unflattened_part_deterministic_id of this BTInsertableInfo.  # noqa: E501


        :return: The unflattened_part_deterministic_id of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._unflattened_part_deterministic_id

    @unflattened_part_deterministic_id.setter
    def unflattened_part_deterministic_id(self, unflattened_part_deterministic_id):
        """Sets the unflattened_part_deterministic_id of this BTInsertableInfo.


        :param unflattened_part_deterministic_id: The unflattened_part_deterministic_id of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._unflattened_part_deterministic_id = unflattened_part_deterministic_id

    @property
    def has_faults(self):
        """Gets the has_faults of this BTInsertableInfo.  # noqa: E501


        :return: The has_faults of this BTInsertableInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_faults

    @has_faults.setter
    def has_faults(self, has_faults):
        """Sets the has_faults of this BTInsertableInfo.


        :param has_faults: The has_faults of this BTInsertableInfo.  # noqa: E501
        :type: bool
        """

        self._has_faults = has_faults

    @property
    def configuration_parameter_values(self):
        """Gets the configuration_parameter_values of this BTInsertableInfo.  # noqa: E501


        :return: The configuration_parameter_values of this BTInsertableInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._configuration_parameter_values

    @configuration_parameter_values.setter
    def configuration_parameter_values(self, configuration_parameter_values):
        """Sets the configuration_parameter_values of this BTInsertableInfo.


        :param configuration_parameter_values: The configuration_parameter_values of this BTInsertableInfo.  # noqa: E501
        :type: list[str]
        """

        self._configuration_parameter_values = configuration_parameter_values

    @property
    def is_flattened_body(self):
        """Gets the is_flattened_body of this BTInsertableInfo.  # noqa: E501


        :return: The is_flattened_body of this BTInsertableInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_flattened_body

    @is_flattened_body.setter
    def is_flattened_body(self, is_flattened_body):
        """Sets the is_flattened_body of this BTInsertableInfo.


        :param is_flattened_body: The is_flattened_body of this BTInsertableInfo.  # noqa: E501
        :type: bool
        """

        self._is_flattened_body = is_flattened_body

    @property
    def body_type(self):
        """Gets the body_type of this BTInsertableInfo.  # noqa: E501


        :return: The body_type of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._body_type

    @body_type.setter
    def body_type(self, body_type):
        """Sets the body_type of this BTInsertableInfo.


        :param body_type: The body_type of this BTInsertableInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["SOLID", "SHEET", "WIRE", "POINT", "MATE_CONNECTOR", "COMPOSITE", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and body_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `body_type` ({0}), must be one of {1}"  # noqa: E501
                .format(body_type, allowed_values)
            )

        self._body_type = body_type

    @property
    def is_mesh(self):
        """Gets the is_mesh of this BTInsertableInfo.  # noqa: E501


        :return: The is_mesh of this BTInsertableInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_mesh

    @is_mesh.setter
    def is_mesh(self, is_mesh):
        """Sets the is_mesh of this BTInsertableInfo.


        :param is_mesh: The is_mesh of this BTInsertableInfo.  # noqa: E501
        :type: bool
        """

        self._is_mesh = is_mesh

    @property
    def href(self):
        """Gets the href of this BTInsertableInfo.  # noqa: E501


        :return: The href of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTInsertableInfo.


        :param href: The href of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTInsertableInfo.  # noqa: E501


        :return: The view_ref of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTInsertableInfo.


        :param view_ref: The view_ref of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

    @property
    def name(self):
        """Gets the name of this BTInsertableInfo.  # noqa: E501


        :return: The name of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTInsertableInfo.


        :param name: The name of this BTInsertableInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTInsertableInfo.  # noqa: E501


        :return: The id of this BTInsertableInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTInsertableInfo.


        :param id: The id of this BTInsertableInfo.  # noqa: E501
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
        if not isinstance(other, BTInsertableInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTInsertableInfo):
            return True

        return self.to_dict() != other.to_dict()
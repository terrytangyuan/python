# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.12.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta2ControllerRevision(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'api_version': 'str',
        'data': 'RuntimeRawExtension',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'revision': 'int'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'data': 'data',
        'kind': 'kind',
        'metadata': 'metadata',
        'revision': 'revision'
    }

    def __init__(self, api_version=None, data=None, kind=None, metadata=None, revision=None):
        """
        V1beta2ControllerRevision - a model defined in Swagger
        """

        self._api_version = None
        self._data = None
        self._kind = None
        self._metadata = None
        self._revision = None
        self.discriminator = None

        if api_version is not None:
          self.api_version = api_version
        if data is not None:
          self.data = data
        if kind is not None:
          self.kind = kind
        if metadata is not None:
          self.metadata = metadata
        self.revision = revision

    @property
    def api_version(self):
        """
        Gets the api_version of this V1beta2ControllerRevision.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :return: The api_version of this V1beta2ControllerRevision.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1beta2ControllerRevision.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1beta2ControllerRevision.
        :type: str
        """

        self._api_version = api_version

    @property
    def data(self):
        """
        Gets the data of this V1beta2ControllerRevision.
        Data is the serialized representation of the state.

        :return: The data of this V1beta2ControllerRevision.
        :rtype: RuntimeRawExtension
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this V1beta2ControllerRevision.
        Data is the serialized representation of the state.

        :param data: The data of this V1beta2ControllerRevision.
        :type: RuntimeRawExtension
        """

        self._data = data

    @property
    def kind(self):
        """
        Gets the kind of this V1beta2ControllerRevision.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :return: The kind of this V1beta2ControllerRevision.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1beta2ControllerRevision.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1beta2ControllerRevision.
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """
        Gets the metadata of this V1beta2ControllerRevision.
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

        :return: The metadata of this V1beta2ControllerRevision.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1beta2ControllerRevision.
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

        :param metadata: The metadata of this V1beta2ControllerRevision.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def revision(self):
        """
        Gets the revision of this V1beta2ControllerRevision.
        Revision indicates the revision of the state represented by Data.

        :return: The revision of this V1beta2ControllerRevision.
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this V1beta2ControllerRevision.
        Revision indicates the revision of the state represented by Data.

        :param revision: The revision of this V1beta2ControllerRevision.
        :type: int
        """
        if revision is None:
            raise ValueError("Invalid value for `revision`, must not be `None`")

        self._revision = revision

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta2ControllerRevision):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

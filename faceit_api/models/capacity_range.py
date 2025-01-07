# coding: utf-8

"""
    Data API

    # This API provide access to FACEIT's data  # noqa: E501

    OpenAPI spec version: 4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from faceit_api.configuration import Configuration


class CapacityRange(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'limit_bytes': 'int',
        'required_bytes': 'int'
    }

    attribute_map = {
        'limit_bytes': 'LimitBytes',
        'required_bytes': 'RequiredBytes'
    }

    def __init__(self, limit_bytes=None, required_bytes=None, _configuration=None):  # noqa: E501
        """CapacityRange - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._limit_bytes = None
        self._required_bytes = None
        self.discriminator = None

        if limit_bytes is not None:
            self.limit_bytes = limit_bytes
        if required_bytes is not None:
            self.required_bytes = required_bytes

    @property
    def limit_bytes(self):
        """Gets the limit_bytes of this CapacityRange.  # noqa: E501

        LimitBytes specifies that a volume must not be bigger than this. The value of 0 indicates an unspecified maximum  # noqa: E501

        :return: The limit_bytes of this CapacityRange.  # noqa: E501
        :rtype: int
        """
        return self._limit_bytes

    @limit_bytes.setter
    def limit_bytes(self, limit_bytes):
        """Sets the limit_bytes of this CapacityRange.

        LimitBytes specifies that a volume must not be bigger than this. The value of 0 indicates an unspecified maximum  # noqa: E501

        :param limit_bytes: The limit_bytes of this CapacityRange.  # noqa: E501
        :type: int
        """

        self._limit_bytes = limit_bytes

    @property
    def required_bytes(self):
        """Gets the required_bytes of this CapacityRange.  # noqa: E501

        RequiredBytes specifies that a volume must be at least this big. The value of 0 indicates an unspecified minimum.  # noqa: E501

        :return: The required_bytes of this CapacityRange.  # noqa: E501
        :rtype: int
        """
        return self._required_bytes

    @required_bytes.setter
    def required_bytes(self, required_bytes):
        """Sets the required_bytes of this CapacityRange.

        RequiredBytes specifies that a volume must be at least this big. The value of 0 indicates an unspecified minimum.  # noqa: E501

        :param required_bytes: The required_bytes of this CapacityRange.  # noqa: E501
        :type: int
        """

        self._required_bytes = required_bytes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CapacityRange, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CapacityRange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CapacityRange):
            return True

        return self.to_dict() != other.to_dict()
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


class UsageData(object):
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
        'ref_count': 'int',
        'size': 'int'
    }

    attribute_map = {
        'ref_count': 'RefCount',
        'size': 'Size'
    }

    def __init__(self, ref_count=None, size=None, _configuration=None):  # noqa: E501
        """UsageData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ref_count = None
        self._size = None
        self.discriminator = None

        self.ref_count = ref_count
        self.size = size

    @property
    def ref_count(self):
        """Gets the ref_count of this UsageData.  # noqa: E501

        The number of containers referencing this volume. This field is set to `-1` if the reference-count is not available.  # noqa: E501

        :return: The ref_count of this UsageData.  # noqa: E501
        :rtype: int
        """
        return self._ref_count

    @ref_count.setter
    def ref_count(self, ref_count):
        """Sets the ref_count of this UsageData.

        The number of containers referencing this volume. This field is set to `-1` if the reference-count is not available.  # noqa: E501

        :param ref_count: The ref_count of this UsageData.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and ref_count is None:
            raise ValueError("Invalid value for `ref_count`, must not be `None`")  # noqa: E501

        self._ref_count = ref_count

    @property
    def size(self):
        """Gets the size of this UsageData.  # noqa: E501

        Amount of disk space used by the volume (in bytes). This information is only available for volumes created with the `\"local\"` volume driver. For volumes created with other volume drivers, this field is set to `-1` (\"not available\")  # noqa: E501

        :return: The size of this UsageData.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this UsageData.

        Amount of disk space used by the volume (in bytes). This information is only available for volumes created with the `\"local\"` volume driver. For volumes created with other volume drivers, this field is set to `-1` (\"not available\")  # noqa: E501

        :param size: The size of this UsageData.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

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
        if issubclass(UsageData, dict):
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
        if not isinstance(other, UsageData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsageData):
            return True

        return self.to_dict() != other.to_dict()

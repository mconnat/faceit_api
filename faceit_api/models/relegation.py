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


class Relegation(object):
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
        'consecutive_losses': 'int'
    }

    attribute_map = {
        'consecutive_losses': 'consecutive_losses'
    }

    def __init__(self, consecutive_losses=None, _configuration=None):  # noqa: E501
        """Relegation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._consecutive_losses = None
        self.discriminator = None

        if consecutive_losses is not None:
            self.consecutive_losses = consecutive_losses

    @property
    def consecutive_losses(self):
        """Gets the consecutive_losses of this Relegation.  # noqa: E501

        Consecutive losses needed for a player to get relegated to the previous tier.  # noqa: E501

        :return: The consecutive_losses of this Relegation.  # noqa: E501
        :rtype: int
        """
        return self._consecutive_losses

    @consecutive_losses.setter
    def consecutive_losses(self, consecutive_losses):
        """Sets the consecutive_losses of this Relegation.

        Consecutive losses needed for a player to get relegated to the previous tier.  # noqa: E501

        :param consecutive_losses: The consecutive_losses of this Relegation.  # noqa: E501
        :type: int
        """

        self._consecutive_losses = consecutive_losses

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
        if issubclass(Relegation, dict):
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
        if not isinstance(other, Relegation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Relegation):
            return True

        return self.to_dict() != other.to_dict()

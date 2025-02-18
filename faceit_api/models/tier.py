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


class Tier(object):
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
        'name': 'str',
        'points_target': 'int',
        'rank': 'int'
    }

    attribute_map = {
        'name': 'name',
        'points_target': 'points_target',
        'rank': 'rank'
    }

    def __init__(self, name=None, points_target=None, rank=None, _configuration=None):  # noqa: E501
        """Tier - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._points_target = None
        self._rank = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if points_target is not None:
            self.points_target = points_target
        if rank is not None:
            self.rank = rank

    @property
    def name(self):
        """Gets the name of this Tier.  # noqa: E501

        The name of the tier  # noqa: E501

        :return: The name of this Tier.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tier.

        The name of the tier  # noqa: E501

        :param name: The name of this Tier.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def points_target(self):
        """Gets the points_target of this Tier.  # noqa: E501

        The target points for the tier  # noqa: E501

        :return: The points_target of this Tier.  # noqa: E501
        :rtype: int
        """
        return self._points_target

    @points_target.setter
    def points_target(self, points_target):
        """Sets the points_target of this Tier.

        The target points for the tier  # noqa: E501

        :param points_target: The points_target of this Tier.  # noqa: E501
        :type: int
        """

        self._points_target = points_target

    @property
    def rank(self):
        """Gets the rank of this Tier.  # noqa: E501

        The rank of the tier  # noqa: E501

        :return: The rank of this Tier.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this Tier.

        The rank of the tier  # noqa: E501

        :param rank: The rank of this Tier.  # noqa: E501
        :type: int
        """

        self._rank = rank

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
        if issubclass(Tier, dict):
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
        if not isinstance(other, Tier):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Tier):
            return True

        return self.to_dict() != other.to_dict()

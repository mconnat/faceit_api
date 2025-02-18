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


class SeasonDetailed(object):
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
        'divisions': 'list[Division]',
        'season': 'Season'
    }

    attribute_map = {
        'divisions': 'divisions',
        'season': 'season'
    }

    def __init__(self, divisions=None, season=None, _configuration=None):  # noqa: E501
        """SeasonDetailed - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._divisions = None
        self._season = None
        self.discriminator = None

        if divisions is not None:
            self.divisions = divisions
        if season is not None:
            self.season = season

    @property
    def divisions(self):
        """Gets the divisions of this SeasonDetailed.  # noqa: E501

        The divisions of the given season.  # noqa: E501

        :return: The divisions of this SeasonDetailed.  # noqa: E501
        :rtype: list[Division]
        """
        return self._divisions

    @divisions.setter
    def divisions(self, divisions):
        """Sets the divisions of this SeasonDetailed.

        The divisions of the given season.  # noqa: E501

        :param divisions: The divisions of this SeasonDetailed.  # noqa: E501
        :type: list[Division]
        """

        self._divisions = divisions

    @property
    def season(self):
        """Gets the season of this SeasonDetailed.  # noqa: E501


        :return: The season of this SeasonDetailed.  # noqa: E501
        :rtype: Season
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this SeasonDetailed.


        :param season: The season of this SeasonDetailed.  # noqa: E501
        :type: Season
        """

        self._season = season

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
        if issubclass(SeasonDetailed, dict):
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
        if not isinstance(other, SeasonDetailed):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SeasonDetailed):
            return True

        return self.to_dict() != other.to_dict()

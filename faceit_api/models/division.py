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


class Division(object):
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
        'assets': 'Assets',
        'config_type': 'str',
        'leaderboard_config': 'LeaderboardConfig',
        'leaderboards': 'list[str]',
        'max_elo': 'int',
        'min_elo': 'int',
        'name': 'str',
        'tiers': 'list[Tier]',
        'type': 'str'
    }

    attribute_map = {
        'assets': 'assets',
        'config_type': 'config_type',
        'leaderboard_config': 'leaderboard_config',
        'leaderboards': 'leaderboards',
        'max_elo': 'max_elo',
        'min_elo': 'min_elo',
        'name': 'name',
        'tiers': 'tiers',
        'type': 'type'
    }

    def __init__(self, assets=None, config_type=None, leaderboard_config=None, leaderboards=None, max_elo=None, min_elo=None, name=None, tiers=None, type=None, _configuration=None):  # noqa: E501
        """Division - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assets = None
        self._config_type = None
        self._leaderboard_config = None
        self._leaderboards = None
        self._max_elo = None
        self._min_elo = None
        self._name = None
        self._tiers = None
        self._type = None
        self.discriminator = None

        if assets is not None:
            self.assets = assets
        if config_type is not None:
            self.config_type = config_type
        if leaderboard_config is not None:
            self.leaderboard_config = leaderboard_config
        if leaderboards is not None:
            self.leaderboards = leaderboards
        if max_elo is not None:
            self.max_elo = max_elo
        if min_elo is not None:
            self.min_elo = min_elo
        if name is not None:
            self.name = name
        if tiers is not None:
            self.tiers = tiers
        if type is not None:
            self.type = type

    @property
    def assets(self):
        """Gets the assets of this Division.  # noqa: E501


        :return: The assets of this Division.  # noqa: E501
        :rtype: Assets
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this Division.


        :param assets: The assets of this Division.  # noqa: E501
        :type: Assets
        """

        self._assets = assets

    @property
    def config_type(self):
        """Gets the config_type of this Division.  # noqa: E501

        The type of the division. Can be nested or classic. Nested means that the division has tiers, classic is without tiers.  # noqa: E501

        :return: The config_type of this Division.  # noqa: E501
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """Sets the config_type of this Division.

        The type of the division. Can be nested or classic. Nested means that the division has tiers, classic is without tiers.  # noqa: E501

        :param config_type: The config_type of this Division.  # noqa: E501
        :type: str
        """

        self._config_type = config_type

    @property
    def leaderboard_config(self):
        """Gets the leaderboard_config of this Division.  # noqa: E501


        :return: The leaderboard_config of this Division.  # noqa: E501
        :rtype: LeaderboardConfig
        """
        return self._leaderboard_config

    @leaderboard_config.setter
    def leaderboard_config(self, leaderboard_config):
        """Sets the leaderboard_config of this Division.


        :param leaderboard_config: The leaderboard_config of this Division.  # noqa: E501
        :type: LeaderboardConfig
        """

        self._leaderboard_config = leaderboard_config

    @property
    def leaderboards(self):
        """Gets the leaderboards of this Division.  # noqa: E501

        The leaderboards of the division  # noqa: E501

        :return: The leaderboards of this Division.  # noqa: E501
        :rtype: list[str]
        """
        return self._leaderboards

    @leaderboards.setter
    def leaderboards(self, leaderboards):
        """Sets the leaderboards of this Division.

        The leaderboards of the division  # noqa: E501

        :param leaderboards: The leaderboards of this Division.  # noqa: E501
        :type: list[str]
        """

        self._leaderboards = leaderboards

    @property
    def max_elo(self):
        """Gets the max_elo of this Division.  # noqa: E501

        Max ELO for a user to be placed in this division after placement matches  # noqa: E501

        :return: The max_elo of this Division.  # noqa: E501
        :rtype: int
        """
        return self._max_elo

    @max_elo.setter
    def max_elo(self, max_elo):
        """Sets the max_elo of this Division.

        Max ELO for a user to be placed in this division after placement matches  # noqa: E501

        :param max_elo: The max_elo of this Division.  # noqa: E501
        :type: int
        """

        self._max_elo = max_elo

    @property
    def min_elo(self):
        """Gets the min_elo of this Division.  # noqa: E501

        Min ELO for a user to be placed in this division after placement matches  # noqa: E501

        :return: The min_elo of this Division.  # noqa: E501
        :rtype: int
        """
        return self._min_elo

    @min_elo.setter
    def min_elo(self, min_elo):
        """Sets the min_elo of this Division.

        Min ELO for a user to be placed in this division after placement matches  # noqa: E501

        :param min_elo: The min_elo of this Division.  # noqa: E501
        :type: int
        """

        self._min_elo = min_elo

    @property
    def name(self):
        """Gets the name of this Division.  # noqa: E501

        The name of the division.  # noqa: E501

        :return: The name of this Division.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Division.

        The name of the division.  # noqa: E501

        :param name: The name of this Division.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tiers(self):
        """Gets the tiers of this Division.  # noqa: E501

        The tiers of the division  # noqa: E501

        :return: The tiers of this Division.  # noqa: E501
        :rtype: list[Tier]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this Division.

        The tiers of the division  # noqa: E501

        :param tiers: The tiers of this Division.  # noqa: E501
        :type: list[Tier]
        """

        self._tiers = tiers

    @property
    def type(self):
        """Gets the type of this Division.  # noqa: E501

        The type of the division.  # noqa: E501

        :return: The type of this Division.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Division.

        The type of the division.  # noqa: E501

        :param type: The type of this Division.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(Division, dict):
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
        if not isinstance(other, Division):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Division):
            return True

        return self.to_dict() != other.to_dict()

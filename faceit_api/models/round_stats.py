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


class RoundStats(object):
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
        'best_of': 'object',
        'competition_id': 'object',
        'game_id': 'object',
        'game_mode': 'object',
        'match_id': 'object',
        'match_round': 'object',
        'played': 'object',
        'round_stats': 'dict(str, object)',
        'teams': 'list[TeamStatsSimple]'
    }

    attribute_map = {
        'best_of': 'best_of',
        'competition_id': 'competition_id',
        'game_id': 'game_id',
        'game_mode': 'game_mode',
        'match_id': 'match_id',
        'match_round': 'match_round',
        'played': 'played',
        'round_stats': 'round_stats',
        'teams': 'teams'
    }

    def __init__(self, best_of=None, competition_id=None, game_id=None, game_mode=None, match_id=None, match_round=None, played=None, round_stats=None, teams=None, _configuration=None):  # noqa: E501
        """RoundStats - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._best_of = None
        self._competition_id = None
        self._game_id = None
        self._game_mode = None
        self._match_id = None
        self._match_round = None
        self._played = None
        self._round_stats = None
        self._teams = None
        self.discriminator = None

        if best_of is not None:
            self.best_of = best_of
        if competition_id is not None:
            self.competition_id = competition_id
        if game_id is not None:
            self.game_id = game_id
        if game_mode is not None:
            self.game_mode = game_mode
        if match_id is not None:
            self.match_id = match_id
        if match_round is not None:
            self.match_round = match_round
        if played is not None:
            self.played = played
        if round_stats is not None:
            self.round_stats = round_stats
        if teams is not None:
            self.teams = teams

    @property
    def best_of(self):
        """Gets the best_of of this RoundStats.  # noqa: E501


        :return: The best_of of this RoundStats.  # noqa: E501
        :rtype: object
        """
        return self._best_of

    @best_of.setter
    def best_of(self, best_of):
        """Sets the best_of of this RoundStats.


        :param best_of: The best_of of this RoundStats.  # noqa: E501
        :type: object
        """

        self._best_of = best_of

    @property
    def competition_id(self):
        """Gets the competition_id of this RoundStats.  # noqa: E501


        :return: The competition_id of this RoundStats.  # noqa: E501
        :rtype: object
        """
        return self._competition_id

    @competition_id.setter
    def competition_id(self, competition_id):
        """Sets the competition_id of this RoundStats.


        :param competition_id: The competition_id of this RoundStats.  # noqa: E501
        :type: object
        """

        self._competition_id = competition_id

    @property
    def game_id(self):
        """Gets the game_id of this RoundStats.  # noqa: E501


        :return: The game_id of this RoundStats.  # noqa: E501
        :rtype: object
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this RoundStats.


        :param game_id: The game_id of this RoundStats.  # noqa: E501
        :type: object
        """

        self._game_id = game_id

    @property
    def game_mode(self):
        """Gets the game_mode of this RoundStats.  # noqa: E501


        :return: The game_mode of this RoundStats.  # noqa: E501
        :rtype: object
        """
        return self._game_mode

    @game_mode.setter
    def game_mode(self, game_mode):
        """Sets the game_mode of this RoundStats.


        :param game_mode: The game_mode of this RoundStats.  # noqa: E501
        :type: object
        """

        self._game_mode = game_mode

    @property
    def match_id(self):
        """Gets the match_id of this RoundStats.  # noqa: E501


        :return: The match_id of this RoundStats.  # noqa: E501
        :rtype: object
        """
        return self._match_id

    @match_id.setter
    def match_id(self, match_id):
        """Sets the match_id of this RoundStats.


        :param match_id: The match_id of this RoundStats.  # noqa: E501
        :type: object
        """

        self._match_id = match_id

    @property
    def match_round(self):
        """Gets the match_round of this RoundStats.  # noqa: E501


        :return: The match_round of this RoundStats.  # noqa: E501
        :rtype: object
        """
        return self._match_round

    @match_round.setter
    def match_round(self, match_round):
        """Sets the match_round of this RoundStats.


        :param match_round: The match_round of this RoundStats.  # noqa: E501
        :type: object
        """

        self._match_round = match_round

    @property
    def played(self):
        """Gets the played of this RoundStats.  # noqa: E501


        :return: The played of this RoundStats.  # noqa: E501
        :rtype: object
        """
        return self._played

    @played.setter
    def played(self, played):
        """Sets the played of this RoundStats.


        :param played: The played of this RoundStats.  # noqa: E501
        :type: object
        """

        self._played = played

    @property
    def round_stats(self):
        """Gets the round_stats of this RoundStats.  # noqa: E501


        :return: The round_stats of this RoundStats.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._round_stats

    @round_stats.setter
    def round_stats(self, round_stats):
        """Sets the round_stats of this RoundStats.


        :param round_stats: The round_stats of this RoundStats.  # noqa: E501
        :type: dict(str, object)
        """

        self._round_stats = round_stats

    @property
    def teams(self):
        """Gets the teams of this RoundStats.  # noqa: E501


        :return: The teams of this RoundStats.  # noqa: E501
        :rtype: list[TeamStatsSimple]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this RoundStats.


        :param teams: The teams of this RoundStats.  # noqa: E501
        :type: list[TeamStatsSimple]
        """

        self._teams = teams

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
        if issubclass(RoundStats, dict):
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
        if not isinstance(other, RoundStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoundStats):
            return True

        return self.to_dict() != other.to_dict()

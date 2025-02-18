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


class Leaderboard(object):
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
        'competition_id': 'str',
        'competition_type': 'str',
        'end_date': 'int',
        'game_id': 'str',
        'group': 'int',
        'leaderboard_id': 'str',
        'leaderboard_mode': 'str',
        'leaderboard_name': 'str',
        'leaderboard_type': 'str',
        'min_matches': 'int',
        'points_per_draw': 'int',
        'points_per_loss': 'int',
        'points_per_win': 'int',
        'points_type': 'str',
        'ranking_boost': 'int',
        'ranking_type': 'str',
        'region': 'str',
        'round': 'int',
        'season': 'int',
        'start_date': 'int',
        'starting_points': 'int',
        'status': 'str'
    }

    attribute_map = {
        'competition_id': 'competition_id',
        'competition_type': 'competition_type',
        'end_date': 'end_date',
        'game_id': 'game_id',
        'group': 'group',
        'leaderboard_id': 'leaderboard_id',
        'leaderboard_mode': 'leaderboard_mode',
        'leaderboard_name': 'leaderboard_name',
        'leaderboard_type': 'leaderboard_type',
        'min_matches': 'min_matches',
        'points_per_draw': 'points_per_draw',
        'points_per_loss': 'points_per_loss',
        'points_per_win': 'points_per_win',
        'points_type': 'points_type',
        'ranking_boost': 'ranking_boost',
        'ranking_type': 'ranking_type',
        'region': 'region',
        'round': 'round',
        'season': 'season',
        'start_date': 'start_date',
        'starting_points': 'starting_points',
        'status': 'status'
    }

    def __init__(self, competition_id=None, competition_type=None, end_date=None, game_id=None, group=None, leaderboard_id=None, leaderboard_mode=None, leaderboard_name=None, leaderboard_type=None, min_matches=None, points_per_draw=None, points_per_loss=None, points_per_win=None, points_type=None, ranking_boost=None, ranking_type=None, region=None, round=None, season=None, start_date=None, starting_points=None, status=None, _configuration=None):  # noqa: E501
        """Leaderboard - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._competition_id = None
        self._competition_type = None
        self._end_date = None
        self._game_id = None
        self._group = None
        self._leaderboard_id = None
        self._leaderboard_mode = None
        self._leaderboard_name = None
        self._leaderboard_type = None
        self._min_matches = None
        self._points_per_draw = None
        self._points_per_loss = None
        self._points_per_win = None
        self._points_type = None
        self._ranking_boost = None
        self._ranking_type = None
        self._region = None
        self._round = None
        self._season = None
        self._start_date = None
        self._starting_points = None
        self._status = None
        self.discriminator = None

        if competition_id is not None:
            self.competition_id = competition_id
        if competition_type is not None:
            self.competition_type = competition_type
        if end_date is not None:
            self.end_date = end_date
        if game_id is not None:
            self.game_id = game_id
        if group is not None:
            self.group = group
        if leaderboard_id is not None:
            self.leaderboard_id = leaderboard_id
        if leaderboard_mode is not None:
            self.leaderboard_mode = leaderboard_mode
        if leaderboard_name is not None:
            self.leaderboard_name = leaderboard_name
        if leaderboard_type is not None:
            self.leaderboard_type = leaderboard_type
        if min_matches is not None:
            self.min_matches = min_matches
        if points_per_draw is not None:
            self.points_per_draw = points_per_draw
        if points_per_loss is not None:
            self.points_per_loss = points_per_loss
        if points_per_win is not None:
            self.points_per_win = points_per_win
        if points_type is not None:
            self.points_type = points_type
        if ranking_boost is not None:
            self.ranking_boost = ranking_boost
        if ranking_type is not None:
            self.ranking_type = ranking_type
        if region is not None:
            self.region = region
        if round is not None:
            self.round = round
        if season is not None:
            self.season = season
        if start_date is not None:
            self.start_date = start_date
        if starting_points is not None:
            self.starting_points = starting_points
        if status is not None:
            self.status = status

    @property
    def competition_id(self):
        """Gets the competition_id of this Leaderboard.  # noqa: E501


        :return: The competition_id of this Leaderboard.  # noqa: E501
        :rtype: str
        """
        return self._competition_id

    @competition_id.setter
    def competition_id(self, competition_id):
        """Sets the competition_id of this Leaderboard.


        :param competition_id: The competition_id of this Leaderboard.  # noqa: E501
        :type: str
        """

        self._competition_id = competition_id

    @property
    def competition_type(self):
        """Gets the competition_type of this Leaderboard.  # noqa: E501


        :return: The competition_type of this Leaderboard.  # noqa: E501
        :rtype: str
        """
        return self._competition_type

    @competition_type.setter
    def competition_type(self, competition_type):
        """Sets the competition_type of this Leaderboard.


        :param competition_type: The competition_type of this Leaderboard.  # noqa: E501
        :type: str
        """

        self._competition_type = competition_type

    @property
    def end_date(self):
        """Gets the end_date of this Leaderboard.  # noqa: E501


        :return: The end_date of this Leaderboard.  # noqa: E501
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Leaderboard.


        :param end_date: The end_date of this Leaderboard.  # noqa: E501
        :type: int
        """

        self._end_date = end_date

    @property
    def game_id(self):
        """Gets the game_id of this Leaderboard.  # noqa: E501


        :return: The game_id of this Leaderboard.  # noqa: E501
        :rtype: str
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this Leaderboard.


        :param game_id: The game_id of this Leaderboard.  # noqa: E501
        :type: str
        """

        self._game_id = game_id

    @property
    def group(self):
        """Gets the group of this Leaderboard.  # noqa: E501


        :return: The group of this Leaderboard.  # noqa: E501
        :rtype: int
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this Leaderboard.


        :param group: The group of this Leaderboard.  # noqa: E501
        :type: int
        """

        self._group = group

    @property
    def leaderboard_id(self):
        """Gets the leaderboard_id of this Leaderboard.  # noqa: E501


        :return: The leaderboard_id of this Leaderboard.  # noqa: E501
        :rtype: str
        """
        return self._leaderboard_id

    @leaderboard_id.setter
    def leaderboard_id(self, leaderboard_id):
        """Sets the leaderboard_id of this Leaderboard.


        :param leaderboard_id: The leaderboard_id of this Leaderboard.  # noqa: E501
        :type: str
        """

        self._leaderboard_id = leaderboard_id

    @property
    def leaderboard_mode(self):
        """Gets the leaderboard_mode of this Leaderboard.  # noqa: E501


        :return: The leaderboard_mode of this Leaderboard.  # noqa: E501
        :rtype: str
        """
        return self._leaderboard_mode

    @leaderboard_mode.setter
    def leaderboard_mode(self, leaderboard_mode):
        """Sets the leaderboard_mode of this Leaderboard.


        :param leaderboard_mode: The leaderboard_mode of this Leaderboard.  # noqa: E501
        :type: str
        """

        self._leaderboard_mode = leaderboard_mode

    @property
    def leaderboard_name(self):
        """Gets the leaderboard_name of this Leaderboard.  # noqa: E501


        :return: The leaderboard_name of this Leaderboard.  # noqa: E501
        :rtype: str
        """
        return self._leaderboard_name

    @leaderboard_name.setter
    def leaderboard_name(self, leaderboard_name):
        """Sets the leaderboard_name of this Leaderboard.


        :param leaderboard_name: The leaderboard_name of this Leaderboard.  # noqa: E501
        :type: str
        """

        self._leaderboard_name = leaderboard_name

    @property
    def leaderboard_type(self):
        """Gets the leaderboard_type of this Leaderboard.  # noqa: E501


        :return: The leaderboard_type of this Leaderboard.  # noqa: E501
        :rtype: str
        """
        return self._leaderboard_type

    @leaderboard_type.setter
    def leaderboard_type(self, leaderboard_type):
        """Sets the leaderboard_type of this Leaderboard.


        :param leaderboard_type: The leaderboard_type of this Leaderboard.  # noqa: E501
        :type: str
        """

        self._leaderboard_type = leaderboard_type

    @property
    def min_matches(self):
        """Gets the min_matches of this Leaderboard.  # noqa: E501


        :return: The min_matches of this Leaderboard.  # noqa: E501
        :rtype: int
        """
        return self._min_matches

    @min_matches.setter
    def min_matches(self, min_matches):
        """Sets the min_matches of this Leaderboard.


        :param min_matches: The min_matches of this Leaderboard.  # noqa: E501
        :type: int
        """

        self._min_matches = min_matches

    @property
    def points_per_draw(self):
        """Gets the points_per_draw of this Leaderboard.  # noqa: E501


        :return: The points_per_draw of this Leaderboard.  # noqa: E501
        :rtype: int
        """
        return self._points_per_draw

    @points_per_draw.setter
    def points_per_draw(self, points_per_draw):
        """Sets the points_per_draw of this Leaderboard.


        :param points_per_draw: The points_per_draw of this Leaderboard.  # noqa: E501
        :type: int
        """

        self._points_per_draw = points_per_draw

    @property
    def points_per_loss(self):
        """Gets the points_per_loss of this Leaderboard.  # noqa: E501


        :return: The points_per_loss of this Leaderboard.  # noqa: E501
        :rtype: int
        """
        return self._points_per_loss

    @points_per_loss.setter
    def points_per_loss(self, points_per_loss):
        """Sets the points_per_loss of this Leaderboard.


        :param points_per_loss: The points_per_loss of this Leaderboard.  # noqa: E501
        :type: int
        """

        self._points_per_loss = points_per_loss

    @property
    def points_per_win(self):
        """Gets the points_per_win of this Leaderboard.  # noqa: E501


        :return: The points_per_win of this Leaderboard.  # noqa: E501
        :rtype: int
        """
        return self._points_per_win

    @points_per_win.setter
    def points_per_win(self, points_per_win):
        """Sets the points_per_win of this Leaderboard.


        :param points_per_win: The points_per_win of this Leaderboard.  # noqa: E501
        :type: int
        """

        self._points_per_win = points_per_win

    @property
    def points_type(self):
        """Gets the points_type of this Leaderboard.  # noqa: E501


        :return: The points_type of this Leaderboard.  # noqa: E501
        :rtype: str
        """
        return self._points_type

    @points_type.setter
    def points_type(self, points_type):
        """Sets the points_type of this Leaderboard.


        :param points_type: The points_type of this Leaderboard.  # noqa: E501
        :type: str
        """

        self._points_type = points_type

    @property
    def ranking_boost(self):
        """Gets the ranking_boost of this Leaderboard.  # noqa: E501


        :return: The ranking_boost of this Leaderboard.  # noqa: E501
        :rtype: int
        """
        return self._ranking_boost

    @ranking_boost.setter
    def ranking_boost(self, ranking_boost):
        """Sets the ranking_boost of this Leaderboard.


        :param ranking_boost: The ranking_boost of this Leaderboard.  # noqa: E501
        :type: int
        """

        self._ranking_boost = ranking_boost

    @property
    def ranking_type(self):
        """Gets the ranking_type of this Leaderboard.  # noqa: E501


        :return: The ranking_type of this Leaderboard.  # noqa: E501
        :rtype: str
        """
        return self._ranking_type

    @ranking_type.setter
    def ranking_type(self, ranking_type):
        """Sets the ranking_type of this Leaderboard.


        :param ranking_type: The ranking_type of this Leaderboard.  # noqa: E501
        :type: str
        """

        self._ranking_type = ranking_type

    @property
    def region(self):
        """Gets the region of this Leaderboard.  # noqa: E501


        :return: The region of this Leaderboard.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Leaderboard.


        :param region: The region of this Leaderboard.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def round(self):
        """Gets the round of this Leaderboard.  # noqa: E501


        :return: The round of this Leaderboard.  # noqa: E501
        :rtype: int
        """
        return self._round

    @round.setter
    def round(self, round):
        """Sets the round of this Leaderboard.


        :param round: The round of this Leaderboard.  # noqa: E501
        :type: int
        """

        self._round = round

    @property
    def season(self):
        """Gets the season of this Leaderboard.  # noqa: E501


        :return: The season of this Leaderboard.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this Leaderboard.


        :param season: The season of this Leaderboard.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def start_date(self):
        """Gets the start_date of this Leaderboard.  # noqa: E501


        :return: The start_date of this Leaderboard.  # noqa: E501
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Leaderboard.


        :param start_date: The start_date of this Leaderboard.  # noqa: E501
        :type: int
        """

        self._start_date = start_date

    @property
    def starting_points(self):
        """Gets the starting_points of this Leaderboard.  # noqa: E501


        :return: The starting_points of this Leaderboard.  # noqa: E501
        :rtype: int
        """
        return self._starting_points

    @starting_points.setter
    def starting_points(self, starting_points):
        """Sets the starting_points of this Leaderboard.


        :param starting_points: The starting_points of this Leaderboard.  # noqa: E501
        :type: int
        """

        self._starting_points = starting_points

    @property
    def status(self):
        """Gets the status of this Leaderboard.  # noqa: E501


        :return: The status of this Leaderboard.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Leaderboard.


        :param status: The status of this Leaderboard.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(Leaderboard, dict):
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
        if not isinstance(other, Leaderboard):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Leaderboard):
            return True

        return self.to_dict() != other.to_dict()

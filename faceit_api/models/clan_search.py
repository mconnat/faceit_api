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


class ClanSearch(object):
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
        'avatar': 'str',
        'game': 'str',
        'id': 'str',
        'join': 'str',
        'last_match_finished': 'datetime',
        'matches_count_24h': 'int',
        'max_skill_level': 'int',
        'members_count': 'int',
        'members_count_24h': 'int',
        'min_skill_level': 'int',
        'name': 'str',
        'organizer_id': 'str',
        'region': 'str',
        'type': 'str'
    }

    attribute_map = {
        'avatar': 'avatar',
        'game': 'game',
        'id': 'id',
        'join': 'join',
        'last_match_finished': 'last_match_finished',
        'matches_count_24h': 'matches_count_24h',
        'max_skill_level': 'max_skill_level',
        'members_count': 'members_count',
        'members_count_24h': 'members_count_24h',
        'min_skill_level': 'min_skill_level',
        'name': 'name',
        'organizer_id': 'organizer_id',
        'region': 'region',
        'type': 'type'
    }

    def __init__(self, avatar=None, game=None, id=None, join=None, last_match_finished=None, matches_count_24h=None, max_skill_level=None, members_count=None, members_count_24h=None, min_skill_level=None, name=None, organizer_id=None, region=None, type=None, _configuration=None):  # noqa: E501
        """ClanSearch - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._avatar = None
        self._game = None
        self._id = None
        self._join = None
        self._last_match_finished = None
        self._matches_count_24h = None
        self._max_skill_level = None
        self._members_count = None
        self._members_count_24h = None
        self._min_skill_level = None
        self._name = None
        self._organizer_id = None
        self._region = None
        self._type = None
        self.discriminator = None

        if avatar is not None:
            self.avatar = avatar
        if game is not None:
            self.game = game
        if id is not None:
            self.id = id
        if join is not None:
            self.join = join
        if last_match_finished is not None:
            self.last_match_finished = last_match_finished
        if matches_count_24h is not None:
            self.matches_count_24h = matches_count_24h
        if max_skill_level is not None:
            self.max_skill_level = max_skill_level
        if members_count is not None:
            self.members_count = members_count
        if members_count_24h is not None:
            self.members_count_24h = members_count_24h
        if min_skill_level is not None:
            self.min_skill_level = min_skill_level
        if name is not None:
            self.name = name
        if organizer_id is not None:
            self.organizer_id = organizer_id
        if region is not None:
            self.region = region
        if type is not None:
            self.type = type

    @property
    def avatar(self):
        """Gets the avatar of this ClanSearch.  # noqa: E501

        The clan's avatar url  # noqa: E501

        :return: The avatar of this ClanSearch.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this ClanSearch.

        The clan's avatar url  # noqa: E501

        :param avatar: The avatar of this ClanSearch.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def game(self):
        """Gets the game of this ClanSearch.  # noqa: E501

        The game of the clan  # noqa: E501

        :return: The game of this ClanSearch.  # noqa: E501
        :rtype: str
        """
        return self._game

    @game.setter
    def game(self, game):
        """Sets the game of this ClanSearch.

        The game of the clan  # noqa: E501

        :param game: The game of this ClanSearch.  # noqa: E501
        :type: str
        """

        self._game = game

    @property
    def id(self):
        """Gets the id of this ClanSearch.  # noqa: E501

        The id of the clan  # noqa: E501

        :return: The id of this ClanSearch.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClanSearch.

        The id of the clan  # noqa: E501

        :param id: The id of this ClanSearch.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def join(self):
        """Gets the join of this ClanSearch.  # noqa: E501

        The clan's join type  # noqa: E501

        :return: The join of this ClanSearch.  # noqa: E501
        :rtype: str
        """
        return self._join

    @join.setter
    def join(self, join):
        """Sets the join of this ClanSearch.

        The clan's join type  # noqa: E501

        :param join: The join of this ClanSearch.  # noqa: E501
        :type: str
        """

        self._join = join

    @property
    def last_match_finished(self):
        """Gets the last_match_finished of this ClanSearch.  # noqa: E501

        The time the clan's last match finished  # noqa: E501

        :return: The last_match_finished of this ClanSearch.  # noqa: E501
        :rtype: datetime
        """
        return self._last_match_finished

    @last_match_finished.setter
    def last_match_finished(self, last_match_finished):
        """Sets the last_match_finished of this ClanSearch.

        The time the clan's last match finished  # noqa: E501

        :param last_match_finished: The last_match_finished of this ClanSearch.  # noqa: E501
        :type: datetime
        """

        self._last_match_finished = last_match_finished

    @property
    def matches_count_24h(self):
        """Gets the matches_count_24h of this ClanSearch.  # noqa: E501

        The clan's matches count in the last 24 hours  # noqa: E501

        :return: The matches_count_24h of this ClanSearch.  # noqa: E501
        :rtype: int
        """
        return self._matches_count_24h

    @matches_count_24h.setter
    def matches_count_24h(self, matches_count_24h):
        """Sets the matches_count_24h of this ClanSearch.

        The clan's matches count in the last 24 hours  # noqa: E501

        :param matches_count_24h: The matches_count_24h of this ClanSearch.  # noqa: E501
        :type: int
        """

        self._matches_count_24h = matches_count_24h

    @property
    def max_skill_level(self):
        """Gets the max_skill_level of this ClanSearch.  # noqa: E501

        The clan's maximum skill level  # noqa: E501

        :return: The max_skill_level of this ClanSearch.  # noqa: E501
        :rtype: int
        """
        return self._max_skill_level

    @max_skill_level.setter
    def max_skill_level(self, max_skill_level):
        """Sets the max_skill_level of this ClanSearch.

        The clan's maximum skill level  # noqa: E501

        :param max_skill_level: The max_skill_level of this ClanSearch.  # noqa: E501
        :type: int
        """

        self._max_skill_level = max_skill_level

    @property
    def members_count(self):
        """Gets the members_count of this ClanSearch.  # noqa: E501

        The clan's members count  # noqa: E501

        :return: The members_count of this ClanSearch.  # noqa: E501
        :rtype: int
        """
        return self._members_count

    @members_count.setter
    def members_count(self, members_count):
        """Sets the members_count of this ClanSearch.

        The clan's members count  # noqa: E501

        :param members_count: The members_count of this ClanSearch.  # noqa: E501
        :type: int
        """

        self._members_count = members_count

    @property
    def members_count_24h(self):
        """Gets the members_count_24h of this ClanSearch.  # noqa: E501

        The clan's members count in the last 24 hours  # noqa: E501

        :return: The members_count_24h of this ClanSearch.  # noqa: E501
        :rtype: int
        """
        return self._members_count_24h

    @members_count_24h.setter
    def members_count_24h(self, members_count_24h):
        """Sets the members_count_24h of this ClanSearch.

        The clan's members count in the last 24 hours  # noqa: E501

        :param members_count_24h: The members_count_24h of this ClanSearch.  # noqa: E501
        :type: int
        """

        self._members_count_24h = members_count_24h

    @property
    def min_skill_level(self):
        """Gets the min_skill_level of this ClanSearch.  # noqa: E501

        The clan's minimum skill level  # noqa: E501

        :return: The min_skill_level of this ClanSearch.  # noqa: E501
        :rtype: int
        """
        return self._min_skill_level

    @min_skill_level.setter
    def min_skill_level(self, min_skill_level):
        """Sets the min_skill_level of this ClanSearch.

        The clan's minimum skill level  # noqa: E501

        :param min_skill_level: The min_skill_level of this ClanSearch.  # noqa: E501
        :type: int
        """

        self._min_skill_level = min_skill_level

    @property
    def name(self):
        """Gets the name of this ClanSearch.  # noqa: E501

        The name of the clan  # noqa: E501

        :return: The name of this ClanSearch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClanSearch.

        The name of the clan  # noqa: E501

        :param name: The name of this ClanSearch.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organizer_id(self):
        """Gets the organizer_id of this ClanSearch.  # noqa: E501

        The clan's organizer id  # noqa: E501

        :return: The organizer_id of this ClanSearch.  # noqa: E501
        :rtype: str
        """
        return self._organizer_id

    @organizer_id.setter
    def organizer_id(self, organizer_id):
        """Sets the organizer_id of this ClanSearch.

        The clan's organizer id  # noqa: E501

        :param organizer_id: The organizer_id of this ClanSearch.  # noqa: E501
        :type: str
        """

        self._organizer_id = organizer_id

    @property
    def region(self):
        """Gets the region of this ClanSearch.  # noqa: E501

        The region of the clan  # noqa: E501

        :return: The region of this ClanSearch.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ClanSearch.

        The region of the clan  # noqa: E501

        :param region: The region of this ClanSearch.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def type(self):
        """Gets the type of this ClanSearch.  # noqa: E501

        The type of the clan  # noqa: E501

        :return: The type of this ClanSearch.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClanSearch.

        The type of the clan  # noqa: E501

        :param type: The type of this ClanSearch.  # noqa: E501
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
        if issubclass(ClanSearch, dict):
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
        if not isinstance(other, ClanSearch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClanSearch):
            return True

        return self.to_dict() != other.to_dict()

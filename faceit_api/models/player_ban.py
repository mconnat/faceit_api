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


class PlayerBan(object):
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
        'ends_at': 'datetime',
        'game': 'str',
        'nickname': 'str',
        'reason': 'str',
        'starts_at': 'datetime',
        'type': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'ends_at': 'ends_at',
        'game': 'game',
        'nickname': 'nickname',
        'reason': 'reason',
        'starts_at': 'starts_at',
        'type': 'type',
        'user_id': 'user_id'
    }

    def __init__(self, ends_at=None, game=None, nickname=None, reason=None, starts_at=None, type=None, user_id=None, _configuration=None):  # noqa: E501
        """PlayerBan - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ends_at = None
        self._game = None
        self._nickname = None
        self._reason = None
        self._starts_at = None
        self._type = None
        self._user_id = None
        self.discriminator = None

        if ends_at is not None:
            self.ends_at = ends_at
        if game is not None:
            self.game = game
        if nickname is not None:
            self.nickname = nickname
        if reason is not None:
            self.reason = reason
        if starts_at is not None:
            self.starts_at = starts_at
        if type is not None:
            self.type = type
        if user_id is not None:
            self.user_id = user_id

    @property
    def ends_at(self):
        """Gets the ends_at of this PlayerBan.  # noqa: E501


        :return: The ends_at of this PlayerBan.  # noqa: E501
        :rtype: datetime
        """
        return self._ends_at

    @ends_at.setter
    def ends_at(self, ends_at):
        """Sets the ends_at of this PlayerBan.


        :param ends_at: The ends_at of this PlayerBan.  # noqa: E501
        :type: datetime
        """

        self._ends_at = ends_at

    @property
    def game(self):
        """Gets the game of this PlayerBan.  # noqa: E501


        :return: The game of this PlayerBan.  # noqa: E501
        :rtype: str
        """
        return self._game

    @game.setter
    def game(self, game):
        """Sets the game of this PlayerBan.


        :param game: The game of this PlayerBan.  # noqa: E501
        :type: str
        """

        self._game = game

    @property
    def nickname(self):
        """Gets the nickname of this PlayerBan.  # noqa: E501


        :return: The nickname of this PlayerBan.  # noqa: E501
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this PlayerBan.


        :param nickname: The nickname of this PlayerBan.  # noqa: E501
        :type: str
        """

        self._nickname = nickname

    @property
    def reason(self):
        """Gets the reason of this PlayerBan.  # noqa: E501


        :return: The reason of this PlayerBan.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this PlayerBan.


        :param reason: The reason of this PlayerBan.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def starts_at(self):
        """Gets the starts_at of this PlayerBan.  # noqa: E501


        :return: The starts_at of this PlayerBan.  # noqa: E501
        :rtype: datetime
        """
        return self._starts_at

    @starts_at.setter
    def starts_at(self, starts_at):
        """Sets the starts_at of this PlayerBan.


        :param starts_at: The starts_at of this PlayerBan.  # noqa: E501
        :type: datetime
        """

        self._starts_at = starts_at

    @property
    def type(self):
        """Gets the type of this PlayerBan.  # noqa: E501


        :return: The type of this PlayerBan.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PlayerBan.


        :param type: The type of this PlayerBan.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def user_id(self):
        """Gets the user_id of this PlayerBan.  # noqa: E501


        :return: The user_id of this PlayerBan.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this PlayerBan.


        :param user_id: The user_id of this PlayerBan.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if issubclass(PlayerBan, dict):
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
        if not isinstance(other, PlayerBan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlayerBan):
            return True

        return self.to_dict() != other.to_dict()
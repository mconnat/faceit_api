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


class TeamSearch(object):
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
        'chat_room_id': 'str',
        'faceit_url': 'str',
        'game': 'str',
        'name': 'str',
        'team_id': 'str',
        'verified': 'bool'
    }

    attribute_map = {
        'avatar': 'avatar',
        'chat_room_id': 'chat_room_id',
        'faceit_url': 'faceit_url',
        'game': 'game',
        'name': 'name',
        'team_id': 'team_id',
        'verified': 'verified'
    }

    def __init__(self, avatar=None, chat_room_id=None, faceit_url=None, game=None, name=None, team_id=None, verified=None, _configuration=None):  # noqa: E501
        """TeamSearch - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._avatar = None
        self._chat_room_id = None
        self._faceit_url = None
        self._game = None
        self._name = None
        self._team_id = None
        self._verified = None
        self.discriminator = None

        if avatar is not None:
            self.avatar = avatar
        if chat_room_id is not None:
            self.chat_room_id = chat_room_id
        if faceit_url is not None:
            self.faceit_url = faceit_url
        if game is not None:
            self.game = game
        if name is not None:
            self.name = name
        if team_id is not None:
            self.team_id = team_id
        if verified is not None:
            self.verified = verified

    @property
    def avatar(self):
        """Gets the avatar of this TeamSearch.  # noqa: E501


        :return: The avatar of this TeamSearch.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this TeamSearch.


        :param avatar: The avatar of this TeamSearch.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def chat_room_id(self):
        """Gets the chat_room_id of this TeamSearch.  # noqa: E501


        :return: The chat_room_id of this TeamSearch.  # noqa: E501
        :rtype: str
        """
        return self._chat_room_id

    @chat_room_id.setter
    def chat_room_id(self, chat_room_id):
        """Sets the chat_room_id of this TeamSearch.


        :param chat_room_id: The chat_room_id of this TeamSearch.  # noqa: E501
        :type: str
        """

        self._chat_room_id = chat_room_id

    @property
    def faceit_url(self):
        """Gets the faceit_url of this TeamSearch.  # noqa: E501


        :return: The faceit_url of this TeamSearch.  # noqa: E501
        :rtype: str
        """
        return self._faceit_url

    @faceit_url.setter
    def faceit_url(self, faceit_url):
        """Sets the faceit_url of this TeamSearch.


        :param faceit_url: The faceit_url of this TeamSearch.  # noqa: E501
        :type: str
        """

        self._faceit_url = faceit_url

    @property
    def game(self):
        """Gets the game of this TeamSearch.  # noqa: E501


        :return: The game of this TeamSearch.  # noqa: E501
        :rtype: str
        """
        return self._game

    @game.setter
    def game(self, game):
        """Sets the game of this TeamSearch.


        :param game: The game of this TeamSearch.  # noqa: E501
        :type: str
        """

        self._game = game

    @property
    def name(self):
        """Gets the name of this TeamSearch.  # noqa: E501


        :return: The name of this TeamSearch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TeamSearch.


        :param name: The name of this TeamSearch.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def team_id(self):
        """Gets the team_id of this TeamSearch.  # noqa: E501


        :return: The team_id of this TeamSearch.  # noqa: E501
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this TeamSearch.


        :param team_id: The team_id of this TeamSearch.  # noqa: E501
        :type: str
        """

        self._team_id = team_id

    @property
    def verified(self):
        """Gets the verified of this TeamSearch.  # noqa: E501


        :return: The verified of this TeamSearch.  # noqa: E501
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this TeamSearch.


        :param verified: The verified of this TeamSearch.  # noqa: E501
        :type: bool
        """

        self._verified = verified

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
        if issubclass(TeamSearch, dict):
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
        if not isinstance(other, TeamSearch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamSearch):
            return True

        return self.to_dict() != other.to_dict()
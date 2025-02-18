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


class Hub(object):
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
        'background_image': 'str',
        'chat_room_id': 'str',
        'cover_image': 'str',
        'description': 'str',
        'faceit_url': 'str',
        'game_data': 'Game',
        'game_id': 'str',
        'hub_id': 'str',
        'join_permission': 'str',
        'max_skill_level': 'int',
        'min_skill_level': 'int',
        'name': 'str',
        'organizer_data': 'Organizer',
        'organizer_id': 'str',
        'players_joined': 'int',
        'region': 'str',
        'rule_id': 'str'
    }

    attribute_map = {
        'avatar': 'avatar',
        'background_image': 'background_image',
        'chat_room_id': 'chat_room_id',
        'cover_image': 'cover_image',
        'description': 'description',
        'faceit_url': 'faceit_url',
        'game_data': 'game_data',
        'game_id': 'game_id',
        'hub_id': 'hub_id',
        'join_permission': 'join_permission',
        'max_skill_level': 'max_skill_level',
        'min_skill_level': 'min_skill_level',
        'name': 'name',
        'organizer_data': 'organizer_data',
        'organizer_id': 'organizer_id',
        'players_joined': 'players_joined',
        'region': 'region',
        'rule_id': 'rule_id'
    }

    def __init__(self, avatar=None, background_image=None, chat_room_id=None, cover_image=None, description=None, faceit_url=None, game_data=None, game_id=None, hub_id=None, join_permission=None, max_skill_level=None, min_skill_level=None, name=None, organizer_data=None, organizer_id=None, players_joined=None, region=None, rule_id=None, _configuration=None):  # noqa: E501
        """Hub - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._avatar = None
        self._background_image = None
        self._chat_room_id = None
        self._cover_image = None
        self._description = None
        self._faceit_url = None
        self._game_data = None
        self._game_id = None
        self._hub_id = None
        self._join_permission = None
        self._max_skill_level = None
        self._min_skill_level = None
        self._name = None
        self._organizer_data = None
        self._organizer_id = None
        self._players_joined = None
        self._region = None
        self._rule_id = None
        self.discriminator = None

        if avatar is not None:
            self.avatar = avatar
        if background_image is not None:
            self.background_image = background_image
        if chat_room_id is not None:
            self.chat_room_id = chat_room_id
        if cover_image is not None:
            self.cover_image = cover_image
        if description is not None:
            self.description = description
        if faceit_url is not None:
            self.faceit_url = faceit_url
        if game_data is not None:
            self.game_data = game_data
        if game_id is not None:
            self.game_id = game_id
        if hub_id is not None:
            self.hub_id = hub_id
        if join_permission is not None:
            self.join_permission = join_permission
        if max_skill_level is not None:
            self.max_skill_level = max_skill_level
        if min_skill_level is not None:
            self.min_skill_level = min_skill_level
        if name is not None:
            self.name = name
        if organizer_data is not None:
            self.organizer_data = organizer_data
        if organizer_id is not None:
            self.organizer_id = organizer_id
        if players_joined is not None:
            self.players_joined = players_joined
        if region is not None:
            self.region = region
        if rule_id is not None:
            self.rule_id = rule_id

    @property
    def avatar(self):
        """Gets the avatar of this Hub.  # noqa: E501


        :return: The avatar of this Hub.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this Hub.


        :param avatar: The avatar of this Hub.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def background_image(self):
        """Gets the background_image of this Hub.  # noqa: E501


        :return: The background_image of this Hub.  # noqa: E501
        :rtype: str
        """
        return self._background_image

    @background_image.setter
    def background_image(self, background_image):
        """Sets the background_image of this Hub.


        :param background_image: The background_image of this Hub.  # noqa: E501
        :type: str
        """

        self._background_image = background_image

    @property
    def chat_room_id(self):
        """Gets the chat_room_id of this Hub.  # noqa: E501


        :return: The chat_room_id of this Hub.  # noqa: E501
        :rtype: str
        """
        return self._chat_room_id

    @chat_room_id.setter
    def chat_room_id(self, chat_room_id):
        """Sets the chat_room_id of this Hub.


        :param chat_room_id: The chat_room_id of this Hub.  # noqa: E501
        :type: str
        """

        self._chat_room_id = chat_room_id

    @property
    def cover_image(self):
        """Gets the cover_image of this Hub.  # noqa: E501


        :return: The cover_image of this Hub.  # noqa: E501
        :rtype: str
        """
        return self._cover_image

    @cover_image.setter
    def cover_image(self, cover_image):
        """Sets the cover_image of this Hub.


        :param cover_image: The cover_image of this Hub.  # noqa: E501
        :type: str
        """

        self._cover_image = cover_image

    @property
    def description(self):
        """Gets the description of this Hub.  # noqa: E501


        :return: The description of this Hub.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Hub.


        :param description: The description of this Hub.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def faceit_url(self):
        """Gets the faceit_url of this Hub.  # noqa: E501


        :return: The faceit_url of this Hub.  # noqa: E501
        :rtype: str
        """
        return self._faceit_url

    @faceit_url.setter
    def faceit_url(self, faceit_url):
        """Sets the faceit_url of this Hub.


        :param faceit_url: The faceit_url of this Hub.  # noqa: E501
        :type: str
        """

        self._faceit_url = faceit_url

    @property
    def game_data(self):
        """Gets the game_data of this Hub.  # noqa: E501


        :return: The game_data of this Hub.  # noqa: E501
        :rtype: Game
        """
        return self._game_data

    @game_data.setter
    def game_data(self, game_data):
        """Sets the game_data of this Hub.


        :param game_data: The game_data of this Hub.  # noqa: E501
        :type: Game
        """

        self._game_data = game_data

    @property
    def game_id(self):
        """Gets the game_id of this Hub.  # noqa: E501


        :return: The game_id of this Hub.  # noqa: E501
        :rtype: str
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this Hub.


        :param game_id: The game_id of this Hub.  # noqa: E501
        :type: str
        """

        self._game_id = game_id

    @property
    def hub_id(self):
        """Gets the hub_id of this Hub.  # noqa: E501


        :return: The hub_id of this Hub.  # noqa: E501
        :rtype: str
        """
        return self._hub_id

    @hub_id.setter
    def hub_id(self, hub_id):
        """Sets the hub_id of this Hub.


        :param hub_id: The hub_id of this Hub.  # noqa: E501
        :type: str
        """

        self._hub_id = hub_id

    @property
    def join_permission(self):
        """Gets the join_permission of this Hub.  # noqa: E501


        :return: The join_permission of this Hub.  # noqa: E501
        :rtype: str
        """
        return self._join_permission

    @join_permission.setter
    def join_permission(self, join_permission):
        """Sets the join_permission of this Hub.


        :param join_permission: The join_permission of this Hub.  # noqa: E501
        :type: str
        """

        self._join_permission = join_permission

    @property
    def max_skill_level(self):
        """Gets the max_skill_level of this Hub.  # noqa: E501


        :return: The max_skill_level of this Hub.  # noqa: E501
        :rtype: int
        """
        return self._max_skill_level

    @max_skill_level.setter
    def max_skill_level(self, max_skill_level):
        """Sets the max_skill_level of this Hub.


        :param max_skill_level: The max_skill_level of this Hub.  # noqa: E501
        :type: int
        """

        self._max_skill_level = max_skill_level

    @property
    def min_skill_level(self):
        """Gets the min_skill_level of this Hub.  # noqa: E501


        :return: The min_skill_level of this Hub.  # noqa: E501
        :rtype: int
        """
        return self._min_skill_level

    @min_skill_level.setter
    def min_skill_level(self, min_skill_level):
        """Sets the min_skill_level of this Hub.


        :param min_skill_level: The min_skill_level of this Hub.  # noqa: E501
        :type: int
        """

        self._min_skill_level = min_skill_level

    @property
    def name(self):
        """Gets the name of this Hub.  # noqa: E501


        :return: The name of this Hub.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Hub.


        :param name: The name of this Hub.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organizer_data(self):
        """Gets the organizer_data of this Hub.  # noqa: E501


        :return: The organizer_data of this Hub.  # noqa: E501
        :rtype: Organizer
        """
        return self._organizer_data

    @organizer_data.setter
    def organizer_data(self, organizer_data):
        """Sets the organizer_data of this Hub.


        :param organizer_data: The organizer_data of this Hub.  # noqa: E501
        :type: Organizer
        """

        self._organizer_data = organizer_data

    @property
    def organizer_id(self):
        """Gets the organizer_id of this Hub.  # noqa: E501


        :return: The organizer_id of this Hub.  # noqa: E501
        :rtype: str
        """
        return self._organizer_id

    @organizer_id.setter
    def organizer_id(self, organizer_id):
        """Sets the organizer_id of this Hub.


        :param organizer_id: The organizer_id of this Hub.  # noqa: E501
        :type: str
        """

        self._organizer_id = organizer_id

    @property
    def players_joined(self):
        """Gets the players_joined of this Hub.  # noqa: E501


        :return: The players_joined of this Hub.  # noqa: E501
        :rtype: int
        """
        return self._players_joined

    @players_joined.setter
    def players_joined(self, players_joined):
        """Sets the players_joined of this Hub.


        :param players_joined: The players_joined of this Hub.  # noqa: E501
        :type: int
        """

        self._players_joined = players_joined

    @property
    def region(self):
        """Gets the region of this Hub.  # noqa: E501


        :return: The region of this Hub.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Hub.


        :param region: The region of this Hub.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def rule_id(self):
        """Gets the rule_id of this Hub.  # noqa: E501


        :return: The rule_id of this Hub.  # noqa: E501
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this Hub.


        :param rule_id: The rule_id of this Hub.  # noqa: E501
        :type: str
        """

        self._rule_id = rule_id

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
        if issubclass(Hub, dict):
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
        if not isinstance(other, Hub):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Hub):
            return True

        return self.to_dict() != other.to_dict()

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


class QueueSimple(object):
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
        'entity_id': 'str',
        'entity_type': 'str',
        'game': 'str',
        'id': 'str',
        'last_modified': 'datetime',
        'open': 'bool',
        'organizer_id': 'str',
        'queue_name': 'str',
        'region': 'str',
        'state': 'str'
    }

    attribute_map = {
        'entity_id': 'entityId',
        'entity_type': 'entityType',
        'game': 'game',
        'id': 'id',
        'last_modified': 'lastModified',
        'open': 'open',
        'organizer_id': 'organizerId',
        'queue_name': 'queueName',
        'region': 'region',
        'state': 'state'
    }

    def __init__(self, entity_id=None, entity_type=None, game=None, id=None, last_modified=None, open=None, organizer_id=None, queue_name=None, region=None, state=None, _configuration=None):  # noqa: E501
        """QueueSimple - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._entity_id = None
        self._entity_type = None
        self._game = None
        self._id = None
        self._last_modified = None
        self._open = None
        self._organizer_id = None
        self._queue_name = None
        self._region = None
        self._state = None
        self.discriminator = None

        if entity_id is not None:
            self.entity_id = entity_id
        if entity_type is not None:
            self.entity_type = entity_type
        if game is not None:
            self.game = game
        if id is not None:
            self.id = id
        if last_modified is not None:
            self.last_modified = last_modified
        if open is not None:
            self.open = open
        if organizer_id is not None:
            self.organizer_id = organizer_id
        if queue_name is not None:
            self.queue_name = queue_name
        if region is not None:
            self.region = region
        if state is not None:
            self.state = state

    @property
    def entity_id(self):
        """Gets the entity_id of this QueueSimple.  # noqa: E501


        :return: The entity_id of this QueueSimple.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this QueueSimple.


        :param entity_id: The entity_id of this QueueSimple.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """Gets the entity_type of this QueueSimple.  # noqa: E501


        :return: The entity_type of this QueueSimple.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this QueueSimple.


        :param entity_type: The entity_type of this QueueSimple.  # noqa: E501
        :type: str
        """

        self._entity_type = entity_type

    @property
    def game(self):
        """Gets the game of this QueueSimple.  # noqa: E501


        :return: The game of this QueueSimple.  # noqa: E501
        :rtype: str
        """
        return self._game

    @game.setter
    def game(self, game):
        """Sets the game of this QueueSimple.


        :param game: The game of this QueueSimple.  # noqa: E501
        :type: str
        """

        self._game = game

    @property
    def id(self):
        """Gets the id of this QueueSimple.  # noqa: E501


        :return: The id of this QueueSimple.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueueSimple.


        :param id: The id of this QueueSimple.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_modified(self):
        """Gets the last_modified of this QueueSimple.  # noqa: E501


        :return: The last_modified of this QueueSimple.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this QueueSimple.


        :param last_modified: The last_modified of this QueueSimple.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def open(self):
        """Gets the open of this QueueSimple.  # noqa: E501


        :return: The open of this QueueSimple.  # noqa: E501
        :rtype: bool
        """
        return self._open

    @open.setter
    def open(self, open):
        """Sets the open of this QueueSimple.


        :param open: The open of this QueueSimple.  # noqa: E501
        :type: bool
        """

        self._open = open

    @property
    def organizer_id(self):
        """Gets the organizer_id of this QueueSimple.  # noqa: E501


        :return: The organizer_id of this QueueSimple.  # noqa: E501
        :rtype: str
        """
        return self._organizer_id

    @organizer_id.setter
    def organizer_id(self, organizer_id):
        """Sets the organizer_id of this QueueSimple.


        :param organizer_id: The organizer_id of this QueueSimple.  # noqa: E501
        :type: str
        """

        self._organizer_id = organizer_id

    @property
    def queue_name(self):
        """Gets the queue_name of this QueueSimple.  # noqa: E501


        :return: The queue_name of this QueueSimple.  # noqa: E501
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this QueueSimple.


        :param queue_name: The queue_name of this QueueSimple.  # noqa: E501
        :type: str
        """

        self._queue_name = queue_name

    @property
    def region(self):
        """Gets the region of this QueueSimple.  # noqa: E501


        :return: The region of this QueueSimple.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this QueueSimple.


        :param region: The region of this QueueSimple.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def state(self):
        """Gets the state of this QueueSimple.  # noqa: E501


        :return: The state of this QueueSimple.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this QueueSimple.


        :param state: The state of this QueueSimple.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if issubclass(QueueSimple, dict):
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
        if not isinstance(other, QueueSimple):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueueSimple):
            return True

        return self.to_dict() != other.to_dict()

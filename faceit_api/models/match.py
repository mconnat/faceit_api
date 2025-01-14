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


class Match(object):
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
        'best_of': 'int',
        'broadcast_start_time': 'int',
        'broadcast_start_time_label': 'str',
        'calculate_elo': 'bool',
        'chat_room_id': 'str',
        'competition_id': 'str',
        'competition_name': 'str',
        'competition_type': 'str',
        'configured_at': 'int',
        'demo_url': 'list[str]',
        'detailed_results': 'list[DetailedMatchResult]',
        'faceit_url': 'str',
        'finished_at': 'int',
        'game': 'str',
        'group': 'int',
        'match_id': 'str',
        'organizer_id': 'str',
        'region': 'str',
        'results': 'MatchResult',
        'round': 'int',
        'scheduled_at': 'int',
        'started_at': 'int',
        'status': 'str',
        'teams': 'dict(str, Faction)',
        'version': 'int',
        'voting': 'object'
    }

    attribute_map = {
        'best_of': 'best_of',
        'broadcast_start_time': 'broadcast_start_time',
        'broadcast_start_time_label': 'broadcast_start_time_label',
        'calculate_elo': 'calculate_elo',
        'chat_room_id': 'chat_room_id',
        'competition_id': 'competition_id',
        'competition_name': 'competition_name',
        'competition_type': 'competition_type',
        'configured_at': 'configured_at',
        'demo_url': 'demo_url',
        'detailed_results': 'detailed_results',
        'faceit_url': 'faceit_url',
        'finished_at': 'finished_at',
        'game': 'game',
        'group': 'group',
        'match_id': 'match_id',
        'organizer_id': 'organizer_id',
        'region': 'region',
        'results': 'results',
        'round': 'round',
        'scheduled_at': 'scheduled_at',
        'started_at': 'started_at',
        'status': 'status',
        'teams': 'teams',
        'version': 'version',
        'voting': 'voting'
    }

    def __init__(self, best_of=None, broadcast_start_time=None, broadcast_start_time_label=None, calculate_elo=None, chat_room_id=None, competition_id=None, competition_name=None, competition_type=None, configured_at=None, demo_url=None, detailed_results=None, faceit_url=None, finished_at=None, game=None, group=None, match_id=None, organizer_id=None, region=None, results=None, round=None, scheduled_at=None, started_at=None, status=None, teams=None, version=None, voting=None, _configuration=None):  # noqa: E501
        """Match - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._best_of = None
        self._broadcast_start_time = None
        self._broadcast_start_time_label = None
        self._calculate_elo = None
        self._chat_room_id = None
        self._competition_id = None
        self._competition_name = None
        self._competition_type = None
        self._configured_at = None
        self._demo_url = None
        self._detailed_results = None
        self._faceit_url = None
        self._finished_at = None
        self._game = None
        self._group = None
        self._match_id = None
        self._organizer_id = None
        self._region = None
        self._results = None
        self._round = None
        self._scheduled_at = None
        self._started_at = None
        self._status = None
        self._teams = None
        self._version = None
        self._voting = None
        self.discriminator = None

        if best_of is not None:
            self.best_of = best_of
        if broadcast_start_time is not None:
            self.broadcast_start_time = broadcast_start_time
        if broadcast_start_time_label is not None:
            self.broadcast_start_time_label = broadcast_start_time_label
        if calculate_elo is not None:
            self.calculate_elo = calculate_elo
        if chat_room_id is not None:
            self.chat_room_id = chat_room_id
        if competition_id is not None:
            self.competition_id = competition_id
        if competition_name is not None:
            self.competition_name = competition_name
        if competition_type is not None:
            self.competition_type = competition_type
        if configured_at is not None:
            self.configured_at = configured_at
        if demo_url is not None:
            self.demo_url = demo_url
        if detailed_results is not None:
            self.detailed_results = detailed_results
        if faceit_url is not None:
            self.faceit_url = faceit_url
        if finished_at is not None:
            self.finished_at = finished_at
        if game is not None:
            self.game = game
        if group is not None:
            self.group = group
        if match_id is not None:
            self.match_id = match_id
        if organizer_id is not None:
            self.organizer_id = organizer_id
        if region is not None:
            self.region = region
        if results is not None:
            self.results = results
        if round is not None:
            self.round = round
        if scheduled_at is not None:
            self.scheduled_at = scheduled_at
        if started_at is not None:
            self.started_at = started_at
        if status is not None:
            self.status = status
        if teams is not None:
            self.teams = teams
        if version is not None:
            self.version = version
        if voting is not None:
            self.voting = voting

    @property
    def best_of(self):
        """Gets the best_of of this Match.  # noqa: E501


        :return: The best_of of this Match.  # noqa: E501
        :rtype: int
        """
        return self._best_of

    @best_of.setter
    def best_of(self, best_of):
        """Sets the best_of of this Match.


        :param best_of: The best_of of this Match.  # noqa: E501
        :type: int
        """

        self._best_of = best_of

    @property
    def broadcast_start_time(self):
        """Gets the broadcast_start_time of this Match.  # noqa: E501


        :return: The broadcast_start_time of this Match.  # noqa: E501
        :rtype: int
        """
        return self._broadcast_start_time

    @broadcast_start_time.setter
    def broadcast_start_time(self, broadcast_start_time):
        """Sets the broadcast_start_time of this Match.


        :param broadcast_start_time: The broadcast_start_time of this Match.  # noqa: E501
        :type: int
        """

        self._broadcast_start_time = broadcast_start_time

    @property
    def broadcast_start_time_label(self):
        """Gets the broadcast_start_time_label of this Match.  # noqa: E501


        :return: The broadcast_start_time_label of this Match.  # noqa: E501
        :rtype: str
        """
        return self._broadcast_start_time_label

    @broadcast_start_time_label.setter
    def broadcast_start_time_label(self, broadcast_start_time_label):
        """Sets the broadcast_start_time_label of this Match.


        :param broadcast_start_time_label: The broadcast_start_time_label of this Match.  # noqa: E501
        :type: str
        """

        self._broadcast_start_time_label = broadcast_start_time_label

    @property
    def calculate_elo(self):
        """Gets the calculate_elo of this Match.  # noqa: E501


        :return: The calculate_elo of this Match.  # noqa: E501
        :rtype: bool
        """
        return self._calculate_elo

    @calculate_elo.setter
    def calculate_elo(self, calculate_elo):
        """Sets the calculate_elo of this Match.


        :param calculate_elo: The calculate_elo of this Match.  # noqa: E501
        :type: bool
        """

        self._calculate_elo = calculate_elo

    @property
    def chat_room_id(self):
        """Gets the chat_room_id of this Match.  # noqa: E501


        :return: The chat_room_id of this Match.  # noqa: E501
        :rtype: str
        """
        return self._chat_room_id

    @chat_room_id.setter
    def chat_room_id(self, chat_room_id):
        """Sets the chat_room_id of this Match.


        :param chat_room_id: The chat_room_id of this Match.  # noqa: E501
        :type: str
        """

        self._chat_room_id = chat_room_id

    @property
    def competition_id(self):
        """Gets the competition_id of this Match.  # noqa: E501


        :return: The competition_id of this Match.  # noqa: E501
        :rtype: str
        """
        return self._competition_id

    @competition_id.setter
    def competition_id(self, competition_id):
        """Sets the competition_id of this Match.


        :param competition_id: The competition_id of this Match.  # noqa: E501
        :type: str
        """

        self._competition_id = competition_id

    @property
    def competition_name(self):
        """Gets the competition_name of this Match.  # noqa: E501


        :return: The competition_name of this Match.  # noqa: E501
        :rtype: str
        """
        return self._competition_name

    @competition_name.setter
    def competition_name(self, competition_name):
        """Sets the competition_name of this Match.


        :param competition_name: The competition_name of this Match.  # noqa: E501
        :type: str
        """

        self._competition_name = competition_name

    @property
    def competition_type(self):
        """Gets the competition_type of this Match.  # noqa: E501


        :return: The competition_type of this Match.  # noqa: E501
        :rtype: str
        """
        return self._competition_type

    @competition_type.setter
    def competition_type(self, competition_type):
        """Sets the competition_type of this Match.


        :param competition_type: The competition_type of this Match.  # noqa: E501
        :type: str
        """

        self._competition_type = competition_type

    @property
    def configured_at(self):
        """Gets the configured_at of this Match.  # noqa: E501


        :return: The configured_at of this Match.  # noqa: E501
        :rtype: int
        """
        return self._configured_at

    @configured_at.setter
    def configured_at(self, configured_at):
        """Sets the configured_at of this Match.


        :param configured_at: The configured_at of this Match.  # noqa: E501
        :type: int
        """

        self._configured_at = configured_at

    @property
    def demo_url(self):
        """Gets the demo_url of this Match.  # noqa: E501


        :return: The demo_url of this Match.  # noqa: E501
        :rtype: list[str]
        """
        return self._demo_url

    @demo_url.setter
    def demo_url(self, demo_url):
        """Sets the demo_url of this Match.


        :param demo_url: The demo_url of this Match.  # noqa: E501
        :type: list[str]
        """

        self._demo_url = demo_url

    @property
    def detailed_results(self):
        """Gets the detailed_results of this Match.  # noqa: E501


        :return: The detailed_results of this Match.  # noqa: E501
        :rtype: list[DetailedMatchResult]
        """
        return self._detailed_results

    @detailed_results.setter
    def detailed_results(self, detailed_results):
        """Sets the detailed_results of this Match.


        :param detailed_results: The detailed_results of this Match.  # noqa: E501
        :type: list[DetailedMatchResult]
        """

        self._detailed_results = detailed_results

    @property
    def faceit_url(self):
        """Gets the faceit_url of this Match.  # noqa: E501


        :return: The faceit_url of this Match.  # noqa: E501
        :rtype: str
        """
        return self._faceit_url

    @faceit_url.setter
    def faceit_url(self, faceit_url):
        """Sets the faceit_url of this Match.


        :param faceit_url: The faceit_url of this Match.  # noqa: E501
        :type: str
        """

        self._faceit_url = faceit_url

    @property
    def finished_at(self):
        """Gets the finished_at of this Match.  # noqa: E501


        :return: The finished_at of this Match.  # noqa: E501
        :rtype: int
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this Match.


        :param finished_at: The finished_at of this Match.  # noqa: E501
        :type: int
        """

        self._finished_at = finished_at

    @property
    def game(self):
        """Gets the game of this Match.  # noqa: E501


        :return: The game of this Match.  # noqa: E501
        :rtype: str
        """
        return self._game

    @game.setter
    def game(self, game):
        """Sets the game of this Match.


        :param game: The game of this Match.  # noqa: E501
        :type: str
        """

        self._game = game

    @property
    def group(self):
        """Gets the group of this Match.  # noqa: E501


        :return: The group of this Match.  # noqa: E501
        :rtype: int
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this Match.


        :param group: The group of this Match.  # noqa: E501
        :type: int
        """

        self._group = group

    @property
    def match_id(self):
        """Gets the match_id of this Match.  # noqa: E501


        :return: The match_id of this Match.  # noqa: E501
        :rtype: str
        """
        return self._match_id

    @match_id.setter
    def match_id(self, match_id):
        """Sets the match_id of this Match.


        :param match_id: The match_id of this Match.  # noqa: E501
        :type: str
        """

        self._match_id = match_id

    @property
    def organizer_id(self):
        """Gets the organizer_id of this Match.  # noqa: E501


        :return: The organizer_id of this Match.  # noqa: E501
        :rtype: str
        """
        return self._organizer_id

    @organizer_id.setter
    def organizer_id(self, organizer_id):
        """Sets the organizer_id of this Match.


        :param organizer_id: The organizer_id of this Match.  # noqa: E501
        :type: str
        """

        self._organizer_id = organizer_id

    @property
    def region(self):
        """Gets the region of this Match.  # noqa: E501


        :return: The region of this Match.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Match.


        :param region: The region of this Match.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def results(self):
        """Gets the results of this Match.  # noqa: E501


        :return: The results of this Match.  # noqa: E501
        :rtype: MatchResult
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this Match.


        :param results: The results of this Match.  # noqa: E501
        :type: MatchResult
        """

        self._results = results

    @property
    def round(self):
        """Gets the round of this Match.  # noqa: E501


        :return: The round of this Match.  # noqa: E501
        :rtype: int
        """
        return self._round

    @round.setter
    def round(self, round):
        """Sets the round of this Match.


        :param round: The round of this Match.  # noqa: E501
        :type: int
        """

        self._round = round

    @property
    def scheduled_at(self):
        """Gets the scheduled_at of this Match.  # noqa: E501


        :return: The scheduled_at of this Match.  # noqa: E501
        :rtype: int
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """Sets the scheduled_at of this Match.


        :param scheduled_at: The scheduled_at of this Match.  # noqa: E501
        :type: int
        """

        self._scheduled_at = scheduled_at

    @property
    def started_at(self):
        """Gets the started_at of this Match.  # noqa: E501


        :return: The started_at of this Match.  # noqa: E501
        :rtype: int
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this Match.


        :param started_at: The started_at of this Match.  # noqa: E501
        :type: int
        """

        self._started_at = started_at

    @property
    def status(self):
        """Gets the status of this Match.  # noqa: E501


        :return: The status of this Match.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Match.


        :param status: The status of this Match.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def teams(self):
        """Gets the teams of this Match.  # noqa: E501


        :return: The teams of this Match.  # noqa: E501
        :rtype: dict(str, Faction)
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this Match.


        :param teams: The teams of this Match.  # noqa: E501
        :type: dict(str, Faction)
        """

        self._teams = teams

    @property
    def version(self):
        """Gets the version of this Match.  # noqa: E501


        :return: The version of this Match.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Match.


        :param version: The version of this Match.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def voting(self):
        """Gets the voting of this Match.  # noqa: E501


        :return: The voting of this Match.  # noqa: E501
        :rtype: object
        """
        return self._voting

    @voting.setter
    def voting(self, voting):
        """Sets the voting of this Match.


        :param voting: The voting of this Match.  # noqa: E501
        :type: object
        """

        self._voting = voting

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
        if issubclass(Match, dict):
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
        if not isinstance(other, Match):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Match):
            return True

        return self.to_dict() != other.to_dict()

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


class Tournament(object):
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
        'anticheat_required': 'bool',
        'best_of': 'object',
        'calculate_elo': 'bool',
        'competition_id': 'str',
        'cover_image': 'str',
        'custom': 'bool',
        'description': 'str',
        'faceit_url': 'str',
        'featured_image': 'str',
        'game_data': 'Game',
        'game_id': 'str',
        'invite_type': 'str',
        'match_type': 'str',
        'max_skill': 'int',
        'membership_type': 'str',
        'min_skill': 'int',
        'name': 'str',
        'number_of_players': 'int',
        'number_of_players_checkedin': 'int',
        'number_of_players_joined': 'int',
        'number_of_players_participants': 'int',
        'organizer_data': 'Organizer',
        'organizer_id': 'str',
        'prize_type': 'str',
        'region': 'str',
        'rounds': 'list[object]',
        'rule': 'str',
        'started_at': 'int',
        'status': 'str',
        'substitutes_allowed': 'int',
        'substitutions_allowed': 'int',
        'team_size': 'int',
        'total_prize': 'object',
        'tournament_id': 'str',
        'voting': 'object',
        'whitelist_countries': 'list[str]'
    }

    attribute_map = {
        'anticheat_required': 'anticheat_required',
        'best_of': 'best_of',
        'calculate_elo': 'calculate_elo',
        'competition_id': 'competition_id',
        'cover_image': 'cover_image',
        'custom': 'custom',
        'description': 'description',
        'faceit_url': 'faceit_url',
        'featured_image': 'featured_image',
        'game_data': 'game_data',
        'game_id': 'game_id',
        'invite_type': 'invite_type',
        'match_type': 'match_type',
        'max_skill': 'max_skill',
        'membership_type': 'membership_type',
        'min_skill': 'min_skill',
        'name': 'name',
        'number_of_players': 'number_of_players',
        'number_of_players_checkedin': 'number_of_players_checkedin',
        'number_of_players_joined': 'number_of_players_joined',
        'number_of_players_participants': 'number_of_players_participants',
        'organizer_data': 'organizer_data',
        'organizer_id': 'organizer_id',
        'prize_type': 'prize_type',
        'region': 'region',
        'rounds': 'rounds',
        'rule': 'rule',
        'started_at': 'started_at',
        'status': 'status',
        'substitutes_allowed': 'substitutes_allowed',
        'substitutions_allowed': 'substitutions_allowed',
        'team_size': 'team_size',
        'total_prize': 'total_prize',
        'tournament_id': 'tournament_id',
        'voting': 'voting',
        'whitelist_countries': 'whitelist_countries'
    }

    def __init__(self, anticheat_required=None, best_of=None, calculate_elo=None, competition_id=None, cover_image=None, custom=None, description=None, faceit_url=None, featured_image=None, game_data=None, game_id=None, invite_type=None, match_type=None, max_skill=None, membership_type=None, min_skill=None, name=None, number_of_players=None, number_of_players_checkedin=None, number_of_players_joined=None, number_of_players_participants=None, organizer_data=None, organizer_id=None, prize_type=None, region=None, rounds=None, rule=None, started_at=None, status=None, substitutes_allowed=None, substitutions_allowed=None, team_size=None, total_prize=None, tournament_id=None, voting=None, whitelist_countries=None, _configuration=None):  # noqa: E501
        """Tournament - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._anticheat_required = None
        self._best_of = None
        self._calculate_elo = None
        self._competition_id = None
        self._cover_image = None
        self._custom = None
        self._description = None
        self._faceit_url = None
        self._featured_image = None
        self._game_data = None
        self._game_id = None
        self._invite_type = None
        self._match_type = None
        self._max_skill = None
        self._membership_type = None
        self._min_skill = None
        self._name = None
        self._number_of_players = None
        self._number_of_players_checkedin = None
        self._number_of_players_joined = None
        self._number_of_players_participants = None
        self._organizer_data = None
        self._organizer_id = None
        self._prize_type = None
        self._region = None
        self._rounds = None
        self._rule = None
        self._started_at = None
        self._status = None
        self._substitutes_allowed = None
        self._substitutions_allowed = None
        self._team_size = None
        self._total_prize = None
        self._tournament_id = None
        self._voting = None
        self._whitelist_countries = None
        self.discriminator = None

        if anticheat_required is not None:
            self.anticheat_required = anticheat_required
        if best_of is not None:
            self.best_of = best_of
        if calculate_elo is not None:
            self.calculate_elo = calculate_elo
        if competition_id is not None:
            self.competition_id = competition_id
        if cover_image is not None:
            self.cover_image = cover_image
        if custom is not None:
            self.custom = custom
        if description is not None:
            self.description = description
        if faceit_url is not None:
            self.faceit_url = faceit_url
        if featured_image is not None:
            self.featured_image = featured_image
        if game_data is not None:
            self.game_data = game_data
        if game_id is not None:
            self.game_id = game_id
        if invite_type is not None:
            self.invite_type = invite_type
        if match_type is not None:
            self.match_type = match_type
        if max_skill is not None:
            self.max_skill = max_skill
        if membership_type is not None:
            self.membership_type = membership_type
        if min_skill is not None:
            self.min_skill = min_skill
        if name is not None:
            self.name = name
        if number_of_players is not None:
            self.number_of_players = number_of_players
        if number_of_players_checkedin is not None:
            self.number_of_players_checkedin = number_of_players_checkedin
        if number_of_players_joined is not None:
            self.number_of_players_joined = number_of_players_joined
        if number_of_players_participants is not None:
            self.number_of_players_participants = number_of_players_participants
        if organizer_data is not None:
            self.organizer_data = organizer_data
        if organizer_id is not None:
            self.organizer_id = organizer_id
        if prize_type is not None:
            self.prize_type = prize_type
        if region is not None:
            self.region = region
        if rounds is not None:
            self.rounds = rounds
        if rule is not None:
            self.rule = rule
        if started_at is not None:
            self.started_at = started_at
        if status is not None:
            self.status = status
        if substitutes_allowed is not None:
            self.substitutes_allowed = substitutes_allowed
        if substitutions_allowed is not None:
            self.substitutions_allowed = substitutions_allowed
        if team_size is not None:
            self.team_size = team_size
        if total_prize is not None:
            self.total_prize = total_prize
        if tournament_id is not None:
            self.tournament_id = tournament_id
        if voting is not None:
            self.voting = voting
        if whitelist_countries is not None:
            self.whitelist_countries = whitelist_countries

    @property
    def anticheat_required(self):
        """Gets the anticheat_required of this Tournament.  # noqa: E501


        :return: The anticheat_required of this Tournament.  # noqa: E501
        :rtype: bool
        """
        return self._anticheat_required

    @anticheat_required.setter
    def anticheat_required(self, anticheat_required):
        """Sets the anticheat_required of this Tournament.


        :param anticheat_required: The anticheat_required of this Tournament.  # noqa: E501
        :type: bool
        """

        self._anticheat_required = anticheat_required

    @property
    def best_of(self):
        """Gets the best_of of this Tournament.  # noqa: E501


        :return: The best_of of this Tournament.  # noqa: E501
        :rtype: object
        """
        return self._best_of

    @best_of.setter
    def best_of(self, best_of):
        """Sets the best_of of this Tournament.


        :param best_of: The best_of of this Tournament.  # noqa: E501
        :type: object
        """

        self._best_of = best_of

    @property
    def calculate_elo(self):
        """Gets the calculate_elo of this Tournament.  # noqa: E501


        :return: The calculate_elo of this Tournament.  # noqa: E501
        :rtype: bool
        """
        return self._calculate_elo

    @calculate_elo.setter
    def calculate_elo(self, calculate_elo):
        """Sets the calculate_elo of this Tournament.


        :param calculate_elo: The calculate_elo of this Tournament.  # noqa: E501
        :type: bool
        """

        self._calculate_elo = calculate_elo

    @property
    def competition_id(self):
        """Gets the competition_id of this Tournament.  # noqa: E501

        DEPRECATED: use tournament_id instead  # noqa: E501

        :return: The competition_id of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._competition_id

    @competition_id.setter
    def competition_id(self, competition_id):
        """Sets the competition_id of this Tournament.

        DEPRECATED: use tournament_id instead  # noqa: E501

        :param competition_id: The competition_id of this Tournament.  # noqa: E501
        :type: str
        """

        self._competition_id = competition_id

    @property
    def cover_image(self):
        """Gets the cover_image of this Tournament.  # noqa: E501


        :return: The cover_image of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._cover_image

    @cover_image.setter
    def cover_image(self, cover_image):
        """Sets the cover_image of this Tournament.


        :param cover_image: The cover_image of this Tournament.  # noqa: E501
        :type: str
        """

        self._cover_image = cover_image

    @property
    def custom(self):
        """Gets the custom of this Tournament.  # noqa: E501


        :return: The custom of this Tournament.  # noqa: E501
        :rtype: bool
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this Tournament.


        :param custom: The custom of this Tournament.  # noqa: E501
        :type: bool
        """

        self._custom = custom

    @property
    def description(self):
        """Gets the description of this Tournament.  # noqa: E501


        :return: The description of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Tournament.


        :param description: The description of this Tournament.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def faceit_url(self):
        """Gets the faceit_url of this Tournament.  # noqa: E501


        :return: The faceit_url of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._faceit_url

    @faceit_url.setter
    def faceit_url(self, faceit_url):
        """Sets the faceit_url of this Tournament.


        :param faceit_url: The faceit_url of this Tournament.  # noqa: E501
        :type: str
        """

        self._faceit_url = faceit_url

    @property
    def featured_image(self):
        """Gets the featured_image of this Tournament.  # noqa: E501


        :return: The featured_image of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._featured_image

    @featured_image.setter
    def featured_image(self, featured_image):
        """Sets the featured_image of this Tournament.


        :param featured_image: The featured_image of this Tournament.  # noqa: E501
        :type: str
        """

        self._featured_image = featured_image

    @property
    def game_data(self):
        """Gets the game_data of this Tournament.  # noqa: E501


        :return: The game_data of this Tournament.  # noqa: E501
        :rtype: Game
        """
        return self._game_data

    @game_data.setter
    def game_data(self, game_data):
        """Sets the game_data of this Tournament.


        :param game_data: The game_data of this Tournament.  # noqa: E501
        :type: Game
        """

        self._game_data = game_data

    @property
    def game_id(self):
        """Gets the game_id of this Tournament.  # noqa: E501


        :return: The game_id of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this Tournament.


        :param game_id: The game_id of this Tournament.  # noqa: E501
        :type: str
        """

        self._game_id = game_id

    @property
    def invite_type(self):
        """Gets the invite_type of this Tournament.  # noqa: E501


        :return: The invite_type of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._invite_type

    @invite_type.setter
    def invite_type(self, invite_type):
        """Sets the invite_type of this Tournament.


        :param invite_type: The invite_type of this Tournament.  # noqa: E501
        :type: str
        """

        self._invite_type = invite_type

    @property
    def match_type(self):
        """Gets the match_type of this Tournament.  # noqa: E501


        :return: The match_type of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this Tournament.


        :param match_type: The match_type of this Tournament.  # noqa: E501
        :type: str
        """

        self._match_type = match_type

    @property
    def max_skill(self):
        """Gets the max_skill of this Tournament.  # noqa: E501


        :return: The max_skill of this Tournament.  # noqa: E501
        :rtype: int
        """
        return self._max_skill

    @max_skill.setter
    def max_skill(self, max_skill):
        """Sets the max_skill of this Tournament.


        :param max_skill: The max_skill of this Tournament.  # noqa: E501
        :type: int
        """

        self._max_skill = max_skill

    @property
    def membership_type(self):
        """Gets the membership_type of this Tournament.  # noqa: E501


        :return: The membership_type of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._membership_type

    @membership_type.setter
    def membership_type(self, membership_type):
        """Sets the membership_type of this Tournament.


        :param membership_type: The membership_type of this Tournament.  # noqa: E501
        :type: str
        """

        self._membership_type = membership_type

    @property
    def min_skill(self):
        """Gets the min_skill of this Tournament.  # noqa: E501


        :return: The min_skill of this Tournament.  # noqa: E501
        :rtype: int
        """
        return self._min_skill

    @min_skill.setter
    def min_skill(self, min_skill):
        """Sets the min_skill of this Tournament.


        :param min_skill: The min_skill of this Tournament.  # noqa: E501
        :type: int
        """

        self._min_skill = min_skill

    @property
    def name(self):
        """Gets the name of this Tournament.  # noqa: E501


        :return: The name of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tournament.


        :param name: The name of this Tournament.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number_of_players(self):
        """Gets the number_of_players of this Tournament.  # noqa: E501


        :return: The number_of_players of this Tournament.  # noqa: E501
        :rtype: int
        """
        return self._number_of_players

    @number_of_players.setter
    def number_of_players(self, number_of_players):
        """Sets the number_of_players of this Tournament.


        :param number_of_players: The number_of_players of this Tournament.  # noqa: E501
        :type: int
        """

        self._number_of_players = number_of_players

    @property
    def number_of_players_checkedin(self):
        """Gets the number_of_players_checkedin of this Tournament.  # noqa: E501


        :return: The number_of_players_checkedin of this Tournament.  # noqa: E501
        :rtype: int
        """
        return self._number_of_players_checkedin

    @number_of_players_checkedin.setter
    def number_of_players_checkedin(self, number_of_players_checkedin):
        """Sets the number_of_players_checkedin of this Tournament.


        :param number_of_players_checkedin: The number_of_players_checkedin of this Tournament.  # noqa: E501
        :type: int
        """

        self._number_of_players_checkedin = number_of_players_checkedin

    @property
    def number_of_players_joined(self):
        """Gets the number_of_players_joined of this Tournament.  # noqa: E501


        :return: The number_of_players_joined of this Tournament.  # noqa: E501
        :rtype: int
        """
        return self._number_of_players_joined

    @number_of_players_joined.setter
    def number_of_players_joined(self, number_of_players_joined):
        """Sets the number_of_players_joined of this Tournament.


        :param number_of_players_joined: The number_of_players_joined of this Tournament.  # noqa: E501
        :type: int
        """

        self._number_of_players_joined = number_of_players_joined

    @property
    def number_of_players_participants(self):
        """Gets the number_of_players_participants of this Tournament.  # noqa: E501


        :return: The number_of_players_participants of this Tournament.  # noqa: E501
        :rtype: int
        """
        return self._number_of_players_participants

    @number_of_players_participants.setter
    def number_of_players_participants(self, number_of_players_participants):
        """Sets the number_of_players_participants of this Tournament.


        :param number_of_players_participants: The number_of_players_participants of this Tournament.  # noqa: E501
        :type: int
        """

        self._number_of_players_participants = number_of_players_participants

    @property
    def organizer_data(self):
        """Gets the organizer_data of this Tournament.  # noqa: E501


        :return: The organizer_data of this Tournament.  # noqa: E501
        :rtype: Organizer
        """
        return self._organizer_data

    @organizer_data.setter
    def organizer_data(self, organizer_data):
        """Sets the organizer_data of this Tournament.


        :param organizer_data: The organizer_data of this Tournament.  # noqa: E501
        :type: Organizer
        """

        self._organizer_data = organizer_data

    @property
    def organizer_id(self):
        """Gets the organizer_id of this Tournament.  # noqa: E501


        :return: The organizer_id of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._organizer_id

    @organizer_id.setter
    def organizer_id(self, organizer_id):
        """Sets the organizer_id of this Tournament.


        :param organizer_id: The organizer_id of this Tournament.  # noqa: E501
        :type: str
        """

        self._organizer_id = organizer_id

    @property
    def prize_type(self):
        """Gets the prize_type of this Tournament.  # noqa: E501


        :return: The prize_type of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._prize_type

    @prize_type.setter
    def prize_type(self, prize_type):
        """Sets the prize_type of this Tournament.


        :param prize_type: The prize_type of this Tournament.  # noqa: E501
        :type: str
        """

        self._prize_type = prize_type

    @property
    def region(self):
        """Gets the region of this Tournament.  # noqa: E501


        :return: The region of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Tournament.


        :param region: The region of this Tournament.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def rounds(self):
        """Gets the rounds of this Tournament.  # noqa: E501


        :return: The rounds of this Tournament.  # noqa: E501
        :rtype: list[object]
        """
        return self._rounds

    @rounds.setter
    def rounds(self, rounds):
        """Sets the rounds of this Tournament.


        :param rounds: The rounds of this Tournament.  # noqa: E501
        :type: list[object]
        """

        self._rounds = rounds

    @property
    def rule(self):
        """Gets the rule of this Tournament.  # noqa: E501


        :return: The rule of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this Tournament.


        :param rule: The rule of this Tournament.  # noqa: E501
        :type: str
        """

        self._rule = rule

    @property
    def started_at(self):
        """Gets the started_at of this Tournament.  # noqa: E501


        :return: The started_at of this Tournament.  # noqa: E501
        :rtype: int
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this Tournament.


        :param started_at: The started_at of this Tournament.  # noqa: E501
        :type: int
        """

        self._started_at = started_at

    @property
    def status(self):
        """Gets the status of this Tournament.  # noqa: E501


        :return: The status of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Tournament.


        :param status: The status of this Tournament.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def substitutes_allowed(self):
        """Gets the substitutes_allowed of this Tournament.  # noqa: E501


        :return: The substitutes_allowed of this Tournament.  # noqa: E501
        :rtype: int
        """
        return self._substitutes_allowed

    @substitutes_allowed.setter
    def substitutes_allowed(self, substitutes_allowed):
        """Sets the substitutes_allowed of this Tournament.


        :param substitutes_allowed: The substitutes_allowed of this Tournament.  # noqa: E501
        :type: int
        """

        self._substitutes_allowed = substitutes_allowed

    @property
    def substitutions_allowed(self):
        """Gets the substitutions_allowed of this Tournament.  # noqa: E501


        :return: The substitutions_allowed of this Tournament.  # noqa: E501
        :rtype: int
        """
        return self._substitutions_allowed

    @substitutions_allowed.setter
    def substitutions_allowed(self, substitutions_allowed):
        """Sets the substitutions_allowed of this Tournament.


        :param substitutions_allowed: The substitutions_allowed of this Tournament.  # noqa: E501
        :type: int
        """

        self._substitutions_allowed = substitutions_allowed

    @property
    def team_size(self):
        """Gets the team_size of this Tournament.  # noqa: E501


        :return: The team_size of this Tournament.  # noqa: E501
        :rtype: int
        """
        return self._team_size

    @team_size.setter
    def team_size(self, team_size):
        """Sets the team_size of this Tournament.


        :param team_size: The team_size of this Tournament.  # noqa: E501
        :type: int
        """

        self._team_size = team_size

    @property
    def total_prize(self):
        """Gets the total_prize of this Tournament.  # noqa: E501


        :return: The total_prize of this Tournament.  # noqa: E501
        :rtype: object
        """
        return self._total_prize

    @total_prize.setter
    def total_prize(self, total_prize):
        """Sets the total_prize of this Tournament.


        :param total_prize: The total_prize of this Tournament.  # noqa: E501
        :type: object
        """

        self._total_prize = total_prize

    @property
    def tournament_id(self):
        """Gets the tournament_id of this Tournament.  # noqa: E501


        :return: The tournament_id of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._tournament_id

    @tournament_id.setter
    def tournament_id(self, tournament_id):
        """Sets the tournament_id of this Tournament.


        :param tournament_id: The tournament_id of this Tournament.  # noqa: E501
        :type: str
        """

        self._tournament_id = tournament_id

    @property
    def voting(self):
        """Gets the voting of this Tournament.  # noqa: E501


        :return: The voting of this Tournament.  # noqa: E501
        :rtype: object
        """
        return self._voting

    @voting.setter
    def voting(self, voting):
        """Sets the voting of this Tournament.


        :param voting: The voting of this Tournament.  # noqa: E501
        :type: object
        """

        self._voting = voting

    @property
    def whitelist_countries(self):
        """Gets the whitelist_countries of this Tournament.  # noqa: E501


        :return: The whitelist_countries of this Tournament.  # noqa: E501
        :rtype: list[str]
        """
        return self._whitelist_countries

    @whitelist_countries.setter
    def whitelist_countries(self, whitelist_countries):
        """Sets the whitelist_countries of this Tournament.


        :param whitelist_countries: The whitelist_countries of this Tournament.  # noqa: E501
        :type: list[str]
        """

        self._whitelist_countries = whitelist_countries

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
        if issubclass(Tournament, dict):
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
        if not isinstance(other, Tournament):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Tournament):
            return True

        return self.to_dict() != other.to_dict()
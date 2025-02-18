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


class BracketsRound(object):
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
        'label': 'str',
        'matches': 'int',
        'round': 'int',
        'start_time': 'int',
        'starts_asap': 'bool',
        'substitution_time': 'int',
        'substitutions_allowed': 'bool'
    }

    attribute_map = {
        'best_of': 'best_of',
        'label': 'label',
        'matches': 'matches',
        'round': 'round',
        'start_time': 'start_time',
        'starts_asap': 'starts_asap',
        'substitution_time': 'substitution_time',
        'substitutions_allowed': 'substitutions_allowed'
    }

    def __init__(self, best_of=None, label=None, matches=None, round=None, start_time=None, starts_asap=None, substitution_time=None, substitutions_allowed=None, _configuration=None):  # noqa: E501
        """BracketsRound - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._best_of = None
        self._label = None
        self._matches = None
        self._round = None
        self._start_time = None
        self._starts_asap = None
        self._substitution_time = None
        self._substitutions_allowed = None
        self.discriminator = None

        if best_of is not None:
            self.best_of = best_of
        if label is not None:
            self.label = label
        if matches is not None:
            self.matches = matches
        if round is not None:
            self.round = round
        if start_time is not None:
            self.start_time = start_time
        if starts_asap is not None:
            self.starts_asap = starts_asap
        if substitution_time is not None:
            self.substitution_time = substitution_time
        if substitutions_allowed is not None:
            self.substitutions_allowed = substitutions_allowed

    @property
    def best_of(self):
        """Gets the best_of of this BracketsRound.  # noqa: E501


        :return: The best_of of this BracketsRound.  # noqa: E501
        :rtype: int
        """
        return self._best_of

    @best_of.setter
    def best_of(self, best_of):
        """Sets the best_of of this BracketsRound.


        :param best_of: The best_of of this BracketsRound.  # noqa: E501
        :type: int
        """

        self._best_of = best_of

    @property
    def label(self):
        """Gets the label of this BracketsRound.  # noqa: E501


        :return: The label of this BracketsRound.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this BracketsRound.


        :param label: The label of this BracketsRound.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def matches(self):
        """Gets the matches of this BracketsRound.  # noqa: E501


        :return: The matches of this BracketsRound.  # noqa: E501
        :rtype: int
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this BracketsRound.


        :param matches: The matches of this BracketsRound.  # noqa: E501
        :type: int
        """

        self._matches = matches

    @property
    def round(self):
        """Gets the round of this BracketsRound.  # noqa: E501


        :return: The round of this BracketsRound.  # noqa: E501
        :rtype: int
        """
        return self._round

    @round.setter
    def round(self, round):
        """Sets the round of this BracketsRound.


        :param round: The round of this BracketsRound.  # noqa: E501
        :type: int
        """

        self._round = round

    @property
    def start_time(self):
        """Gets the start_time of this BracketsRound.  # noqa: E501


        :return: The start_time of this BracketsRound.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this BracketsRound.


        :param start_time: The start_time of this BracketsRound.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def starts_asap(self):
        """Gets the starts_asap of this BracketsRound.  # noqa: E501


        :return: The starts_asap of this BracketsRound.  # noqa: E501
        :rtype: bool
        """
        return self._starts_asap

    @starts_asap.setter
    def starts_asap(self, starts_asap):
        """Sets the starts_asap of this BracketsRound.


        :param starts_asap: The starts_asap of this BracketsRound.  # noqa: E501
        :type: bool
        """

        self._starts_asap = starts_asap

    @property
    def substitution_time(self):
        """Gets the substitution_time of this BracketsRound.  # noqa: E501


        :return: The substitution_time of this BracketsRound.  # noqa: E501
        :rtype: int
        """
        return self._substitution_time

    @substitution_time.setter
    def substitution_time(self, substitution_time):
        """Sets the substitution_time of this BracketsRound.


        :param substitution_time: The substitution_time of this BracketsRound.  # noqa: E501
        :type: int
        """

        self._substitution_time = substitution_time

    @property
    def substitutions_allowed(self):
        """Gets the substitutions_allowed of this BracketsRound.  # noqa: E501


        :return: The substitutions_allowed of this BracketsRound.  # noqa: E501
        :rtype: bool
        """
        return self._substitutions_allowed

    @substitutions_allowed.setter
    def substitutions_allowed(self, substitutions_allowed):
        """Sets the substitutions_allowed of this BracketsRound.


        :param substitutions_allowed: The substitutions_allowed of this BracketsRound.  # noqa: E501
        :type: bool
        """

        self._substitutions_allowed = substitutions_allowed

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
        if issubclass(BracketsRound, dict):
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
        if not isinstance(other, BracketsRound):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BracketsRound):
            return True

        return self.to_dict() != other.to_dict()

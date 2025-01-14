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


class ChampionshipSchedule(object):
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
        '_date': 'int',
        'status': 'str'
    }

    attribute_map = {
        '_date': 'date',
        'status': 'status'
    }

    def __init__(self, _date=None, status=None, _configuration=None):  # noqa: E501
        """ChampionshipSchedule - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__date = None
        self._status = None
        self.discriminator = None

        if _date is not None:
            self._date = _date
        if status is not None:
            self.status = status

    @property
    def _date(self):
        """Gets the _date of this ChampionshipSchedule.  # noqa: E501


        :return: The _date of this ChampionshipSchedule.  # noqa: E501
        :rtype: int
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ChampionshipSchedule.


        :param _date: The _date of this ChampionshipSchedule.  # noqa: E501
        :type: int
        """

        self.__date = _date

    @property
    def status(self):
        """Gets the status of this ChampionshipSchedule.  # noqa: E501


        :return: The status of this ChampionshipSchedule.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ChampionshipSchedule.


        :param status: The status of this ChampionshipSchedule.  # noqa: E501
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
        if issubclass(ChampionshipSchedule, dict):
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
        if not isinstance(other, ChampionshipSchedule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChampionshipSchedule):
            return True

        return self.to_dict() != other.to_dict()

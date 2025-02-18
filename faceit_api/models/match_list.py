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


class MatchList(object):
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
        'end': 'int',
        'items': 'list[Match]',
        'start': 'int'
    }

    attribute_map = {
        'end': 'end',
        'items': 'items',
        'start': 'start'
    }

    def __init__(self, end=None, items=None, start=None, _configuration=None):  # noqa: E501
        """MatchList - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._end = None
        self._items = None
        self._start = None
        self.discriminator = None

        if end is not None:
            self.end = end
        if items is not None:
            self.items = items
        if start is not None:
            self.start = start

    @property
    def end(self):
        """Gets the end of this MatchList.  # noqa: E501


        :return: The end of this MatchList.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this MatchList.


        :param end: The end of this MatchList.  # noqa: E501
        :type: int
        """

        self._end = end

    @property
    def items(self):
        """Gets the items of this MatchList.  # noqa: E501


        :return: The items of this MatchList.  # noqa: E501
        :rtype: list[Match]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this MatchList.


        :param items: The items of this MatchList.  # noqa: E501
        :type: list[Match]
        """

        self._items = items

    @property
    def start(self):
        """Gets the start of this MatchList.  # noqa: E501


        :return: The start of this MatchList.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this MatchList.


        :param start: The start of this MatchList.  # noqa: E501
        :type: int
        """

        self._start = start

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
        if issubclass(MatchList, dict):
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
        if not isinstance(other, MatchList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MatchList):
            return True

        return self.to_dict() != other.to_dict()

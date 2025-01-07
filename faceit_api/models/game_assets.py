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


class GameAssets(object):
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
        'cover': 'str',
        'featured_img_l': 'str',
        'featured_img_m': 'str',
        'featured_img_s': 'str',
        'flag_img_icon': 'str',
        'flag_img_l': 'str',
        'flag_img_m': 'str',
        'flag_img_s': 'str',
        'landing_page': 'str'
    }

    attribute_map = {
        'cover': 'cover',
        'featured_img_l': 'featured_img_l',
        'featured_img_m': 'featured_img_m',
        'featured_img_s': 'featured_img_s',
        'flag_img_icon': 'flag_img_icon',
        'flag_img_l': 'flag_img_l',
        'flag_img_m': 'flag_img_m',
        'flag_img_s': 'flag_img_s',
        'landing_page': 'landing_page'
    }

    def __init__(self, cover=None, featured_img_l=None, featured_img_m=None, featured_img_s=None, flag_img_icon=None, flag_img_l=None, flag_img_m=None, flag_img_s=None, landing_page=None, _configuration=None):  # noqa: E501
        """GameAssets - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cover = None
        self._featured_img_l = None
        self._featured_img_m = None
        self._featured_img_s = None
        self._flag_img_icon = None
        self._flag_img_l = None
        self._flag_img_m = None
        self._flag_img_s = None
        self._landing_page = None
        self.discriminator = None

        if cover is not None:
            self.cover = cover
        if featured_img_l is not None:
            self.featured_img_l = featured_img_l
        if featured_img_m is not None:
            self.featured_img_m = featured_img_m
        if featured_img_s is not None:
            self.featured_img_s = featured_img_s
        if flag_img_icon is not None:
            self.flag_img_icon = flag_img_icon
        if flag_img_l is not None:
            self.flag_img_l = flag_img_l
        if flag_img_m is not None:
            self.flag_img_m = flag_img_m
        if flag_img_s is not None:
            self.flag_img_s = flag_img_s
        if landing_page is not None:
            self.landing_page = landing_page

    @property
    def cover(self):
        """Gets the cover of this GameAssets.  # noqa: E501


        :return: The cover of this GameAssets.  # noqa: E501
        :rtype: str
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        """Sets the cover of this GameAssets.


        :param cover: The cover of this GameAssets.  # noqa: E501
        :type: str
        """

        self._cover = cover

    @property
    def featured_img_l(self):
        """Gets the featured_img_l of this GameAssets.  # noqa: E501


        :return: The featured_img_l of this GameAssets.  # noqa: E501
        :rtype: str
        """
        return self._featured_img_l

    @featured_img_l.setter
    def featured_img_l(self, featured_img_l):
        """Sets the featured_img_l of this GameAssets.


        :param featured_img_l: The featured_img_l of this GameAssets.  # noqa: E501
        :type: str
        """

        self._featured_img_l = featured_img_l

    @property
    def featured_img_m(self):
        """Gets the featured_img_m of this GameAssets.  # noqa: E501


        :return: The featured_img_m of this GameAssets.  # noqa: E501
        :rtype: str
        """
        return self._featured_img_m

    @featured_img_m.setter
    def featured_img_m(self, featured_img_m):
        """Sets the featured_img_m of this GameAssets.


        :param featured_img_m: The featured_img_m of this GameAssets.  # noqa: E501
        :type: str
        """

        self._featured_img_m = featured_img_m

    @property
    def featured_img_s(self):
        """Gets the featured_img_s of this GameAssets.  # noqa: E501


        :return: The featured_img_s of this GameAssets.  # noqa: E501
        :rtype: str
        """
        return self._featured_img_s

    @featured_img_s.setter
    def featured_img_s(self, featured_img_s):
        """Sets the featured_img_s of this GameAssets.


        :param featured_img_s: The featured_img_s of this GameAssets.  # noqa: E501
        :type: str
        """

        self._featured_img_s = featured_img_s

    @property
    def flag_img_icon(self):
        """Gets the flag_img_icon of this GameAssets.  # noqa: E501


        :return: The flag_img_icon of this GameAssets.  # noqa: E501
        :rtype: str
        """
        return self._flag_img_icon

    @flag_img_icon.setter
    def flag_img_icon(self, flag_img_icon):
        """Sets the flag_img_icon of this GameAssets.


        :param flag_img_icon: The flag_img_icon of this GameAssets.  # noqa: E501
        :type: str
        """

        self._flag_img_icon = flag_img_icon

    @property
    def flag_img_l(self):
        """Gets the flag_img_l of this GameAssets.  # noqa: E501


        :return: The flag_img_l of this GameAssets.  # noqa: E501
        :rtype: str
        """
        return self._flag_img_l

    @flag_img_l.setter
    def flag_img_l(self, flag_img_l):
        """Sets the flag_img_l of this GameAssets.


        :param flag_img_l: The flag_img_l of this GameAssets.  # noqa: E501
        :type: str
        """

        self._flag_img_l = flag_img_l

    @property
    def flag_img_m(self):
        """Gets the flag_img_m of this GameAssets.  # noqa: E501


        :return: The flag_img_m of this GameAssets.  # noqa: E501
        :rtype: str
        """
        return self._flag_img_m

    @flag_img_m.setter
    def flag_img_m(self, flag_img_m):
        """Sets the flag_img_m of this GameAssets.


        :param flag_img_m: The flag_img_m of this GameAssets.  # noqa: E501
        :type: str
        """

        self._flag_img_m = flag_img_m

    @property
    def flag_img_s(self):
        """Gets the flag_img_s of this GameAssets.  # noqa: E501


        :return: The flag_img_s of this GameAssets.  # noqa: E501
        :rtype: str
        """
        return self._flag_img_s

    @flag_img_s.setter
    def flag_img_s(self, flag_img_s):
        """Sets the flag_img_s of this GameAssets.


        :param flag_img_s: The flag_img_s of this GameAssets.  # noqa: E501
        :type: str
        """

        self._flag_img_s = flag_img_s

    @property
    def landing_page(self):
        """Gets the landing_page of this GameAssets.  # noqa: E501


        :return: The landing_page of this GameAssets.  # noqa: E501
        :rtype: str
        """
        return self._landing_page

    @landing_page.setter
    def landing_page(self, landing_page):
        """Sets the landing_page of this GameAssets.


        :param landing_page: The landing_page of this GameAssets.  # noqa: E501
        :type: str
        """

        self._landing_page = landing_page

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
        if issubclass(GameAssets, dict):
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
        if not isinstance(other, GameAssets):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GameAssets):
            return True

        return self.to_dict() != other.to_dict()
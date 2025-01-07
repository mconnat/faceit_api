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


class PluginSettings(object):
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
        'args': 'list[str]',
        'devices': 'list[PluginDevice]',
        'env': 'list[str]',
        'mounts': 'list[PluginMount]'
    }

    attribute_map = {
        'args': 'Args',
        'devices': 'Devices',
        'env': 'Env',
        'mounts': 'Mounts'
    }

    def __init__(self, args=None, devices=None, env=None, mounts=None, _configuration=None):  # noqa: E501
        """PluginSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._args = None
        self._devices = None
        self._env = None
        self._mounts = None
        self.discriminator = None

        self.args = args
        self.devices = devices
        self.env = env
        self.mounts = mounts

    @property
    def args(self):
        """Gets the args of this PluginSettings.  # noqa: E501

        args  # noqa: E501

        :return: The args of this PluginSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this PluginSettings.

        args  # noqa: E501

        :param args: The args of this PluginSettings.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and args is None:
            raise ValueError("Invalid value for `args`, must not be `None`")  # noqa: E501

        self._args = args

    @property
    def devices(self):
        """Gets the devices of this PluginSettings.  # noqa: E501

        devices  # noqa: E501

        :return: The devices of this PluginSettings.  # noqa: E501
        :rtype: list[PluginDevice]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this PluginSettings.

        devices  # noqa: E501

        :param devices: The devices of this PluginSettings.  # noqa: E501
        :type: list[PluginDevice]
        """
        if self._configuration.client_side_validation and devices is None:
            raise ValueError("Invalid value for `devices`, must not be `None`")  # noqa: E501

        self._devices = devices

    @property
    def env(self):
        """Gets the env of this PluginSettings.  # noqa: E501

        env  # noqa: E501

        :return: The env of this PluginSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this PluginSettings.

        env  # noqa: E501

        :param env: The env of this PluginSettings.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and env is None:
            raise ValueError("Invalid value for `env`, must not be `None`")  # noqa: E501

        self._env = env

    @property
    def mounts(self):
        """Gets the mounts of this PluginSettings.  # noqa: E501

        mounts  # noqa: E501

        :return: The mounts of this PluginSettings.  # noqa: E501
        :rtype: list[PluginMount]
        """
        return self._mounts

    @mounts.setter
    def mounts(self, mounts):
        """Sets the mounts of this PluginSettings.

        mounts  # noqa: E501

        :param mounts: The mounts of this PluginSettings.  # noqa: E501
        :type: list[PluginMount]
        """
        if self._configuration.client_side_validation and mounts is None:
            raise ValueError("Invalid value for `mounts`, must not be `None`")  # noqa: E501

        self._mounts = mounts

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
        if issubclass(PluginSettings, dict):
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
        if not isinstance(other, PluginSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PluginSettings):
            return True

        return self.to_dict() != other.to_dict()
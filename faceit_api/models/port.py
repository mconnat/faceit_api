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


class Port(object):
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
        'ip': 'str',
        'private_port': 'int',
        'public_port': 'int',
        'type': 'str'
    }

    attribute_map = {
        'ip': 'IP',
        'private_port': 'PrivatePort',
        'public_port': 'PublicPort',
        'type': 'Type'
    }

    def __init__(self, ip=None, private_port=None, public_port=None, type=None, _configuration=None):  # noqa: E501
        """Port - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ip = None
        self._private_port = None
        self._public_port = None
        self._type = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        self.private_port = private_port
        if public_port is not None:
            self.public_port = public_port
        self.type = type

    @property
    def ip(self):
        """Gets the ip of this Port.  # noqa: E501

        Host IP address that the container's port is mapped to  # noqa: E501

        :return: The ip of this Port.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Port.

        Host IP address that the container's port is mapped to  # noqa: E501

        :param ip: The ip of this Port.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def private_port(self):
        """Gets the private_port of this Port.  # noqa: E501

        Port on the container  # noqa: E501

        :return: The private_port of this Port.  # noqa: E501
        :rtype: int
        """
        return self._private_port

    @private_port.setter
    def private_port(self, private_port):
        """Sets the private_port of this Port.

        Port on the container  # noqa: E501

        :param private_port: The private_port of this Port.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and private_port is None:
            raise ValueError("Invalid value for `private_port`, must not be `None`")  # noqa: E501

        self._private_port = private_port

    @property
    def public_port(self):
        """Gets the public_port of this Port.  # noqa: E501

        Port exposed on the host  # noqa: E501

        :return: The public_port of this Port.  # noqa: E501
        :rtype: int
        """
        return self._public_port

    @public_port.setter
    def public_port(self, public_port):
        """Sets the public_port of this Port.

        Port exposed on the host  # noqa: E501

        :param public_port: The public_port of this Port.  # noqa: E501
        :type: int
        """

        self._public_port = public_port

    @property
    def type(self):
        """Gets the type of this Port.  # noqa: E501

        type  # noqa: E501

        :return: The type of this Port.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Port.

        type  # noqa: E501

        :param type: The type of this Port.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(Port, dict):
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
        if not isinstance(other, Port):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Port):
            return True

        return self.to_dict() != other.to_dict()

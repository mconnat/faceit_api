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


class Info(object):
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
        'accessible_topology': 'list[Topology]',
        'capacity_bytes': 'int',
        'volume_context': 'dict(str, str)',
        'volume_id': 'str'
    }

    attribute_map = {
        'accessible_topology': 'AccessibleTopology',
        'capacity_bytes': 'CapacityBytes',
        'volume_context': 'VolumeContext',
        'volume_id': 'VolumeID'
    }

    def __init__(self, accessible_topology=None, capacity_bytes=None, volume_context=None, volume_id=None, _configuration=None):  # noqa: E501
        """Info - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accessible_topology = None
        self._capacity_bytes = None
        self._volume_context = None
        self._volume_id = None
        self.discriminator = None

        if accessible_topology is not None:
            self.accessible_topology = accessible_topology
        if capacity_bytes is not None:
            self.capacity_bytes = capacity_bytes
        if volume_context is not None:
            self.volume_context = volume_context
        if volume_id is not None:
            self.volume_id = volume_id

    @property
    def accessible_topology(self):
        """Gets the accessible_topology of this Info.  # noqa: E501

        AccessibleTopolgoy is the topology this volume is actually accessible from.  # noqa: E501

        :return: The accessible_topology of this Info.  # noqa: E501
        :rtype: list[Topology]
        """
        return self._accessible_topology

    @accessible_topology.setter
    def accessible_topology(self, accessible_topology):
        """Sets the accessible_topology of this Info.

        AccessibleTopolgoy is the topology this volume is actually accessible from.  # noqa: E501

        :param accessible_topology: The accessible_topology of this Info.  # noqa: E501
        :type: list[Topology]
        """

        self._accessible_topology = accessible_topology

    @property
    def capacity_bytes(self):
        """Gets the capacity_bytes of this Info.  # noqa: E501

        CapacityBytes is the capacity of the volume in bytes. A value of 0 indicates that the capacity is unknown.  # noqa: E501

        :return: The capacity_bytes of this Info.  # noqa: E501
        :rtype: int
        """
        return self._capacity_bytes

    @capacity_bytes.setter
    def capacity_bytes(self, capacity_bytes):
        """Sets the capacity_bytes of this Info.

        CapacityBytes is the capacity of the volume in bytes. A value of 0 indicates that the capacity is unknown.  # noqa: E501

        :param capacity_bytes: The capacity_bytes of this Info.  # noqa: E501
        :type: int
        """

        self._capacity_bytes = capacity_bytes

    @property
    def volume_context(self):
        """Gets the volume_context of this Info.  # noqa: E501

        VolumeContext is the context originating from the CSI storage plugin when the Volume is created.  # noqa: E501

        :return: The volume_context of this Info.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._volume_context

    @volume_context.setter
    def volume_context(self, volume_context):
        """Sets the volume_context of this Info.

        VolumeContext is the context originating from the CSI storage plugin when the Volume is created.  # noqa: E501

        :param volume_context: The volume_context of this Info.  # noqa: E501
        :type: dict(str, str)
        """

        self._volume_context = volume_context

    @property
    def volume_id(self):
        """Gets the volume_id of this Info.  # noqa: E501

        VolumeID is the ID of the Volume as seen by the CSI storage plugin. This is distinct from the Volume's Swarm ID, which is the ID used by all of the Docker Engine to refer to the Volume. If this field is blank, then the Volume has not been successfully created yet.  # noqa: E501

        :return: The volume_id of this Info.  # noqa: E501
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this Info.

        VolumeID is the ID of the Volume as seen by the CSI storage plugin. This is distinct from the Volume's Swarm ID, which is the ID used by all of the Docker Engine to refer to the Volume. If this field is blank, then the Volume has not been successfully created yet.  # noqa: E501

        :param volume_id: The volume_id of this Info.  # noqa: E501
        :type: str
        """

        self._volume_id = volume_id

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
        if issubclass(Info, dict):
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
        if not isinstance(other, Info):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Info):
            return True

        return self.to_dict() != other.to_dict()
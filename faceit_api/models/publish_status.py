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


class PublishStatus(object):
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
        'node_id': 'str',
        'publish_context': 'dict(str, str)',
        'state': 'PublishState'
    }

    attribute_map = {
        'node_id': 'NodeID',
        'publish_context': 'PublishContext',
        'state': 'State'
    }

    def __init__(self, node_id=None, publish_context=None, state=None, _configuration=None):  # noqa: E501
        """PublishStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._node_id = None
        self._publish_context = None
        self._state = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if publish_context is not None:
            self.publish_context = publish_context
        if state is not None:
            self.state = state

    @property
    def node_id(self):
        """Gets the node_id of this PublishStatus.  # noqa: E501

        NodeID is the ID of the swarm node this Volume is published to.  # noqa: E501

        :return: The node_id of this PublishStatus.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this PublishStatus.

        NodeID is the ID of the swarm node this Volume is published to.  # noqa: E501

        :param node_id: The node_id of this PublishStatus.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def publish_context(self):
        """Gets the publish_context of this PublishStatus.  # noqa: E501

        PublishContext is the PublishContext returned by the CSI plugin when a volume is published.  # noqa: E501

        :return: The publish_context of this PublishStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._publish_context

    @publish_context.setter
    def publish_context(self, publish_context):
        """Sets the publish_context of this PublishStatus.

        PublishContext is the PublishContext returned by the CSI plugin when a volume is published.  # noqa: E501

        :param publish_context: The publish_context of this PublishStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._publish_context = publish_context

    @property
    def state(self):
        """Gets the state of this PublishStatus.  # noqa: E501


        :return: The state of this PublishStatus.  # noqa: E501
        :rtype: PublishState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PublishStatus.


        :param state: The state of this PublishStatus.  # noqa: E501
        :type: PublishState
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
        if issubclass(PublishStatus, dict):
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
        if not isinstance(other, PublishStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublishStatus):
            return True

        return self.to_dict() != other.to_dict()
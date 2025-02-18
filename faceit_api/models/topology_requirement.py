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


class TopologyRequirement(object):
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
        'preferred': 'list[Topology]',
        'requisite': 'list[Topology]'
    }

    attribute_map = {
        'preferred': 'Preferred',
        'requisite': 'Requisite'
    }

    def __init__(self, preferred=None, requisite=None, _configuration=None):  # noqa: E501
        """TopologyRequirement - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._preferred = None
        self._requisite = None
        self.discriminator = None

        if preferred is not None:
            self.preferred = preferred
        if requisite is not None:
            self.requisite = requisite

    @property
    def preferred(self):
        """Gets the preferred of this TopologyRequirement.  # noqa: E501

        Preferred is a list of Topologies that the volume should attempt to be provisioned in.  Taken from the CSI spec:  Specifies the list of topologies the CO would prefer the volume to be provisioned in.  This field is OPTIONAL. If TopologyRequirement is specified either requisite or preferred or both MUST be specified.  An SP MUST attempt to make the provisioned volume available using the preferred topologies in order from first to last.  If requisite is specified, all topologies in preferred list MUST also be present in the list of requisite topologies.  If the SP is unable to make the provisioned volume available from any of the preferred topologies, the SP MAY choose a topology from the list of requisite topologies. If the list of requisite topologies is not specified, then the SP MAY choose from the list of all possible topologies. If the list of requisite topologies is specified and the SP is unable to make the provisioned volume available from any of the requisite topologies it MUST fail the CreateVolume call.  Example 1: Given a volume should be accessible from a single zone, and requisite = {\"region\": \"R1\", \"zone\": \"Z2\"}, {\"region\": \"R1\", \"zone\": \"Z3\"} preferred = {\"region\": \"R1\", \"zone\": \"Z3\"} then the SP SHOULD first attempt to make the provisioned volume available from \"zone\" \"Z3\" in the \"region\" \"R1\" and fall back to \"zone\" \"Z2\" in the \"region\" \"R1\" if that is not possible.  Example 2: Given a volume should be accessible from a single zone, and requisite = {\"region\": \"R1\", \"zone\": \"Z2\"}, {\"region\": \"R1\", \"zone\": \"Z3\"}, {\"region\": \"R1\", \"zone\": \"Z4\"}, {\"region\": \"R1\", \"zone\": \"Z5\"} preferred = {\"region\": \"R1\", \"zone\": \"Z4\"}, {\"region\": \"R1\", \"zone\": \"Z2\"} then the SP SHOULD first attempt to make the provisioned volume accessible from \"zone\" \"Z4\" in the \"region\" \"R1\" and fall back to \"zone\" \"Z2\" in the \"region\" \"R1\" if that is not possible. If that is not possible, the SP may choose between either the \"zone\" \"Z3\" or \"Z5\" in the \"region\" \"R1\".  Example 3: Given a volume should be accessible from TWO zones (because an opaque parameter in CreateVolumeRequest, for example, specifies the volume is accessible from two zones, aka synchronously replicated), and requisite = {\"region\": \"R1\", \"zone\": \"Z2\"}, {\"region\": \"R1\", \"zone\": \"Z3\"}, {\"region\": \"R1\", \"zone\": \"Z4\"}, {\"region\": \"R1\", \"zone\": \"Z5\"} preferred = {\"region\": \"R1\", \"zone\": \"Z5\"}, {\"region\": \"R1\", \"zone\": \"Z3\"} then the SP SHOULD first attempt to make the provisioned volume accessible from the combination of the two \"zones\" \"Z5\" and \"Z3\" in the \"region\" \"R1\". If that's not possible, it should fall back to a combination of \"Z5\" and other possibilities from the list of requisite. If that's not possible, it should fall back  to a combination of \"Z3\" and other possibilities from the list of requisite. If that's not possible, it should fall back  to a combination of other possibilities from the list of requisite.  # noqa: E501

        :return: The preferred of this TopologyRequirement.  # noqa: E501
        :rtype: list[Topology]
        """
        return self._preferred

    @preferred.setter
    def preferred(self, preferred):
        """Sets the preferred of this TopologyRequirement.

        Preferred is a list of Topologies that the volume should attempt to be provisioned in.  Taken from the CSI spec:  Specifies the list of topologies the CO would prefer the volume to be provisioned in.  This field is OPTIONAL. If TopologyRequirement is specified either requisite or preferred or both MUST be specified.  An SP MUST attempt to make the provisioned volume available using the preferred topologies in order from first to last.  If requisite is specified, all topologies in preferred list MUST also be present in the list of requisite topologies.  If the SP is unable to make the provisioned volume available from any of the preferred topologies, the SP MAY choose a topology from the list of requisite topologies. If the list of requisite topologies is not specified, then the SP MAY choose from the list of all possible topologies. If the list of requisite topologies is specified and the SP is unable to make the provisioned volume available from any of the requisite topologies it MUST fail the CreateVolume call.  Example 1: Given a volume should be accessible from a single zone, and requisite = {\"region\": \"R1\", \"zone\": \"Z2\"}, {\"region\": \"R1\", \"zone\": \"Z3\"} preferred = {\"region\": \"R1\", \"zone\": \"Z3\"} then the SP SHOULD first attempt to make the provisioned volume available from \"zone\" \"Z3\" in the \"region\" \"R1\" and fall back to \"zone\" \"Z2\" in the \"region\" \"R1\" if that is not possible.  Example 2: Given a volume should be accessible from a single zone, and requisite = {\"region\": \"R1\", \"zone\": \"Z2\"}, {\"region\": \"R1\", \"zone\": \"Z3\"}, {\"region\": \"R1\", \"zone\": \"Z4\"}, {\"region\": \"R1\", \"zone\": \"Z5\"} preferred = {\"region\": \"R1\", \"zone\": \"Z4\"}, {\"region\": \"R1\", \"zone\": \"Z2\"} then the SP SHOULD first attempt to make the provisioned volume accessible from \"zone\" \"Z4\" in the \"region\" \"R1\" and fall back to \"zone\" \"Z2\" in the \"region\" \"R1\" if that is not possible. If that is not possible, the SP may choose between either the \"zone\" \"Z3\" or \"Z5\" in the \"region\" \"R1\".  Example 3: Given a volume should be accessible from TWO zones (because an opaque parameter in CreateVolumeRequest, for example, specifies the volume is accessible from two zones, aka synchronously replicated), and requisite = {\"region\": \"R1\", \"zone\": \"Z2\"}, {\"region\": \"R1\", \"zone\": \"Z3\"}, {\"region\": \"R1\", \"zone\": \"Z4\"}, {\"region\": \"R1\", \"zone\": \"Z5\"} preferred = {\"region\": \"R1\", \"zone\": \"Z5\"}, {\"region\": \"R1\", \"zone\": \"Z3\"} then the SP SHOULD first attempt to make the provisioned volume accessible from the combination of the two \"zones\" \"Z5\" and \"Z3\" in the \"region\" \"R1\". If that's not possible, it should fall back to a combination of \"Z5\" and other possibilities from the list of requisite. If that's not possible, it should fall back  to a combination of \"Z3\" and other possibilities from the list of requisite. If that's not possible, it should fall back  to a combination of other possibilities from the list of requisite.  # noqa: E501

        :param preferred: The preferred of this TopologyRequirement.  # noqa: E501
        :type: list[Topology]
        """

        self._preferred = preferred

    @property
    def requisite(self):
        """Gets the requisite of this TopologyRequirement.  # noqa: E501

        Requisite specifies a list of Topologies, at least one of which the volume must be accessible from.  Taken verbatim from the CSI Spec:  Specifies the list of topologies the provisioned volume MUST be accessible from. This field is OPTIONAL. If TopologyRequirement is specified either requisite or preferred or both MUST be specified.  If requisite is specified, the provisioned volume MUST be accessible from at least one of the requisite topologies.  Given x = number of topologies provisioned volume is accessible from n = number of requisite topologies The CO MUST ensure n >= 1. The SP MUST ensure x >= 1 If x==n, then the SP MUST make the provisioned volume available to all topologies from the list of requisite topologies. If it is unable to do so, the SP MUST fail the CreateVolume call. For example, if a volume should be accessible from a single zone, and requisite = {\"region\": \"R1\", \"zone\": \"Z2\"} then the provisioned volume MUST be accessible from the \"region\" \"R1\" and the \"zone\" \"Z2\". Similarly, if a volume should be accessible from two zones, and requisite = {\"region\": \"R1\", \"zone\": \"Z2\"}, {\"region\": \"R1\", \"zone\": \"Z3\"} then the provisioned volume MUST be accessible from the \"region\" \"R1\" and both \"zone\" \"Z2\" and \"zone\" \"Z3\".  If x<n, then the SP SHALL choose x unique topologies from the list of requisite topologies. If it is unable to do so, the SP MUST fail the CreateVolume call. For example, if a volume should be accessible from a single zone, and requisite = {\"region\": \"R1\", \"zone\": \"Z2\"}, {\"region\": \"R1\", \"zone\": \"Z3\"} then the SP may choose to make the provisioned volume available in either the \"zone\" \"Z2\" or the \"zone\" \"Z3\" in the \"region\" \"R1\". Similarly, if a volume should be accessible from two zones, and requisite = {\"region\": \"R1\", \"zone\": \"Z2\"}, {\"region\": \"R1\", \"zone\": \"Z3\"}, {\"region\": \"R1\", \"zone\": \"Z4\"} then the provisioned volume MUST be accessible from any combination of two unique topologies: e.g. \"R1/Z2\" and \"R1/Z3\", or \"R1/Z2\" and \"R1/Z4\", or \"R1/Z3\" and \"R1/Z4\".  If x>n, then the SP MUST make the provisioned volume available from all topologies from the list of requisite topologies and MAY choose the remaining x-n unique topologies from the list of all possible topologies. If it is unable to do so, the SP MUST fail the CreateVolume call. For example, if a volume should be accessible from two zones, and requisite = {\"region\": \"R1\", \"zone\": \"Z2\"} then the provisioned volume MUST be accessible from the \"region\" \"R1\" and the \"zone\" \"Z2\" and the SP may select the second zone independently, e.g. \"R1/Z4\".  # noqa: E501

        :return: The requisite of this TopologyRequirement.  # noqa: E501
        :rtype: list[Topology]
        """
        return self._requisite

    @requisite.setter
    def requisite(self, requisite):
        """Sets the requisite of this TopologyRequirement.

        Requisite specifies a list of Topologies, at least one of which the volume must be accessible from.  Taken verbatim from the CSI Spec:  Specifies the list of topologies the provisioned volume MUST be accessible from. This field is OPTIONAL. If TopologyRequirement is specified either requisite or preferred or both MUST be specified.  If requisite is specified, the provisioned volume MUST be accessible from at least one of the requisite topologies.  Given x = number of topologies provisioned volume is accessible from n = number of requisite topologies The CO MUST ensure n >= 1. The SP MUST ensure x >= 1 If x==n, then the SP MUST make the provisioned volume available to all topologies from the list of requisite topologies. If it is unable to do so, the SP MUST fail the CreateVolume call. For example, if a volume should be accessible from a single zone, and requisite = {\"region\": \"R1\", \"zone\": \"Z2\"} then the provisioned volume MUST be accessible from the \"region\" \"R1\" and the \"zone\" \"Z2\". Similarly, if a volume should be accessible from two zones, and requisite = {\"region\": \"R1\", \"zone\": \"Z2\"}, {\"region\": \"R1\", \"zone\": \"Z3\"} then the provisioned volume MUST be accessible from the \"region\" \"R1\" and both \"zone\" \"Z2\" and \"zone\" \"Z3\".  If x<n, then the SP SHALL choose x unique topologies from the list of requisite topologies. If it is unable to do so, the SP MUST fail the CreateVolume call. For example, if a volume should be accessible from a single zone, and requisite = {\"region\": \"R1\", \"zone\": \"Z2\"}, {\"region\": \"R1\", \"zone\": \"Z3\"} then the SP may choose to make the provisioned volume available in either the \"zone\" \"Z2\" or the \"zone\" \"Z3\" in the \"region\" \"R1\". Similarly, if a volume should be accessible from two zones, and requisite = {\"region\": \"R1\", \"zone\": \"Z2\"}, {\"region\": \"R1\", \"zone\": \"Z3\"}, {\"region\": \"R1\", \"zone\": \"Z4\"} then the provisioned volume MUST be accessible from any combination of two unique topologies: e.g. \"R1/Z2\" and \"R1/Z3\", or \"R1/Z2\" and \"R1/Z4\", or \"R1/Z3\" and \"R1/Z4\".  If x>n, then the SP MUST make the provisioned volume available from all topologies from the list of requisite topologies and MAY choose the remaining x-n unique topologies from the list of all possible topologies. If it is unable to do so, the SP MUST fail the CreateVolume call. For example, if a volume should be accessible from two zones, and requisite = {\"region\": \"R1\", \"zone\": \"Z2\"} then the provisioned volume MUST be accessible from the \"region\" \"R1\" and the \"zone\" \"Z2\" and the SP may select the second zone independently, e.g. \"R1/Z4\".  # noqa: E501

        :param requisite: The requisite of this TopologyRequirement.  # noqa: E501
        :type: list[Topology]
        """

        self._requisite = requisite

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
        if issubclass(TopologyRequirement, dict):
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
        if not isinstance(other, TopologyRequirement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TopologyRequirement):
            return True

        return self.to_dict() != other.to_dict()

# coding: utf-8

"""
    RIC subscription

    This is the initial REST API for RIC subscription  # noqa: E501

    OpenAPI spec version: 0.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ricxappframe_ID.subsclient.configuration import Configuration


class SubscriptionInstance(object):
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
        'xapp_event_instance_id': 'int',
        'e2_event_instance_id': 'int',
        'error_cause': 'str',
        'error_source': 'str',
        'timeout_type': 'str'
    }

    attribute_map = {
        'xapp_event_instance_id': 'XappEventInstanceId',
        'e2_event_instance_id': 'E2EventInstanceId',
        'error_cause': 'ErrorCause',
        'error_source': 'ErrorSource',
        'timeout_type': 'TimeoutType'
    }

    def __init__(self, xapp_event_instance_id=None, e2_event_instance_id=None, error_cause=None, error_source=None, timeout_type=None, _configuration=None):  # noqa: E501
        """SubscriptionInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._xapp_event_instance_id = None
        self._e2_event_instance_id = None
        self._error_cause = None
        self._error_source = None
        self._timeout_type = None
        self.discriminator = None

        self.xapp_event_instance_id = xapp_event_instance_id
        self.e2_event_instance_id = e2_event_instance_id
        if error_cause is not None:
            self.error_cause = error_cause
        if error_source is not None:
            self.error_source = error_source
        if timeout_type is not None:
            self.timeout_type = timeout_type

    @property
    def xapp_event_instance_id(self):
        """Gets the xapp_event_instance_id of this SubscriptionInstance.  # noqa: E501


        :return: The xapp_event_instance_id of this SubscriptionInstance.  # noqa: E501
        :rtype: int
        """
        return self._xapp_event_instance_id

    @xapp_event_instance_id.setter
    def xapp_event_instance_id(self, xapp_event_instance_id):
        """Sets the xapp_event_instance_id of this SubscriptionInstance.


        :param xapp_event_instance_id: The xapp_event_instance_id of this SubscriptionInstance.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and xapp_event_instance_id is None:
            raise ValueError("Invalid value for `xapp_event_instance_id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                xapp_event_instance_id is not None and xapp_event_instance_id > 65535):  # noqa: E501
            raise ValueError("Invalid value for `xapp_event_instance_id`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self._configuration.client_side_validation and
                xapp_event_instance_id is not None and xapp_event_instance_id < 0):  # noqa: E501
            raise ValueError("Invalid value for `xapp_event_instance_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._xapp_event_instance_id = xapp_event_instance_id

    @property
    def e2_event_instance_id(self):
        """Gets the e2_event_instance_id of this SubscriptionInstance.  # noqa: E501


        :return: The e2_event_instance_id of this SubscriptionInstance.  # noqa: E501
        :rtype: int
        """
        return self._e2_event_instance_id

    @e2_event_instance_id.setter
    def e2_event_instance_id(self, e2_event_instance_id):
        """Sets the e2_event_instance_id of this SubscriptionInstance.


        :param e2_event_instance_id: The e2_event_instance_id of this SubscriptionInstance.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and e2_event_instance_id is None:
            raise ValueError("Invalid value for `e2_event_instance_id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                e2_event_instance_id is not None and e2_event_instance_id > 65535):  # noqa: E501
            raise ValueError("Invalid value for `e2_event_instance_id`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self._configuration.client_side_validation and
                e2_event_instance_id is not None and e2_event_instance_id < 0):  # noqa: E501
            raise ValueError("Invalid value for `e2_event_instance_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._e2_event_instance_id = e2_event_instance_id

    @property
    def error_cause(self):
        """Gets the error_cause of this SubscriptionInstance.  # noqa: E501

        Descriptive error cause. Empty string when no error.  # noqa: E501

        :return: The error_cause of this SubscriptionInstance.  # noqa: E501
        :rtype: str
        """
        return self._error_cause

    @error_cause.setter
    def error_cause(self, error_cause):
        """Sets the error_cause of this SubscriptionInstance.

        Descriptive error cause. Empty string when no error.  # noqa: E501

        :param error_cause: The error_cause of this SubscriptionInstance.  # noqa: E501
        :type: str
        """

        self._error_cause = error_cause

    @property
    def error_source(self):
        """Gets the error_source of this SubscriptionInstance.  # noqa: E501

        Source of error cause.  # noqa: E501

        :return: The error_source of this SubscriptionInstance.  # noqa: E501
        :rtype: str
        """
        return self._error_source

    @error_source.setter
    def error_source(self, error_source):
        """Sets the error_source of this SubscriptionInstance.

        Source of error cause.  # noqa: E501

        :param error_source: The error_source of this SubscriptionInstance.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUBMGR", "RTMGR", "DBAAS", "ASN1", "E2Node"]  # noqa: E501
        if (self._configuration.client_side_validation and
                error_source not in allowed_values):
            raise ValueError(
                "Invalid value for `error_source` ({0}), must be one of {1}"  # noqa: E501
                .format(error_source, allowed_values)
            )

        self._error_source = error_source

    @property
    def timeout_type(self):
        """Gets the timeout_type of this SubscriptionInstance.  # noqa: E501

        Type timeout. xApp should retry if timeout occurs.  # noqa: E501

        :return: The timeout_type of this SubscriptionInstance.  # noqa: E501
        :rtype: str
        """
        return self._timeout_type

    @timeout_type.setter
    def timeout_type(self, timeout_type):
        """Sets the timeout_type of this SubscriptionInstance.

        Type timeout. xApp should retry if timeout occurs.  # noqa: E501

        :param timeout_type: The timeout_type of this SubscriptionInstance.  # noqa: E501
        :type: str
        """
        allowed_values = ["E2-Timeout", "RTMGR-Timeout", "DBAAS-Timeout"]  # noqa: E501
        if (self._configuration.client_side_validation and
                timeout_type not in allowed_values):
            raise ValueError(
                "Invalid value for `timeout_type` ({0}), must be one of {1}"  # noqa: E501
                .format(timeout_type, allowed_values)
            )

        self._timeout_type = timeout_type

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
        if issubclass(SubscriptionInstance, dict):
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
        if not isinstance(other, SubscriptionInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionInstance):
            return True

        return self.to_dict() != other.to_dict()

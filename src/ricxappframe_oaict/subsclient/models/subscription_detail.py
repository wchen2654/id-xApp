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


class SubscriptionDetail(object):
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
        'event_triggers': 'EventTriggerDefinition',
        'action_to_be_setup_list': 'ActionsToBeSetup'
    }

    attribute_map = {
        'xapp_event_instance_id': 'XappEventInstanceId',
        'event_triggers': 'EventTriggers',
        'action_to_be_setup_list': 'ActionToBeSetupList'
    }

    def __init__(self, xapp_event_instance_id=None, event_triggers=None, action_to_be_setup_list=None, _configuration=None):  # noqa: E501
        """SubscriptionDetail - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._xapp_event_instance_id = None
        self._event_triggers = None
        self._action_to_be_setup_list = None
        self.discriminator = None

        self.xapp_event_instance_id = xapp_event_instance_id
        self.event_triggers = event_triggers
        self.action_to_be_setup_list = action_to_be_setup_list

    @property
    def xapp_event_instance_id(self):
        """Gets the xapp_event_instance_id of this SubscriptionDetail.  # noqa: E501


        :return: The xapp_event_instance_id of this SubscriptionDetail.  # noqa: E501
        :rtype: int
        """
        return self._xapp_event_instance_id

    @xapp_event_instance_id.setter
    def xapp_event_instance_id(self, xapp_event_instance_id):
        """Sets the xapp_event_instance_id of this SubscriptionDetail.


        :param xapp_event_instance_id: The xapp_event_instance_id of this SubscriptionDetail.  # noqa: E501
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
    def event_triggers(self):
        """Gets the event_triggers of this SubscriptionDetail.  # noqa: E501


        :return: The event_triggers of this SubscriptionDetail.  # noqa: E501
        :rtype: EventTriggerDefinition
        """
        return self._event_triggers

    @event_triggers.setter
    def event_triggers(self, event_triggers):
        """Sets the event_triggers of this SubscriptionDetail.


        :param event_triggers: The event_triggers of this SubscriptionDetail.  # noqa: E501
        :type: EventTriggerDefinition
        """
        if self._configuration.client_side_validation and event_triggers is None:
            raise ValueError("Invalid value for `event_triggers`, must not be `None`")  # noqa: E501

        self._event_triggers = event_triggers

    @property
    def action_to_be_setup_list(self):
        """Gets the action_to_be_setup_list of this SubscriptionDetail.  # noqa: E501


        :return: The action_to_be_setup_list of this SubscriptionDetail.  # noqa: E501
        :rtype: ActionsToBeSetup
        """
        return self._action_to_be_setup_list

    @action_to_be_setup_list.setter
    def action_to_be_setup_list(self, action_to_be_setup_list):
        """Sets the action_to_be_setup_list of this SubscriptionDetail.


        :param action_to_be_setup_list: The action_to_be_setup_list of this SubscriptionDetail.  # noqa: E501
        :type: ActionsToBeSetup
        """
        if self._configuration.client_side_validation and action_to_be_setup_list is None:
            raise ValueError("Invalid value for `action_to_be_setup_list`, must not be `None`")  # noqa: E501

        self._action_to_be_setup_list = action_to_be_setup_list

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
        if issubclass(SubscriptionDetail, dict):
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
        if not isinstance(other, SubscriptionDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionDetail):
            return True

        return self.to_dict() != other.to_dict()

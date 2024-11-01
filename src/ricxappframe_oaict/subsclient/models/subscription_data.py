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


class SubscriptionData(object):
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
        'subscription_id': 'int',
        'meid': 'str',
        'client_endpoint': 'list[str]',
        'subscription_instances': 'list[SubscriptionInstance]'
    }

    attribute_map = {
        'subscription_id': 'SubscriptionId',
        'meid': 'Meid',
        'client_endpoint': 'ClientEndpoint',
        'subscription_instances': 'SubscriptionInstances'
    }

    def __init__(self, subscription_id=None, meid=None, client_endpoint=None, subscription_instances=None, _configuration=None):  # noqa: E501
        """SubscriptionData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._subscription_id = None
        self._meid = None
        self._client_endpoint = None
        self._subscription_instances = None
        self.discriminator = None

        if subscription_id is not None:
            self.subscription_id = subscription_id
        if meid is not None:
            self.meid = meid
        if client_endpoint is not None:
            self.client_endpoint = client_endpoint
        if subscription_instances is not None:
            self.subscription_instances = subscription_instances

    @property
    def subscription_id(self):
        """Gets the subscription_id of this SubscriptionData.  # noqa: E501


        :return: The subscription_id of this SubscriptionData.  # noqa: E501
        :rtype: int
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this SubscriptionData.


        :param subscription_id: The subscription_id of this SubscriptionData.  # noqa: E501
        :type: int
        """

        self._subscription_id = subscription_id

    @property
    def meid(self):
        """Gets the meid of this SubscriptionData.  # noqa: E501


        :return: The meid of this SubscriptionData.  # noqa: E501
        :rtype: str
        """
        return self._meid

    @meid.setter
    def meid(self, meid):
        """Sets the meid of this SubscriptionData.


        :param meid: The meid of this SubscriptionData.  # noqa: E501
        :type: str
        """

        self._meid = meid

    @property
    def client_endpoint(self):
        """Gets the client_endpoint of this SubscriptionData.  # noqa: E501


        :return: The client_endpoint of this SubscriptionData.  # noqa: E501
        :rtype: list[str]
        """
        return self._client_endpoint

    @client_endpoint.setter
    def client_endpoint(self, client_endpoint):
        """Sets the client_endpoint of this SubscriptionData.


        :param client_endpoint: The client_endpoint of this SubscriptionData.  # noqa: E501
        :type: list[str]
        """

        self._client_endpoint = client_endpoint

    @property
    def subscription_instances(self):
        """Gets the subscription_instances of this SubscriptionData.  # noqa: E501


        :return: The subscription_instances of this SubscriptionData.  # noqa: E501
        :rtype: list[SubscriptionInstance]
        """
        return self._subscription_instances

    @subscription_instances.setter
    def subscription_instances(self, subscription_instances):
        """Sets the subscription_instances of this SubscriptionData.


        :param subscription_instances: The subscription_instances of this SubscriptionData.  # noqa: E501
        :type: list[SubscriptionInstance]
        """

        self._subscription_instances = subscription_instances

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
        if issubclass(SubscriptionData, dict):
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
        if not isinstance(other, SubscriptionData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionData):
            return True

        return self.to_dict() != other.to_dict()

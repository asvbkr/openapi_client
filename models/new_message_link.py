# coding: utf-8

"""
    TamTam Bot API

    # About Bot API allows bots to interact with TamTam. Methods are called by sending HTTPS requests to [botapi.tamtam.chat](https://botapi.tamtam.chat) domain. Bots are third-party applications that use TamTam features. A bot can legitimately take part in a conversation. It can be achieved through HTTP requests to the TamTam Bot API. ## Features TamTam bots of the current version are able to: - Communicate with users and respond to requests - Recommend users complete actions via programmed buttons - Request personal data from users (name, short reference, phone number) We'll keep working on expanding bot capabilities in the future. ## Examples Bots can be used for the following purposes: - Providing support, answering frequently asked questions - Sending typical information - Voting - Likes/dislikes - Following external links - Forwarding a user to a chat/channel ## @PrimeBot We are beta testing bots in TamTam now. To become a beta tester, please, contact us on **[@support](https://tt.me/support)** or [team@tamtam.chat](mailto:team@tamtam.chat). We'll give you access to [PrimeBot](https://tt.me/primebot), all TamTam bots creator. It will help you choose a unique short name for a bot and fill in its full name and description. With PrimeBot you can create bots as well as edit and delete them and browse information on bots you have created. #### [PrimeBot](https://tt.me/primebot) commands: `/start` &mdash; start a dialog with a bot<br/> `/create` &mdash; create a bot, assign the unique short name to it (from 4 to 64 characters)<br/> `/set_name [name]` &mdash; assign a short or full name to the bot (up to 200 characters)<br/> `/set_description [description]` &mdash; enter the description for the bot profile (up to 400 characters)<br/> `/set_picture [URL]` &mdash; enter the URL of bot's picture<br/> `/delete [username]` &mdash; delete the bot<br/> `/list` &mdash; show the list of all bots<br/> `/get_token` &mdash; obtain a token for a bot<br/> `/revoke` &mdash; request a new token<br/> `/help` &mdash; help<br/> ## HTTP verbs `GET` &mdash; getting resources, parameters are transmitted via URL<br/> `POST` &mdash; creation of resources (for example, sending new messages)<br/> `PUT` &mdash; editing resources<br/> `DELETE` &mdash; deleting resources<br/>`PATCH` &mdash; patching resources ## HTTP response codes `200` &mdash; successful operation<br/> `400` &mdash; invalid request<br/> `401` &mdash; authentication error<br/> `404` &mdash; resource not found<br/> `405` &mdash; method not allowed<br/> `429` &mdash; the number of requests is exceeded<br/> `503` &mdash; service unavailable<br/> ## Resources format For content requests (PUT and POST) and responses, the API uses the JSON format. All strings are UTF-8 encoded. Date/time fields are represented as the number of milliseconds that have elapsed since 00:00 January 1, 1970 in the long format. To get it, you can simply multiply the UNIX timestamp by 1000. All date/time fields have a UTC timezone. ## Error responses In case of an error, the API returns a response with the corresponding HTTP code and JSON with the following fields: <br/> `code` - the string with the error key <br/> `message` - a string describing the error </br> For example: ```bash > http https://botapi.tamtam.chat/chats?access_token={EXAMPLE_TOKEN} HTTP / 1.1 403 Forbidden Cache-Control: no-cache Connection: Keep-Alive Content-Length: 57 Content-Type: application / json; charset = utf-8 Set-Cookie: web_ui_lang = ru; Path = /; Domain = .tamtam.chat; Expires = 2019-03-24T11: 45: 36.500Z {    \"code\": \"verify.token\",    \"message\": \"Invalid access_token\" } ``` ## Receiving Notifications TamTam Bot API supports 2 options of receiving notifications on new dialog events for bots: - Push notifications via WebHook. To receive data via WebHook, you'll have to [add subscription](https://dev.tamtam.chat/#operation/subscribe); - Notifications upon request via [long polling](#operation/getUpdates) API. All data can be received via long polling **by default** after creating the bot,  Both methods **cannot** be used simultaneously. Refer to the response schema of [/updates](https://dev.tamtam.chat/#operation/getUpdates) method to check all available types of updates. ## Message buttons You can program buttons for users answering a bot. TamTam supports the following types of buttons: <br/> `callback` &mdash; sends a notification to a bot (via WebHook or long polling) <br/> `link` &mdash; makes a user to follow a link <br/> `request_contact` &mdash; requests the user permission to access contact information (phone number, short link, email) <br/> You may also send a message with an [InlineKeyboard]() type attachment to start creating buttons. When the user presses a button, the bot receives the answer with filled callback field. It is recommended to edit that message so the user can receive updated buttons. # Versioning API models and interface may change over time. To make sure your bot will get the right info, we strongly recommend adding API version number to each request. You can add it as `v` parameter to each HTTP-request. For instance, `v=0.1.2`. To specify the data model version you are getting through WebHook subscription, use the `version` property in the request body of the [subscribe](https://dev.tamtam.chat/#operation/subscribe) request. # Libraries We have created [Java library](https://github.com/tamtam-chat/tamtam-bot-api) to make using API easier. # Changelog ##### Version 0.1.5 - Added `id` property to media attachments (`VideoAttachment`, `AudioAttachment`) so you can reuse attachment from one message in another - Added ability to create *linked* message: replied or forwarded. See `link` in `NewMessageBody` - `intent` property marked as required only for `CallbackButton` ##### Version 0.1.4  - Added `user_ids` parameter to [get members](#operation/getMembers) in chat by id - `attachment` property of [send message](#operation/sendMessage) request body marked as deprecated  ##### Version 0.1.3 - Added method to [delete](https://dev.tamtam.chat/#operation/deleteMessages) messages - Added ability to [get](https://dev.tamtam.chat/#operation/getMessages) particular messages by ID - Added `is_admin` flag to `ChatMember` - Added `message` property to `MessageCallbackUpdate` - Renamed property `message` to `body` for `Message` schema - Added reusable `token` to `PhotoAttachment`. It allows to attach the same photo more than once.  # noqa: E501

    OpenAPI spec version: 0.1.5
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class NewMessageLink(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'MessageLinkType',
        'mid': 'str'
    }

    attribute_map = {
        'type': 'type',
        'mid': 'mid'
    }

    def __init__(self, type=None, mid=None):  # noqa: E501
        """NewMessageLink - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._mid = None
        self.discriminator = None

        self.type = type
        self.mid = mid

    @property
    def type(self):
        """Gets the type of this NewMessageLink.  # noqa: E501

        Type of message link  # noqa: E501

        :return: The type of this NewMessageLink.  # noqa: E501
        :rtype: MessageLinkType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NewMessageLink.

        Type of message link  # noqa: E501

        :param type: The type of this NewMessageLink.  # noqa: E501
        :type: MessageLinkType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def mid(self):
        """Gets the mid of this NewMessageLink.  # noqa: E501

        Message identifier of original message  # noqa: E501

        :return: The mid of this NewMessageLink.  # noqa: E501
        :rtype: str
        """
        return self._mid

    @mid.setter
    def mid(self, mid):
        """Sets the mid of this NewMessageLink.

        Message identifier of original message  # noqa: E501

        :param mid: The mid of this NewMessageLink.  # noqa: E501
        :type: str
        """
        if mid is None:
            raise ValueError("Invalid value for `mid`, must not be `None`")  # noqa: E501

        self._mid = mid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NewMessageLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

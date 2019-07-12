# coding: utf-8

"""
    TamTam Bot API

    # About Bot API allows bots to interact with TamTam. Methods are called by sending HTTPS requests to [botapi.tamtam.chat](https://botapi.tamtam.chat) domain. Bots are third-party applications that use TamTam features. A bot can legitimately take part in a conversation. It can be achieved through HTTP requests to the TamTam Bot API. ## Features TamTam bots of the current version are able to: - Communicate with users and respond to requests - Recommend users complete actions via programmed buttons - Request personal data from users (name, short reference, phone number) We'll keep working on expanding bot capabilities in the future. ## Examples Bots can be used for the following purposes: - Providing support, answering frequently asked questions - Sending typical information - Voting - Likes/dislikes - Following external links - Forwarding a user to a chat/channel ## @PrimeBot We are beta testing bots in TamTam now. To become a beta tester, please, contact us on **[@support](https://tt.me/support)** or [team@tamtam.chat](mailto:team@tamtam.chat). We'll give you access to [PrimeBot](https://tt.me/primebot), all TamTam bots creator. It will help you choose a unique short name for a bot and fill in its full name and description. With PrimeBot you can create bots as well as edit and delete them and browse information on bots you have created. #### [PrimeBot](https://tt.me/primebot) commands: `/start` &mdash; start a dialog with a bot  `/create` &mdash; create a bot, assign the unique short name to it (from 4 to 64 characters)  `/set_name [name]` &mdash; assign a short or full name to the bot (up to 200 characters)  `/set_description [description]` &mdash; enter the description for the bot profile (up to 400 characters)  `/set_picture [URL]` &mdash; enter the URL of bot's picture  `/delete [username]` &mdash; delete the bot  `/list` &mdash; show the list of all bots  `/get_token` &mdash; obtain a token for a bot  `/revoke` &mdash; request a new token  `/help` &mdash; help  ## HTTP verbs `GET` &mdash; getting resources, parameters are transmitted via URL  `POST` &mdash; creation of resources (for example, sending new messages)  `PUT` &mdash; editing resources  `DELETE` &mdash; deleting resources  `PATCH` &mdash; patching resources ## HTTP response codes `200` &mdash; successful operation  `400` &mdash; invalid request  `401` &mdash; authentication error  `404` &mdash; resource not found  `405` &mdash; method not allowed  `429` &mdash; the number of requests is exceeded  `503` &mdash; service unavailable  ## Resources format For content requests (PUT and POST) and responses, the API uses the JSON format. All strings are UTF-8 encoded. Date/time fields are represented as the number of milliseconds that have elapsed since 00:00 January 1, 1970 in the long format. To get it, you can simply multiply the UNIX timestamp by 1000. All date/time fields have a UTC timezone. ## Error responses In case of an error, the API returns a response with the corresponding HTTP code and JSON with the following fields:   `code` - the string with the error key   `message` - a string describing the error </br>  For example: ```bash > http https://botapi.tamtam.chat/chats?access_token={EXAMPLE_TOKEN} HTTP / 1.1 403 Forbidden Cache-Control: no-cache Connection: Keep-Alive Content-Length: 57 Content-Type: application / json; charset = utf-8 Set-Cookie: web_ui_lang = ru; Path = /; Domain = .tamtam.chat; Expires = 2019-03-24T11: 45: 36.500Z {    \"code\": \"verify.token\",    \"message\": \"Invalid access_token\" } ``` ## Receiving Notifications TamTam Bot API supports 2 options of receiving notifications on new dialog events for bots: - Push notifications via WebHook. To receive data via WebHook, you'll have to [add subscription](https://dev.tamtam.chat/#operation/subscribe); - Notifications upon request via [long polling](#operation/getUpdates) API. All data can be received via long polling **by default** after creating the bot,  Both methods **cannot** be used simultaneously. Refer to the response schema of [/updates](https://dev.tamtam.chat/#operation/getUpdates) method to check all available types of updates. ## Message buttons You can program buttons for users answering a bot. TamTam supports the following types of buttons:   `callback` &mdash; sends a notification to a bot (via WebHook or long polling)   `link` &mdash; makes a user to follow a link   `request_contact` &mdash; requests the user permission to access contact information (phone number, short link, email)   You may also send a message with an [InlineKeyboard]() type attachment to start creating buttons. When the user presses a button, the bot receives the answer with filled callback field. It is recommended to edit that message so the user can receive updated buttons. # Versioning API models and interface may change over time. To make sure your bot will get the right info, we strongly recommend adding API version number to each request. You can add it as `v` parameter to each HTTP-request. For instance, `v=0.1.2`. To specify the data model version you are getting through WebHook subscription, use the `version` property in the request body of the [subscribe](https://dev.tamtam.chat/#operation/subscribe) request. # Libraries We have created [Java library](https://github.com/tamtam-chat/tamtam-bot-api) to make using API easier. # Changelog ##### Version 0.1.7  - It is now **required** to pass `marker` parameter in [/updates](#operation/getUpdates) requests, except initial  - Added full `User` object to update types: bot_started, bot_added, bot_removed, user_added, user_removed, chat_title_changed - Added `size` and `filename` to [`FileAttachment`](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.json#L1916) - Added [`token`](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.json#L1957) property to video/audio/file attachments allows you to reuse attachments uploaded by another user  ##### Version 0.1.6 - Added method to [edit bot info](#operation/editMyInfo) - Added statistics for messages in channel - `Message.sender` and `UserWithPhoto.avatar_url/full_avatar_url` removed from required properties  ##### Version 0.1.5 - Added `id` property to media attachments (`VideoAttachment`, `AudioAttachment`) so you can reuse attachment from one message in another - Added ability to create *linked* message: replied or forwarded. See `link` in `NewMessageBody` - `intent` property marked as required only for `CallbackButton`  ##### Version 0.1.4  - Added `user_ids` parameter to [get members](#operation/getMembers) in chat by id - `attachment` property of [send message](#operation/sendMessage) request body marked as deprecated  ##### Version 0.1.3 - Added method to [delete](https://dev.tamtam.chat/#operation/deleteMessages) messages - Added ability to [get](https://dev.tamtam.chat/#operation/getMessages) particular messages by ID - Added `is_admin` flag to `ChatMember` - Added `message` property to `MessageCallbackUpdate` - Renamed property `message` to `body` for `Message` schema - Added reusable `token` to `PhotoAttachment`. It allows to attach the same photo more than once.  # noqa: E501

    OpenAPI spec version: 0.1.8
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from .user_with_photo import UserWithPhoto


class ChatMember(UserWithPhoto):
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
        'user_id': 'int',
        'name': 'str',
        'username': 'str',
        'avatar_url': 'str',
        'full_avatar_url': 'str',
        'last_access_time': 'int',
        'is_owner': 'bool',
        'is_admin': 'bool',
        'join_time': 'int',
        'permissions': 'list[ChatAdminPermission]'
    }

    attribute_map = {
        'user_id': 'user_id',
        'name': 'name',
        'username': 'username',
        'avatar_url': 'avatar_url',
        'full_avatar_url': 'full_avatar_url',
        'last_access_time': 'last_access_time',
        'is_owner': 'is_owner',
        'is_admin': 'is_admin',
        'join_time': 'join_time',
        'permissions': 'permissions'
    }

    def __init__(self, user_id=None, name=None, username=None, avatar_url=None, full_avatar_url=None, last_access_time=None, is_owner=None, is_admin=None, join_time=None, permissions=None):  # noqa: E501
        """ChatMember - a model defined in OpenAPI"""  # noqa: E501

        super(ChatMember, self).__init__(user_id, name, username, avatar_url, full_avatar_url)
        self._last_access_time = None
        self._is_owner = None
        self._is_admin = None
        self._join_time = None
        self._permissions = None
        self.discriminator = None

        self.last_access_time = last_access_time
        self.is_owner = is_owner
        self.is_admin = is_admin
        self.join_time = join_time
        self.permissions = permissions

    @property
    def last_access_time(self):
        """Gets the last_access_time of this ChatMember.  # noqa: E501


        :return: The last_access_time of this ChatMember.  # noqa: E501
        :rtype: int
        """
        return self._last_access_time

    @last_access_time.setter
    def last_access_time(self, last_access_time):
        """Sets the last_access_time of this ChatMember.


        :param last_access_time: The last_access_time of this ChatMember.  # noqa: E501
        :type: int
        """
        if last_access_time is None:
            raise ValueError("Invalid value for `last_access_time`, must not be `None`")  # noqa: E501

        self._last_access_time = last_access_time

    @property
    def is_owner(self):
        """Gets the is_owner of this ChatMember.  # noqa: E501


        :return: The is_owner of this ChatMember.  # noqa: E501
        :rtype: bool
        """
        return self._is_owner

    @is_owner.setter
    def is_owner(self, is_owner):
        """Sets the is_owner of this ChatMember.


        :param is_owner: The is_owner of this ChatMember.  # noqa: E501
        :type: bool
        """
        if is_owner is None:
            raise ValueError("Invalid value for `is_owner`, must not be `None`")  # noqa: E501

        self._is_owner = is_owner

    @property
    def is_admin(self):
        """Gets the is_admin of this ChatMember.  # noqa: E501


        :return: The is_admin of this ChatMember.  # noqa: E501
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """Sets the is_admin of this ChatMember.


        :param is_admin: The is_admin of this ChatMember.  # noqa: E501
        :type: bool
        """
        if is_admin is None:
            raise ValueError("Invalid value for `is_admin`, must not be `None`")  # noqa: E501

        self._is_admin = is_admin

    @property
    def join_time(self):
        """Gets the join_time of this ChatMember.  # noqa: E501


        :return: The join_time of this ChatMember.  # noqa: E501
        :rtype: int
        """
        return self._join_time

    @join_time.setter
    def join_time(self, join_time):
        """Sets the join_time of this ChatMember.


        :param join_time: The join_time of this ChatMember.  # noqa: E501
        :type: int
        """
        if join_time is None:
            raise ValueError("Invalid value for `join_time`, must not be `None`")  # noqa: E501

        self._join_time = join_time

    @property
    def permissions(self):
        """Gets the permissions of this ChatMember.  # noqa: E501

        Permissions in chat if member is admin. `null` otherwise  # noqa: E501

        :return: The permissions of this ChatMember.  # noqa: E501
        :rtype: list[ChatAdminPermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this ChatMember.

        Permissions in chat if member is admin. `null` otherwise  # noqa: E501

        :param permissions: The permissions of this ChatMember.  # noqa: E501
        :type: list[ChatAdminPermission]
        """

        self._permissions = permissions

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
        if not isinstance(other, ChatMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

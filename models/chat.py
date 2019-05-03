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


class Chat(object):
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
        'chat_id': 'int',
        'type': 'ChatType',
        'status': 'ChatStatus',
        'title': 'str',
        'icon': 'Image',
        'last_event_time': 'int',
        'participants_count': 'int',
        'owner_id': 'int',
        'participants': 'dict(str, int)',
        'is_public': 'bool',
        'link': 'str',
        'description': 'object'
    }

    attribute_map = {
        'chat_id': 'chat_id',
        'type': 'type',
        'status': 'status',
        'title': 'title',
        'icon': 'icon',
        'last_event_time': 'last_event_time',
        'participants_count': 'participants_count',
        'owner_id': 'owner_id',
        'participants': 'participants',
        'is_public': 'is_public',
        'link': 'link',
        'description': 'description'
    }

    def __init__(self, chat_id=None, type=None, status=None, title=None, icon=None, last_event_time=None, participants_count=None, owner_id=None, participants=None, is_public=None, link=None, description=None):  # noqa: E501
        """Chat - a model defined in OpenAPI"""  # noqa: E501

        self._chat_id = None
        self._type = None
        self._status = None
        self._title = None
        self._icon = None
        self._last_event_time = None
        self._participants_count = None
        self._owner_id = None
        self._participants = None
        self._is_public = None
        self._link = None
        self._description = None
        self.discriminator = None

        self.chat_id = chat_id
        self.type = type
        self.status = status
        self.title = title
        self.icon = icon
        self.last_event_time = last_event_time
        self.participants_count = participants_count
        self.owner_id = owner_id
        self.participants = participants
        self.is_public = is_public
        self.link = link
        self.description = description

    @property
    def chat_id(self):
        """Gets the chat_id of this Chat.  # noqa: E501

        Chats identifier  # noqa: E501

        :return: The chat_id of this Chat.  # noqa: E501
        :rtype: int
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        """Sets the chat_id of this Chat.

        Chats identifier  # noqa: E501

        :param chat_id: The chat_id of this Chat.  # noqa: E501
        :type: int
        """
        if chat_id is None:
            raise ValueError("Invalid value for `chat_id`, must not be `None`")  # noqa: E501

        self._chat_id = chat_id

    @property
    def type(self):
        """Gets the type of this Chat.  # noqa: E501

        Type of chat. One of: dialog, chat, channel  # noqa: E501

        :return: The type of this Chat.  # noqa: E501
        :rtype: ChatType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Chat.

        Type of chat. One of: dialog, chat, channel  # noqa: E501

        :param type: The type of this Chat.  # noqa: E501
        :type: ChatType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def status(self):
        """Gets the status of this Chat.  # noqa: E501

        Chat status. One of:  - active: bot is active member of chat  - removed: bot was kicked  - left: bot intentionally left chat  - closed: chat was closed  # noqa: E501

        :return: The status of this Chat.  # noqa: E501
        :rtype: ChatStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Chat.

        Chat status. One of:  - active: bot is active member of chat  - removed: bot was kicked  - left: bot intentionally left chat  - closed: chat was closed  # noqa: E501

        :param status: The status of this Chat.  # noqa: E501
        :type: ChatStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def title(self):
        """Gets the title of this Chat.  # noqa: E501

        Visible title of chat. Can be null for dialogs  # noqa: E501

        :return: The title of this Chat.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Chat.

        Visible title of chat. Can be null for dialogs  # noqa: E501

        :param title: The title of this Chat.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def icon(self):
        """Gets the icon of this Chat.  # noqa: E501

        Icon of chat  # noqa: E501

        :return: The icon of this Chat.  # noqa: E501
        :rtype: Image
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this Chat.

        Icon of chat  # noqa: E501

        :param icon: The icon of this Chat.  # noqa: E501
        :type: Image
        """

        self._icon = icon

    @property
    def last_event_time(self):
        """Gets the last_event_time of this Chat.  # noqa: E501

        Time of last event occured in chat  # noqa: E501

        :return: The last_event_time of this Chat.  # noqa: E501
        :rtype: int
        """
        return self._last_event_time

    @last_event_time.setter
    def last_event_time(self, last_event_time):
        """Sets the last_event_time of this Chat.

        Time of last event occured in chat  # noqa: E501

        :param last_event_time: The last_event_time of this Chat.  # noqa: E501
        :type: int
        """
        if last_event_time is None:
            raise ValueError("Invalid value for `last_event_time`, must not be `None`")  # noqa: E501

        self._last_event_time = last_event_time

    @property
    def participants_count(self):
        """Gets the participants_count of this Chat.  # noqa: E501

        Number of people in chat. Always 2 for `dialog` chat type  # noqa: E501

        :return: The participants_count of this Chat.  # noqa: E501
        :rtype: int
        """
        return self._participants_count

    @participants_count.setter
    def participants_count(self, participants_count):
        """Sets the participants_count of this Chat.

        Number of people in chat. Always 2 for `dialog` chat type  # noqa: E501

        :param participants_count: The participants_count of this Chat.  # noqa: E501
        :type: int
        """
        if participants_count is None:
            raise ValueError("Invalid value for `participants_count`, must not be `None`")  # noqa: E501

        self._participants_count = participants_count

    @property
    def owner_id(self):
        """Gets the owner_id of this Chat.  # noqa: E501

        Identifier of chat owner. Visible only for chat admins  # noqa: E501

        :return: The owner_id of this Chat.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Chat.

        Identifier of chat owner. Visible only for chat admins  # noqa: E501

        :param owner_id: The owner_id of this Chat.  # noqa: E501
        :type: int
        """

        self._owner_id = owner_id

    @property
    def participants(self):
        """Gets the participants of this Chat.  # noqa: E501

        Participants in chat with time of last activity. Can be *null* when you request list of chats. Visible for chat admins only  # noqa: E501

        :return: The participants of this Chat.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """Sets the participants of this Chat.

        Participants in chat with time of last activity. Can be *null* when you request list of chats. Visible for chat admins only  # noqa: E501

        :param participants: The participants of this Chat.  # noqa: E501
        :type: dict(str, int)
        """

        self._participants = participants

    @property
    def is_public(self):
        """Gets the is_public of this Chat.  # noqa: E501

        Is current chat publicly available. Always `false` for dialogs  # noqa: E501

        :return: The is_public of this Chat.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this Chat.

        Is current chat publicly available. Always `false` for dialogs  # noqa: E501

        :param is_public: The is_public of this Chat.  # noqa: E501
        :type: bool
        """
        if is_public is None:
            raise ValueError("Invalid value for `is_public`, must not be `None`")  # noqa: E501

        self._is_public = is_public

    @property
    def link(self):
        """Gets the link of this Chat.  # noqa: E501

        Link on chat if it is public  # noqa: E501

        :return: The link of this Chat.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this Chat.

        Link on chat if it is public  # noqa: E501

        :param link: The link of this Chat.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def description(self):
        """Gets the description of this Chat.  # noqa: E501

        Chat description  # noqa: E501

        :return: The description of this Chat.  # noqa: E501
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Chat.

        Chat description  # noqa: E501

        :param description: The description of this Chat.  # noqa: E501
        :type: object
        """

        self._description = description

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
        if not isinstance(other, Chat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

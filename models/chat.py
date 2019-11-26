# coding: utf-8

"""
    TamTam Bot API

    # About Bot API allows bots to interact with TamTam. Methods are called by sending HTTPS requests to [botapi.tamtam.chat](https://botapi.tamtam.chat) domain. Bots are third-party applications that use TamTam features. A bot can legitimately take part in a conversation. It can be achieved through HTTP requests to the TamTam Bot API.  ## Features TamTam bots of the current version are able to: - Communicate with users and respond to requests - Recommend users complete actions via programmed buttons - Request personal data from users (name, short reference, phone number) We'll keep working on expanding bot capabilities in the future.  ## Examples Bots can be used for the following purposes: - Providing support, answering frequently asked questions - Sending typical information - Voting - Likes/dislikes - Following external links - Forwarding a user to a chat/channel  ## @PrimeBot [PrimeBot](https://tt.me/primebot) is the main bot in TamTam, all bots creator. Use PrimeBot to create and edit your bots. Feel free to contact us for any questions, [@support](https://tt.me/support) or [team@tamtam.chat](mailto:team@tamtam.chat).  ## HTTP verbs `GET` &mdash; getting resources, parameters are transmitted via URL  `POST` &mdash; creation of resources (for example, sending new messages)  `PUT` &mdash; editing resources  `DELETE` &mdash; deleting resources  `PATCH` &mdash; patching resources  ## HTTP response codes `200` &mdash; successful operation  `400` &mdash; invalid request  `401` &mdash; authentication error  `404` &mdash; resource not found  `405` &mdash; method is not allowed  `429` &mdash; the number of requests is exceeded  `503` &mdash; service unavailable  ## Resources format For content requests (PUT and POST) and responses, the API uses the JSON format. All strings are UTF-8 encoded. Date/time fields are represented as the number of milliseconds that have elapsed since 00:00 January 1, 1970 in the long format. To get it, you can simply multiply the UNIX timestamp by 1000. All date/time fields have a UTC timezone. ## Error responses In case of an error, the API returns a response with the corresponding HTTP code and JSON with the following fields:  `code` - the string with the error key  `message` - a string describing the error </br>  For example: ```bash > http https://botapi.tamtam.chat/chats?access_token={EXAMPLE_TOKEN} HTTP / 1.1 403 Forbidden Cache-Control: no-cache Connection: Keep-Alive Content-Length: 57 Content-Type: application / json; charset = utf-8 Set-Cookie: web_ui_lang = ru; Path = /; Domain = .tamtam.chat; Expires = 2019-03-24T11: 45: 36.500Z {    \"code\": \"verify.token\",    \"message\": \"Invalid access_token\" } ``` ## Receiving Notifications TamTam Bot API supports 2 options of receiving notifications on new dialog events for bots: - Push notifications via WebHook. To receive data via WebHook, you'll have to [add subscription](https://dev.tamtam.chat/#operation/subscribe); - Notifications upon request via [long polling](#operation/getUpdates) API. All data can be received via long polling **by default** after creating the bot,  Both methods **cannot** be used simultaneously. Refer to the response schema of [/updates](https://dev.tamtam.chat/#operation/getUpdates) method to check all available types of updates.  ## Message buttons You can program buttons for users answering a bot. TamTam supports the following types of buttons:  `callback` &mdash; sends a notification with payload to a bot (via WebHook or long polling)  `link` &mdash; makes a user to follow a link  `request_contact` &mdash; requests the user permission to access contact information (phone number, short link, email)  `request_geo_location` &mdash; asks user to provide current geo location  `chat` &mdash; creates chat associated with message  To start create buttons [send message](#operation/sendMessage) with `InlineKeyboardAttachment`: ```json {   \"text\": \"It is message with inline keyboard\",   \"attachments\": [     {       \"type\": \"inline_keyboard\",       \"payload\": {         \"buttons\": [           [             {               \"type\": \"callback\",               \"text\": \"Press me!\",               \"payload\": \"button1 pressed\"             }           ],           [             {               \"type\": \"chat\",               \"text\": \"Discuss\",               \"chat_title\": \"Message discussion\"             }           ]         ]       }     }   ] } ``` ### Chat button Chat button is a button that starts chat assosiated with the current message. It will be **private** chat with a link, bot will be added as administrator by default.  Chat will be created as soon as the first user taps on button. Bot will receive `message_chat_created` update.  Bot can set title and description of new chat by setting `chat_title` and `chat_description` properties.  Whereas keyboard can contain several `chat`-buttons there is `uuid` property to distinct them between each other. In case you do not pass `uuid` we will generate it. If you edit message, pass `uuid` so we know that this button starts the same chat as before.  Chat button also can contain `start_payload` that will be sent to bot as part of `message_chat_created` update.  ## Deep linking TamTam supports deep linking mechanism for bots. It allows passing additional payload to the bot on startup. Deep link can contain any data encoded into string up to **128** characters long. Longer strings will be omitted and **not** passed to the bot.  Each bot has start link that looks like: ``` https://tt.me/%BOT_USERNAME%/start/%PAYLOAD% ``` As soon as user clicks on such link we open dialog with bot and send this payload to bot as part of `bot_started` update: ```json {     \"update_type\": \"bot_started\",     \"timestamp\": 1573226679188,     \"chat_id\": 1234567890,     \"user\": {         \"user_id\": 1234567890,         \"name\": \"Boris\",         \"username\": \"borisd84\"     },     \"payload\": \"any data meaningful to bot\" } ```  Deep linking mechanism is supported for iOS version 2.7.0 and Android 2.9.0 and higher.  # Versioning API models and interface may change over time. To make sure your bot will get the right info, we strongly recommend adding API version number to each request. You can add it as `v` parameter to each HTTP-request. For instance, `v=0.1.2`. To specify the data model version you are getting through WebHook subscription, use the `version` property in the request body of the [subscribe](https://dev.tamtam.chat/#operation/subscribe) request.  # Libraries We have created [Java library](https://github.com/tamtam-chat/tamtam-bot-api) to make using API easier.  # Changelog ##### Version 0.1.10 - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/a9ef3a1b8f4e1a75b55a9b80877eddc2c6f07ec4) `disable_link_preview` parameter to POST:/messages method to disable links parsing in text - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/eb99e8ab97b55fa196d9957fca34d2316a4ca8aa) `sending_file` action - [Removed](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/7a5ab5f0ea1336b3460d1827a6a7b3b141e19776) several deprecated properties - `photo` upload type [renamed](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/74505883e6acb306686a6d141414aeaf5131ef49) to `image`. *C* is for consistency  ##### Version 0.1.9 - Added method to [get chat administrators](#operation/getAdmins) - For `type: dialog` chats [added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/ff9e2472941d4dd2de540db0d0ea8b9c3d0ed01a#diff-7e9de78f42fb0d2ae80878b90c87300aR1160) `dialog_with_user` - Added `url` for [messages](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/137dd9dfa4e583d429f017ba69c20caa9deac105) in public chats/channels - [**Removed**](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/ff9e2472941d4dd2de540db0d0ea8b9c3d0ed01a) `callback_id` of `InlineKeyboardAttachment` - [**Removed**](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/2ebf36b22758ea3487304f5b0d0d811798e78b61) `user_id` of `CallbackAnswer`. It is no longer required. Just use `callback_id` of `Callback` - Several minor improvements: check [diff](https://github.com/tamtam-chat/tamtam-bot-api-schema/compare/beccbe5f4fbed32182a13e257ca1cfae7f40ea8d...master) for all changes  ##### Version 0.1.8 - Added `code`, `width`, `height` to [StickerAttachment](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1580) - `token` is now only one required property for video/audio/file attachments - `sender` and `chat_id` of [LinkedMessage](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1401) are now optional - Added clarifying `message` to [SimpleQueryResult](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1938)  To see changelog for older versions visit our [GitHub](https://github.com/tamtam-chat/tamtam-bot-api-schema/releases).  # noqa: E501

    OpenAPI spec version: 0.1.11
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
        'description': 'object',
        'dialog_with_user': 'UserWithPhoto',
        'messages_count': 'int',
        'chat_message_id': 'str'
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
        'description': 'description',
        'dialog_with_user': 'dialog_with_user',
        'messages_count': 'messages_count',
        'chat_message_id': 'chat_message_id'
    }

    def __init__(self, chat_id=None, type=None, status=None, title=None, icon=None, last_event_time=None, participants_count=None, owner_id=None, participants=None, is_public=None, link=None, description=None, dialog_with_user=None, messages_count=None, chat_message_id=None):  # noqa: E501
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
        self._dialog_with_user = None
        self._messages_count = None
        self._chat_message_id = None
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
        self.dialog_with_user = dialog_with_user
        self.messages_count = messages_count
        self.chat_message_id = chat_message_id

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

        Time of last event occurred in chat  # noqa: E501

        :return: The last_event_time of this Chat.  # noqa: E501
        :rtype: int
        """
        return self._last_event_time

    @last_event_time.setter
    def last_event_time(self, last_event_time):
        """Sets the last_event_time of this Chat.

        Time of last event occurred in chat  # noqa: E501

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

    @property
    def dialog_with_user(self):
        """Gets the dialog_with_user of this Chat.  # noqa: E501

        Another user in conversation. For `dialog` type chats only  # noqa: E501

        :return: The dialog_with_user of this Chat.  # noqa: E501
        :rtype: UserWithPhoto
        """
        return self._dialog_with_user

    @dialog_with_user.setter
    def dialog_with_user(self, dialog_with_user):
        """Sets the dialog_with_user of this Chat.

        Another user in conversation. For `dialog` type chats only  # noqa: E501

        :param dialog_with_user: The dialog_with_user of this Chat.  # noqa: E501
        :type: UserWithPhoto
        """

        self._dialog_with_user = dialog_with_user

    @property
    def messages_count(self):
        """Gets the messages_count of this Chat.  # noqa: E501

        Messages count in chat. Only for group chats and channels. **Not available** for dialogs  # noqa: E501

        :return: The messages_count of this Chat.  # noqa: E501
        :rtype: int
        """
        return self._messages_count

    @messages_count.setter
    def messages_count(self, messages_count):
        """Sets the messages_count of this Chat.

        Messages count in chat. Only for group chats and channels. **Not available** for dialogs  # noqa: E501

        :param messages_count: The messages_count of this Chat.  # noqa: E501
        :type: int
        """

        self._messages_count = messages_count

    @property
    def chat_message_id(self):
        """Gets the chat_message_id of this Chat.  # noqa: E501

        Identifier of message that contains `chat` button initialized chat  # noqa: E501

        :return: The chat_message_id of this Chat.  # noqa: E501
        :rtype: str
        """
        return self._chat_message_id

    @chat_message_id.setter
    def chat_message_id(self, chat_message_id):
        """Sets the chat_message_id of this Chat.

        Identifier of message that contains `chat` button initialized chat  # noqa: E501

        :param chat_message_id: The chat_message_id of this Chat.  # noqa: E501
        :type: str
        """

        self._chat_message_id = chat_message_id

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

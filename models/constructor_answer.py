# coding: utf-8

# noinspection SpellCheckingInspection
"""
    TamTam Bot API

    # About Bot API allows bots to interact with TamTam. Methods are called by sending HTTPS requests to [botapi.tamtam.chat](https://botapi.tamtam.chat) domain. Bots are third-party applications that use TamTam features. A bot can legitimately take part in a conversation. It can be achieved through HTTP requests to the TamTam Bot API.  ## Features TamTam bots of the current version are able to: - Communicate with users and respond to requests - Recommend users complete actions via programmed buttons - Request personal data from users (name, short reference, phone number) We'll keep working on expanding bot capabilities in the future.  ## Examples Bots can be used for the following purposes: - Providing support, answering frequently asked questions - Sending typical information - Voting - Likes/dislikes - Following external links - Forwarding a user to a chat/channel  ## @PrimeBot [PrimeBot](https://tt.me/primebot) is the main bot in TamTam, all bots creator. Use PrimeBot to create and edit your bots. Feel free to contact us for any questions, [@support](https://tt.me/support) or [team@tamtam.chat](mailto:team@tamtam.chat).  ## HTTP verbs `GET` &mdash; getting resources, parameters are transmitted via URL  `POST` &mdash; creation of resources (for example, sending new messages)  `PUT` &mdash; editing resources  `DELETE` &mdash; deleting resources  `PATCH` &mdash; patching resources  ## HTTP response codes `200` &mdash; successful operation  `400` &mdash; invalid request  `401` &mdash; authentication error  `404` &mdash; resource not found  `405` &mdash; method is not allowed  `429` &mdash; the number of requests is exceeded  `503` &mdash; service unavailable  ## Resources format For content requests (PUT and POST) and responses, the API uses the JSON format. All strings are UTF-8 encoded. Date/time fields are represented as the number of milliseconds that have elapsed since 00:00 January 1, 1970 in the long format. To get it, you can simply multiply the UNIX timestamp by 1000. All date/time fields have a UTC timezone. ## Error responses In case of an error, the API returns a response with the corresponding HTTP code and JSON with the following fields:  `code` - the string with the error key  `message` - a string describing the error </br>  For example: ```bash > http https://botapi.tamtam.chat/chats?access_token={EXAMPLE_TOKEN} HTTP / 1.1 403 Forbidden Cache-Control: no-cache Connection: Keep-Alive Content-Length: 57 Content-Type: application / json; charset = utf-8 Set-Cookie: web_ui_lang = ru; Path = /; Domain = .tamtam.chat; Expires = 2019-03-24T11: 45: 36.500Z {    \"code\": \"verify.token\",    \"message\": \"Invalid access_token\" } ``` ## Receiving Notifications TamTam Bot API supports 2 options of receiving notifications on new dialog events for bots: - Push notifications via WebHook. To receive data via WebHook, you'll have to [add subscription](https://dev.tamtam.chat/#operation/subscribe); - Notifications upon request via [long polling](#operation/getUpdates) API. All data can be received via long polling **by default** after creating the bot,  Both methods **cannot** be used simultaneously. Refer to the response schema of [/updates](https://dev.tamtam.chat/#operation/getUpdates) method to check all available types of updates.  ## Message buttons You can program buttons for users answering a bot. TamTam supports the following types of buttons:  `callback` &mdash; sends a notification with payload to a bot (via WebHook or long polling)  `link` &mdash; makes a user to follow a link  `request_contact` &mdash; requests the user permission to access contact information (phone number, short link, email)  `request_geo_location` &mdash; asks user to provide current geo location  `chat` &mdash; creates chat associated with message  To start create buttons [send message](#operation/sendMessage) with `InlineKeyboardAttachment`: ```json {   \"text\": \"It is message with inline keyboard\",   \"attachments\": [     {       \"type\": \"inline_keyboard\",       \"payload\": {         \"buttons\": [           [             {               \"type\": \"callback\",               \"text\": \"Press me!\",               \"payload\": \"button1 pressed\"             }           ],           [             {               \"type\": \"chat\",               \"text\": \"Discuss\",               \"chat_title\": \"Message discussion\"             }           ]         ]       }     }   ] } ``` ### Chat button Chat button is a button that starts chat assosiated with the current message. It will be **private** chat with a link, bot will be added as administrator by default.  Chat will be created as soon as the first user taps on button. Bot will receive `message_chat_created` update.  Bot can set title and description of new chat by setting `chat_title` and `chat_description` properties.  Whereas keyboard can contain several `chat`-buttons there is `uuid` property to distinct them between each other. In case you do not pass `uuid` we will generate it. If you edit message, pass `uuid` so we know that this button starts the same chat as before.  Chat button also can contain `start_payload` that will be sent to bot as part of `message_chat_created` update.  ## Deep linking TamTam supports deep linking mechanism for bots. It allows passing additional payload to the bot on startup. Deep link can contain any data encoded into string up to **128** characters long. Longer strings will be omitted and **not** passed to the bot.  Each bot has start link that looks like: ``` https://tt.me/%BOT_USERNAME%/start/%PAYLOAD% ``` As soon as user clicks on such link we open dialog with bot and send this payload to bot as part of `bot_started` update: ```json {     \"update_type\": \"bot_started\",     \"timestamp\": 1573226679188,     \"chat_id\": 1234567890,     \"user\": {         \"user_id\": 1234567890,         \"name\": \"Boris\",         \"username\": \"borisd84\"     },     \"payload\": \"any data meaningful to bot\" } ```  Deep linking mechanism is supported for iOS version 2.7.0 and Android 2.9.0 and higher.  # Versioning API models and interface may change over time. To make sure your bot will get the right info, we strongly recommend adding API version number to each request. You can add it as `v` parameter to each HTTP-request. For instance, `v=0.1.2`. To specify the data model version you are getting through WebHook subscription, use the `version` property in the request body of the [subscribe](https://dev.tamtam.chat/#operation/subscribe) request.  # Libraries We have created [Java library](https://github.com/tamtam-chat/tamtam-bot-api) to make using API easier.  # Changelog ##### Version 0.1.10 - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/a9ef3a1b8f4e1a75b55a9b80877eddc2c6f07ec4) `disable_link_preview` parameter to POST:/messages method to disable links parsing in text - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/eb99e8ab97b55fa196d9957fca34d2316a4ca8aa) `sending_file` action - [Removed](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/7a5ab5f0ea1336b3460d1827a6a7b3b141e19776) several deprecated properties - `photo` upload type [renamed](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/74505883e6acb306686a6d141414aeaf5131ef49) to `image`. *C* is for consistency  ##### Version 0.1.9 - Added method to [get chat administrators](#operation/getAdmins) - For `type: dialog` chats [added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/ff9e2472941d4dd2de540db0d0ea8b9c3d0ed01a#diff-7e9de78f42fb0d2ae80878b90c87300aR1160) `dialog_with_user` - Added `url` for [messages](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/137dd9dfa4e583d429f017ba69c20caa9deac105) in public chats/channels - [**Removed**](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/ff9e2472941d4dd2de540db0d0ea8b9c3d0ed01a) `callback_id` of `InlineKeyboardAttachment` - [**Removed**](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/2ebf36b22758ea3487304f5b0d0d811798e78b61) `user_id` of `CallbackAnswer`. It is no longer required. Just use `callback_id` of `Callback` - Several minor improvements: check [diff](https://github.com/tamtam-chat/tamtam-bot-api-schema/compare/beccbe5f4fbed32182a13e257ca1cfae7f40ea8d...master) for all changes  ##### Version 0.1.8 - Added `code`, `width`, `height` to [StickerAttachment](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1580) - `token` is now only one required property for video/audio/file attachments - `sender` and `chat_id` of [LinkedMessage](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1401) are now optional - Added clarifying `message` to [SimpleQueryResult](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1938)  To see changelog for older versions visit our [GitHub](https://github.com/tamtam-chat/tamtam-bot-api-schema/releases).  # noqa: E501

    OpenAPI spec version: 0.1.11
    Generated by: https://openapi-generator.tech
"""


import pprint

import six


class ConstructorAnswer(object):
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
        'messages': 'list[NewMessageBody]',
        'allow_user_input': 'bool',
        'hint': 'str',
        'data': 'String',
        'keyboard': 'Keyboard',
        'placeholder': 'str'
    }

    attribute_map = {
        'messages': 'messages',
        'allow_user_input': 'allow_user_input',
        'hint': 'hint',
        'data': 'data',
        'keyboard': 'keyboard',
        'placeholder': 'placeholder'
    }

    def __init__(self, messages=None, allow_user_input=None, hint=None, data=None, keyboard=None, placeholder=None):  # noqa: E501
        """ConstructorAnswer - a model defined in OpenAPI"""  # noqa: E501

        self._messages = None
        self._allow_user_input = None
        self._hint = None
        self._data = None
        self._keyboard = None
        self._placeholder = None
        self.discriminator = None

        if messages is not None:
            self.messages = messages
        if allow_user_input is not None:
            self.allow_user_input = allow_user_input
        self.hint = hint
        if data is not None:
            self.data = data
        self.keyboard = keyboard
        self.placeholder = placeholder

    @property
    def messages(self):
        """Gets the messages of this ConstructorAnswer.  # noqa: E501

        Array of prepared messages. This messages will be sent as user taps on \"Send\" button  # noqa: E501

        :return: The messages of this ConstructorAnswer.  # noqa: E501
        :rtype: list[NewMessageBody]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this ConstructorAnswer.

        Array of prepared messages. This messages will be sent as user taps on \"Send\" button  # noqa: E501

        :param messages: The messages of this ConstructorAnswer.  # noqa: E501
        :type: list[NewMessageBody]
        """

        self._messages = messages

    @property
    def allow_user_input(self):
        """Gets the allow_user_input of this ConstructorAnswer.  # noqa: E501

        If `true` user can send any input manually. Otherwise, only keyboard will be shown  # noqa: E501

        :return: The allow_user_input of this ConstructorAnswer.  # noqa: E501
        :rtype: bool
        """
        return self._allow_user_input

    @allow_user_input.setter
    def allow_user_input(self, allow_user_input):
        """Sets the allow_user_input of this ConstructorAnswer.

        If `true` user can send any input manually. Otherwise, only keyboard will be shown  # noqa: E501

        :param allow_user_input: The allow_user_input of this ConstructorAnswer.  # noqa: E501
        :type: bool
        """

        self._allow_user_input = allow_user_input

    @property
    def hint(self):
        """Gets the hint of this ConstructorAnswer.  # noqa: E501

        Hint to user. Will be shown on top of keyboard  # noqa: E501

        :return: The hint of this ConstructorAnswer.  # noqa: E501
        :rtype: str
        """
        return self._hint

    @hint.setter
    def hint(self, hint):
        """Sets the hint of this ConstructorAnswer.

        Hint to user. Will be shown on top of keyboard  # noqa: E501

        :param hint: The hint of this ConstructorAnswer.  # noqa: E501
        :type: str
        """

        self._hint = hint

    @property
    def data(self):
        """Gets the data of this ConstructorAnswer.  # noqa: E501

        In this property you can store any additional data up to 8KB. We send this data back to bot within the next construction request. It is handy to store here any state of construction session  # noqa: E501

        :return: The data of this ConstructorAnswer.  # noqa: E501
        :rtype: String
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ConstructorAnswer.

        In this property you can store any additional data up to 8KB. We send this data back to bot within the next construction request. It is handy to store here any state of construction session  # noqa: E501

        :param data: The data of this ConstructorAnswer.  # noqa: E501
        :type: String
        """

        self._data = data

    @property
    def keyboard(self):
        """Gets the keyboard of this ConstructorAnswer.  # noqa: E501

        Keyboard to show to user in constructor mode  # noqa: E501

        :return: The keyboard of this ConstructorAnswer.  # noqa: E501
        :rtype: Keyboard
        """
        return self._keyboard

    @keyboard.setter
    def keyboard(self, keyboard):
        """Sets the keyboard of this ConstructorAnswer.

        Keyboard to show to user in constructor mode  # noqa: E501

        :param keyboard: The keyboard of this ConstructorAnswer.  # noqa: E501
        :type: Keyboard
        """

        self._keyboard = keyboard

    @property
    def placeholder(self):
        """Gets the placeholder of this ConstructorAnswer.  # noqa: E501

        Text to show over the text field  # noqa: E501

        :return: The placeholder of this ConstructorAnswer.  # noqa: E501
        :rtype: str
        """
        return self._placeholder

    @placeholder.setter
    def placeholder(self, placeholder):
        """Sets the placeholder of this ConstructorAnswer.

        Text to show over the text field  # noqa: E501

        :param placeholder: The placeholder of this ConstructorAnswer.  # noqa: E501
        :type: str
        """

        self._placeholder = placeholder

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
        if not isinstance(other, ConstructorAnswer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

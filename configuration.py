# coding: utf-8

"""
    TamTam Bot API

    # About Bot API allows bots to interact with TamTam. Methods are called by sending HTTPS requests to [botapi.tamtam.chat](https://botapi.tamtam.chat) domain. Bots are third-party applications that use TamTam features. A bot can legitimately take part in a conversation. It can be achieved through HTTP requests to the TamTam Bot API. ## Features TamTam bots of the current version are able to: - Communicate with users and respond to requests - Recommend users complete actions via programmed buttons - Request personal data from users (name, short reference, phone number) We'll keep working on expanding bot capabilities in the future. ## Examples Bots can be used for the following purposes: - Providing support, answering frequently asked questions - Sending typical information - Voting - Likes/dislikes - Following external links - Forwarding a user to a chat/channel ## @PrimeBot We are beta testing bots in TamTam now. To become a beta tester, please, contact us on **[@support](https://tt.me/support)** or [team@tamtam.chat](mailto:team@tamtam.chat). We'll give you access to [PrimeBot](https://tt.me/primebot), all TamTam bots creator. It will help you choose a unique short name for a bot and fill in its full name and description. With PrimeBot you can create bots as well as edit and delete them and browse information on bots you have created. #### [PrimeBot](https://tt.me/primebot) commands: `/start` &mdash; start a dialog with a bot  `/create` &mdash; create a bot, assign the unique short name to it (from 4 to 64 characters)  `/set_name [name]` &mdash; assign a short or full name to the bot (up to 200 characters)  `/set_description [description]` &mdash; enter the description for the bot profile (up to 400 characters)  `/set_picture [URL]` &mdash; enter the URL of bot's picture  `/delete [username]` &mdash; delete the bot  `/list` &mdash; show the list of all bots  `/get_token` &mdash; obtain a token for a bot  `/revoke` &mdash; request a new token  `/help` &mdash; help  ## HTTP verbs `GET` &mdash; getting resources, parameters are transmitted via URL  `POST` &mdash; creation of resources (for example, sending new messages)  `PUT` &mdash; editing resources  `DELETE` &mdash; deleting resources  `PATCH` &mdash; patching resources ## HTTP response codes `200` &mdash; successful operation  `400` &mdash; invalid request  `401` &mdash; authentication error  `404` &mdash; resource not found  `405` &mdash; method not allowed  `429` &mdash; the number of requests is exceeded  `503` &mdash; service unavailable  ## Resources format For content requests (PUT and POST) and responses, the API uses the JSON format. All strings are UTF-8 encoded. Date/time fields are represented as the number of milliseconds that have elapsed since 00:00 January 1, 1970 in the long format. To get it, you can simply multiply the UNIX timestamp by 1000. All date/time fields have a UTC timezone. ## Error responses In case of an error, the API returns a response with the corresponding HTTP code and JSON with the following fields:   `code` - the string with the error key   `message` - a string describing the error </br>  For example: ```bash > http https://botapi.tamtam.chat/chats?access_token={EXAMPLE_TOKEN} HTTP / 1.1 403 Forbidden Cache-Control: no-cache Connection: Keep-Alive Content-Length: 57 Content-Type: application / json; charset = utf-8 Set-Cookie: web_ui_lang = ru; Path = /; Domain = .tamtam.chat; Expires = 2019-03-24T11: 45: 36.500Z {    \"code\": \"verify.token\",    \"message\": \"Invalid access_token\" } ``` ## Receiving Notifications TamTam Bot API supports 2 options of receiving notifications on new dialog events for bots: - Push notifications via WebHook. To receive data via WebHook, you'll have to [add subscription](https://dev.tamtam.chat/#operation/subscribe); - Notifications upon request via [long polling](#operation/getUpdates) API. All data can be received via long polling **by default** after creating the bot,  Both methods **cannot** be used simultaneously. Refer to the response schema of [/updates](https://dev.tamtam.chat/#operation/getUpdates) method to check all available types of updates. ## Message buttons You can program buttons for users answering a bot. TamTam supports the following types of buttons:   `callback` &mdash; sends a notification to a bot (via WebHook or long polling)   `link` &mdash; makes a user to follow a link   `request_contact` &mdash; requests the user permission to access contact information (phone number, short link, email)   You may also send a message with an [InlineKeyboard]() type attachment to start creating buttons. When the user presses a button, the bot receives the answer with filled callback field. It is recommended to edit that message so the user can receive updated buttons. # Versioning API models and interface may change over time. To make sure your bot will get the right info, we strongly recommend adding API version number to each request. You can add it as `v` parameter to each HTTP-request. For instance, `v=0.1.2`. To specify the data model version you are getting through WebHook subscription, use the `version` property in the request body of the [subscribe](https://dev.tamtam.chat/#operation/subscribe) request. # Libraries We have created [Java library](https://github.com/tamtam-chat/tamtam-bot-api) to make using API easier. # Changelog ##### Version 0.1.6 - Added method to [edit bot info](#operation/editMyInfo) - Added statistics for messages in channel - `Message.sender` and `UserWithPhoto.avatar_url/full_avatar_url` removed from required properties  ##### Version 0.1.5 - Added `id` property to media attachments (`VideoAttachment`, `AudioAttachment`) so you can reuse attachment from one message in another - Added ability to create *linked* message: replied or forwarded. See `link` in `NewMessageBody` - `intent` property marked as required only for `CallbackButton`  ##### Version 0.1.4  - Added `user_ids` parameter to [get members](#operation/getMembers) in chat by id - `attachment` property of [send message](#operation/sendMessage) request body marked as deprecated  ##### Version 0.1.3 - Added method to [delete](https://dev.tamtam.chat/#operation/deleteMessages) messages - Added ability to [get](https://dev.tamtam.chat/#operation/getMessages) particular messages by ID - Added `is_admin` flag to `ChatMember` - Added `message` property to `MessageCallbackUpdate` - Renamed property `message` to `body` for `Message` schema - Added reusable `token` to `PhotoAttachment`. It allows to attach the same photo more than once.  # noqa: E501

    OpenAPI spec version: 0.1.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import copy
import logging
import multiprocessing
import sys
import urllib3

import six
from six.moves import http_client as httplib


class TypeWithDefault(type):
    def __init__(cls, name, bases, dct):
        super(TypeWithDefault, cls).__init__(name, bases, dct)
        cls._default = None

    def __call__(cls):
        if cls._default is None:
            cls._default = type.__call__(cls)
        return copy.copy(cls._default)

    def set_default(cls, default):
        cls._default = copy.copy(default)


class Configuration(six.with_metaclass(TypeWithDefault, object)):
    api_version = '0.1.7'
    """NOTE: This class is auto generated by OpenAPI Generator

    Ref: https://openapi-generator.tech
    Do not edit the class manually.
    """

    def __init__(self):
        """Constructor"""
        # Default Base url
        self.host = "https://botapi.tamtam.chat"
        # self.host = "https://test2.tamtam.chat"
        # Temp file folder for downloading files
        self.temp_folder_path = None

        # Authentication Settings
        # dict to store API key(s)
        self.api_key = {}
        # dict to store API prefix (e.g. Bearer)
        self.api_key_prefix = {}
        # Username for HTTP basic authentication
        self.username = ""
        # Password for HTTP basic authentication
        self.password = ""

        # Logging Settings
        self.logger = {}
        self.logger["package_logger"] = logging.getLogger("openapi_client")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        # Log format
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        # Log stream handler
        self.logger_stream_handler = None
        # Log file handler
        self.logger_file_handler = None
        # Debug file location
        self.logger_file = None
        # Debug switch
        self.debug = False

        # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate when calling API
        # from https server.
        self.verify_ssl = True
        # Set this to customize the certificate file to verify the peer.
        self.ssl_ca_cert = None
        # client certificate file
        self.cert_file = None
        # client key file
        self.key_file = None
        # Set this to True/False to enable/disable SSL hostname verification.
        self.assert_hostname = None

        # urllib3 connection pool's maximum number of connections saved
        # per pool. urllib3 uses 1 connection as default value, but this is
        # not the best value when you are making a lot of possibly parallel
        # requests to the same host, which is often the case here.
        # cpu_count * 5 is used as default value to increase performance.
        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5

        # Proxy URL
        self.proxy = None
        # Safe chars for path_param
        self.safe_chars_for_path_param = ''

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier):
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :return: The token for api key authentication.
        """
        if (self.api_key.get(identifier) and
                self.api_key_prefix.get(identifier)):
            return self.api_key_prefix[identifier] + ' ' + self.api_key[identifier]  # noqa: E501
        elif self.api_key.get(identifier):
            return self.api_key[identifier]

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        return urllib3.util.make_headers(
            basic_auth=self.username + ':' + self.password
        ).get('authorization')

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        return {
            'access_token':
                {
                    'type': 'api_key',
                    'in': 'query',
                    'key': 'access_token',
                    'value': self.get_api_key_with_prefix('access_token')
                },

        }

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n" \
               "OS: {env}\n" \
               "Python Version: {pyversion}\n" \
               "Version of the API: {api_version}\n" \
               "SDK Package Version: 1.0.0". \
            format(env=sys.platform, pyversion=sys.version, api_version=self.api_version)

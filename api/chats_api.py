# coding: utf-8

"""
    TamTam Bot API

    # About Bot API allows bots to interact with TamTam. Methods are called by sending HTTPS requests to [botapi.tamtam.chat](https://botapi.tamtam.chat) domain. Bots are third-party applications that use TamTam features. A bot can legitimately take part in a conversation. It can be achieved through HTTP requests to the TamTam Bot API.  ## Features TamTam bots of the current version are able to: - Communicate with users and respond to requests - Recommend users complete actions via programmed buttons - Request personal data from users (name, short reference, phone number) We'll keep working on expanding bot capabilities in the future.  ## Examples Bots can be used for the following purposes: - Providing support, answering frequently asked questions - Sending typical information - Voting - Likes/dislikes - Following external links - Forwarding a user to a chat/channel  ## @PrimeBot [PrimeBot](https://tt.me/primebot) is the main bot in TamTam, all bots creator. Use PrimeBot to create and edit your bots. Feel free to contact us for any questions, [@support](https://tt.me/support) or [team@tamtam.chat](mailto:team@tamtam.chat).  ## HTTP verbs `GET` &mdash; getting resources, parameters are transmitted via URL  `POST` &mdash; creation of resources (for example, sending new messages)  `PUT` &mdash; editing resources  `DELETE` &mdash; deleting resources  `PATCH` &mdash; patching resources  ## HTTP response codes `200` &mdash; successful operation  `400` &mdash; invalid request  `401` &mdash; authentication error  `404` &mdash; resource not found  `405` &mdash; method is not allowed  `429` &mdash; the number of requests is exceeded  `503` &mdash; service unavailable  ## Resources format For content requests (PUT and POST) and responses, the API uses the JSON format. All strings are UTF-8 encoded. Date/time fields are represented as the number of milliseconds that have elapsed since 00:00 January 1, 1970 in the long format. To get it, you can simply multiply the UNIX timestamp by 1000. All date/time fields have a UTC timezone. ## Error responses In case of an error, the API returns a response with the corresponding HTTP code and JSON with the following fields:  `code` - the string with the error key  `message` - a string describing the error </br>  For example: ```bash > http https://botapi.tamtam.chat/chats?access_token={EXAMPLE_TOKEN} HTTP / 1.1 403 Forbidden Cache-Control: no-cache Connection: Keep-Alive Content-Length: 57 Content-Type: application / json; charset = utf-8 Set-Cookie: web_ui_lang = ru; Path = /; Domain = .tamtam.chat; Expires = 2019-03-24T11: 45: 36.500Z {    \"code\": \"verify.token\",    \"message\": \"Invalid access_token\" } ``` ## Receiving notifications TamTam Bot API supports 2 options of receiving notifications on new events for bots: - Push notifications via WebHook. To receive data via WebHook, you'll have to [add subscription](https://dev.tamtam.chat/#operation/subscribe); - Notifications upon request via [long polling](#operation/getUpdates) API. All data can be received via long polling **by default** after creating the bot.  Both methods **cannot** be used simultaneously. Refer to the response schema of [/updates](https://dev.tamtam.chat/#operation/getUpdates) method to check all available types of updates.  ### Webhook There is some notes about how we handle webhook subscription: 1. Sometimes webhook notification cannot be delivered in case when bot server or network is down.    In such case we well retry delivery in a short period of time (from 30 to 60 seconds) and will do this until get   `200 OK` status code from your server, but not longer than **8 hours** (*may change over time*) since update happened.    We also consider any non `200`-response from server as failed delivery.  2. To protect your bot from unexpected high load we send **no more than 100** notifications per second by default.   If you want increase this limit, contact us at [@support](https://tt.me/support).   It should be from one of the following subnets: ``` 185.16.150.0/30 185.16.150.84/30 185.16.150.152/30 185.16.150.192/30 ```   ## Message buttons You can program buttons for users answering a bot. TamTam supports the following types of buttons:  `callback` &mdash; sends a notification with payload to a bot (via WebHook or long polling)  `link` &mdash; makes a user to follow a link  `request_contact` &mdash; requests the user permission to access contact information (phone number, short link, email)  `request_geo_location` &mdash; asks user to provide current geo location  `chat` &mdash; creates chat associated with message  To start create buttons [send message](#operation/sendMessage) with `InlineKeyboardAttachment`: ```json {   \"text\": \"It is message with inline keyboard\",   \"attachments\": [     {       \"type\": \"inline_keyboard\",       \"payload\": {         \"buttons\": [           [             {               \"type\": \"callback\",               \"text\": \"Press me!\",               \"payload\": \"button1 pressed\"             }           ],           [             {               \"type\": \"chat\",               \"text\": \"Discuss\",               \"chat_title\": \"Message discussion\"             }           ]         ]       }     }   ] } ``` ### Chat button Chat button is a button that starts chat assosiated with the current message. It will be **private** chat with a link, bot will be added as administrator by default.  Chat will be created as soon as the first user taps on button. Bot will receive `message_chat_created` update.  Bot can set title and description of new chat by setting `chat_title` and `chat_description` properties.  Whereas keyboard can contain several `chat`-buttons there is `uuid` property to distinct them between each other. In case you do not pass `uuid` we will generate it. If you edit message, pass `uuid` so we know that this button starts the same chat as before.  Chat button also can contain `start_payload` that will be sent to bot as part of `message_chat_created` update.  ## Deep linking TamTam supports deep linking mechanism for bots. It allows passing additional payload to the bot on startup. Deep link can contain any data encoded into string up to **128** characters long. Longer strings will be omitted and **not** passed to the bot.  Each bot has start link that looks like: ``` https://tt.me/%BOT_USERNAME%/start/%PAYLOAD% ``` As soon as user clicks on such link we open dialog with bot and send this payload to bot as part of `bot_started` update: ```json {     \"update_type\": \"bot_started\",     \"timestamp\": 1573226679188,     \"chat_id\": 1234567890,     \"user\": {         \"user_id\": 1234567890,         \"name\": \"Boris\",         \"username\": \"borisd84\"     },     \"payload\": \"any data meaningful to bot\" } ```  Deep linking mechanism is supported for iOS version 2.7.0 and Android 2.9.0 and higher.  ## Constructors Constructor is a bot that can create a message for user: add buttons, attach some media, insert text.  You can enable constructor mode for your bot via [@PrimeBot](https://tt.me/primebot) sending [/constructor_mode](https://tt.me/primebot/start/constructor_mode) command.  For bot developers, it looks like request-response interaction where TamTam application sends `message_construction_request` on behalf of user. Bot [responds](#operation/construct) to it with `messages` ready to go or `keyboard` in case it requires further action from user.  Bot also can set up UI parts such as `hint` or `placeholder`, allow or not user's input: ![Constructor UI parts](https://dev.tamtam.chat/static/hint-079a332a51a2e9e6d415ec716389661b.png)  As soon as user finishes composing a message, they can post it. Bot will receive `message_constructed_update` with posted message.  Constructors are supported for iOS version 2.7.0 and Android 2.9.0 and higher.  ## Text formatting  Message text can be improved with basic formatting such as: **strong**, *emphasis*, ~strikethough~,  <ins>underline</ins>, `code` or link. You can use either markdown-like or HTML formatting.  To enable text formatting set the `format` property of [NewMessageBody](#tag/new_message_model).  ### TamTam flavored Markdown To enable [Markdown](https://spec.commonmark.org/0.29/) parsing, set the `format` property of [NewMessageBody](#tag/new_message_model) to `markdown`.  We currently support only the following syntax:  `*empasized*` or `_empasized_` for *italic* text  `**strong**` or `__strong__` for __bold__ text  `~~strikethough~~`  for ~strikethough~ text  `++underline++`  for <ins>underlined</ins> text  ``` `code` ``` or ` ```code``` ` for `monospaced` text  `^^important^^` for highlighted text (colored in red, by default)  `[Inline URL](https://dev.tamtam.chat/)` for inline URLs  `[User mention](tamtam://user/%user_id%)` for user mentions without username  ### HTML support  To enable HTML parsing, set the `format` property of [NewMessageBody](#tag/new_message_model) to `html`.   Only the following HTML tags are supported. All others will be stripped:  Emphasized: `<i>` or `<em>`  Strong: `<b>` or `<strong>`  Strikethrough: `<del>` or `<s>`  Underlined: `<ins>` or `<u>`  Link: `<a href=\"https://dev.tamtam.chat\">Docs</a>`  Monospaced text: `<pre>` or `<code>`  Highlighted text: `<mark>`  Text formatting is supported for iOS since version 3.1 and Android since 2.20.0.  # Versioning API models and interface may change over time. To make sure your bot will get the right info, we strongly recommend adding API version number to each request. You can add it as `v` parameter to each HTTP-request. For instance, `v=0.1.2`. To specify the data model version you are getting through WebHook subscription, use the `version` property in the request body of the [subscribe](https://dev.tamtam.chat/#operation/subscribe) request.  # Libraries We have developed the official [Java client](https://github.com/tamtam-chat/tamtam-bot-api) and [SDK](https://github.com/tamtam-chat/tamtam-bot-sdk).  Also check out unofficial libraries, created by our enthusiasts: - [Kotlin DSL client](https://github.com/Namazed/TamTamBotApiClientDsl) - [GO client](https://github.com/neonxp/tamtam) - [Node.js module](https://github.com/vershininivan/node-tamtam-botapi)  #### Python: - [Python client](https://github.com/asvbkr/openapi_client) - [tamtam.py](https://github.com/uwinx/tamtam.py) - [registriren/botapitamtam](https://github.com/registriren/botapitamtam)  # Changelog ##### Version 0.3.0 - Added methods to [pin](#operation/pinMessage)/[unpin](#operation/unpinMessage) messages in chats/channels - Added `is_bot` flag to [`User`](#tag/user_model) model  Check out the complete [diff](https://github.com/tamtam-chat/tamtam-bot-api-schema/compare/v0.2.1..v0.3.0) for this release.  ##### Version 0.2.1 - [Added](#operation/getChatByLink) method to get chat by its `@link` - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/compare/v0.2.0..HEAD#diff-7e9de78f42fb0d2ae80878b90c87300aR1240) `description` for users in some cases - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/compare/v0.2.0..HEAD#diff-7e9de78f42fb0d2ae80878b90c87300aR2555) `user_locale` to `message_created` update in dialogs  Check out the complete [diff](https://github.com/tamtam-chat/tamtam-bot-api-schema/compare/v0.2.0..v0.2.1) for this release.  ##### Version 0.2.0 - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/09c95259d6c8c424f82b50eab93872e7db2ca208) new type of button to start new chat - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/ea4581d83d7132663d6cc5c2c61c058a2bd46aac) Constructors API that allows bots to create message on behalf of a user - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/c5ff03175407819aceebd9c25de49eed566a0ce1) support for deep-links - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/ff4cc4f93662d6c25db11fac72d9fcbf1f66cad8) ability to block users in chats - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/b965bfb0d02933e819435312e6ab184a3dfc0250) `chat_id` and `user_id` to `message_removed` update - Added meta information for video attachments - Other minor improvements and fixes. Check out complete [diff](https://github.com/tamtam-chat/tamtam-bot-api-schema/compare/v0.1.11...v0.1.10) for this version  ##### Version 0.1.10 - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/a9ef3a1b8f4e1a75b55a9b80877eddc2c6f07ec4) `disable_link_preview` parameter to POST:/messages method to disable links parsing in text - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/eb99e8ab97b55fa196d9957fca34d2316a4ca8aa) `sending_file` action - [Removed](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/7a5ab5f0ea1336b3460d1827a6a7b3b141e19776) several deprecated properties - `photo` upload type [renamed](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/74505883e6acb306686a6d141414aeaf5131ef49) to `image`. *C* is for consistency  To see changelog for older versions visit our [GitHub](https://github.com/tamtam-chat/tamtam-bot-api-schema/releases).  # noqa: E501

    OpenAPI spec version: 0.5.2
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient


class ChatsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_members(self, chat_id, user_ids_list, **kwargs):  # noqa: E501
        """Add members  # noqa: E501

        Adds members to chat. Additional permissions may require.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_members(chat_id, user_ids_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier (required)
        :param UserIdsList user_ids_list: (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_members_with_http_info(chat_id, user_ids_list, **kwargs)  # noqa: E501
        else:
            (data) = self.add_members_with_http_info(chat_id, user_ids_list, **kwargs)  # noqa: E501
            return data

    def add_members_with_http_info(self, chat_id, user_ids_list, **kwargs):  # noqa: E501
        """Add members  # noqa: E501

        Adds members to chat. Additional permissions may require.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_members_with_http_info(chat_id, user_ids_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier (required)
        :param UserIdsList user_ids_list: (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['chat_id', 'user_ids_list']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_members" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in local_var_params or
                local_var_params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `add_members`")  # noqa: E501
        # verify the required parameter 'user_ids_list' is set
        if ('user_ids_list' not in local_var_params or
                local_var_params['user_ids_list'] is None):
            raise ValueError("Missing the required parameter `user_ids_list` when calling `add_members`")  # noqa: E501

        if 'chat_id' in local_var_params and not re.search('-?\\d+', str(local_var_params['chat_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `chat_id` when calling `add_members`, must conform to the pattern `/\\-?\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chatId'] = local_var_params['chat_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_ids_list' in local_var_params:
            body_params = local_var_params['user_ids_list']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/chats/{chatId}/members', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimpleQueryResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def edit_chat(self, chat_id, chat_patch, **kwargs):  # noqa: E501
        """Edit chat info  # noqa: E501

        Edits chat info: title, icon, etc…  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_chat(chat_id, chat_patch, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier (required)
        :param ChatPatch chat_patch: (required)
        :return: Chat
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.edit_chat_with_http_info(chat_id, chat_patch, **kwargs)  # noqa: E501
        else:
            (data) = self.edit_chat_with_http_info(chat_id, chat_patch, **kwargs)  # noqa: E501
            return data

    def edit_chat_with_http_info(self, chat_id, chat_patch, **kwargs):  # noqa: E501
        """Edit chat info  # noqa: E501

        Edits chat info: title, icon, etc…  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_chat_with_http_info(chat_id, chat_patch, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier (required)
        :param ChatPatch chat_patch: (required)
        :return: Chat
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['chat_id', 'chat_patch']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_chat" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in local_var_params or
                local_var_params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `edit_chat`")  # noqa: E501
        # verify the required parameter 'chat_patch' is set
        if ('chat_patch' not in local_var_params or
                local_var_params['chat_patch'] is None):
            raise ValueError("Missing the required parameter `chat_patch` when calling `edit_chat`")  # noqa: E501

        if 'chat_id' in local_var_params and not re.search('-?\\d+', str(local_var_params['chat_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `chat_id` when calling `edit_chat`, must conform to the pattern `/\\-?\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chatId'] = local_var_params['chat_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'chat_patch' in local_var_params:
            body_params = local_var_params['chat_patch']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/chats/{chatId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Chat',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_admins(self, chat_id, **kwargs):  # noqa: E501
        """Get chat admins  # noqa: E501

        Returns all chat administrators. Bot must be **administrator** in requested chat.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admins(chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier (required)
        :return: ChatMembersList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_admins_with_http_info(chat_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_admins_with_http_info(chat_id, **kwargs)  # noqa: E501
            return data

    def get_admins_with_http_info(self, chat_id, **kwargs):  # noqa: E501
        """Get chat admins  # noqa: E501

        Returns all chat administrators. Bot must be **administrator** in requested chat.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admins_with_http_info(chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier (required)
        :return: ChatMembersList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['chat_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_admins" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in local_var_params or
                local_var_params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `get_admins`")  # noqa: E501

        if 'chat_id' in local_var_params and not re.search('-?\\d+', str(local_var_params['chat_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `chat_id` when calling `get_admins`, must conform to the pattern `/\\-\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chatId'] = local_var_params['chat_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/chats/{chatId}/members/admins', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChatMembersList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_chat(self, chat_id, **kwargs):  # noqa: E501
        """Get chat  # noqa: E501

        Returns info about chat.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chat(chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Requested chat identifier (required)
        :return: Chat
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_chat_with_http_info(chat_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_chat_with_http_info(chat_id, **kwargs)  # noqa: E501
            return data

    def get_chat_with_http_info(self, chat_id, **kwargs):  # noqa: E501
        """Get chat  # noqa: E501

        Returns info about chat.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chat_with_http_info(chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Requested chat identifier (required)
        :return: Chat
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['chat_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chat" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in local_var_params or
                local_var_params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `get_chat`")  # noqa: E501

        if 'chat_id' in local_var_params and not re.search('-?\\d+', str(local_var_params['chat_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `chat_id` when calling `get_chat`, must conform to the pattern `/\\-?\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chatId'] = local_var_params['chat_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/chats/{chatId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Chat',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_chat_by_link(self, chat_link, **kwargs):  # noqa: E501
        """Get chat by link  # noqa: E501

        Returns chat/channel information by its public link or dialog with user by username  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chat_by_link(chat_link, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str chat_link: Public chat link or username (required)
        :return: Chat
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_chat_by_link_with_http_info(chat_link, **kwargs)  # noqa: E501
        else:
            (data) = self.get_chat_by_link_with_http_info(chat_link, **kwargs)  # noqa: E501
            return data

    def get_chat_by_link_with_http_info(self, chat_link, **kwargs):  # noqa: E501
        """Get chat by link  # noqa: E501

        Returns chat/channel information by its public link or dialog with user by username  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chat_by_link_with_http_info(chat_link, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str chat_link: Public chat link or username (required)
        :return: Chat
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['chat_link']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chat_by_link" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'chat_link' is set
        if ('chat_link' not in local_var_params or
                local_var_params['chat_link'] is None):
            raise ValueError("Missing the required parameter `chat_link` when calling `get_chat_by_link`")  # noqa: E501

        if 'chat_link' in local_var_params and not re.search(r'@?[a-zA-Z]+[a-zA-Z0-9-_]*', local_var_params['chat_link']):  # noqa: E501
            raise ValueError("Invalid value for parameter `chat_link` when calling `get_chat_by_link`, must conform to the pattern `/@?[a-zA-Z]+[a-zA-Z0-9-_]*/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'chat_link' in local_var_params:
            path_params['chatLink'] = local_var_params['chat_link']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/chats/{chatLink}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Chat',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_chats(self, **kwargs):  # noqa: E501
        """Get all chats  # noqa: E501

        Returns information about chats that bot participated in: a result list and marker points to the next page  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int count: Number of chats requested
        :param int marker: Points to next data page. `null` for the first page
        :return: ChatList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_chats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_chats_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_chats_with_http_info(self, **kwargs):  # noqa: E501
        """Get all chats  # noqa: E501

        Returns information about chats that bot participated in: a result list and marker points to the next page  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int count: Number of chats requested
        :param int marker: Points to next data page. `null` for the first page
        :return: ChatList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['count', 'marker']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chats" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `count` when calling `get_chats`, must be a value less than or equal to `100`")  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `count` when calling `get_chats`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'count' in local_var_params:
            query_params.append(('count', local_var_params['count']))  # noqa: E501
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/chats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChatList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_members(self, chat_id, **kwargs):  # noqa: E501
        """Get members  # noqa: E501

        Returns users participated in chat.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_members(chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier (required)
        :param list[int] user_ids: *Since* version [0.1.4](#section/About/Changelog).  Comma-separated list of users identifiers to get their membership. When this parameter is passed, both `count` and `marker` are ignored
        :param int marker: Marker
        :param int count: Count
        :return: ChatMembersList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_members_with_http_info(chat_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_members_with_http_info(chat_id, **kwargs)  # noqa: E501
            return data

    def get_members_with_http_info(self, chat_id, **kwargs):  # noqa: E501
        """Get members  # noqa: E501

        Returns users participated in chat.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_members_with_http_info(chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier (required)
        :param list[int] user_ids: *Since* version [0.1.4](#section/About/Changelog).  Comma-separated list of users identifiers to get their membership. When this parameter is passed, both `count` and `marker` are ignored
        :param int marker: Marker
        :param int count: Count
        :return: ChatMembersList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['chat_id', 'user_ids', 'marker', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_members" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in local_var_params or
                local_var_params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `get_members`")  # noqa: E501

        if 'chat_id' in local_var_params and not re.search('-?\\d+', str(local_var_params['chat_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `chat_id` when calling `get_members`, must conform to the pattern `/\\-?\\d+/`")  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `count` when calling `get_members`, must be a value less than or equal to `100`")  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `count` when calling `get_members`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chatId'] = local_var_params['chat_id']  # noqa: E501

        query_params = []
        if 'user_ids' in local_var_params:
            query_params.append(('user_ids', local_var_params['user_ids']))  # noqa: E501
            collection_formats['user_ids'] = 'csv'  # noqa: E501
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))  # noqa: E501
        if 'count' in local_var_params:
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/chats/{chatId}/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChatMembersList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_membership(self, chat_id, **kwargs):  # noqa: E501
        """Get chat membership  # noqa: E501

        Returns chat membership info for current bot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_membership(chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier (required)
        :return: ChatMember
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_membership_with_http_info(chat_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_membership_with_http_info(chat_id, **kwargs)  # noqa: E501
            return data

    def get_membership_with_http_info(self, chat_id, **kwargs):  # noqa: E501
        """Get chat membership  # noqa: E501

        Returns chat membership info for current bot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_membership_with_http_info(chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier (required)
        :return: ChatMember
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['chat_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_membership" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in local_var_params or
                local_var_params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `get_membership`")  # noqa: E501

        if 'chat_id' in local_var_params and not re.search('-?\\d+', str(local_var_params['chat_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `chat_id` when calling `get_membership`, must conform to the pattern `/\\-?\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chatId'] = local_var_params['chat_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/chats/{chatId}/members/me', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChatMember',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_pinned_message(self, chat_id, **kwargs):  # noqa: E501
        """Get pinned message  # noqa: E501

        Get pinned message in chat or channel.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pinned_message(chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier to get its pinned message (required)
        :return: GetPinnedMessageResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_pinned_message_with_http_info(chat_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_pinned_message_with_http_info(chat_id, **kwargs)  # noqa: E501
            return data

    def get_pinned_message_with_http_info(self, chat_id, **kwargs):  # noqa: E501
        """Get pinned message  # noqa: E501

        Get pinned message in chat or channel.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pinned_message_with_http_info(chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier to get its pinned message (required)
        :return: GetPinnedMessageResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['chat_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pinned_message" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in local_var_params or
                local_var_params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `get_pinned_message`")  # noqa: E501

        if 'chat_id' in local_var_params and not re.search('-?\\d+', str(local_var_params['chat_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `chat_id` when calling `get_pinned_message`, must conform to the pattern `/\\-?\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chatId'] = local_var_params['chat_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/chats/{chatId}/pin', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetPinnedMessageResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def leave_chat(self, chat_id, **kwargs):  # noqa: E501
        """Leave chat  # noqa: E501

        Removes bot from chat members.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.leave_chat(chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.leave_chat_with_http_info(chat_id, **kwargs)  # noqa: E501
        else:
            (data) = self.leave_chat_with_http_info(chat_id, **kwargs)  # noqa: E501
            return data

    def leave_chat_with_http_info(self, chat_id, **kwargs):  # noqa: E501
        """Leave chat  # noqa: E501

        Removes bot from chat members.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.leave_chat_with_http_info(chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['chat_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method leave_chat" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in local_var_params or
                local_var_params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `leave_chat`")  # noqa: E501

        if 'chat_id' in local_var_params and not re.search('-?\\d+', str(local_var_params['chat_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `chat_id` when calling `leave_chat`, must conform to the pattern `/\\-?\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chatId'] = local_var_params['chat_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/chats/{chatId}/members/me', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimpleQueryResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pin_message(self, chat_id, pin_message_body, **kwargs):  # noqa: E501
        """Pin message  # noqa: E501

        Pins message in chat or channel.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pin_message(chat_id, pin_message_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier where message should be pinned (required)
        :param PinMessageBody pin_message_body: (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pin_message_with_http_info(chat_id, pin_message_body, **kwargs)  # noqa: E501
        else:
            (data) = self.pin_message_with_http_info(chat_id, pin_message_body, **kwargs)  # noqa: E501
            return data

    def pin_message_with_http_info(self, chat_id, pin_message_body, **kwargs):  # noqa: E501
        """Pin message  # noqa: E501

        Pins message in chat or channel.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pin_message_with_http_info(chat_id, pin_message_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier where message should be pinned (required)
        :param PinMessageBody pin_message_body: (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['chat_id', 'pin_message_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pin_message" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in local_var_params or
                local_var_params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `pin_message`")  # noqa: E501
        # verify the required parameter 'pin_message_body' is set
        if ('pin_message_body' not in local_var_params or
                local_var_params['pin_message_body'] is None):
            raise ValueError("Missing the required parameter `pin_message_body` when calling `pin_message`")  # noqa: E501

        if 'chat_id' in local_var_params and not re.search('-?\\d+', str(local_var_params['chat_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `chat_id` when calling `pin_message`, must conform to the pattern `/\\-?\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chatId'] = local_var_params['chat_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'pin_message_body' in local_var_params:
            body_params = local_var_params['pin_message_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/chats/{chatId}/pin', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimpleQueryResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_member(self, chat_id, user_id, **kwargs):  # noqa: E501
        """Remove member  # noqa: E501

        Removes member from chat. Additional permissions may require.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_member(chat_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier (required)
        :param int user_id: User id to remove from chat (required)
        :param bool block: Set to `true` if user should be blocked in chat. Applicable only for chats that have public or private link. Ignored otherwise
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_member_with_http_info(chat_id, user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_member_with_http_info(chat_id, user_id, **kwargs)  # noqa: E501
            return data

    def remove_member_with_http_info(self, chat_id, user_id, **kwargs):  # noqa: E501
        """Remove member  # noqa: E501

        Removes member from chat. Additional permissions may require.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_member_with_http_info(chat_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier (required)
        :param int user_id: User id to remove from chat (required)
        :param bool block: Set to `true` if user should be blocked in chat. Applicable only for chats that have public or private link. Ignored otherwise
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['chat_id', 'user_id', 'block']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_member" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in local_var_params or
                local_var_params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `remove_member`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in local_var_params or
                local_var_params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `remove_member`")  # noqa: E501

        if 'chat_id' in local_var_params and not re.search('-?\\d+', str(local_var_params['chat_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `chat_id` when calling `remove_member`, must conform to the pattern `/\\-?\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chatId'] = local_var_params['chat_id']  # noqa: E501

        query_params = []
        if 'user_id' in local_var_params:
            query_params.append(('user_id', local_var_params['user_id']))  # noqa: E501
        if 'block' in local_var_params:
            query_params.append(('block', local_var_params['block']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/chats/{chatId}/members', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimpleQueryResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_action(self, chat_id, action_request_body, **kwargs):  # noqa: E501
        """Send action  # noqa: E501

        Send bot action to chat  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_action(chat_id, action_request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier (required)
        :param ActionRequestBody action_request_body: (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_action_with_http_info(chat_id, action_request_body, **kwargs)  # noqa: E501
        else:
            (data) = self.send_action_with_http_info(chat_id, action_request_body, **kwargs)  # noqa: E501
            return data

    def send_action_with_http_info(self, chat_id, action_request_body, **kwargs):  # noqa: E501
        """Send action  # noqa: E501

        Send bot action to chat  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_action_with_http_info(chat_id, action_request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier (required)
        :param ActionRequestBody action_request_body: (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['chat_id', 'action_request_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_action" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in local_var_params or
                local_var_params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `send_action`")  # noqa: E501
        # verify the required parameter 'action_request_body' is set
        if ('action_request_body' not in local_var_params or
                local_var_params['action_request_body'] is None):
            raise ValueError("Missing the required parameter `action_request_body` when calling `send_action`")  # noqa: E501

        if 'chat_id' in local_var_params and not re.search('-?\\d+', str(local_var_params['chat_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `chat_id` when calling `send_action`, must conform to the pattern `/\\-?\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chatId'] = local_var_params['chat_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'action_request_body' in local_var_params:
            body_params = local_var_params['action_request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/chats/{chatId}/actions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimpleQueryResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def unpin_message(self, chat_id, **kwargs):  # noqa: E501
        """Unpin message  # noqa: E501

        Unpins message in chat or channel.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unpin_message(chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier to remove pinned message (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.unpin_message_with_http_info(chat_id, **kwargs)  # noqa: E501
        else:
            (data) = self.unpin_message_with_http_info(chat_id, **kwargs)  # noqa: E501
            return data

    def unpin_message_with_http_info(self, chat_id, **kwargs):  # noqa: E501
        """Unpin message  # noqa: E501

        Unpins message in chat or channel.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unpin_message_with_http_info(chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier to remove pinned message (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['chat_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unpin_message" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in local_var_params or
                local_var_params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `unpin_message`")  # noqa: E501

        if 'chat_id' in local_var_params and not re.search('-?\\d+', str(local_var_params['chat_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `chat_id` when calling `unpin_message`, must conform to the pattern `/\\-?\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chatId'] = local_var_params['chat_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/chats/{chatId}/pin', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimpleQueryResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

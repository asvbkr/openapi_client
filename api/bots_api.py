# coding: utf-8

"""
    TamTam Bot API

    # About Bot API allows bots to interact with TamTam. Methods are called by sending HTTPS requests to [botapi.tamtam.chat](https://botapi.tamtam.chat) domain. Bots are third-party applications that use TamTam features. A bot can legitimately take part in a conversation. It can be achieved through HTTP requests to the TamTam Bot API. ## Features TamTam bots of the current version are able to: - Communicate with users and respond to requests - Recommend users complete actions via programmed buttons - Request personal data from users (name, short reference, phone number) We'll keep working on expanding bot capabilities in the future. ## Examples Bots can be used for the following purposes: - Providing support, answering frequently asked questions - Sending typical information - Voting - Likes/dislikes - Following external links - Forwarding a user to a chat/channel ## @PrimeBot We are beta testing bots in TamTam now. To become a beta tester, please, contact us on **[@support](https://tt.me/support)** or [team@tamtam.chat](mailto:team@tamtam.chat). We'll give you access to [PrimeBot](https://tt.me/primebot), all TamTam bots creator. It will help you choose a unique short name for a bot and fill in its full name and description. With PrimeBot you can create bots as well as edit and delete them and browse information on bots you have created. #### [PrimeBot](https://tt.me/primebot) commands: `/start` &mdash; start a dialog with a bot  `/create` &mdash; create a bot, assign the unique short name to it (from 4 to 64 characters)  `/set_name [name]` &mdash; assign a short or full name to the bot (up to 200 characters)  `/set_description [description]` &mdash; enter the description for the bot profile (up to 400 characters)  `/set_picture [URL]` &mdash; enter the URL of bot's picture  `/delete [username]` &mdash; delete the bot  `/list` &mdash; show the list of all bots  `/get_token` &mdash; obtain a token for a bot  `/revoke` &mdash; request a new token  `/help` &mdash; help  ## HTTP verbs `GET` &mdash; getting resources, parameters are transmitted via URL  `POST` &mdash; creation of resources (for example, sending new messages)  `PUT` &mdash; editing resources  `DELETE` &mdash; deleting resources  `PATCH` &mdash; patching resources ## HTTP response codes `200` &mdash; successful operation  `400` &mdash; invalid request  `401` &mdash; authentication error  `404` &mdash; resource not found  `405` &mdash; method not allowed  `429` &mdash; the number of requests is exceeded  `503` &mdash; service unavailable  ## Resources format For content requests (PUT and POST) and responses, the API uses the JSON format. All strings are UTF-8 encoded. Date/time fields are represented as the number of milliseconds that have elapsed since 00:00 January 1, 1970 in the long format. To get it, you can simply multiply the UNIX timestamp by 1000. All date/time fields have a UTC timezone. ## Error responses In case of an error, the API returns a response with the corresponding HTTP code and JSON with the following fields:   `code` - the string with the error key   `message` - a string describing the error </br>  For example: ```bash > http https://botapi.tamtam.chat/chats?access_token={EXAMPLE_TOKEN} HTTP / 1.1 403 Forbidden Cache-Control: no-cache Connection: Keep-Alive Content-Length: 57 Content-Type: application / json; charset = utf-8 Set-Cookie: web_ui_lang = ru; Path = /; Domain = .tamtam.chat; Expires = 2019-03-24T11: 45: 36.500Z {    \"code\": \"verify.token\",    \"message\": \"Invalid access_token\" } ``` ## Receiving Notifications TamTam Bot API supports 2 options of receiving notifications on new dialog events for bots: - Push notifications via WebHook. To receive data via WebHook, you'll have to [add subscription](https://dev.tamtam.chat/#operation/subscribe); - Notifications upon request via [long polling](#operation/getUpdates) API. All data can be received via long polling **by default** after creating the bot,  Both methods **cannot** be used simultaneously. Refer to the response schema of [/updates](https://dev.tamtam.chat/#operation/getUpdates) method to check all available types of updates. ## Message buttons You can program buttons for users answering a bot. TamTam supports the following types of buttons:   `callback` &mdash; sends a notification to a bot (via WebHook or long polling)   `link` &mdash; makes a user to follow a link   `request_contact` &mdash; requests the user permission to access contact information (phone number, short link, email)   You may also send a message with an [InlineKeyboard]() type attachment to start creating buttons. When the user presses a button, the bot receives the answer with filled callback field. It is recommended to edit that message so the user can receive updated buttons. # Versioning API models and interface may change over time. To make sure your bot will get the right info, we strongly recommend adding API version number to each request. You can add it as `v` parameter to each HTTP-request. For instance, `v=0.1.2`. To specify the data model version you are getting through WebHook subscription, use the `version` property in the request body of the [subscribe](https://dev.tamtam.chat/#operation/subscribe) request. # Libraries We have created [Java library](https://github.com/tamtam-chat/tamtam-bot-api) to make using API easier. # Changelog ##### Version 0.1.7  - It is now **required** to pass `marker` parameter in [/updates](#operation/getUpdates) requests, except initial  - Added full `User` object to update types: bot_started, bot_added, bot_removed, user_added, user_removed, chat_title_changed - Added `size` and `filename` to [`FileAttachment`](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.json#L1916) - Added [`token`](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.json#L1957) property to video/audio/file attachments allows you to reuse attachments uploaded by another user  ##### Version 0.1.6 - Added method to [edit bot info](#operation/editMyInfo) - Added statistics for messages in channel - `Message.sender` and `UserWithPhoto.avatar_url/full_avatar_url` removed from required properties  ##### Version 0.1.5 - Added `id` property to media attachments (`VideoAttachment`, `AudioAttachment`) so you can reuse attachment from one message in another - Added ability to create *linked* message: replied or forwarded. See `link` in `NewMessageBody` - `intent` property marked as required only for `CallbackButton`  ##### Version 0.1.4  - Added `user_ids` parameter to [get members](#operation/getMembers) in chat by id - `attachment` property of [send message](#operation/sendMessage) request body marked as deprecated  ##### Version 0.1.3 - Added method to [delete](https://dev.tamtam.chat/#operation/deleteMessages) messages - Added ability to [get](https://dev.tamtam.chat/#operation/getMessages) particular messages by ID - Added `is_admin` flag to `ChatMember` - Added `message` property to `MessageCallbackUpdate` - Renamed property `message` to `body` for `Message` schema - Added reusable `token` to `PhotoAttachment`. It allows to attach the same photo more than once.  # noqa: E501

    OpenAPI spec version: 0.1.8
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient


class BotsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def edit_my_info(self, bot_patch, **kwargs):  # noqa: E501
        """Edit current bot info  # noqa: E501

        Edits current bot info. Fill only the fields you want to update. All remaining fields will stay untouched  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_my_info(bot_patch, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BotPatch bot_patch: (required)
        :return: BotInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.edit_my_info_with_http_info(bot_patch, **kwargs)  # noqa: E501
        else:
            (data) = self.edit_my_info_with_http_info(bot_patch, **kwargs)  # noqa: E501
            return data

    def edit_my_info_with_http_info(self, bot_patch, **kwargs):  # noqa: E501
        """Edit current bot info  # noqa: E501

        Edits current bot info. Fill only the fields you want to update. All remaining fields will stay untouched  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_my_info_with_http_info(bot_patch, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BotPatch bot_patch: (required)
        :return: BotInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['bot_patch']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_my_info" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'bot_patch' is set
        if ('bot_patch' not in local_var_params or
                local_var_params['bot_patch'] is None):
            raise ValueError("Missing the required parameter `bot_patch` when calling `edit_my_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bot_patch' in local_var_params:
            body_params = local_var_params['bot_patch']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/me', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BotInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_my_info(self, **kwargs):  # noqa: E501
        """Get current bot info  # noqa: E501

        Returns info about current bot. Current bot can be identified by access token. Method returns bot identifier, name and avatar (if any)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_my_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: BotInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_my_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_my_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_my_info_with_http_info(self, **kwargs):  # noqa: E501
        """Get current bot info  # noqa: E501

        Returns info about current bot. Current bot can be identified by access token. Method returns bot identifier, name and avatar (if any)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_my_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: BotInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_my_info" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/me', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BotInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

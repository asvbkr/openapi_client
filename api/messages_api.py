# coding: utf-8

"""
    TamTam Bot API

    # About Bot API allows bots to interact with TamTam. Methods are called by sending HTTPS requests to [botapi.tamtam.chat](https://botapi.tamtam.chat) domain. Bots are third-party applications that use TamTam features. A bot can legitimately take part in a conversation. It can be achieved through HTTP requests to the TamTam Bot API.  ## Features TamTam bots of the current version are able to: - Communicate with users and respond to requests - Recommend users complete actions via programmed buttons - Request personal data from users (name, short reference, phone number) We'll keep working on expanding bot capabilities in the future.  ## Examples Bots can be used for the following purposes: - Providing support, answering frequently asked questions - Sending typical information - Voting - Likes/dislikes - Following external links - Forwarding a user to a chat/channel  ## @PrimeBot [PrimeBot](https://tt.me/primebot) is the main bot in TamTam, all bots creator. Use PrimeBot to create and edit your bots. Feel free to contact us for any questions, [@support](https://tt.me/support) or [team@tamtam.chat](mailto:team@tamtam.chat).  ## HTTP verbs `GET` &mdash; getting resources, parameters are transmitted via URL  `POST` &mdash; creation of resources (for example, sending new messages)  `PUT` &mdash; editing resources  `DELETE` &mdash; deleting resources  `PATCH` &mdash; patching resources  ## HTTP response codes `200` &mdash; successful operation  `400` &mdash; invalid request  `401` &mdash; authentication error  `404` &mdash; resource not found  `405` &mdash; method is not allowed  `429` &mdash; the number of requests is exceeded  `503` &mdash; service unavailable  ## Resources format For content requests (PUT and POST) and responses, the API uses the JSON format. All strings are UTF-8 encoded. Date/time fields are represented as the number of milliseconds that have elapsed since 00:00 January 1, 1970 in the long format. To get it, you can simply multiply the UNIX timestamp by 1000. All date/time fields have a UTC timezone. ## Error responses In case of an error, the API returns a response with the corresponding HTTP code and JSON with the following fields:  `code` - the string with the error key  `message` - a string describing the error </br>  For example: ```bash > http https://botapi.tamtam.chat/chats?access_token={EXAMPLE_TOKEN} HTTP / 1.1 403 Forbidden Cache-Control: no-cache Connection: Keep-Alive Content-Length: 57 Content-Type: application / json; charset = utf-8 Set-Cookie: web_ui_lang = ru; Path = /; Domain = .tamtam.chat; Expires = 2019-03-24T11: 45: 36.500Z {    \"code\": \"verify.token\",    \"message\": \"Invalid access_token\" } ``` ## Receiving Notifications TamTam Bot API supports 2 options of receiving notifications on new dialog events for bots: - Push notifications via WebHook. To receive data via WebHook, you'll have to [add subscription](https://dev.tamtam.chat/#operation/subscribe); - Notifications upon request via [long polling](#operation/getUpdates) API. All data can be received via long polling **by default** after creating the bot,  Both methods **cannot** be used simultaneously. Refer to the response schema of [/updates](https://dev.tamtam.chat/#operation/getUpdates) method to check all available types of updates.  ## Message buttons You can program buttons for users answering a bot. TamTam supports the following types of buttons:  `callback` &mdash; sends a notification with payload to a bot (via WebHook or long polling)  `link` &mdash; makes a user to follow a link  `request_contact` &mdash; requests the user permission to access contact information (phone number, short link, email)  `request_geo_location` &mdash; asks user to provide current geo location  `chat` &mdash; creates chat associated with message  To start create buttons [send message](#operation/sendMessage) with `InlineKeyboardAttachment`: ```json {   \"text\": \"It is message with inline keyboard\",   \"attachments\": [     {       \"type\": \"inline_keyboard\",       \"payload\": {         \"buttons\": [           [             {               \"type\": \"callback\",               \"text\": \"Press me!\",               \"payload\": \"button1 pressed\"             }           ],           [             {               \"type\": \"chat\",               \"text\": \"Discuss\",               \"chat_title\": \"Message discussion\"             }           ]         ]       }     }   ] } ``` ### Chat button Chat button is a button that starts chat assosiated with the current message. It will be **private** chat with a link, bot will be added as administrator by default.  Chat will be created as soon as the first user taps on button. Bot will receive `message_chat_created` update.  Bot can set title and description of new chat by setting `chat_title` and `chat_description` properties.  Whereas keyboard can contain several `chat`-buttons there is `uuid` property to distinct them between each other. In case you do not pass `uuid` we will generate it. If you edit message, pass `uuid` so we know that this button starts the same chat as before.  Chat button also can contain `start_payload` that will be sent to bot as part of `message_chat_created` update.  ## Deep linking TamTam supports deep linking mechanism for bots. It allows passing additional payload to the bot on startup. Deep link can contain any data encoded into string up to **128** characters long. Longer strings will be omitted and **not** passed to the bot.  Each bot has start link that looks like: ``` https://tt.me/%BOT_USERNAME%/start/%PAYLOAD% ``` As soon as user clicks on such link we open dialog with bot and send this payload to bot as part of `bot_started` update: ```json {     \"update_type\": \"bot_started\",     \"timestamp\": 1573226679188,     \"chat_id\": 1234567890,     \"user\": {         \"user_id\": 1234567890,         \"name\": \"Boris\",         \"username\": \"borisd84\"     },     \"payload\": \"any data meaningful to bot\" } ```  Deep linking mechanism is supported for iOS version 2.7.0 and Android 2.9.0 and higher.  # Versioning API models and interface may change over time. To make sure your bot will get the right info, we strongly recommend adding API version number to each request. You can add it as `v` parameter to each HTTP-request. For instance, `v=0.1.2`. To specify the data model version you are getting through WebHook subscription, use the `version` property in the request body of the [subscribe](https://dev.tamtam.chat/#operation/subscribe) request.  # Libraries We have created [Java library](https://github.com/tamtam-chat/tamtam-bot-api) to make using API easier.  # Changelog ##### Version 0.1.10 - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/a9ef3a1b8f4e1a75b55a9b80877eddc2c6f07ec4) `disable_link_preview` parameter to POST:/messages method to disable links parsing in text - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/eb99e8ab97b55fa196d9957fca34d2316a4ca8aa) `sending_file` action - [Removed](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/7a5ab5f0ea1336b3460d1827a6a7b3b141e19776) several deprecated properties - `photo` upload type [renamed](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/74505883e6acb306686a6d141414aeaf5131ef49) to `image`. *C* is for consistency  ##### Version 0.1.9 - Added method to [get chat administrators](#operation/getAdmins) - For `type: dialog` chats [added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/ff9e2472941d4dd2de540db0d0ea8b9c3d0ed01a#diff-7e9de78f42fb0d2ae80878b90c87300aR1160) `dialog_with_user` - Added `url` for [messages](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/137dd9dfa4e583d429f017ba69c20caa9deac105) in public chats/channels - [**Removed**](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/ff9e2472941d4dd2de540db0d0ea8b9c3d0ed01a) `callback_id` of `InlineKeyboardAttachment` - [**Removed**](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/2ebf36b22758ea3487304f5b0d0d811798e78b61) `user_id` of `CallbackAnswer`. It is no longer required. Just use `callback_id` of `Callback` - Several minor improvements: check [diff](https://github.com/tamtam-chat/tamtam-bot-api-schema/compare/beccbe5f4fbed32182a13e257ca1cfae7f40ea8d...master) for all changes  ##### Version 0.1.8 - Added `code`, `width`, `height` to [StickerAttachment](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1580) - `token` is now only one required property for video/audio/file attachments - `sender` and `chat_id` of [LinkedMessage](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1401) are now optional - Added clarifying `message` to [SimpleQueryResult](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1938)  To see changelog for older versions visit our [GitHub](https://github.com/tamtam-chat/tamtam-bot-api-schema/releases).  # noqa: E501

    OpenAPI spec version: 0.1.11
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient


class MessagesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def answer_on_callback(self, callback_id, callback_answer, **kwargs):  # noqa: E501
        """Answer on callback  # noqa: E501

        This method should be called to send an answer after a user has clicked the button. The answer may be an updated message or/and a one-time user notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.answer_on_callback(callback_id, callback_answer, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str callback_id: Identifies a button clicked by user. Bot receives this identifier after user pressed button as part of `MessageCallbackUpdate` (required)
        :param CallbackAnswer callback_answer: (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.answer_on_callback_with_http_info(callback_id, callback_answer, **kwargs)  # noqa: E501
        else:
            (data) = self.answer_on_callback_with_http_info(callback_id, callback_answer, **kwargs)  # noqa: E501
            return data

    def answer_on_callback_with_http_info(self, callback_id, callback_answer, **kwargs):  # noqa: E501
        """Answer on callback  # noqa: E501

        This method should be called to send an answer after a user has clicked the button. The answer may be an updated message or/and a one-time user notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.answer_on_callback_with_http_info(callback_id, callback_answer, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str callback_id: Identifies a button clicked by user. Bot receives this identifier after user pressed button as part of `MessageCallbackUpdate` (required)
        :param CallbackAnswer callback_answer: (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['callback_id', 'callback_answer']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method answer_on_callback" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'callback_id' is set
        if ('callback_id' not in local_var_params or
                local_var_params['callback_id'] is None):
            raise ValueError("Missing the required parameter `callback_id` when calling `answer_on_callback`")  # noqa: E501
        # verify the required parameter 'callback_answer' is set
        if ('callback_answer' not in local_var_params or
                local_var_params['callback_answer'] is None):
            raise ValueError("Missing the required parameter `callback_answer` when calling `answer_on_callback`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'callback_id' in local_var_params:
            query_params.append(('callback_id', local_var_params['callback_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'callback_answer' in local_var_params:
            body_params = local_var_params['callback_answer']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/answers', 'POST',
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

    def construct(self, session_id, constructor_answer, **kwargs):  # noqa: E501
        """Construct message  # noqa: E501

        Sends answer on construction request. Answer can contain any prepared message and/or keyboard to help user interact with bot.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.construct(session_id, constructor_answer, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: Constructor session identifier (required)
        :param ConstructorAnswer constructor_answer: (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.construct_with_http_info(session_id, constructor_answer, **kwargs)  # noqa: E501
        else:
            (data) = self.construct_with_http_info(session_id, constructor_answer, **kwargs)  # noqa: E501
            return data

    def construct_with_http_info(self, session_id, constructor_answer, **kwargs):  # noqa: E501
        """Construct message  # noqa: E501

        Sends answer on construction request. Answer can contain any prepared message and/or keyboard to help user interact with bot.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.construct_with_http_info(session_id, constructor_answer, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: Constructor session identifier (required)
        :param ConstructorAnswer constructor_answer: (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['session_id', 'constructor_answer']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method construct" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'session_id' is set
        if ('session_id' not in local_var_params or
                local_var_params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `construct`")  # noqa: E501
        # verify the required parameter 'constructor_answer' is set
        if ('constructor_answer' not in local_var_params or
                local_var_params['constructor_answer'] is None):
            raise ValueError("Missing the required parameter `constructor_answer` when calling `construct`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'session_id' in local_var_params:
            query_params.append(('session_id', local_var_params['session_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'constructor_answer' in local_var_params:
            body_params = local_var_params['constructor_answer']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/answers/constructor', 'POST',
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

    def delete_message(self, message_id, **kwargs):  # noqa: E501
        """Delete message  # noqa: E501

        Deletes message in a dialog or in a chat if bot has permission to delete messages.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_message(message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message_id: Deleting message identifier (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_message_with_http_info(message_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_message_with_http_info(message_id, **kwargs)  # noqa: E501
            return data

    def delete_message_with_http_info(self, message_id, **kwargs):  # noqa: E501
        """Delete message  # noqa: E501

        Deletes message in a dialog or in a chat if bot has permission to delete messages.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_message_with_http_info(message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message_id: Deleting message identifier (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['message_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_message" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'message_id' is set
        if ('message_id' not in local_var_params or
                local_var_params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `delete_message`")  # noqa: E501

        if ('message_id' in local_var_params and
                len(local_var_params['message_id']) < 1):
            raise ValueError("Invalid value for parameter `message_id` when calling `delete_message`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'message_id' in local_var_params:
            query_params.append(('message_id', local_var_params['message_id']))  # noqa: E501

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
            '/messages', 'DELETE',
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

    def edit_message(self, message_id, new_message_body, **kwargs):  # noqa: E501
        """Edit message  # noqa: E501

        Updated message should be sent as `NewMessageBody` in a request body. In case `attachments` field is `null`, the current message attachments won’t be changed. In case of sending an empty list in this field, all attachments will be deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_message(message_id, new_message_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message_id: Editing message identifier (required)
        :param NewMessageBody new_message_body: (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.edit_message_with_http_info(message_id, new_message_body, **kwargs)  # noqa: E501
        else:
            (data) = self.edit_message_with_http_info(message_id, new_message_body, **kwargs)  # noqa: E501
            return data

    def edit_message_with_http_info(self, message_id, new_message_body, **kwargs):  # noqa: E501
        """Edit message  # noqa: E501

        Updated message should be sent as `NewMessageBody` in a request body. In case `attachments` field is `null`, the current message attachments won’t be changed. In case of sending an empty list in this field, all attachments will be deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_message_with_http_info(message_id, new_message_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message_id: Editing message identifier (required)
        :param NewMessageBody new_message_body: (required)
        :return: SimpleQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['message_id', 'new_message_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_message" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'message_id' is set
        if ('message_id' not in local_var_params or
                local_var_params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `edit_message`")  # noqa: E501
        # verify the required parameter 'new_message_body' is set
        if ('new_message_body' not in local_var_params or
                local_var_params['new_message_body'] is None):
            raise ValueError("Missing the required parameter `new_message_body` when calling `edit_message`")  # noqa: E501

        if ('message_id' in local_var_params and
                len(local_var_params['message_id']) < 1):
            raise ValueError("Invalid value for parameter `message_id` when calling `edit_message`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'message_id' in local_var_params:
            query_params.append(('message_id', local_var_params['message_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'new_message_body' in local_var_params:
            body_params = local_var_params['new_message_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/messages', 'PUT',
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

    def get_message_by_id(self, message_id, **kwargs):  # noqa: E501
        """Get message  # noqa: E501

        Returns single message by its identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_message_by_id(message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message_id: Message identifier (`mid`) to get single message in chat (required)
        :return: Message
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_message_by_id_with_http_info(message_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_message_by_id_with_http_info(message_id, **kwargs)  # noqa: E501
            return data

    def get_message_by_id_with_http_info(self, message_id, **kwargs):  # noqa: E501
        """Get message  # noqa: E501

        Returns single message by its identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_message_by_id_with_http_info(message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message_id: Message identifier (`mid`) to get single message in chat (required)
        :return: Message
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['message_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_message_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'message_id' is set
        if ('message_id' not in local_var_params or
                local_var_params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `get_message_by_id`")  # noqa: E501

        if 'message_id' in local_var_params and not re.search(r'[a-zA-Z0-9_\\-]+', local_var_params['message_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `message_id` when calling `get_message_by_id`, must conform to the pattern `/[a-zA-Z0-9_\\-]+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'message_id' in local_var_params:
            path_params['messageId'] = local_var_params['message_id']  # noqa: E501

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
            '/messages/{messageId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Message',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_messages(self, **kwargs):  # noqa: E501
        """Get messages  # noqa: E501

        Returns messages in chat: result page and marker referencing to the next page. Messages traversed in reverse direction so the latest message in chat will be first in result array. Therefore if you use `from` and `to` parameters, `to` must be **less than** `from`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_messages(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier to get messages in chat
        :param list[str] message_ids: Comma-separated list of message ids to get
        :param int _from: Start time for requested messages
        :param int to: End time for requested messages
        :param int count: Maximum amount of messages in response
        :return: MessageList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_messages_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_messages_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_messages_with_http_info(self, **kwargs):  # noqa: E501
        """Get messages  # noqa: E501

        Returns messages in chat: result page and marker referencing to the next page. Messages traversed in reverse direction so the latest message in chat will be first in result array. Therefore if you use `from` and `to` parameters, `to` must be **less than** `from`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_messages_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier to get messages in chat
        :param list[str] message_ids: Comma-separated list of message ids to get
        :param int _from: Start time for requested messages
        :param int to: End time for requested messages
        :param int count: Maximum amount of messages in response
        :return: MessageList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['chat_id', 'message_ids', '_from', 'to', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_messages" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `count` when calling `get_messages`, must be a value less than or equal to `100`")  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `count` when calling `get_messages`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'chat_id' in local_var_params:
            query_params.append(('chat_id', local_var_params['chat_id']))  # noqa: E501
        if 'message_ids' in local_var_params:
            query_params.append(('message_ids', local_var_params['message_ids']))  # noqa: E501
            collection_formats['message_ids'] = 'csv'  # noqa: E501
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))  # noqa: E501
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
            '/messages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MessageList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_message(self, new_message_body, **kwargs):  # noqa: E501
        """Send message  # noqa: E501

        Sends a message to a chat. As a result for this method new message identifier returns. ### Attaching media Attaching media to messages is a three-step process.  At first step, you should [obtain a URL to upload](#operation/getUploadUrl) your media files.  At the second, you should upload binary of appropriate format to URL you obtained at the previous step. See [upload](https://dev.tamtam.chat/#operation/getUploadUrl) section for details.  Finally, if the upload process was successful, you will receive JSON-object in a response body.  Use this object to create attachment. Construct an object with two properties: - `type` with the value set to appropriate media type - and `payload` filled with the JSON you've got.  For example, you can attach a video to message this way:  1. Get URL to upload. Execute following: ```shell curl -X POST 'https://botapi.tamtam.chat/uploads?access_token=%access_token%&type=video' ``` As the result it will return URL for the next step. ```json {     \"url\": \"http://vu.mycdn.me/upload.do…\" } ```  2. Use this url to upload your binary: ```shell curl -i -X POST   -H \"Content-Type: multipart/form-data\"   -F \"data=@movie.mp4\" \"http://vu.mycdn.me/upload.do…\" ``` As the result it will return JSON you can attach to message: ```json   {     \"token\": \"_3Rarhcf1PtlMXy8jpgie8Ai_KARnVFYNQTtmIRWNh4\"   } ``` 3. Send message with attach: ```json {     \"text\": \"Message with video\",     \"attachments\": [         {             \"type\": \"video\",             \"payload\": {                 \"token\": \"_3Rarhcf1PtlMXy8jpgie8Ai_KARnVFYNQTtmIRWNh4\"             }         }     ] } ```  **Important notice**:  It may take time for the server to process your file (audio/video or any binary). While a file is not processed you can't attach it. It means the last step will fail with `400` error. Try to send a message again until you'll get a successful result.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_message(new_message_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewMessageBody new_message_body: (required)
        :param int user_id: Fill this parameter if you want to send message to user
        :param int chat_id: Fill this if you send message to chat
        :param bool disable_link_preview: If `false`, server will not generate media preview for links in text
        :return: SendMessageResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_message_with_http_info(new_message_body, **kwargs)  # noqa: E501
        else:
            (data) = self.send_message_with_http_info(new_message_body, **kwargs)  # noqa: E501
            return data

    def send_message_with_http_info(self, new_message_body, **kwargs):  # noqa: E501
        """Send message  # noqa: E501

        Sends a message to a chat. As a result for this method new message identifier returns. ### Attaching media Attaching media to messages is a three-step process.  At first step, you should [obtain a URL to upload](#operation/getUploadUrl) your media files.  At the second, you should upload binary of appropriate format to URL you obtained at the previous step. See [upload](https://dev.tamtam.chat/#operation/getUploadUrl) section for details.  Finally, if the upload process was successful, you will receive JSON-object in a response body.  Use this object to create attachment. Construct an object with two properties: - `type` with the value set to appropriate media type - and `payload` filled with the JSON you've got.  For example, you can attach a video to message this way:  1. Get URL to upload. Execute following: ```shell curl -X POST 'https://botapi.tamtam.chat/uploads?access_token=%access_token%&type=video' ``` As the result it will return URL for the next step. ```json {     \"url\": \"http://vu.mycdn.me/upload.do…\" } ```  2. Use this url to upload your binary: ```shell curl -i -X POST   -H \"Content-Type: multipart/form-data\"   -F \"data=@movie.mp4\" \"http://vu.mycdn.me/upload.do…\" ``` As the result it will return JSON you can attach to message: ```json   {     \"token\": \"_3Rarhcf1PtlMXy8jpgie8Ai_KARnVFYNQTtmIRWNh4\"   } ``` 3. Send message with attach: ```json {     \"text\": \"Message with video\",     \"attachments\": [         {             \"type\": \"video\",             \"payload\": {                 \"token\": \"_3Rarhcf1PtlMXy8jpgie8Ai_KARnVFYNQTtmIRWNh4\"             }         }     ] } ```  **Important notice**:  It may take time for the server to process your file (audio/video or any binary). While a file is not processed you can't attach it. It means the last step will fail with `400` error. Try to send a message again until you'll get a successful result.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_message_with_http_info(new_message_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewMessageBody new_message_body: (required)
        :param int user_id: Fill this parameter if you want to send message to user
        :param int chat_id: Fill this if you send message to chat
        :param bool disable_link_preview: If `false`, server will not generate media preview for links in text
        :return: SendMessageResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['new_message_body', 'user_id', 'chat_id', 'disable_link_preview']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_message" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'new_message_body' is set
        if ('new_message_body' not in local_var_params or
                local_var_params['new_message_body'] is None):
            raise ValueError("Missing the required parameter `new_message_body` when calling `send_message`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in local_var_params:
            query_params.append(('user_id', local_var_params['user_id']))  # noqa: E501
        if 'chat_id' in local_var_params:
            query_params.append(('chat_id', local_var_params['chat_id']))  # noqa: E501
        if 'disable_link_preview' in local_var_params:
            query_params.append(('disable_link_preview', local_var_params['disable_link_preview']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'new_message_body' in local_var_params:
            body_params = local_var_params['new_message_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/messages', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SendMessageResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

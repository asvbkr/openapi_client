# coding: utf-8

"""
    TamTam Bot API

    # About Bot API allows bots to interact with TamTam. Methods are called by sending HTTPS requests to [botapi.tamtam.chat](https://botapi.tamtam.chat) domain. Bots are third-party applications that use TamTam features. A bot can legitimately take part in a conversation. It can be achieved through HTTP requests to the TamTam Bot API. ## Features TamTam bots of the current version are able to: - Communicate with users and respond to requests - Recommend users complete actions via programmed buttons - Request personal data from users (name, short reference, phone number) We'll keep working on expanding bot capabilities in the future. ## Examples Bots can be used for the following purposes: - Providing support, answering frequently asked questions - Sending typical information - Voting - Likes/dislikes - Following external links - Forwarding a user to a chat/channel ## @PrimeBot We are beta testing bots in TamTam now. To become a beta tester, please, contact us on **[@support](https://tt.me/support)** or [team@tamtam.chat](mailto:team@tamtam.chat). We'll give you access to [PrimeBot](https://tt.me/primebot), all TamTam bots creator. It will help you choose a unique short name for a bot and fill in its full name and description. With PrimeBot you can create bots as well as edit and delete them and browse information on bots you have created. #### [PrimeBot](https://tt.me/primebot) commands: `/start` &mdash; start a dialog with a bot  `/create` &mdash; create a bot, assign the unique short name to it (from 4 to 64 characters)  `/set_name [name]` &mdash; assign a short or full name to the bot (up to 200 characters)  `/set_description [description]` &mdash; enter the description for the bot profile (up to 400 characters)  `/set_picture [URL]` &mdash; enter the URL of bot's picture  `/delete [username]` &mdash; delete the bot  `/list` &mdash; show the list of all bots  `/get_token` &mdash; obtain a token for a bot  `/revoke` &mdash; request a new token  `/help` &mdash; help  ## HTTP verbs `GET` &mdash; getting resources, parameters are transmitted via URL  `POST` &mdash; creation of resources (for example, sending new messages)  `PUT` &mdash; editing resources  `DELETE` &mdash; deleting resources  `PATCH` &mdash; patching resources ## HTTP response codes `200` &mdash; successful operation  `400` &mdash; invalid request  `401` &mdash; authentication error  `404` &mdash; resource not found  `405` &mdash; method not allowed  `429` &mdash; the number of requests is exceeded  `503` &mdash; service unavailable  ## Resources format For content requests (PUT and POST) and responses, the API uses the JSON format. All strings are UTF-8 encoded. Date/time fields are represented as the number of milliseconds that have elapsed since 00:00 January 1, 1970 in the long format. To get it, you can simply multiply the UNIX timestamp by 1000. All date/time fields have a UTC timezone. ## Error responses In case of an error, the API returns a response with the corresponding HTTP code and JSON with the following fields:   `code` - the string with the error key   `message` - a string describing the error </br>  For example: ```bash > http https://botapi.tamtam.chat/chats?access_token={EXAMPLE_TOKEN} HTTP / 1.1 403 Forbidden Cache-Control: no-cache Connection: Keep-Alive Content-Length: 57 Content-Type: application / json; charset = utf-8 Set-Cookie: web_ui_lang = ru; Path = /; Domain = .tamtam.chat; Expires = 2019-03-24T11: 45: 36.500Z {    \"code\": \"verify.token\",    \"message\": \"Invalid access_token\" } ``` ## Receiving Notifications TamTam Bot API supports 2 options of receiving notifications on new dialog events for bots: - Push notifications via WebHook. To receive data via WebHook, you'll have to [add subscription](https://dev.tamtam.chat/#operation/subscribe); - Notifications upon request via [long polling](#operation/getUpdates) API. All data can be received via long polling **by default** after creating the bot,  Both methods **cannot** be used simultaneously. Refer to the response schema of [/updates](https://dev.tamtam.chat/#operation/getUpdates) method to check all available types of updates. ## Message buttons You can program buttons for users answering a bot. TamTam supports the following types of buttons:   `callback` &mdash; sends a notification to a bot (via WebHook or long polling)   `link` &mdash; makes a user to follow a link   `request_contact` &mdash; requests the user permission to access contact information (phone number, short link, email)   You may also send a message with an [InlineKeyboard]() type attachment to start creating buttons. When the user presses a button, the bot receives the answer with filled callback field. It is recommended to edit that message so the user can receive updated buttons. # Versioning API models and interface may change over time. To make sure your bot will get the right info, we strongly recommend adding API version number to each request. You can add it as `v` parameter to each HTTP-request. For instance, `v=0.1.2`. To specify the data model version you are getting through WebHook subscription, use the `version` property in the request body of the [subscribe](https://dev.tamtam.chat/#operation/subscribe) request. # Libraries We have created [Java library](https://github.com/tamtam-chat/tamtam-bot-api) to make using API easier. # Changelog ##### Version 0.1.6 - Added method to [edit bot info](#operation/editMyInfo) - Added statistics for messages in channel - `Message.sender` and `UserWithPhoto.avatar_url/full_avatar_url` removed from required properties  ##### Version 0.1.5 - Added `id` property to media attachments (`VideoAttachment`, `AudioAttachment`) so you can reuse attachment from one message in another - Added ability to create *linked* message: replied or forwarded. See `link` in `NewMessageBody` - `intent` property marked as required only for `CallbackButton`  ##### Version 0.1.4  - Added `user_ids` parameter to [get members](#operation/getMembers) in chat by id - `attachment` property of [send message](#operation/sendMessage) request body marked as deprecated  ##### Version 0.1.3 - Added method to [delete](https://dev.tamtam.chat/#operation/deleteMessages) messages - Added ability to [get](https://dev.tamtam.chat/#operation/getMessages) particular messages by ID - Added `is_admin` flag to `ChatMember` - Added `message` property to `MessageCallbackUpdate` - Renamed property `message` to `body` for `Message` schema - Added reusable `token` to `PhotoAttachment`. It allows to attach the same photo more than once.  # noqa: E501

    OpenAPI spec version: 0.1.7
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

        if 'message_id' in local_var_params and not re.search('mid\\.[a-z0-9]{32}', str(local_var_params['message_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `message_id` when calling `delete_message`, must conform to the pattern `/mid\\.[a-z0-9]{32}/`")  # noqa: E501
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

        if 'message_id' in local_var_params and not re.search(r'mid\.[a-z0-9]{32}', local_var_params['message_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `message_id` when calling `edit_message`, must conform to the pattern `/mid\\.[a-z0-9]{32}/`")  # noqa: E501
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

    def get_messages(self, **kwargs):  # noqa: E501
        """Get messages  # noqa: E501

        Returns messages in chat: result page and marker referencing to the next page. Messages traversed in reverse direction so the latest message in chat will be first in result array. Therefore if you use `from` and `to` parameters, `to` must be **less than** `from`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_messages(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chat_id: Chat identifier to get messages in chat
        :param list[str] message_ids: Messages ids you want to get
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
        :param list[str] message_ids: Messages ids you want to get
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
            collection_formats['message_ids'] = 'multi'  # noqa: E501
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

        Sends a message to a chat. As a result for this method new message identifier returns. ### Attaching media Attaching media to messages is a three-step process.  At first step, you should [obtain a URL to upload](#operation/getUploadUrl) your media files.  At the second, you should upload binary of appropriate format to URL you obtained at the previous step. See [upload](https://dev.tamtam.chat/#operation/getUploadUrl) section for details.  Finally, if the upload process was successful, you will receive JSON-object in a response body.  Use this object to create attachment. Construct an object with two properties:  - `type` with the value set to appropriate media type  - and `payload` filled with the JSON you've got.   For example, you can attach a video to message this way:  1. Get URL to upload. Execute following: ```shell curl -X POST \\   'https://botapi.tamtam.chat/uploads?access_token=%access_token%&type=video' ``` As the result it will return URL for the next step. ```json {     \"url\": \"http://vu.mycdn.me/upload.do…\" } ```   2. Use this url to upload your binary:  ```shell curl -i -X POST      -H \"Content-Type: multipart/form-data\"      -F \"data=@movie.mp4\" \"http://vu.mycdn.me/upload.do…\" ``` As the result it will return JSON you can attach to message: ```json {     \"id\": 1234567890 } ``` 3. Send message with attach: ```json {  \"text\": \"Message with video\",  \"attachments\": [   {    \"type\": \"video\",    \"payload\": {        \"id\": 1173574260020    }   }  ] } ```  **Important notice**:  It may take time for the server to process your file (audio/video or any binary). While a file is not processed you can't attach it. It means the last step will fail with `400` error. Try to send a message again until you'll get a successful result.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_message(new_message_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewMessageBody new_message_body: (required)
        :param int user_id: Fill this parameter if you want to send message to user
        :param int chat_id: Fill this if you send message to chat
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

        Sends a message to a chat. As a result for this method new message identifier returns. ### Attaching media Attaching media to messages is a three-step process.  At first step, you should [obtain a URL to upload](#operation/getUploadUrl) your media files.  At the second, you should upload binary of appropriate format to URL you obtained at the previous step. See [upload](https://dev.tamtam.chat/#operation/getUploadUrl) section for details.  Finally, if the upload process was successful, you will receive JSON-object in a response body.  Use this object to create attachment. Construct an object with two properties:  - `type` with the value set to appropriate media type  - and `payload` filled with the JSON you've got.   For example, you can attach a video to message this way:  1. Get URL to upload. Execute following: ```shell curl -X POST \\   'https://botapi.tamtam.chat/uploads?access_token=%access_token%&type=video' ``` As the result it will return URL for the next step. ```json {     \"url\": \"http://vu.mycdn.me/upload.do…\" } ```   2. Use this url to upload your binary:  ```shell curl -i -X POST      -H \"Content-Type: multipart/form-data\"      -F \"data=@movie.mp4\" \"http://vu.mycdn.me/upload.do…\" ``` As the result it will return JSON you can attach to message: ```json {     \"id\": 1234567890 } ``` 3. Send message with attach: ```json {  \"text\": \"Message with video\",  \"attachments\": [   {    \"type\": \"video\",    \"payload\": {        \"id\": 1173574260020    }   }  ] } ```  **Important notice**:  It may take time for the server to process your file (audio/video or any binary). While a file is not processed you can't attach it. It means the last step will fail with `400` error. Try to send a message again until you'll get a successful result.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_message_with_http_info(new_message_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewMessageBody new_message_body: (required)
        :param int user_id: Fill this parameter if you want to send message to user
        :param int chat_id: Fill this if you send message to chat
        :return: SendMessageResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['new_message_body', 'user_id', 'chat_id']  # noqa: E501
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

# coding: utf-8

# flake8: noqa
"""
    TamTam Bot API

    # About Bot API allows bots to interact with TamTam. Methods are called by sending HTTPS requests to [botapi.tamtam.chat](https://botapi.tamtam.chat) domain. Bots are third-party applications that use TamTam features. A bot can legitimately take part in a conversation. It can be achieved through HTTP requests to the TamTam Bot API.  ## Features TamTam bots of the current version are able to: - Communicate with users and respond to requests - Recommend users complete actions via programmed buttons - Request personal data from users (name, short reference, phone number) We'll keep working on expanding bot capabilities in the future.  ## Examples Bots can be used for the following purposes: - Providing support, answering frequently asked questions - Sending typical information - Voting - Likes/dislikes - Following external links - Forwarding a user to a chat/channel  ## @PrimeBot [PrimeBot](https://tt.me/primebot) is the main bot in TamTam, all bots creator. Use PrimeBot to create and edit your bots. Feel free to contact us for any questions, [@support](https://tt.me/support) or [team@tamtam.chat](mailto:team@tamtam.chat).  #### [PrimeBot](https://tt.me/primebot) commands: `/start` &mdash; start a dialog with a bot  `/create` &mdash; create a bot, assign the unique short name to it (from 4 to 64 characters)  `/set_name [name]` &mdash; assign a short or full name to the bot (up to 200 characters)  `/set_description [description]` &mdash; enter the description for the bot profile (up to 400 characters)  `/set_picture [URL]` &mdash; enter the URL of bot's picture  `/delete [username]` &mdash; delete the bot  `/list` &mdash; show the list of all bots  `/get_token` &mdash; obtain a token for a bot  `/revoke` &mdash; request a new token  `/help` &mdash; help  ## HTTP verbs `GET` &mdash; getting resources, parameters are transmitted via URL  `POST` &mdash; creation of resources (for example, sending new messages)  `PUT` &mdash; editing resources  `DELETE` &mdash; deleting resources  `PATCH` &mdash; patching resources  ## HTTP response codes `200` &mdash; successful operation  `400` &mdash; invalid request  `401` &mdash; authentication error  `404` &mdash; resource not found  `405` &mdash; method is not allowed  `429` &mdash; the number of requests is exceeded  `503` &mdash; service unavailable  ## Resources format For content requests (PUT and POST) and responses, the API uses the JSON format. All strings are UTF-8 encoded. Date/time fields are represented as the number of milliseconds that have elapsed since 00:00 January 1, 1970 in the long format. To get it, you can simply multiply the UNIX timestamp by 1000. All date/time fields have a UTC timezone. ## Error responses In case of an error, the API returns a response with the corresponding HTTP code and JSON with the following fields:  `code` - the string with the error key  `message` - a string describing the error </br>  For example: ```bash > http https://botapi.tamtam.chat/chats?access_token={EXAMPLE_TOKEN} HTTP / 1.1 403 Forbidden Cache-Control: no-cache Connection: Keep-Alive Content-Length: 57 Content-Type: application / json; charset = utf-8 Set-Cookie: web_ui_lang = ru; Path = /; Domain = .tamtam.chat; Expires = 2019-03-24T11: 45: 36.500Z {    \"code\": \"verify.token\",    \"message\": \"Invalid access_token\" } ``` ## Receiving Notifications TamTam Bot API supports 2 options of receiving notifications on new dialog events for bots: - Push notifications via WebHook. To receive data via WebHook, you'll have to [add subscription](https://dev.tamtam.chat/#operation/subscribe); - Notifications upon request via [long polling](#operation/getUpdates) API. All data can be received via long polling **by default** after creating the bot,  Both methods **cannot** be used simultaneously. Refer to the response schema of [/updates](https://dev.tamtam.chat/#operation/getUpdates) method to check all available types of updates.  ## Message buttons You can program buttons for users answering a bot. TamTam supports the following types of buttons:  `callback` &mdash; sends a notification to a bot (via WebHook or long polling)  `link` &mdash; makes a user to follow a link  `request_contact` &mdash; requests the user permission to access contact information (phone number, short link, email)  You may also send a message with an [InlineKeyboard]() type attachment to start creating buttons. When the user presses a button, the bot receives the answer with filled callback field. It is recommended to edit that message so the user can receive updated buttons.  # Versioning API models and interface may change over time. To make sure your bot will get the right info, we strongly recommend adding API version number to each request. You can add it as `v` parameter to each HTTP-request. For instance, `v=0.1.2`. To specify the data model version you are getting through WebHook subscription, use the `version` property in the request body of the [subscribe](https://dev.tamtam.chat/#operation/subscribe) request.  # Libraries We have created [Java library](https://github.com/tamtam-chat/tamtam-bot-api) to make using API easier.  # Changelog ##### Version 0.1.9 - Added method to [get chat administrators](#operation/getAdmins) - For `type: dialog` chats [added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/ff9e2472941d4dd2de540db0d0ea8b9c3d0ed01a#diff-7e9de78f42fb0d2ae80878b90c87300aR1160) `dialog_with_user` - Added `url` for [messages](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/137dd9dfa4e583d429f017ba69c20caa9deac105) in public chats/channels - [**Removed**](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/ff9e2472941d4dd2de540db0d0ea8b9c3d0ed01a) `callback_id` of `InlineKeyboardAttachment` - [**Removed**](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/2ebf36b22758ea3487304f5b0d0d811798e78b61) `user_id` of `CallbackAnswer`. It is no longer required. Just use `callback_id` of `Callback` - Several minor improvements: check [diff](https://github.com/tamtam-chat/tamtam-bot-api-schema/compare/beccbe5f4fbed32182a13e257ca1cfae7f40ea8d...master) for all changes  ##### Version 0.1.8 - Added `code`, `width`, `height` to [StickerAttachment](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1580) - `token` is now only one required property for video/audio/file attachments - `sender` and `chat_id` of [LinkedMessage](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1401) are now optional - Added clarifying `message` to [SimpleQueryResult](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1938)  ##### Version 0.1.7 - It is now **required** to pass `marker` parameter in [/updates](#operation/getUpdates) requests, except initial - Added full `User` object to update types: bot_started, bot_added, bot_removed, user_added, user_removed, chat_title_changed - Added `size` and `filename` to [`FileAttachment`](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1503) - Added [`token`](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1525) property to video/audio/file attachments allows you to reuse attachments uploaded by another user  ##### Version 0.1.6 - Added method to [edit bot info](#operation/editMyInfo) - Added statistics for messages in channel - `Message.sender` and `UserWithPhoto.avatar_url/full_avatar_url` removed from required properties  # noqa: E501

    OpenAPI spec version: 0.1.10
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from openapi_client.models.action_request_body import ActionRequestBody
from openapi_client.models.attachment import Attachment
from openapi_client.models.attachment_payload import AttachmentPayload
from openapi_client.models.attachment_request import AttachmentRequest
from openapi_client.models.audio_attachment import AudioAttachment
from openapi_client.models.audio_attachment_request import AudioAttachmentRequest
from openapi_client.models.bot_added_to_chat_update import BotAddedToChatUpdate
from openapi_client.models.bot_command import BotCommand
from openapi_client.models.bot_info import BotInfo
from openapi_client.models.bot_patch import BotPatch
from openapi_client.models.bot_removed_from_chat_update import BotRemovedFromChatUpdate
from openapi_client.models.bot_started_update import BotStartedUpdate
from openapi_client.models.button import Button
from openapi_client.models.callback import Callback
from openapi_client.models.callback_answer import CallbackAnswer
from openapi_client.models.callback_button import CallbackButton
from openapi_client.models.chat import Chat
from openapi_client.models.chat_admin_permission import ChatAdminPermission
from openapi_client.models.chat_list import ChatList
from openapi_client.models.chat_member import ChatMember
from openapi_client.models.chat_members_list import ChatMembersList
from openapi_client.models.chat_patch import ChatPatch
from openapi_client.models.chat_status import ChatStatus
from openapi_client.models.chat_title_changed_update import ChatTitleChangedUpdate
from openapi_client.models.chat_type import ChatType
from openapi_client.models.contact_attachment import ContactAttachment
from openapi_client.models.contact_attachment_payload import ContactAttachmentPayload
from openapi_client.models.contact_attachment_request import ContactAttachmentRequest
from openapi_client.models.contact_attachment_request_payload import ContactAttachmentRequestPayload
from openapi_client.models.error import Error
from openapi_client.models.file_attachment import FileAttachment
from openapi_client.models.file_attachment_payload import FileAttachmentPayload
from openapi_client.models.file_attachment_request import FileAttachmentRequest
from openapi_client.models.get_subscriptions_result import GetSubscriptionsResult
from openapi_client.models.image import Image
from openapi_client.models.inline_keyboard_attachment import InlineKeyboardAttachment
from openapi_client.models.inline_keyboard_attachment_request import InlineKeyboardAttachmentRequest
from openapi_client.models.inline_keyboard_attachment_request_payload import InlineKeyboardAttachmentRequestPayload
from openapi_client.models.intent import Intent
from openapi_client.models.keyboard import Keyboard
from openapi_client.models.link_button import LinkButton
from openapi_client.models.linked_message import LinkedMessage
from openapi_client.models.location_attachment import LocationAttachment
from openapi_client.models.location_attachment_request import LocationAttachmentRequest
from openapi_client.models.media_attachment_payload import MediaAttachmentPayload
from openapi_client.models.message import Message
from openapi_client.models.message_body import MessageBody
from openapi_client.models.message_callback_update import MessageCallbackUpdate
from openapi_client.models.message_created_update import MessageCreatedUpdate
from openapi_client.models.message_edited_update import MessageEditedUpdate
from openapi_client.models.message_link_type import MessageLinkType
from openapi_client.models.message_list import MessageList
from openapi_client.models.message_removed_update import MessageRemovedUpdate
from openapi_client.models.message_stat import MessageStat
from openapi_client.models.new_message_body import NewMessageBody
from openapi_client.models.new_message_link import NewMessageLink
from openapi_client.models.photo_attachment import PhotoAttachment
from openapi_client.models.photo_attachment_payload import PhotoAttachmentPayload
from openapi_client.models.photo_attachment_request import PhotoAttachmentRequest
from openapi_client.models.photo_attachment_request_payload import PhotoAttachmentRequestPayload
from openapi_client.models.photo_token import PhotoToken
from openapi_client.models.photo_tokens import PhotoTokens
from openapi_client.models.recipient import Recipient
from openapi_client.models.request_contact_button import RequestContactButton
from openapi_client.models.request_geo_location_button import RequestGeoLocationButton
from openapi_client.models.send_message_result import SendMessageResult
from openapi_client.models.sender_action import SenderAction
from openapi_client.models.share_attachment import ShareAttachment
from openapi_client.models.simple_query_result import SimpleQueryResult
from openapi_client.models.sticker_attachment import StickerAttachment
from openapi_client.models.sticker_attachment_payload import StickerAttachmentPayload
from openapi_client.models.sticker_attachment_request import StickerAttachmentRequest
from openapi_client.models.sticker_attachment_request_payload import StickerAttachmentRequestPayload
from openapi_client.models.subscription import Subscription
from openapi_client.models.subscription_request_body import SubscriptionRequestBody
from openapi_client.models.update import Update
from openapi_client.models.update_list import UpdateList
from openapi_client.models.upload_endpoint import UploadEndpoint
from openapi_client.models.upload_type import UploadType
from openapi_client.models.uploaded_info import UploadedInfo
from openapi_client.models.user import User
from openapi_client.models.user_added_to_chat_update import UserAddedToChatUpdate
from openapi_client.models.user_ids_list import UserIdsList
from openapi_client.models.user_removed_from_chat_update import UserRemovedFromChatUpdate
from openapi_client.models.user_with_photo import UserWithPhoto
from openapi_client.models.video_attachment import VideoAttachment
from openapi_client.models.video_attachment_request import VideoAttachmentRequest

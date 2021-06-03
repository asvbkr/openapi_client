# coding: utf-8

# flake8: noqa
"""
    TamTam Bot API

    # About Bot API allows bots to interact with TamTam. Methods are called by sending HTTPS requests to [botapi.tamtam.chat](https://botapi.tamtam.chat) domain. Bots are third-party applications that use TamTam features. A bot can legitimately take part in a conversation. It can be achieved through HTTP requests to the TamTam Bot API.  ## Features TamTam bots of the current version are able to: - Communicate with users and respond to requests - Recommend users complete actions via programmed buttons - Request personal data from users (name, short reference, phone number) We'll keep working on expanding bot capabilities in the future.  ## Examples Bots can be used for the following purposes: - Providing support, answering frequently asked questions - Sending typical information - Voting - Likes/dislikes - Following external links - Forwarding a user to a chat/channel  ## @PrimeBot [PrimeBot](https://tt.me/primebot) is the main bot in TamTam, all bots creator. Use PrimeBot to create and edit your bots. Feel free to contact us for any questions, [@support](https://tt.me/support) or [team@tamtam.chat](mailto:team@tamtam.chat).  ## HTTP verbs `GET` &mdash; getting resources, parameters are transmitted via URL  `POST` &mdash; creation of resources (for example, sending new messages)  `PUT` &mdash; editing resources  `DELETE` &mdash; deleting resources  `PATCH` &mdash; patching resources  ## HTTP response codes `200` &mdash; successful operation  `400` &mdash; invalid request  `401` &mdash; authentication error  `404` &mdash; resource not found  `405` &mdash; method is not allowed  `429` &mdash; the number of requests is exceeded  `503` &mdash; service unavailable  ## Resources format For content requests (PUT and POST) and responses, the API uses the JSON format. All strings are UTF-8 encoded. Date/time fields are represented as the number of milliseconds that have elapsed since 00:00 January 1, 1970 in the long format. To get it, you can simply multiply the UNIX timestamp by 1000. All date/time fields have a UTC timezone. ## Error responses In case of an error, the API returns a response with the corresponding HTTP code and JSON with the following fields:  `code` - the string with the error key  `message` - a string describing the error </br>  For example: ```bash > http https://botapi.tamtam.chat/chats?access_token={EXAMPLE_TOKEN} HTTP / 1.1 403 Forbidden Cache-Control: no-cache Connection: Keep-Alive Content-Length: 57 Content-Type: application / json; charset = utf-8 Set-Cookie: web_ui_lang = ru; Path = /; Domain = .tamtam.chat; Expires = 2019-03-24T11: 45: 36.500Z {    \"code\": \"verify.token\",    \"message\": \"Invalid access_token\" } ``` ## Receiving notifications TamTam Bot API supports 2 options of receiving notifications on new events for bots: - Push notifications via WebHook. To receive data via WebHook, you'll have to [add subscription](https://dev.tamtam.chat/#operation/subscribe); - Notifications upon request via [long polling](#operation/getUpdates) API. All data can be received via long polling **by default** after creating the bot.  Both methods **cannot** be used simultaneously. Refer to the response schema of [/updates](https://dev.tamtam.chat/#operation/getUpdates) method to check all available types of updates.  ### Webhook There is some notes about how we handle webhook subscription: 1. Sometimes webhook notification cannot be delivered in case when bot server or network is down.    In such case we well retry delivery in a short period of time (from 30 to 60 seconds) and will do this until get   `200 OK` status code from your server, but not longer than **8 hours** (*may change over time*) since update happened.    We also consider any non `200`-response from server as failed delivery.  2. To protect your bot from unexpected high load we send **no more than 100** notifications per second by default.   If you want increase this limit, contact us at [@support](https://tt.me/support).   It should be from one of the following subnets: ``` 185.16.150.0/30 185.16.150.84/30 185.16.150.152/30 185.16.150.192/30 ```   ## Message buttons You can program buttons for users answering a bot. TamTam supports the following types of buttons:  `callback` &mdash; sends a notification with payload to a bot (via WebHook or long polling)  `link` &mdash; makes a user to follow a link  `request_contact` &mdash; requests the user permission to access contact information (phone number, short link, email)  `request_geo_location` &mdash; asks user to provide current geo location  `chat` &mdash; creates chat associated with message  To start create buttons [send message](#operation/sendMessage) with `InlineKeyboardAttachment`: ```json {   \"text\": \"It is message with inline keyboard\",   \"attachments\": [     {       \"type\": \"inline_keyboard\",       \"payload\": {         \"buttons\": [           [             {               \"type\": \"callback\",               \"text\": \"Press me!\",               \"payload\": \"button1 pressed\"             }           ],           [             {               \"type\": \"chat\",               \"text\": \"Discuss\",               \"chat_title\": \"Message discussion\"             }           ]         ]       }     }   ] } ``` ### Chat button Chat button is a button that starts chat assosiated with the current message. It will be **private** chat with a link, bot will be added as administrator by default.  Chat will be created as soon as the first user taps on button. Bot will receive `message_chat_created` update.  Bot can set title and description of new chat by setting `chat_title` and `chat_description` properties.  Whereas keyboard can contain several `chat`-buttons there is `uuid` property to distinct them between each other. In case you do not pass `uuid` we will generate it. If you edit message, pass `uuid` so we know that this button starts the same chat as before.  Chat button also can contain `start_payload` that will be sent to bot as part of `message_chat_created` update.  ## Deep linking TamTam supports deep linking mechanism for bots. It allows passing additional payload to the bot on startup. Deep link can contain any data encoded into string up to **128** characters long. Longer strings will be omitted and **not** passed to the bot.  Each bot has start link that looks like: ``` https://tt.me/%BOT_USERNAME%/start/%PAYLOAD% ``` As soon as user clicks on such link we open dialog with bot and send this payload to bot as part of `bot_started` update: ```json {     \"update_type\": \"bot_started\",     \"timestamp\": 1573226679188,     \"chat_id\": 1234567890,     \"user\": {         \"user_id\": 1234567890,         \"name\": \"Boris\",         \"username\": \"borisd84\"     },     \"payload\": \"any data meaningful to bot\" } ```  Deep linking mechanism is supported for iOS version 2.7.0 and Android 2.9.0 and higher.  ## Constructors Constructor is a bot that can create a message for user: add buttons, attach some media, insert text.  You can enable constructor mode for your bot via [@PrimeBot](https://tt.me/primebot) sending [/constructor_mode](https://tt.me/primebot/start/constructor_mode) command.  For bot developers, it looks like request-response interaction where TamTam application sends `message_construction_request` on behalf of user. Bot [responds](#operation/construct) to it with `messages` ready to go or `keyboard` in case it requires further action from user.  Bot also can set up UI parts such as `hint` or `placeholder`, allow or not user's input: ![Constructor UI parts](https://dev.tamtam.chat/static/hint-079a332a51a2e9e6d415ec716389661b.png)  As soon as user finishes composing a message, they can post it. Bot will receive `message_constructed_update` with posted message.  Constructors are supported for iOS version 2.7.0 and Android 2.9.0 and higher.  ## Text formatting  Message text can be improved with basic formatting such as: **strong**, *emphasis*, ~strikethough~,  <ins>underline</ins>, `code` or link. You can use either markdown-like or HTML formatting.  To enable text formatting set the `format` property of [NewMessageBody](#tag/new_message_model).  ### TamTam flavored Markdown To enable [Markdown](https://spec.commonmark.org/0.29/) parsing, set the `format` property of [NewMessageBody](#tag/new_message_model) to `markdown`.  We currently support only the following syntax:  `*empasized*` or `_empasized_` for *italic* text  `**strong**` or `__strong__` for __bold__ text  `~~strikethough~~`  for ~strikethough~ text  `++underline++`  for <ins>underlined</ins> text  ``` `code` ``` or ` ```code``` ` for `monospaced` text  `^^important^^` for highlighted text (colored in red, by default)  `[Inline URL](https://dev.tamtam.chat/)` for inline URLs  `[User mention](tamtam://user/%user_id%)` for user mentions without username  ### HTML support  To enable HTML parsing, set the `format` property of [NewMessageBody](#tag/new_message_model) to `html`.   Only the following HTML tags are supported. All others will be stripped:  Emphasized: `<i>` or `<em>`  Strong: `<b>` or `<strong>`  Strikethrough: `<del>` or `<s>`  Underlined: `<ins>` or `<u>`  Link: `<a href=\"https://dev.tamtam.chat\">Docs</a>`  Monospaced text: `<pre>` or `<code>`  Highlighted text: `<mark>`  Text formatting is supported for iOS since version 3.1 and Android since 2.20.0.  # Versioning API models and interface may change over time. To make sure your bot will get the right info, we strongly recommend adding API version number to each request. You can add it as `v` parameter to each HTTP-request. For instance, `v=0.1.2`. To specify the data model version you are getting through WebHook subscription, use the `version` property in the request body of the [subscribe](https://dev.tamtam.chat/#operation/subscribe) request.  # Libraries We have developed the official [Java client](https://github.com/tamtam-chat/tamtam-bot-api) and [SDK](https://github.com/tamtam-chat/tamtam-bot-sdk).  Also check out unofficial libraries, created by our enthusiasts: - [Kotlin DSL client](https://github.com/Namazed/TamTamBotApiClientDsl) - [GO client](https://github.com/neonxp/tamtam) - [Node.js module](https://github.com/vershininivan/node-tamtam-botapi)  #### Python: - [Python client](https://github.com/asvbkr/openapi_client) - [tamtam.py](https://github.com/uwinx/tamtam.py) - [registriren/botapitamtam](https://github.com/registriren/botapitamtam)  # Changelog ##### Version 0.3.0 - Added methods to [pin](#operation/pinMessage)/[unpin](#operation/unpinMessage) messages in chats/channels - Added `is_bot` flag to [`User`](#tag/user_model) model  Check out the complete [diff](https://github.com/tamtam-chat/tamtam-bot-api-schema/compare/v0.2.1..v0.3.0) for this release.  ##### Version 0.2.1 - [Added](#operation/getChatByLink) method to get chat by its `@link` - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/compare/v0.2.0..HEAD#diff-7e9de78f42fb0d2ae80878b90c87300aR1240) `description` for users in some cases - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/compare/v0.2.0..HEAD#diff-7e9de78f42fb0d2ae80878b90c87300aR2555) `user_locale` to `message_created` update in dialogs  Check out the complete [diff](https://github.com/tamtam-chat/tamtam-bot-api-schema/compare/v0.2.0..v0.2.1) for this release.  ##### Version 0.2.0 - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/09c95259d6c8c424f82b50eab93872e7db2ca208) new type of button to start new chat - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/ea4581d83d7132663d6cc5c2c61c058a2bd46aac) Constructors API that allows bots to create message on behalf of a user - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/c5ff03175407819aceebd9c25de49eed566a0ce1) support for deep-links - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/ff4cc4f93662d6c25db11fac72d9fcbf1f66cad8) ability to block users in chats - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/b965bfb0d02933e819435312e6ab184a3dfc0250) `chat_id` and `user_id` to `message_removed` update - Added meta information for video attachments - Other minor improvements and fixes. Check out complete [diff](https://github.com/tamtam-chat/tamtam-bot-api-schema/compare/v0.1.11...v0.1.10) for this version  ##### Version 0.1.10 - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/a9ef3a1b8f4e1a75b55a9b80877eddc2c6f07ec4) `disable_link_preview` parameter to POST:/messages method to disable links parsing in text - [Added](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/eb99e8ab97b55fa196d9957fca34d2316a4ca8aa) `sending_file` action - [Removed](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/7a5ab5f0ea1336b3460d1827a6a7b3b141e19776) several deprecated properties - `photo` upload type [renamed](https://github.com/tamtam-chat/tamtam-bot-api-schema/commit/74505883e6acb306686a6d141414aeaf5131ef49) to `image`. *C* is for consistency  To see changelog for older versions visit our [GitHub](https://github.com/tamtam-chat/tamtam-bot-api-schema/releases).  # noqa: E501

    OpenAPI spec version: 0.5.2
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
from openapi_client.models.callback_constructor_input import CallbackConstructorInput
from openapi_client.models.chat import Chat
from openapi_client.models.chat_admin_permission import ChatAdminPermission
from openapi_client.models.chat_button import ChatButton
from openapi_client.models.chat_list import ChatList
from openapi_client.models.chat_member import ChatMember
from openapi_client.models.chat_members_list import ChatMembersList
from openapi_client.models.chat_patch import ChatPatch
from openapi_client.models.chat_status import ChatStatus
from openapi_client.models.chat_title_changed_update import ChatTitleChangedUpdate
from openapi_client.models.chat_type import ChatType
from openapi_client.models.constructed_message import ConstructedMessage
from openapi_client.models.constructor_answer import ConstructorAnswer
from openapi_client.models.constructor_input import ConstructorInput
from openapi_client.models.contact_attachment import ContactAttachment
from openapi_client.models.contact_attachment_payload import ContactAttachmentPayload
from openapi_client.models.contact_attachment_request import ContactAttachmentRequest
from openapi_client.models.contact_attachment_request_payload import ContactAttachmentRequestPayload
from openapi_client.models.error import Error
from openapi_client.models.file_attachment import FileAttachment
from openapi_client.models.file_attachment_payload import FileAttachmentPayload
from openapi_client.models.file_attachment_request import FileAttachmentRequest
from openapi_client.models.get_pinned_message_result import GetPinnedMessageResult
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
from openapi_client.models.message_chat_created_update import MessageChatCreatedUpdate
from openapi_client.models.message_constructed_update import MessageConstructedUpdate
from openapi_client.models.message_construction_request import MessageConstructionRequest
from openapi_client.models.message_constructor_input import MessageConstructorInput
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
from openapi_client.models.pin_message_body import PinMessageBody
from openapi_client.models.recipient import Recipient
from openapi_client.models.request_contact_button import RequestContactButton
from openapi_client.models.request_geo_location_button import RequestGeoLocationButton
from openapi_client.models.send_message_result import SendMessageResult
from openapi_client.models.sender_action import SenderAction
from openapi_client.models.share_attachment import ShareAttachment
from openapi_client.models.share_attachment_payload import ShareAttachmentPayload
from openapi_client.models.share_attachment_request import ShareAttachmentRequest
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

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import CHANNEL_ID, ADMINS
from helper_func import encode

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "Forward the First Message from the DB Channel (with Quotes)..", chat_id = message.from_user.id, filters=filters.forwarded, timeout=30)
        except:
            return
        if first_message.forward_from_chat:
            if first_message.forward_from_chat.id == CHANNEL_ID:
                f_msg_id = first_message.forward_from_message_id
                break
        await first_message.reply_text("Forward from the Assigned Channel only...", quote = True)
        continue
    while True:
        try:
            second_message = await client.ask(text = "Forward the Last Message from DB Channel (with Quotes)..", chat_id = message.from_user.id, filters=filters.forwarded, timeout=30)
        except:
            return
        if second_message.forward_from_chat:
            if second_message.forward_from_chat.id == CHANNEL_ID:
                s_msg_id = second_message.forward_from_message_id
                break
        await second_message.reply_text("Forward from the Assigned Channel only...", quote = True)
        continue

    string = f"get-{f_msg_id * abs(CHANNEL_ID)}-{s_msg_id * abs(CHANNEL_ID)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True, reply_markup=reply_markup)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..", chat_id = message.from_user.id, filters=filters.forwarded, timeout=30)
        except:
            return
        if channel_message.forward_from_chat:
            if channel_message.forward_from_chat.id == CHANNEL_ID:
                msg_id = channel_message.forward_from_message_id
                break
        await channel_message.reply_text("Forward from the Assigned Channel only...", quote = True)
        continue

    base64_string = await encode(f"get-{msg_id}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True, reply_markup=reply_markup)

#(©)Codexbotz

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id

# TODO: This could really use some proper error handling instead of bare-except, remaining boilerplate is because of it...

async def reply_share_url(client: Client, string: str, message: Message) -> None:
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True, reply_markup=reply_markup)


async def recieve_forwarded_msg(client, message):
    while True:
        try:
            message = await client.ask(text = "Forward the First Message from DB Channel (with Quotes)..\n\nor Send the DB Channel Post Link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return [None, None]
        msg_id = await get_message_id(client, message)
        if msg_id:
            return message, msg_id
        else:
            await message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    first_message = recieve_forwarded_msg(client, message)
    second_message = recieve_forwarded_msg(client, message)
    
    if None in [first_message, second_message]:
        return
    else:
        f_msg_id = first_message[0]
        s_msg_id, second_message = second_message


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    await reply_share_url(client, string, second_message)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    message = recieve_forwarded_msg(client, message)
    
    if message is None:
        return
    else:
        message, msg_id = message
    
    string = f"get-{msg_id * abs(client.db_channel.id)}" 
    await reply_share_url(client, string, message)
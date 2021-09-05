import os
import asyncio
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from database.support import users_info
from database.sql import add_user, query_msg
from config import OWNER_ID

USERS_LIST = """<b>⭕️Total:</b>\n\n⭕️Subscribers - {}\n⭕️Blocked- {}"""

WAIT_MSG = """"<b>Processing ...</b>"""

REPLY_ERROR = """<code>Use this command as a replay to any telegram message with out any spaces.</code>"""

@Client.on_message(filters.private & filters.command('start'))
async def start_bot(bot, m: Message):
    id = m.from_user.id
    user_name = '@' + m.from_user.username if m.from_user.username else None
    await add_user(id, user_name)
     

@Client.on_message(filters.private & filters.command('users'))
async def subscribers_count(bot, m: Message):
    id = m.from_user.id
    if id not in OWNER_ID:
        return
    msg = await m.reply_text(WAIT_MSG)
    messages = await users_info(bot)
    active = messages[0]
    blocked = messages[1]
    await m.delete()
    await msg.edit(USERS_LIST.format(active, blocked))



@Client.on_message(filters.private & filters.command('broadcast'))
async def send_text(bot, m: Message):
    id = m.from_user.id
    if id not in OWNER_ID:
        return
    if (" " not in m.text) and ("broadcast" in m.text) and (m.reply_to_message is not None):
        query = await query_msg()
        for row in query:
            chat_id = int(row[0])
            try:
                await bot.copy_message(
                    chat_id=chat_id,
                    from_chat_id=m.chat.id,
                    message_id=m.reply_to_message.message_id,
                    caption=m.caption,
                    reply_markup=m.reply_markup
                )
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except Exception:
                pass
    else:
        msg = await m.reply_text(REPLY_ERROR, m.message_id)
        await asyncio.sleep(8)
        await msg.delete()

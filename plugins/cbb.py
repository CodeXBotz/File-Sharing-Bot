#(©)moviedhamaka11

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href=''>ಮೆಂಟಲ್</a>\n○ Language : <code>ಕನ್ನಡ</code>\n○ Library : <a href=''>Playit Backup</a>\n○ Source Code : <a href=''>ಬೇಕಾ ನಿಂಗೆ</a>\n○ Channel : @moviedhamaka11\n○ Support Group : @moviedhamaka11group</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

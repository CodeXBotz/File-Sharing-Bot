#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Pemilik Chanel : <a href='tg://user?id={OWNER_ID}'>pentil kuda</a>\n○ Language : <code>Python3</code>\n○ Channel : <a href='https://t.me/Jhonny_perkasa'>@Jhonny_perkasa</a>\n○ BANTU SUPPORT <a href='https://t.me/Jhonny_perkasa'>@Jhonny_perkasa</a>BIAR BACOL MAKIN BANYAK</b></b>",
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
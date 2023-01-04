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
            text = f""" \n
😋𝙸 𝙰𝙼 𝙰 𝙾𝙵𝙵𝙸𝙲𝙸𝙰𝙻 𝚂𝚃𝙾𝚁𝙰𝙶𝙴 𝙱𝙾𝚃😋
     𝙸 𝙰𝙼 𝙿𝙰𝚁𝚃 𝙾𝙵 @Cinecoder
🤤🥴𝙳𝚁𝙴𝙰𝙼𝙻𝙰𝙽𝙳 𝙾𝙵 𝙿𝚄𝙱𝙶 𝙲𝙾𝙽𝙵𝙸𝙶🥴🤤
╭━━━━━━━━━━━━━━━➣
[❤‍🔥]➠👑𝙲𝚁𝙴𝙰𝚃𝙾𝚁👑 : <a href='tg://user?id={OWNER_ID}'>𝙽𝙾𝙾𝙱 </a>
[❤‍🔥]➠👨‍💻𝙻𝚊𝚗𝚐𝚞𝚊𝚐𝚎👨‍💻: <a herf='https://python3.com'>𝙿𝚈𝚃𝙷𝙾𝙽3 </a>
[❤‍🔥]➠🎮𝙲𝙷𝙰𝙽𝙽𝙴𝙻🎮 : <a herf='https://t.me/Cinecoder'>@𝙲𝙸𝙽𝙴𝙲𝙾𝙳𝙴𝚁 </a>
[❤‍🔥]➠✏️𝙻𝙸𝙱𝚁𝙰𝚁𝚈✏️ : <a href='https://docs.pyrogram.org/'>𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 </a>
╰━━━━━━━━━━━━━━━➣
𝚆𝙰𝙽𝚃 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙱𝙾𝚃 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 @GaikwadKunal
""",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🚫 𝙲𝙻𝙾𝚂𝙴 🚫", callback_data = "close")
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

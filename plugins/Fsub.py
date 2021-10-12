from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from pyrogram.errors import UserNotParticipant

 

 

@Client.on_message()

async def check(c, m):

    try:

        if not await c.db.is_user_exist(m.from_user.id):

            await c.db.add_user(m.from_user.id)

    except:

        pass

 

    try:

        chat = await c.get_chat_member(-1001554407676m.from_user.id)

        if chat.status == "kicked":

            await m.reply("You are Banned 😝", quote=True)

            m.stop_propagation()

    except UserNotParticipant:

        button = [[InlineKeyboardButton('🍿 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋', url='https://t.me/joinchat/9A_k-fV_qDdlN2Vl')], [InlineKeyboardButton('Refresh 🔄', url='http://t.me/file_to_links_A_bot?start=')]]

        markup = InlineKeyboardMarkup(button)

        return await m.reply(

            f"Hey {m.from_user.first_name},\n\n"

            "**You must join my channel for using me.**\n\n"

            "Press this button to join now 👇",

            parse_mode='markdown',

            reply_markup=markup)

    m.continue_propagation()

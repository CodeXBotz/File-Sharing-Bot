#(©)Codexbotz

from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNELS, CHANNEL_ID, PORT

BANNER = f"""\n\n
░█████╗░░█████╗░██████╗░███████╗██╗░░██╗██████╗░░█████╗░████████╗███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝╚════██║
██║░░╚═╝██║░░██║██║░░██║█████╗░░░╚███╔╝░██████╦╝██║░░██║░░░██║░░░░░███╔═╝
██║░░██╗██║░░██║██║░░██║██╔══╝░░░██╔██╗░██╔══██╗██║░░██║░░░██║░░░██╔══╝░░
╚█████╔╝╚█████╔╝██████╔╝███████╗██╔╝╚██╗██████╦╝╚█████╔╝░░░██║░░░███████╗
░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚══════╝
"""

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER(__name__)
    
    async def panic(self): # for use in plugins
        self.LOGGER.info("\nBot Stopped. Join https://t.me/CodeXBotzSupport for support")
        sys.exit()
    
    async def parse_invite_link(self, channel):
        try:
            link = (await self.get_chat(channel)).invite_link
            if not link:
                await self.export_chat_invite_link(channel)
                link = (await self.get_chat(channel)).invite_link
            self.invitelink = link
        except Exception as a:
            self.LOGGER.warning(a)
            self.LOGGER.warning(f"Bot can't export invite link from one of the channels! [ID: {channel}]")
            self.LOGGER.warning("Please Double check the FORCE_SUB_CHANNELS values and make sure Bot is admin in channel with 'invite users via link' permission.")
            self.panic()

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.start_timestamp = datetime.now()

        self.force_sub = {
            "active": bool(FORCE_SUB_CHANNELS)
        }
        
        if self.force_sub["active"]:
            ids = FORCE_SUB_CHANNELS.split(";") #
            self.force_sub["ids"] = ids         # This could've beed a nice walrus operator, but its only Python 3.11+ :(
            self.force_sub["links"] = [self.parse_invite_link(id) for id in ids]
            
                
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER.warning(e)
            self.LOGGER.warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.panic()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER.info(f"Bot Running..!\n\nCreated by \nhttps://t.me/CodeXBotz")
        self.LOGGER.info()
        self.username = usr_bot_me.username
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info("Bot stopped.")

if __name__ == "__main__":
    Bot().run()
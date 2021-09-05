import asyncio
from database.sql import query_msg
from pyrogram.errors import FloodWait

async def users_info(bot):
    users = 0
    blocked = 0
    identity = await query_msg()
    for id in identity:
        name = bool()
        try:
            name = await bot.send_chat_action(int(id[0]), "typing")
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception:
            pass
        if bool(name):
            users += 1
        else:
            blocked += 1
    return users, blocked

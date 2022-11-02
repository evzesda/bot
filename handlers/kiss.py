 
from pyrogram import *
from pyrogram.types import *
from helpers.basic import edit_or_reply
 
import asyncio
from handlers.help import *
 
 
@Client.on_message(filters.me & (filters.command(["kiss"], ["."]) | filters.regex("^kiss"))) 
async def hello_world(client: Client, message: Message):
    mg = await message.edit("😘😘😘")
    await asyncio.sleep(0.2)
    await mg.edit("😘😘😘😘😘")
    await asyncio.sleep(0.2)
    await mg.edit("😘😘😘😘😘😘😘")
    await asyncio.sleep(0.2) 
    await mg.edit("😘😘😘😘😘😘😘😘")
    await asyncio.sleep(0.2) 
    await mg.edit("😘😘😘😘😘😘😘😘")
    await asyncio.sleep(0.2) 
    await mg.edit("😘😘😘😘😘😘😘") 
    await asyncio.sleep(0.2) 
    await mg.edit("😘😘😘😘😘😘😘") 
    await asyncio.sleep(0.2) 
    await mg.edit("😘😘😘😘😘😘")


add_command_help(
    "kiss",
    [
        [".kiss", "Random editing Reply."],
    ],
)

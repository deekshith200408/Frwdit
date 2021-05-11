#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import FloodWait
from config import Config
from translation import Translation

FROM = Config.FROM_CHANNEL
TO = Config.TO_CHANNEL
FILTER = Config.FILTER_TYPE

@Client.on_message(filters.private & filters.command(["run"]))
async def run(bot, message):
    if str(message.from_user.id) not in Config.OWNER_ID:
        return
    buttons = [[
        InlineKeyboardButton(' 𝙲𝙻𝙾𝚂𝙴 𝙿𝚁𝙾𝙶𝚁𝙰𝙼𝙴', callback_data='stop_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    m = await bot.send_message(
        text="<i>🚀𝐅𝐢𝐥𝐞 𝐅𝐨𝐫𝐰𝐚𝐫𝐝𝐢𝐧𝐠 𝐒𝐭𝐚𝐫𝐭𝐞𝐝.𝐒𝐭𝐚𝐲 𝐓𝐮𝐧𝐞𝐝 😉</i>",
        reply_markup=reply_markup,
        chat_id=message.chat.id
    )

    files_count = 0
    async for message in bot.USER.search_messages(chat_id=FROM,offset=Config.SKIP_NO,limit=Config.LIMIT,filter=FILTER):
        try:
            if message.video:
                file_name = message.video.file_name
            elif message.document:
                file_name = message.document.file_name
            elif message.audio:
                file_name = message.audio.file_name
            else:
                file_name = None
            await bot.copy_message(
                chat_id=TO,
                from_chat_id=FROM,       
                caption=Translation.CAPTION.format(file_name),
                message_id=message.message_id
            )
            files_count += 1
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception as e:
            print(e)
            pass
   # await m.delete()
    buttons = [[
        InlineKeyboardButton('⚔️JOIN OUR GROUP⚔️', url='https://t.me/UM_Requests')
    ]] 
    reply_markup = InlineKeyboardMarkup(buttons)
    await m.edit(
        text=f"<u><i>🛸𝐒𝐔𝐂𝐒𝐔𝐒𝐅𝐔𝐋𝐘 𝐅𝐎𝐑𝐖𝐎𝐑𝐃𝐄𝐃 𝐀𝐋𝐋 𝐓𝐎 𝐆𝐈𝐕𝐄𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋.</i></u>\n\n<b>𝚃𝙾𝚃𝙻𝙴 𝙵𝙾𝚁𝚆𝚁𝙳𝙴𝙳 𝙵𝙸𝙻𝙴𝚂 𝙸𝚂:-</b> <code>{files_count}</code> <b>Files</b>\n<b>𝙏𝙝𝙖𝙣𝙠𝙨 𝙛𝙤𝙧 𝙪𝙨𝙞𝙣𝙜 𝘿𝙀𝙀𝙆𝙎 𝘾𝙧𝙚𝙖𝙩𝙚𝙙 𝙗𝙤𝙩❤️</b>",
        reply_markup=reply_markup
    )
        

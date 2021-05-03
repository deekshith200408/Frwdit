import os
from config import Config

class Translation(object):
  START_TXT = """<b>🥰 𝗛𝗔𝗶 {}!!</b>
<i>😎𝗜 𝗔𝗠 𝗦𝗜𝗠𝗣𝗟𝗘 𝗔𝗨𝗧𝗢 𝗙𝗜𝗟𝗘 𝗙𝗢𝗥𝗪𝗢𝗥𝗗𝗘𝗥 𝗕𝗢𝗧.📽️

🤹𝗧𝗛𝗜𝗦 𝗕𝗢𝗧 𝗙𝗢𝗥𝗪𝗢𝗥𝗗 𝗔𝗟𝗟 𝗙𝗜𝗟𝗘𝗦 𝗧𝗢 𝗢𝗡𝗘 𝗣𝗨𝗕𝗟𝗜𝗖 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗣𝗘𝗥𝗦𝗢𝗡𝗔𝗟 𝗖𝗛𝗔𝗡𝗡𝗘𝗟.🤹

🏅𝐌𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐞𝐝 𝐛𝐲 =» @Deeks_04_8...""" 
     


  CAPTION = "<code>{}</code>\n\n" + str(Config.CAPTION)
  HELP_TXT = """<b>⚡Follow These Steps!!💎</b>
<b>♻️ Currectly fill your Heroku Config vars</b> <code>FROM_CHANNEL</code> and <code>TO_CHANNEL</code> <b>and other Vars</b>
<b>♻️ Then give admin permission in your personal telegram channel</b>
<b>♻️ Then send any message In your personal telegram channel</b>
<b>♻️ Then use /run command in your bot</b>

<b><u>Available Command</b></u>

💎 /start - <b>Bot Alive</b>
💎 /help - <b>more help</b>
💎 /run - <b>start forward</b>
💎 /about - <b>About Me</b>"""
  ABOUT_TXT = """<b><u>👔MY INFO</b></u>

<b>ʙᴏᴛs ɴᴀᴍᴇ :</b> <code>ᴜᴍʀ ғᴏʀᴡᴏʀᴅᴇʀ ʙᴏᴛ</code>
<b>ғᴜɴᴅᴇʀ:</b> <code>ᴅᴇᴇᴋsʜɪᴛʜ ɢᴏᴡᴅᴀs</code>"""

import os
from config import Config

class Translation(object):
  START_TXT = """<b>🥰 𝗛𝗔𝗶 {}!!</b>
<i>😎𝗜 𝗔𝗠 𝗦𝗜𝗠𝗣𝗟𝗘 𝗔𝗨𝗧𝗢 𝗙𝗜𝗟𝗘 𝗙𝗢𝗥𝗪𝗢𝗥𝗗𝗘𝗥 𝗕𝗢𝗧.📽️

🤹𝗧𝗛𝗜𝗦 𝗕𝗢𝗧 𝗙𝗢𝗥𝗪𝗢𝗥𝗗 𝗔𝗟𝗟 𝗙𝗜𝗟𝗘𝗦 𝗧𝗢 𝗢𝗡𝗘 𝗣𝗨𝗕𝗟𝗜𝗖 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗣𝗘𝗥𝗦𝗢𝗡𝗔𝗟 𝗖𝗛𝗔𝗡𝗡𝗘𝗟.🤹

🏅𝐌𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐞𝐝 𝐛𝐲 =» @Deeks_04_8...""" 
     


  CAPTION = "<code>{}</code>\n\n" + str(Config.CAPTION)
  HELP_TXT = """⚡ғᴏʟʟᴏᴡ ᴛʜᴇsᴇ sᴛᴇᴘs!!😎
♻️ ᴄᴜʀʀᴇᴄᴛʟʏ ғɪʟʟ ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ ᴄᴏɴғɪɢ  - ғʀᴏᴍ_ᴄʜᴀɴɴᴇʟ ᴀɴᴅ - ᴛᴏ_ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴠᴀʀs.
♻️ ᴛʜᴇɴ ɢɪᴠᴇ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ ɪɴ ʏᴏᴜʀ ᴘᴇʀsᴏɴᴀʟ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ.
♻️ ᴛʜᴇɴ sᴇɴᴅ ᴀɴʏ ᴍᴇssᴀɢᴇ ɪɴ ʏᴏᴜʀ ᴘᴇʀsᴏɴᴀʟ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ.
♻️ ᴛʜᴇɴ ᴜsᴇ /run ᴄᴏᴍᴍᴀɴᴅ ɪɴ ʏᴏᴜʀ ʙᴏᴛ.

⚔️ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅ⚔️

💎 /start - ʙᴏᴛ ᴀʟɪᴠᴇ.
💎 /help - ᴍᴏʀᴇ ʜᴇʟᴘ.
💎 /run - sᴛᴀʀᴛ ғᴏʀᴡᴀʀᴅ.
💎 /about - ᴀʙᴏᴜᴛ ᴍᴇ."""
  ABOUT_TXT = """<b><u>👔MY INFO</b></u>

<b>ʙᴏᴛs ɴᴀᴍᴇ :</b> <code>ᴜᴍʀ ғᴏʀᴡᴏʀᴅᴇʀ ʙᴏᴛ</code>
<b>ғᴜɴᴅᴇʀ:</b> <code>ᴅᴇᴇᴋsʜɪᴛʜ ɢᴏᴡᴅᴀs</code>"""

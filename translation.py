import os
from config import Config

class Translation(object):
  START_TXT = """<b> 𝐻𝐼 {}!!</b>
<i>𝐼'𝑚 𝑆𝑖𝑚𝑝𝑙𝑒 𝐴𝑢𝑡𝑜 𝑓𝑖𝑙𝑒 𝐹𝑜𝑟𝑤𝑎𝑟𝑑 𝐵𝑜𝑡

𝑇𝒉𝑖𝑠 𝐵𝑜𝑡 𝑓𝑜𝑟𝑤𝑎𝑟𝑑 𝑎𝑙𝑙 𝑓𝑖𝑙𝑒𝑠 𝑡𝑜 𝑂𝑛𝑒 𝑃𝑢𝑏𝑙𝑖𝑐 𝑐𝒉𝑎𝑛𝑛𝑒𝑙 𝑡𝑜 𝑌𝑜𝑢𝑟 𝑃𝑒𝑟𝑠𝑜𝑛𝑎𝑙 𝑐𝒉𝑎𝑛𝑛𝑒𝑙

𝑀𝑜𝑟𝑒 𝑑𝑒𝑡𝑎𝑖𝑙𝑠/help</i>"""
  CAPTION = "<code>{}</code>\n\n" + str(Config.CAPTION)
  HELP_TXT = """<b>Follow These Steps!!</b>
<b>• Currectly fill your Heroku Config vars</b> <code>FROM_CHANNEL</code> and <code>TO_CHANNEL</code> <b>and other Vars</b>
<b>• Then give admin permission in your personal telegram channel</b>
<b>• Then send any message In your personal telegram channel</b>
<b>• Then use /run command in your bot</b>

<b><u>Available Command</b></u>

* /start - <b>Bot Alive</b>
* /help - <b>more help</b>
* /run - <b>start forward</b>
* /about - <b>About Me</b>"""
  ABOUT_TXT = """<b><u>My Info</b></u>

<b>Name :</b> <code>Auto Forward Bot</code>
<b>Credit :</b> <code>ᴅᴇᴇᴋsʜɪᴛʜ ɢᴏᴡᴅᴀs</code>

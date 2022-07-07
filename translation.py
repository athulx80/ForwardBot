import os
from config import Config

class Translation(object):
  START_TXT = """<b>Hey {}!!</b>
<i>I'm Simple Auto file Forward Bot
This Bot forward all files to One Public channel to Your Personal channel
More details /help</i>"""
  CAPTION = "`{}`\n\n" + str(Config.CAPTION)
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

<b>•𝙽𝙰𝙼𝙴 :</b> <code>𝙰𝚄𝚃𝙾 𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝙱𝙾𝚃</code>
<b>•𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁::</b> <a href='https://t.me/athulx80'>𝙰𝚃𝙷𝚄𝙻</a>
<b>•𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 :</b> <code>𝙿𝚈𝚃𝙷𝙾𝙽𝟹</code>
<b>•𝙻𝙸𝙱𝚁𝙰𝚁𝚈 :</b> <code>𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝚅𝟷.𝟸.𝟿</code>
<b>•𝚂𝙴𝚁𝚅𝙴𝚁 :</b> <code>𝙷𝙴𝚁𝙾𝙺𝚄</code>
<b>•𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ::</b> <a href='https://t.me/+jG8skQAT68I5MmRl'>𝙼𝙾𝚅𝙸𝙴𝚂 𝙴𝙼𝙿𝙸𝚁𝙴</a>"""

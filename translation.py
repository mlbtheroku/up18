from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
<b>Hey {} </b>

<b>I am Telegram Most Powerful Url Uploader Bot</b>

<b>I can Upload Any Link in File or Video</b>

<b>Use Help Command to Know How to Use me</b>

<b>Made With 💕 By </b><b>@Tellybots_4u</b>
"""
    HELP_TEXT = """
<b>Link to Media or File</b>
➠ Send a link for upload to telegram file or media.</b>

<b>Set Thumbnail</b>
➠ Send a photo to make it as permanent thumbnail.</b>

<b>Deleting Thumbnail</b>
➠ Send /delthumbnail to delete thumbnail.</b>

<b>Show Thumbnail</b>
➠ <b>Send /viewthumbnail to view custom thumbnail.</b>

<b>Made With 💕 By</b><b> @Tellybots_4u</b>
"""
    ABOUT_TEXT = """
- **🤖 Bot :** URL Uploader\n
- **👲 Developer :** [Tellybots_4u](https://telegram.me/tellybots_4u)\n
- **👥 Channel :** [Fayas Noushad](https://telegram.me/tellybots_4u)\n
- **❄️ Credits :** Everyone in this journey\n
- **🍴 Source :** [Click here](https://t.me/tellybots_digital)\n
- **📝 Language :** [Python3](https://python.org)\n
- **📚 Library :** [Pyrogram v1.2.0](https://pyrogram.org)\n
- **🌟 Server :** [Heroku](https://heroku.com)\n
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Update Channel', url='https://telegram.me/tellybots_4u'),
        InlineKeyboardButton('💬 Support Group', url='https://telegram.me/tellybots_support')
        ],[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = """<b>Select The Desired Format As Per Wish for Uploading</b>"""
    CHECKING_LINK = "<code>Analysing Your Link</code>⏳"
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    DOWNLOAD_START = "<code>Downloading To My server Please Wait...</code>"    
    UPLOAD_START = "<code>Uploading into Telegram...</code>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    CUSTOM_CAPTION_UL_FILE = "<b>Join :-</b> @Tellybots_4u"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    REPORT_SITE_TEXT = "<code>Sorry not uploading in this site here because this site is reporting site.</code>"
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    FORCE_SUBSCRIBE_TEXT = "<code>Please Join My Updates Channel for using me 😌😉....</code>"
    FREE_USER_LIMIT_Q_SZE = "Sorry Friend, Free users can only 1 request per {} minutes. Please try again after {} seconds later."

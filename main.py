#MIT License

#Copyright (c) 2021 subinps

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
from pyrogram.raw import functions, types
from pyrogram import Client, idle
from pyromod import listen
from config import Config
STATUS=Config.STATUS

USER=Config.USER
bot = Client(
    "InstaSessibon",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    workers=50,
    plugins=dict(root="plugins")
    )


async def main():
    async with bot:
        await bot.download_media(Config.INSTA_SESSIONFILE_ID, file_name=f"./{Config.USER}")
        Config.L.load_session_from_file(USER, filename=f"./{USER}")
        STATUS.add(1)

if Config.INSTA_SESSIONFILE_ID:
    bot.run(main())

bot.start()
bot.send(
    functions.bots.SetBotCommands(
        commands=[
            types.BotCommand(
                command="start",
                description="Check if bot alive"
            ),
            types.BotCommand(
                command="help",
                description="How to use"
            ),
            types.BotCommand(
                command="login",
                description="login into your Instagram account"
            ),
            types.BotCommand(
                command="logout",
                description="Logout from Instagram"
            ),
            types.BotCommand(
                command="account",
                description="Shows details of logged in account"
            ),
            types.BotCommand(
                command="posts",
                description="Download all posts from given username"
            ),
            types.BotCommand(
                command="feed",
                description="Download posts in your feed"
            ),
            types.BotCommand(
                command="igtv",
                description="Download IGTV videos of given username"
            ),
            types.BotCommand(
                command="saved",
                description="Download specified number of posts from your saved posts "
            ),
            types.BotCommand(
                command="story",
                description="Download stories of given username"
            ),
            types.BotCommand(
                command="stories",
                description="Downloads stories off all your followees"
            ),
            types.BotCommand(
                command="followers",
                description="Sends a list of followers of given username"
            ),
            types.BotCommand(
                command="followees",
                description="Sends a list followees of given username"
            ),
            types.BotCommand(
                command="fans",
                description="Get a list of followees who is following back."
            ),
            types.BotCommand(
                command="notfollowing",
                description="Get a list of followees who is not following back."
            ),
            types.BotCommand(
                command="tagged",
                description="Download all posts tagged with given username"
            ),
            types.BotCommand(
                command="highlights",
                description="Downloads highlights from given username"
            ),
            types.BotCommand(
                command="restart",
                description="Stop all processes and restart bot"
            ),
        ]
    )
)

idle()
bot.stop()

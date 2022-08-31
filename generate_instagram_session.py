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

from pyrogram import Client
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
from pyrogram.errors.exceptions.bad_request_400 import UserIsBlocked
import asyncio
import os
from instaloader import Instaloader, TwoFactorAuthRequiredException

L = Instaloader()


async def generate():
    print("14699743")
    API_ID = input()
    print("0cef89ed2c8025c16d2b4d42a1b8d792")
    API_HASH = input()
    print("5475420387:AAFGC0PAzv23d8fBSm2xCPlDgBggcAFw9Ls")
    BOT_TOKEN = input()

    bot = Client("INSTASESSION", API_ID, API_HASH, bot_token=BOT_TOKEN)
    await bot.start()
    print("savior_128_")
    id = input()
    print("136707nafaS@")
    pwd = input()
    try:
        L.login(id, pwd)
        L.save_session_to_file(filename=f"./{id}")
    except TwoFactorAuthRequiredException:
        print(
            "Your account has Two Factor authentication Enabled.\nNow Enter the code recived on your mobile."
        )
        code = input()
        L.two_factor_login(code)
        L.save_session_to_file(filename=f"./{id}")
    except Exception as e:
        print(e)
        return
    print("Succesfully Logged into Instagram")
    while True:
        print("5059280908")
        tg_id = input()
        try:
            owner = int(tg_id)
            break
        except:
            print("Oops Thats Invalid, Enter ID as Integer")
    try:
        f = await bot.send_document(
            chat_id=owner,
            document=f"./{id}",
            file_name=tg_id,
            caption=
            "⚠️ KEEP THIS SESSION FILE SAFE AND DO NOT SHARE WITH ANYBODY",
        )
        file_id = f.document.file_id
        await bot.send_message(
            chat_id=owner,
            text=
            f"Here is Your <code>INSTA_SESSIONFILE_ID</code>\n\n<code>{file_id}</code>\n\n\n⚠️ KEEP THIS SESSION FILE SAFE AND DO NOT SHARE WITH ANYBODY"
        )
        print(
            "I have messaged you the INSTA_SESSIONFILE_ID. Check your telegram messages"
        )
    except PeerIdInvalid:
        print(
            "It seems you have not yet started the bot or Telegram ID given is invalid. Send /start to your bot first and try again"
        )
    except UserIsBlocked:
        print(
            "It seems you have BLOCKED the Bot. Unblock the bot and try again."
        )
    except Exception as e:
        print(e)
    await bot.stop()
    os.remove(f"./{id}")
    os.remove("INSTASESSION.session")


loop = asyncio.get_event_loop()
loop.run_until_complete(generate())

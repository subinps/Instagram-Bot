# Instagram Manager Bot
The most advanced Instagram Downloader Bot.

```
Please fork this repository don't import code
Made with Python3
(C) @subinps
Copyright permission under MIT License
License -> https://github.com/subinps/Instagram-Bot/blob/main/LICENSE
```


You can Download almost anything From your Instagram Account.

**What Can Be Downloaded?:**
```
    1. All posts of any Profile. (Both Public and Private,for private profiles you need to be a follower.)
    2. All Posts from your feed.
    3. Stories of any profile (Both Public and Private,for private profiles you need to be a follower.)
    4. DP of any profile (No need to follow)
    5. Followers and Followees List of any Profile.
    6. List of followees who follows back the given username.
    7. List of followees who are not following back the given username.
    8. Stories of your Followees.
    9. Tagged posts of any profile.
    10. Your saved Posts.
    11. IGTV videos.
    12. Highlights from any profiles.
    13. Any Public Post from Link(Post/Reels/IGTV)

```

**Available Commands and Usage**
```
/start - Check wheather bot alive.
/restart - Restart the bot (If you messed up anything use /restart.)
/help - Shows this menu.
/login - Login into your account.
/logout - Logout of your account.
/account - Shows the details of logged in account.

/posts <username> - Download posts of any username. Use /posts to download own posts or  /posts <username> for others.
Example : /posts samantharuthprabhuoffl

/igtv <username> - Download IGTV videos from given username. If no username given, downloads your IGTV.

/feed <number of posts to download> - Downloads posts from your feed.If no number specified all posts from feed will be downloaded.
Example: /feed 10 to download latest 10 posts from feed.

/saved <number of posts to download> - Downloads your saved posts. If no number specified all saved posts will be downloaded.
Example: /saved 10 to download latest 10 saved posts.

/followers <username> - Get a list of all followers of given username. If no username given, then your list will be retrieved.
Example: /followers samantharuthprabhuoffl

/followees <username> - Get a list of all followees of given username. If no username given, then your list will be retrieved.

/fans <username> - Get a list of of followees who follow back the given username. If no username given, your list will be retrieved.

/notfollowing <username> - Get a list of followees who is not following back the given username.

/tagged <username> - Downloads all posts in which given username is tagged. If nothing given your tagged posts will be downloaded.

/story <username> - Downloads all stories from given username. If nothing given your stories will be downloaded.

/stories - Downloads all the stories of all your followees.

/highlights <username> - Downloads highlights from given username, If nothing given your highlights will be downloaded.

```

### Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/subinps/Instagram-Bot)

Watch This [Video](https://youtu.be/aVkmoVPSOYI) Tutorial For Better Understanding.

While Deploying fill `INSTA_SESSIONFILE_ID`, either by running [generate_instagram_session.py](https://github.com/subinps/Instagram-Bot/blob/main/generate_instagram_session.py]) in terminal or using /login after deploy or use [repl.it](https://replit.com/@subinps/generateInstagramSession)

For Generating Session after deployment, You Must leave the Variable as blank and fill manually after generating `INSTA_SESSIONFILE_ID` from your bot by sending /login.


### Deploy to VPS

```sh
git clone https://github.com/subinps/Instagram-Bot
cd Instagram-Bot
pip3 install -r requirements.txt
# <Create Variables appropriately>
python3 main.py
```

### Variables

* `API_HASH` API Hash from [my.telegram.org](https://my.telegram.org/)
* `API_ID` API ID from [my.telegram.org](https://my.telegram.org/)
* `BOT_TOKEN` Bot token from [@BotFather](https://telegram.dog/BotFather)
* `OWNER_ID` Telegram Id of Owner.
* `INSTAGRAM_USERNAME` Your Instagram username
* `INSTA_SESSIONFILE_ID` Your Instagram session file ID. Generate either by running [generate_instagram_session.py](https://github.com/subinps/Instagram-Bot/blob/main/generate_instagram_session.py]) in terminal or using /login after deploy or use [repl.it](https://replit.com/@subinps/generateInstagramSession)


### Note

```
Contributions are welcomed, But Kanging and editing a few lines wont make you a Developer.
Fork the repo, Do not Import code.

```

#### Support

Connect Me On [Telegram](https://telegram.dog/subinps_bot)


```
LEGAL DISCLAIMER

Developer or his team won't be liable for any loss caused by MISUSE of this Script.
This Bot is Indended to be used only for Educational Purposes.

```

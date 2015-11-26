# MonstercatConnectNotifier
[![Build Status](https://travis-ci.org/z3ntu/MonstercatYoutubeNotifier.svg)](https://travis-ci.org/z3ntu/MonstercatYoutubeNotifier)
## Requirements
- Python 3 or newer
- A Google Account
- A Telegram account

## Setup
- Copy `config.DEFAULT.py` to `config.py`

#### Create your Telegram bot
- Write `/newbot` to [@BotFather](http://telegram.me/botfather) on Telegram and follow the instructions
- Copy the token you get at the end into `bot_token` in `config.py`

#### Create your Telegram channel
This depends on the platform you are doing this on (these instructions are for Telegram desktop)
- Click the "create" icon in the search field
- Choose `New channel` and give it a name
- Add your bot (use the @username) as an administrator to the channel
- Copy the channel username into `chat_id` in `config.py` (that it looks like `chat_id="@mcatyoutube"`)

#### Get an API Key from Google
- Go to https://console.developers.google.com/
- Open the sidebar and go to *API Manager*
- You will get to a page called _Create a project_. Give it a name and click create.
- Wait.
- Go to *Credentials* in the sidebar.
- Click *Add credentials* and then *API Key*
- Choose *Server key*. Give it a name and hit create.
- Copy the API Key into your `config.py` file.
- Go to *Overview* in the sidebar.
- Go down to the *YouTube Data API* and click *Enable API*.

#### General
- Start `notifier.py`

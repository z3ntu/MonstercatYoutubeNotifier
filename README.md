# MonstercatConnectNotifier
[![Build Status](https://travis-ci.org/z3ntu/MonstercatYoutubeNotifier.svg)](https://travis-ci.org/z3ntu/MonstercatYoutubeNotifier)
## Requirements
- Python 3 or newer
- A Google (Youtube) Account
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

#### Get a YouTube API Key
- _coming soon_

#### General
- Start `notifier.py`

#!/usr/bin/python3

import json
import os
import pickle
import sys
from time import strftime

import requests

import config

YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/search"
DATA_PATH = os.path.expanduser('~/.monstercatconnect/')
SAVE_FILE = DATA_PATH + "youtubesave.dat"
LOG_FILE = DATA_PATH + "youtubeoutput.log"

TELEGRAM_API_BASE = "https://api.telegram.org/bot" + config.telegram['bot_token'] + "/"

# temp
LOG = sys.__stdout__

REMOVED_COOKIE_FILE = False


class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = LOG

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()


def main():
    create_directories()
    global LOG
    LOG = open(LOG_FILE, "a")

    log("------ BEGIN MONSTERCATYOUTUBENOTIFIER ------")

    # based on http://stackoverflow.com/a/616672/3527128
    sys.stderr = Logger()

    new = load_videos()
    new_info = get_video_info(new)
    old_info = load_from_file(SAVE_FILE)
    new_items = list(set(new_info) - set(old_info))

    if len(new_items):
        for new_item in new_items:
            send_message(new_item[1])
    else:
        log("No new song!")

    # write to file if everything worked (no exceptions etc)
    write_to_file(SAVE_FILE, new_info)


def load_videos():
    log("Loading video list...")
    payload = {"key": config.youtube['api_key'], "channelId": config.youtube['channel_id'], "part": "snippet,id",
               "order": "date", "maxResults": 5}
    videos_raw = requests.get(YOUTUBE_API_URL, params=payload)

    # PARSE RESPONSE INTO JSON
    return json.loads(videos_raw.text)


def get_video_info(videos):
    video_ids = []
    for video in videos['items']:
        video_ids.append((video['id']['videoId'], video['snippet']['title']))
    return video_ids


def create_directories():
    os.makedirs(DATA_PATH, exist_ok=True)


def write_to_file(filename, list_to_save):
    log("Saving data to file...")
    with open(filename, 'wb') as f:
        pickle.dump(list_to_save, f)


def load_from_file(filename):
    log("Loading data from file...")
    if not os.path.isfile(filename):
        return []
    with open(filename, 'rb') as f:
        return pickle.load(f)


def send_message(message):
    if "test" in sys.argv:
        return
    log("Sending message")
    requesturl = TELEGRAM_API_BASE + "sendMessage"
    payload = {"chat_id": config.telegram['chat_id'], "text": message}

    response = requests.post(requesturl, data=payload)
    log(response.text)
    return


def log(message):
    if "cron" not in sys.argv:
        print("[" + strftime("%Y-%m-%d %H:%M:%S") + "] " + message)
    LOG.write("[" + strftime("%Y-%m-%d %H:%M:%S") + "] " + message + "\n")


if __name__ == '__main__':
    main()

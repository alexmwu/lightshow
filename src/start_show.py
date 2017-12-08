from __future__ import unicode_literals
import logging
import youtube_dl
import json

# needs to happen before importing led_strip
import os

SYNCHRONIZED_LIGHTS_HOME = '/home/pi/lightshowpi/'
import sys
sys.path.insert(0, SYNCHRONIZED_LIGHTS_HOME + 'py')
# ensure __init__.py is in the above dir for this to be used as a module
import synchronized_lights_led_strip

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


OUT_DIR = '/home/pi/Music/'
EXT = 'mp3'

def my_hook(d):
    if d['status'] == 'finished':
        print("Done downloading")
    if d['status'] == 'downloading':
        print(d['filename'], d['_percent_str'], d['_eta_str'])

class MyLogger(object):
    global logger
    def debug(self, msg):
        logger.debug(msg)

    def warning(self, msg):
        logger.warning(msg)

    def error(self, msg):
        logger.error(msg)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': EXT,
        'preferredquality': '320',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    # search and dl first yt result
    'default_search': 'ytsearch',
    'outtmpl': OUT_DIR + '%(title)s.%(ext)s',
}

def start(event):
    global logger
    global ydl_opts

    logger.info(event)
    # parse song from event
    song_to_play = event['song']

    # save to specific location

    # use youtube-dl if possible
    file_name = None
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info('ytsearch:' + song_to_play)
        # only downloaded one
        title = result['entries'][0]['title']
        file_name = title + '.' + EXT

    logger.info(file_name)
    play_song(OUT_DIR + file_name)

def play_song(song):
    lightshow = synchronized_lights_led_strip.Lightshow(song)
    lightshow.play_song()


if __name__ == "__main__":
    evt = json.loads('{\"song\": \"All I Want for Christmas Is You\"}')
    start(evt, None)

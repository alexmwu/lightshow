import logging
from __future__ import unicode_literals
import youtube_dl
import rpi_ws281x
sys.path.insert(0, '/home/pi/lightshowpi/py')
import synchronized_lights_led_strip

logger = logging.getLogger()
logger.setLevel(logging.INFO)

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
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [],
    # search and dl first yt result
    'default_search': 'ytsearch1',
    'outtmpl': '/home/pi/Music',
}

def start(event, context):
    logger.info('in here')
    logger.info(event)
    # parse song from event
    song_to_play = event['song']

    # save to specific location
    ydl_opts['outtmpl'] += 'song'

    logger.info(song)
    logger.info(ydl_opts['outtmpl'])
    # use youtube-dl if possible
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])
    # play if locally available
    except SameFileError as e:
        # play there
        play_song(song)
    except Exception as e:
        print(e)

    # use lightshowpi

def play_song(song):
    # set file name
    args.file = song
    lightshow = Lightshow()
    lightshow.play_song()


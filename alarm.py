import os
import random
import subprocess
import argparse
import datetime


def get_random_video():
    steven_folder = "/Users/paulnichols/Documents/Movies/StevenUniverse/"
    video_path = random.choice(os.listdir(steven_folder))
    return steven_folder + video_path


def play_video():

    cmd = 'set volume output volume 30'
    asrun(cmd)

    video = get_random_video()
    vlc_path = "/Applications/VLC.app"
    try:
        p = subprocess.Popen(['open', '-a', vlc_path, video])
    except Exception as e:
        pass
    volume_level = 10
    for i in range(6):
        cmd = 'set volume output volume {}'.format(volume_level)
        asrun(cmd)
        sleep(30)
        volume_level += 5


def asrun(ascript):
    "Run the given AppleScript and return the standard output and error."

    osa = subprocess.Popen(['osascript', '-'],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE)
    return osa.communicate(ascript)[0]


if __name__ == '__main__':
    play_video()

import os
import random
import subprocess
import argparse
import datetime
from time import sleep


def get_random_video():
    cougar_town_folder = "/Users/paulnichols/Documents/Movies/CougarTown/"
    scrubs_folder = "/Users/paulnichols/Documents/Movies/Scrubs/"
    show_folder = random.choice([cougar_town_folder, scrubs_folder])
    video_path = random.choice(os.listdir(show_folder))
    while os.path.isdir(video_path):
        video_path = random.choice(os.listdir(show_folder))
    return show_folder + video_path


def play_video():

    video = get_random_video()
    vlc_path = "/Applications/VLC.app"
    try:
        p = subprocess.Popen(['open', '-a', vlc_path, video])
    except Exception as e:
        pass


def asrun(ascript):
    "Run the given AppleScript and return the standard output and error."

    osa = subprocess.Popen(['osascript', '-'],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE)
    return osa.communicate(ascript)[0]


if __name__ == '__main__':
    play_video()

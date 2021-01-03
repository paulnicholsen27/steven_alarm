import os
import random
import subprocess
import argparse
import datetime
from time import sleep


parser = argparse.ArgumentParser()
parser.add_argument(
    "-s", "--show",
    help="show you wish to watch (1 - 30 Rock \n 2 - Cougar Town \n 3 - Friends \n 4 - Parks and Rec \n 5 - Scrubs",
    default=0,
    type=str)
    
a = parser.parse_args()

def get_random_video(show_folder):

    video_path = random.choice(os.listdir(show_folder))
    while os.path.isdir(video_path):
        print("video path {} is a directory").format(video_path)
        video_path = random.choice(os.listdir(show_folder))
    return show_folder + video_path


def play_video():
    thirty_rock_folder = "/Users/paulnichols/Documents/Movies/30Rock/"
    cougar_town_folder = "/Users/paulnichols/Documents/Movies/CougarTown/"
    friends_folder = "/Users/paulnichols/Documents/Movies/Friends/"
    parks_and_rec_folder = "/Users/paulnichols/Documents/Movies/ParksAndRecreation/"
    scrubs_folder = "/Users/paulnichols/Documents/Movies/Scrubs/"
    show_map = {
        1: thirty_rock_folder,
        2: cougar_town_folder,
        3: friends_folder,
        4: parks_and_rec_folder,
        5: scrubs_folder
    }
    if a.show == "list":
        for k, v in show_map.iteritems():
            show_name = v.split("/")[-2]
            print("{}: {}".format(k, show_name))
        return
    else:
        show_number = int(a.show)
    show_folder = show_map.get(show_number, random.choice(list(show_map.values())))
    print(show_folder)
    video = get_random_video(show_folder)
    vlc_path = "/Applications/VLC.app"
    try:
        p = subprocess.Popen(['open', '-a', vlc_path, video])
        print("playing {}".format(video))

    except Exception as e:
        print("error playing {}".format(video))
        pass


def asrun(ascript):
    "Run the given AppleScript and return the standard output and error."

    osa = subprocess.Popen(['osascript', '-'],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE)
    return osa.communicate(ascript)[0]


if __name__ == '__main__':
    play_video()

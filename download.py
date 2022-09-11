#!/usr/bin/python3

import argparse
import os
import re
import requests
import signal
import sys
import urllib3
from colorama import init, Fore

init(autoreset=True)
clipr_xyz_url = "https://clipr.xyz/"
# Colors
blue, red, green, lgcyan = Fore.BLUE, Fore.RED, Fore.GREEN, Fore.LIGHTCYAN_EX
status = f"{Fore.YELLOW}[{Fore.LIGHTMAGENTA_EX}*{Fore.YELLOW}]{blue}"
good_status = f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{blue}"
urllib3.disable_warnings()


def get_args():
    parser = argparse.ArgumentParser()
    group1 = parser.add_mutually_exclusive_group(required=True)
    group1.add_argument("-f", "--file", help="File with clips to download", default=False)
    group1.add_argument("-c", "--clip", help="Clip to download", default=False)
    parser.add_argument("-p", "--path", help="Path where all downloaded clips will be stored", required=True)
    parser.add_argument("-r", "--resolution", help="Resolution that the downloaded clip will have, by default: 1080p",
                        default="1080", choices=["1080", "720", "480", "360"])
    args = parser.parse_args()
    return args.file, args.clip, args.path, args.resolution


def capture1080p(text):
    return re.findall(r'<span>1080p</span>\n(?:.+\n)+.*[^-\d]\.mp4">\n<span>Download</span>', text)[0]


def capture720p(text):
    findall = re.findall(r'<span>720p</span>\n(?:.+\n)+.*.mp4">\n<span>Download</span>', text)
    return findall[0]


def capture480p(text):
    return re.findall(r'<span>480p</span>\n(?:.+\n)+.*480\.mp4">\n<span>Download</span>', text)[0]


def capture360p(text):
    return re.findall(r'<span>360p</span>\n(?:.+\n)+.*360\.mp4">\n<span>Download</span>', text)[0]


def check_resolution(resolution, resolution_content):
    if resolution == "1080":
        return capture1080p(resolution_content)

    elif resolution == "720":
        return capture720p(resolution_content)

    elif resolution == "480":
        return capture480p(resolution_content)

    elif resolution == "360":
        return capture360p(resolution_content)


# Gets the link of the clip to be downloaded
def get_clip_download_link(resol_link):
    clip2download = re.findall(r'(https://.*.mp4)"', resol_link)[0]
    return clip2download


# Send a request to the "url" with the clip to be downloaded
def ask4clip(url, resolution):
    global s
    s = requests.session()
    s.get(clipr_xyz_url)
    r = s.get(url)
    resol_link = check_resolution(resolution, r.text)
    return resol_link


# Gets the clip identifier, example: OutstandingTriumphantTubersAsianGlow-XDV9sQ1F89eD24de
def parse_clip_url(clip_url):
    id_clip_url = re.findall(r'https://.*/(.*)$', clip_url)[0]

    # If the url has a "?" remove it
    if "?" in id_clip_url:
        id_clip_url = re.findall(r'(.*)\?', id_clip_url)[0]
    return id_clip_url


# Download The clip and save it with the "id_clip_url" as name
def download(clip2download, id_clip_url, clip_path):
    r = s.get(clip2download)
    final_path = os.path.join(clip_path, id_clip_url + ".mp4")
    with open(final_path, "wb") as f:
        print(f"\t{blue}{good_status} {Fore.YELLOW}Saving on: {lgcyan}{final_path}\n")
        f.write(r.content)
        f.close()


# Function to download a list of clips from a file
def dl_list(clip_resolution, clip_path, clips_file):
    all_clips = read_clips_file(clips_file).split()
    clip2download_arr = dict()

    print(f"{blue}{status} Getting the {lgcyan}urls{blue} to download the {lgcyan}clips")

    for clip in all_clips:
        id_clip_url = parse_clip_url(clip)
        ask_clip = ask4clip(clipr_xyz_url + id_clip_url, clip_resolution)
        clip2download = get_clip_download_link(ask_clip)
        user_name = re.findall(r'https://.*/(.*)/.*/.*', clip)[0]
        clip2download_arr.update({user_name + '-' + id_clip_url: clip2download})

    for id_clip_url, clip2download in clip2download_arr.items():
        print(f"{blue}{status} Downloading: {lgcyan}{clip2download}")
        download(clip2download, id_clip_url, clip_path)


def read_clips_file(clips_file):
    with open(clips_file, "r") as f:
        clips = f.read()
        f.close()
    return clips


def check_path(path):
    if not os.path.isdir(path):
        print(f"{red}[!]{blue} The path: {lgcyan}{path}{blue} does {lgcyan}not exist")
        sys.exit()


# Main Function
def main(clips_file, clip_path, clip_resolution):
    check_path(clip_path)
    dl_list(clip_resolution, clip_path, clips_file)


def sig_handler():
    print(f"\n{red}[!]{blue} Exiting...\n")
    sys.exit()


signal.signal(signal.SIGINT, sig_handler)

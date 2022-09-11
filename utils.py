import os

from config import ROOT_DIR


# Check and Create Directory
def check_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)


# To get videos from dataset directory
def get_videos(dataset):
    list_of_videos = []

    print(f"Dataset: {dataset}")
    for root, dirs, files in os.walk(os.path.join(ROOT_DIR, dataset)):
        list_of_videos += [os.path.join(root, file) for file in files if file.find(".mp4") != -1]

    return list_of_videos

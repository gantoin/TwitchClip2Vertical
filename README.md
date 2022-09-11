# Twitch clips to vertical video (for TikTok, Youtube Shorts, etc.)
🤖 IA which creates automatically vertical content from a twitch clip

⚠️ Important: This is a work in progress, and the code is not yet ready for production.

⚠️ Important 2: The clips need to be in this kind of format → fixed webcam with only one face and a game or other activity.

---

Heavily inspired by the following repertoires :

- https://github.com/EhsanMrh/UID.video_face_cropper

- https://github.com/c0rnf13ld/TwitClips

♥️ Many thanks to you @EhsanMrh & @c0rnf13ld

---

## How to use it
First, you need to install the requirements :
```bash
pip install -r requirements.txt
```

Program works with python 3.8

Then, you need to fill the resources/clips.txt file with the twitch clips you want to convert :
```bash
https://clips.twitch.tv/.../...
https://clips.twitch.tv/.../...
...
```

Finally, you can run the script :
```bash
python3 main.py
```

Your videos will be in the folder resources/faces_videos.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Tips
💌 If you want to support me, you can do it here : https://ko-fi.com/gantoin

## License
[MIT](https://choosealicense.com/licenses/mit/)

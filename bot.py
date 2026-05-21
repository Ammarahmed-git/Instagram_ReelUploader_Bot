import os
import time
import random
import shutil
import schedule

from dotenv import load_dotenv
from instagrapi import Client
from openai import OpenAI

# LOAD ENV
load_dotenv()

IG_USERNAME = os.getenv("IG_USERNAME")
IG_PASSWORD = os.getenv("IG_PASSWORD")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# AI CLIENT
ai = OpenAI(api_key=OPENAI_API_KEY)

# INSTAGRAM LOGIN
cl = Client()

cl.login(
    IG_USERNAME,
    IG_PASSWORD
)

VIDEOS_FOLDER = "videos"
UPLOADED_FOLDER = "uploaded"

# GENERATE CAPTION
def generate_caption(video_name):

    prompt = f"""
    Create a viral Instagram reel caption
    with emojis and hashtags for:
    {video_name}
    """

    response = ai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

# UPLOAD REEL
def upload_reel():

    videos = [
        file for file in os.listdir(VIDEOS_FOLDER)
        if file.endswith(".mp4")
    ]

    if len(videos) == 0:
        print("No videos found")
        return

    selected_video = random.choice(videos)

    video_path = os.path.join(
        VIDEOS_FOLDER,
        selected_video
    )

    print(f"Uploading: {selected_video}")

    caption = generate_caption(selected_video)


    # HUMAN DELAY
    time.sleep(random.randint(30,120))

    cl.clip_upload(
        video_path,
        caption=caption
    )

    print("Upload successful")

    shutil.move(
        video_path,
        os.path.join(
            UPLOADED_FOLDER,
            selected_video
        )
    )

# EVERY 20 MINUTES
schedule.every(20).minutes.do(upload_reel)

print("Bot started...")

while True:

    schedule.run_pending()

    time.sleep(5)
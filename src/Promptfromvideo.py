# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 15:13:27 2024

@author: ChenS11
"""
import base64
import cv2
import os
import requests
import subprocess
import time
from openai import AzureOpenAI
from environment import endpoint,tok
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from IPython.display import Image, display, Audio, Markdown
from moviepy.editor import VideoFileClip

os.environ['AZURE_OPENAI_ENDPOINT'] = endpoint
os.environ['AZURE_OPENAI_API_KEY'] = tok
# encode video into Videodata folder
VIDEO_PATH = "./Videodata/Foodvideo.mp4"

def process_video(video_path, seconds_per_frame=2):
    base64Frames = []
    base_video_path, _ = os.path.splitext(video_path)

    video = cv2.VideoCapture(video_path)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)
    frames_to_skip = int(fps * seconds_per_frame)
    curr_frame=0

    # Loop through the video and extract frames at specified sampling rate
    while curr_frame < total_frames - 1:
        video.set(cv2.CAP_PROP_POS_FRAMES, curr_frame)
        success, frame = video.read()
        if not success:
            break
        _, buffer = cv2.imencode(".jpg", frame)
        base64Frames.append(base64.b64encode(buffer).decode("utf-8"))
        curr_frame += frames_to_skip
    video.release()

    # Extract audio from video
    audio_path = f"{base_video_path}.mp3"
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path, bitrate="32k")
    clip.audio.close()
    clip.close()

    print(f"Extracted {len(base64Frames)} frames")
    print(f"Extracted audio to {audio_path}")
    return base64Frames, audio_path

# Extract 1 frame per second. You can adjust the `seconds_per_frame` parameter to change the sampling rate
base64Frames, audio_path = process_video(VIDEO_PATH, seconds_per_frame=2)
print(len(base64Frames))
# Initialize the AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"), 
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-02-01"
)


# Transcribe the audio
# transcription = client.audio.transcriptions.create(
#     model="whisper-1",
#     file=open(audio_path, "rb"),
# )
## OPTIONAL: Uncomment the line below to print the transcription
#print("Transcript: ", transcription.text + "\n\n")
## Generate a summary with visual and audio

# response = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#     {"role": "system", "content": "You are generating a video summary. Please provide a summary of the video. Respond in Markdown."},
#     {"role": "user", "content": [
#         "These are the frames from the video.",
#         *map(lambda x: {"type": "image_url", 
#                         "image_url": {"url": f'data:image/jpg;base64,{x}', "detail": "low"}}, base64Frames)
#         ],
#     }
#     ],
#     temperature=0,
# )
# print(response.choices[0].message.content)





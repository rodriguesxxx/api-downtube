import os
import subprocess
from flask import send_file

VIDEO_ID = ""
VIDEO_NAME = ""

class DownloadService:
    
    def __init__(self, videoId="", videoName=""):
        global VIDEO_ID, VIDEO_NAME
        VIDEO_ID = videoId
        VIDEO_NAME = videoName
    
    @staticmethod
    def download():

        cmd = [
            "yt-dlp",
            "-f",
            "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
            "-o",
            f"temp/{VIDEO_NAME}",
            f"https://www.youtube.com/watch?v={VIDEO_ID}",
        ]

        subprocess.run(cmd)
    
    @staticmethod
    def saveVideo():
        dir_video = f'src/temp/{VIDEO_NAME}.mp4'
        resposta = send_file(dir_video, as_attachment=True)
        return resposta


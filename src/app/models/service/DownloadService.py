import os
import subprocess
from flask import send_file

VIDEO_ID = ""

class DownloadService:
    
    def __init__(self, videoId=""):
        global VIDEO_ID
        VIDEO_ID = videoId
    
    @staticmethod
    def download():

        cmd = [
            "yt-dlp",
            "-f",
            "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
            "-o",
            f"temp/{VIDEO_ID}",
            f"https://www.youtube.com/watch?v={VIDEO_ID}",
        ]

        subprocess.run(cmd)
    
    @staticmethod
    def saveVideo():
        dir_video = f'src/temp/{VIDEO_ID}.mp4'
        resposta = send_file(dir_video, as_attachment=True)
        return resposta


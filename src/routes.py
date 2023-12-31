from flask import Flask, request, redirect, render_template, send_file, jsonify
from app.controllers.YoutubeApiController import YoutubeApiController as ytController
from app.controllers.DownloadController import DownloadController as dlController
import threading
from markupsafe import escape
import json
import os
import time


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/docs')
def docs():
    return render_template("documentation.html")


@app.route('/search/name/<videoId>')
def name(videoId):
    return ytController(videoId = escape(videoId)).videoName()

@app.route('/search/id/<videoName>')
def id(videoName):
    return ytController(videoName = escape(videoName)).videoId  ()

@app.route('/search/thumb/<videoId>')
def thumb(videoId):
    return ytController(videoId = escape(videoId)).videoThumb()    

@app.route('/search/extractId', methods=["POST", ])
def extractId():
    raw_data = request.data.decode('utf-8')
    json_data = json.loads(raw_data)
    
    return ytController(videoUrl=json_data['url']).videoExtractId()


def process_download(videoId, bugFix):
    
    try:
        dlController(videoId=videoId).downloadVideo()
    except BaseException:
        pass

@app.route('/download/video', methods=["POST", ])
def download():
    raw_data = request.data.decode('utf-8')
    json_data = json.loads(raw_data)
    videoId = ytController(videoUrl=json_data['url']).videoExtractId()
    # videoName = name(videoId)
    download_thread = threading.Thread(target=process_download, args=(videoId, ""))
    download_thread.start()
    download_date = {
        "url" : f"https://api-downtube-v2.onrender.com/download/save/{videoId}"
    }
    return jsonify(download_date)


# @app.route('/download/music/<videoId>')

@app.route('/download/save/<videoName>')
def save(videoName = "", text=""):
    dir_video = f'temp/{videoName}.mp4'
    print(os.system('pwd'))
    if os.path.exists(dir_video):
        dir_video = f'temp/{videoName}.mp4'
        return send_file(dir_video, as_attachment=True)
    
    return "convertendo video, aguarde..."

    

@app.route("/delete")
def delete():
    dir_ = "temp/"
    files = os.listdir(dir_)
    print(files)
    for file in files:
        os.remove(dir_+file)
    return "delete all files"
    






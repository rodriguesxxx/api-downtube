from ..models.service.DownloadService import DownloadService as dlService
VIDEO_ID = ""
VIDEO_NAME = ""

class DownloadController:

    def __init__(self, videoId="", videoName=""):
        global VIDEO_ID, VIDEO_NAME
        VIDEO_ID = videoId
        VIDEO_NAME = videoName

    @staticmethod
    def downloadVideo():
        dlService(VIDEO_ID, VIDEO_NAME).download()

    @staticmethod 
    def saveVideo():
        return dlService(videoName=VIDEO_NAME).saveVideo()

    @staticmethod
    def deleteVideo():
        pass

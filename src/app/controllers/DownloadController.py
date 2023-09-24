from ..models.service.DownloadService import DownloadService as dlService
VIDEO_ID = ""

class DownloadController:

    def __init__(self, videoId=""):
        global VIDEO_ID
        VIDEO_ID = videoId

    @staticmethod
    def downloadVideo():
        dlService(VIDEO_ID).download()

    @staticmethod 
    def saveVideo():
        return dlService(videoId=VIDEO_ID).saveVideo()

    @staticmethod
    def deleteVideo():
        pass

from ..models.service.SearchVideo import SearchVideo
from ..models.apis.api_utilities.ApiUtil import YoutubeApiUtil as api_util
VIDEO_URL = ""
VIDEO_ID = ""
VIDEO_NAME = ""

class YoutubeApiController:
    
    def __init__(self, videoUrl = "", videoId = "", videoName=""):
        global VIDEO_URL, VIDEO_ID, VIDEO_NAME
        VIDEO_URL = videoUrl
        VIDEO_ID = videoId
        VIDEO_NAME = videoName
        
    @staticmethod
    def videoName():
        return SearchVideo().name(VIDEO_ID)
    
    @staticmethod
    def videoId():
        return SearchVideo().id(VIDEO_NAME)
    
    @staticmethod
    def videoThumb():
        return SearchVideo().thumb(VIDEO_ID)
    
    @staticmethod
    def videoExtractId():
        return api_util().extractId(url=VIDEO_URL)
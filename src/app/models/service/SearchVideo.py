#### AQUI VAI A INTEGRACAO COM A API DO YT#####
from ..apis.api_handlers.YoutubeApi import YoutubeApi as yt_api



class SearchVideo:
    
    @staticmethod
    def id(videoName):
        return yt_api(videoName=videoName).getVideoIdByName()
    
    @staticmethod
    def name(videoId):
        return  yt_api(videoId=videoId).getVideoName()

    @staticmethod
    def thumb(videoId):
        return yt_api(videoId=videoId).getVideoThumb()
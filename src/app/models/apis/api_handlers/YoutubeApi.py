from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from ..api_utilities.ApiUtil import YoutubeApiUtil as yt_utils

all_video_info = []
video_id_by_name = []

class YoutubeApi:

    def __init__(self, videoId = "", videoName = ""):
        self.video_id = videoId
        self.video_name = videoName
        self.__api_key = "AIzaSyDS9yOTdsaim4X6ueteu_fX4UWalbpWVQE"
        self.__youtubeV3 = build("youtube", "v3", developerKey=self.__api_key)
        global all_video_info, video_id_by_name
        all_video_info = self.__getAllVideoInfo()
        video_id_by_name = self.__getVideoIdByName()
    
    def __getAllVideoInfo(self):
        try:
            return self.__youtubeV3.videos().list(part='snippet', id=self.video_id).execute()
        except HttpError as error:
            return None
        
    def __getVideoIdByName(self):
        try:
            response = self.__youtubeV3.search().list(part='snippet', q=self.video_name, type='video').execute()
            videos = response['items']
            for video in videos:
                title = video['snippet']['title']
                if '#shorts' not in title.lower() and '#shots' not in title.lower():
                    return video["id"]["videoId"]
            return ""
        
        except HttpError as error:
            return None
    
    @staticmethod
    def getVideoName():
        if(all_video_info):
            video_name = all_video_info['items'][0]['snippet']['title']
            return video_name
    
    @staticmethod
    def getVideoThumb():
        if(all_video_info):
            url = all_video_info['items'][0]['snippet']['thumbnails']['default']['url']
            return url
    @staticmethod
    def getVideoIdByName():
        return video_id_by_name
        
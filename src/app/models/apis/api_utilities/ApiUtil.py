class YoutubeApiUtil:
    
    @staticmethod
    def extractId(url):

        if('/watch' in url):
            video_id = url.split('v=')
            return video_id[1] 
        
        if('youtu.be/' in url):
            video_id = url.split('/')
            return video_id[-1]
        
        return "This Invalid Url"
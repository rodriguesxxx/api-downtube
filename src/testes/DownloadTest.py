import requests

class DownloadTest():
    
    def download_video(self):
        url = "http://localhost:5000/download/video"
        requestBody = {"url":"https://youtu.be/me2Rwxrp3gQ"}
        response = requests.post( url=url, json=requestBody )

        return response
    
    def save_video(self, data_json):
        urlDownload = data_json['url']
        response = requests.get(url=urlDownload)

        return response


test = DownloadTest()
responseDownload = test.download_video()

def test_content_type():
    assert responseDownload.headers['Content-Type'] == 'application/json'

responseSave = test.save_video(responseDownload.json())

def test_status_code():
    assert responseSave.status_code == 200

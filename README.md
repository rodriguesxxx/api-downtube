# api-downtube

[![STATE - EM DESENVOLVIMENTO](https://img.shields.io/badge/STATE-EM_DESENVOLVIMENTO-green)](https://)

API for youtube video download and integration in your system.

The idea for the development of this project came from the following problem: How can I download a youtube video in one line of code? so I entered the following dilemma, can I do this?
And the answer is: I did.

I faced some challenges being the first API in my life and I wanted to implement solid concepts as much as possible. Even if I miss some, but I will continue this project and refactor your code.

I learned many things throughout the development of this project, from the MVC architecture pattern, to the powerful frameork flask.
I am very satisfied with the result and this is just the beginning.

## Topics

- <a href="#what-problem-does-this-api-solve">What problem does this API solve?</a>

- <a href="#Architecture">Architecture</a>


## What problem does this API solve?

The possibility for you with few lines of code to integrate youtube videos in a simple and fast way.
In addition to being able to download videos and audios for free. No need to access third-party platforms where you don't know what's going on behind the scenes. Because we at downtube value open source

## Architecture

![arch](https://github.com/daniel-rodrigues1089/api-downtube/assets/117450018/1d127ab8-57b0-4d60-91ef-708ab875eab8)



The flask will receive the endpoint and call the controller of that endpoint which in turn will call a model. Depending on the user's request, the model can consume the youtube API or download a certain video using yt-dlp

## Features

 - ### Download videos
 - ### Download musics
 - ### Search main video information
 - ### Search video by url
 - ### Search video by name
 - ### integrate video in your application with iframe

### - Download videos

Download any video on youtube, passing its url as a parameter.

#### download flow example:

![exemple-download](https://github.com/daniel-rodrigues1089/api-downtube/assets/117450018/02f69bd0-fb59-482e-9c5d-682c5344f5b6)


#### code exemple:
```python
import requests

endpoint = "https://downtube-api/download/video"
body = {'url':"https://www.youtube.com/watch?v=TV7HOGNXybU"}

request = requests.post(url = endpoint, json = body) #return: <Response [code]>

if request.status_code == 200:
    videoDownloadUrl = request.text
else:
    print("bad requets, code error -> ", request.status_code)
```

### - Download musics

Download any music on youtube, passing its url as a parameter.

#### code exemple:

```python
import requests

endpoint = "https://downtube-api/download/music"
body = {'url':"https://www.youtube.com/watch?v=TV7HOGNXybU"}

request = requests.post(url = endpoint, json = body) #return: <Response [code]>

if request.status_code == 200:
    videoDownloadUrl = request.text
else:
    print("bad requets, code error -> ", request.status_code)
```

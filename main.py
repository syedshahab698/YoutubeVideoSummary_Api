# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:07:40 2021

@author: syeds
"""

from  youtube_transcript_api import YouTubeTranscriptApi

url = 'https://www.youtube.com/watch?v=cIZWgPmpRVc&t=353s'

url_id = url[url.find('?v=')+3:]

try:
    srt = YouTubeTranscriptApi.get_transcript(url_id)
    print([i['text'] for i in srt])
except:
    print("Sorry, there are no subtitles in the video")
























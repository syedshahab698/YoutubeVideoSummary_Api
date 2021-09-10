# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:07:40 2021

@author: syeds
"""
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from  youtube_transcript_api import YouTubeTranscriptApi



def get_summary_of_video(url):
    LANGUAGE = "english"
    SENTENCES_COUNT = 10
    url_id = url[url.find('?v=')+3:]
    srt = YouTubeTranscriptApi.get_transcript(url_id)
    subtitle_string = " ".join([i['text'] for i in srt])
    
    # print("Sorry, there are no subtitles in the video")
    
    
    parser = PlaintextParser.from_string(subtitle_string, Tokenizer(LANGUAGE))
    	   
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    
    summary_output  = ""
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        summary_output = summary_output +" ".join(sentence.words)+ "    "
    
    return summary_output


if __name__ == "__main__":
    url = 'https://www.youtube.com/watch?v=-7or4r8GLQY'
    print(get_summary_of_video(url))























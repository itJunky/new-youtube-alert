#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from googleapiclient.discovery import build
import json
from conf import token 

with build('youtube', 'v3', developerKey=token) as youtube:
    response = youtube.search().list(
            channelId='UCfhQ8TdwGVP3YwCR6wQ2vqA',
            maxResults=10,
            order='date',
            part='id, snippet'
    ).execute()
    for video in response['items']:
        print(video['snippet']['title'])
        #print(video['snippet']['description'])
        print(video['id']['videoId'])

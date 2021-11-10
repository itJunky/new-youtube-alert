#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from googleapiclient.discovery import build
import json
from conf import token
from common import in_db, store_in_db

with build('youtube', 'v3', developerKey=token) as youtube:
    response = youtube.search().list(
            channelId='UCfhQ8TdwGVP3YwCR6wQ2vqA',
            maxResults=10,
            order='date',
            part='id, snippet'
    ).execute()
    for video in response['items']:
        title = video['snippet']['title']
        vid = video['id']['videoId']

        if not in_db(vid):
            #TODO send to TG
            print("{} - {}".format(vid, title))
            store_in_db(vid)


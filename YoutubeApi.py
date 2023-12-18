from googleapiclient.discovery import build
import random
from datetime import datetime, timedelta

class YoutubeApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def get_random_video(self, start_year, end_year, keyword_in_title, video_length):
        # Set the start and end dates for the publication range based on provided years
        start_date = f"{start_year}-01-01T00:00:00Z"
        end_date = f"{end_year}-12-31T23:59:59Z"

        search_response = self.youtube.search().list(
            part='id',
            type='video',
            videoEmbeddable='true',
            maxResults=50,
            publishedAfter=start_date,
            publishedBefore=end_date,
            q=keyword_in_title,
            videoDuration=video_length  # Set the duration range in seconds
        ).execute()

        videos = search_response.get('items', [])
        if videos:
            random_video = random.choice(videos)
            video_id = random_video['id']['videoId']
            return f"https://www.youtube.com/watch?v={video_id}"
        else:
            return None

    # Example usage:
'''
            publishedAfter=(datetime.utcnow() - timedelta(days=365)).isoformat(),
            location='37.7749,-122.4194',
            locationRadius='50km',
            videoDuration='medium',
            order='date
            '''






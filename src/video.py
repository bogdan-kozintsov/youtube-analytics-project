from src.channel import Channel


class Video:

    def __init__(self, video_id: str) -> None:
        self.video_id = video_id
        try:
            self.video_info = Channel.get_service().videos().list(part='snippet,statistics', id=self.video_id).execute()
            self.title = self.video_info["items"][0]["snippet"]["title"]
            self.url = f"https://www.youtube.com/watch/{self.video_id}"
            self.view_count = self.video_info['items'][0]['statistics']['viewCount']
            self.like_count = self.video_info['items'][0]['statistics']['likeCount']
        except IndexError:
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None


    def __str__(self):
        return self.video_title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

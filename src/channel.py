import json
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from pprint import pprint

load_dotenv('../.env')
API_KEY: str = os.getenv('API_KEY')


class Channel:
    """Класс для ютуб-канала"""

    __youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.__youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

    def __str__(self):
        return f'{self.channel['items'][0]['snippet']['title']} (https://www.youtube.com/channel/{self.__channel_id})'

    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def to_json(self, json_file: str) -> None:
        data = json.dumps(self.channel)
        with open(json_file, 'w', encoding="utf-8") as f:
            f.write(data)

    @property
    def channel_id(self) -> str:
        """Выводит id канала"""
        return self.__channel_id

    @property
    def title(self) -> str:
        """Выводит в консоль название канала"""
        return self.channel['items'][0]['snippet']['title']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале"""
        channel = self.__youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        pprint(channel)

    @property
    def url(self):
        """Выводит в консоль ссылку на канал"""
        return f'https://www.youtube.com/channel/%s' % self.__channel_id

    @property
    def subscriber_сount(self):
        """Выводит в консоль количество подписчиков"""
        return self.channel['items'][0]['statistics']['subscriberCount']

    @property
    def video_сount(self):
        """Выводит в консоль количество видео"""
        return self.channel['items'][0]['statistics']['videoCount']

    @property
    def view_сount(self):
        """Выводит в консоль общее количество просмотров"""
        return self.channel['items'][0]['statistics']['viewCount']

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=API_KEY)

    '''
    получить данные о канале по его id
    docs: https://developers.google.com/youtube/v3/docs/channels/list

    сервис для быстрого получения id канала: https://commentpicker.com/youtube-channel-id.php
    '''

    # channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel
    # channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
    # printj(channel)

    '''
    получить данные по видеороликам в плейлисте
    docs: https://developers.google.com/youtube/v3/docs/playlistItems/list

    получить id плейлиста можно из браузера, например
    https://www.youtube.com/playlist?list=PLH-XmS0lSi_zdhYvcwUfv0N88LQRt6UZn
    или из ответа API: см. playlists выше
    '''
    playlist_id = 'PLH-XmS0lSi_zdhYvcwUfv0N88LQRt6UZn'
    playlist_videos = __youtube.playlistItems().list(playlistId=playlist_id,
                                                     part='contentDetails',
                                                     maxResults=50,
                                                     ).execute()

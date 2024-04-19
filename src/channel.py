import json
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
import isodate


class Channel:
    """Класс для ютуб-канала"""
    load_dotenv('../.env')
    API_KEY: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    '''
    получить данные о канале по его id
    docs: https://developers.google.com/youtube/v3/docs/channels/list

    сервис для быстрого получения id канала: https://commentpicker.com/youtube-channel-id.php
    '''

    channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel
    channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
    printj(channel)

    '''
    получить данные по видеороликам в плейлисте
    docs: https://developers.google.com/youtube/v3/docs/playlistItems/list

    получить id плейлиста можно из браузера, например
    https://www.youtube.com/playlist?list=PLH-XmS0lSi_zdhYvcwUfv0N88LQRt6UZn
    или из ответа API: см. playlists выше
    '''
    playlist_id = 'PLH-XmS0lSi_zdhYvcwUfv0N88LQRt6UZn'
    playlist_videos = youtube.playlistItems().list(playlistId=playlist_id,
                                                   part='contentDetails',
                                                   maxResults=50,
                                                   ).execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.__channel_id)

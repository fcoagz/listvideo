from typing import List
from pytube import Playlist
from ..models import Video, Channel

URL_YOUTUBE = "https://www.youtube.com/playlist?list="

class MetaDataPlaylist:
    def __init__(self, id_playlist: str = None) -> None:
        if not isinstance(id_playlist, str):
            raise ValueError('El id_playlist debe ser una cadena.')
        
        self.id_playlist = id_playlist
        self._playlist = None
        self._metadata = None
    
    def _get_data_playlist(self) -> Playlist:
        if self._playlist is None:
            self._playlist = Playlist(f'{URL_YOUTUBE}{self.id_playlist}')
        return self._playlist
    
    def _get_metadata(self):
        if self._metadata is None:
            videos = self._get_data_playlist().videos
            author_videos = {}

            for video in videos:
                hours, remainder = divmod(video.length, 3600)
                minutes, seconds = divmod(remainder, 60)

                video_data = Video(
                    title=video.title,
                    description=video.description,
                    length=f"{hours}h {minutes}min" if hours else f"{minutes}min {seconds}sec",
                    url=video.watch_url,
                    thumbnail_url=video.thumbnail_url,
                    author=video.author,
                    id_author=video.channel_id
                )
                if video.author in author_videos:
                    author_videos[video.author].append(video_data)
                else:
                    author_videos[video.author] = [video_data]
                
            data = []
            for author, videos in author_videos.items():
                if len(videos) > 1:
                    channel_data = Channel(
                        author=author,
                        videos=videos
                    )
                    data.append(channel_data)
                else:
                    for video in videos:
                        video.id_author = None
                data.extend(videos)
            self._metadata = data
        return self._metadata
    
    @property
    def title(self):
        """
        title of the playlist
        """
        return self._get_data_playlist().title
    
    @property
    def description(self):
        """
        description of the playlist
        """
        return self._get_data_playlist().description
    
    @property
    def author(self):
        """
        author of the playlist
        """
        return self._get_data_playlist().owner
    
    @property
    def videos(self) -> List[Video]:
        """
        list of videos stored in the playlist

        ```py 
        from listvideo import Playlist

        ID_PLAYLIST = "PLSmRNdrEZb6SFpcg0IUDjSCpS7W1SNfvp"

        lv = Playlist(ID_PLAYLIST)

        videos = lv.videos
        for i in range(len(videos)):
            print(f'{i}. {videos[i].title}')
        ```
        """
        metadata = self._get_metadata()
        videos = []
        
        for data in metadata:
            if isinstance(data, Video):
                videos.append(data)
        return videos
    
    @property
    def channels(self) -> List[Channel]:
        """
        organize and store YouTube channels that have more than two videos on the playlist

        ```py
        from listvideo import Playlist

        ID_PLAYLIST = "PLSmRNdrEZb6SFpcg0IUDjSCpS7W1SNfvp"

        lv = Playlist(ID_PLAYLIST)

        channels = lv.channels
        for channel in channels:
            if channel.author == 'midudev':
                print(channel)
                break
        ```
        """
        metadata = self._get_metadata()
        channels = []
        
        for data in metadata:
            if isinstance(data, Channel):
                channels.append(data)
        return channels
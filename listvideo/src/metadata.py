from pytube import Playlist, Channel
from cachetools import TTLCache, cached

from .const import ID_PLAYLIST

cache = TTLCache(maxsize=1024, ttl=(60*60)*6)

@cached(cache)
def metadata(key: str):
    try:
        if key not in cache:
            pl = Playlist(f'https://www.youtube.com/playlist?list={ID_PLAYLIST}')
            author_videos = {}
            for video in pl.videos:
                hours, remainder = divmod(video.length, 3600)
                minutes, seconds = divmod(remainder, 60)

                video_data = {
                    'title': video.title,
                    'description': video.description,
                    'length': f"{hours}h {minutes}min" if hours else f"{minutes}min {seconds}sec",
                    'url': video.watch_url,
                    'author': video.author,
                    'id_author': video.channel_id
                }
                if video.author in author_videos:
                    author_videos[video.author].append(video_data)
                else:
                    author_videos[video.author] = [video_data]
            
            for author, videos in author_videos.items():
                if len(videos) > 1:
                    channel_data = {
                        'author': author,
                        'videos': videos
                    }
                    cache[videos[0]['id_author']] = channel_data
                else:
                    for video in videos:
                        _ = video.pop('id_author')

                if 'playlist' not in cache:
                    cache['playlist'] = []
                cache['playlist'].extend(videos)

        return cache[key]

    
    except KeyError as e:
        raise Exception(f'Propiedad no encontrada: {e}')

from typing import List
from dataclasses import dataclass

@dataclass
class Video:
    title: str
    description: str
    length: str
    url: str
    thumbnail_url: str
    author: str
    id_author: str | None

@dataclass
class Channel:
    author: str
    videos: List[Video]
# listvideo

ListVideo es una biblioteca que facilita la interacción con las listas de reproducción de YouTube. Permite acceder a los metadatos de los videos y organizarlos de manera eficiente.

## Uso

La clase `Playlist` permite interactuar con una lista de reproducción de YouTube. Para utilizarla, debes instanciarla con el ID de la lista de reproducción que deseas analizar.

### Obtener información de la lista de reproducción

```py
from listvideo import Playlist

ID_PLAYLIST = "ID-PLAYLIST-YT"
lv = Playlist(ID_PLAYLIST)

author = lv.author # Obtiene el creador de la lista de reproducción
title  = lv.title # Obtiene el título de la lista de reproducción
```

### Acceder a la información de cada video
```py
from listvideo import Playlist

ID_PLAYLIST = "ID-PLAYLIST-YT"
lv = Playlist(ID_PLAYLIST)

videos = lv.videos
for i in range(len(videos)):
    print(f'{i}. {videos[i].title} - {videos[i].author}') # Imprime el título y el autor de cada video
```

La clase `Video` tiene varios atributos que puedes utilizar para obtener información detallada sobre cada video:

```py
class Video:
    title: str # Título del video
    description: str # Descripción del video
    length: str # Duración del video
    url: str # URL del video
    thumbnail_url: str # URL de la miniatura del video
    author: str # Autor del video
    id_author: str | None # ID del autor del video (puede ser None)
```

El objetivo de ListVideo es permitirte organizar y almacenar canales de YouTube que tengan más de dos videos en la lista de reproducción.

```py
from listvideo import Playlist

ID_PLAYLIST = "ID-PLAYLIST-YT"

lv = Playlist(ID_PLAYLIST)

channels = lv.channels
for channel in channels:
    if channel.author == 'midudev':
        print(channel)
        break

```

## API de listvideo
 ListVideo proporciona una API y un sistema de caché para reducir el consumo de solicitudes en tiempo real. 

```py
from listvideo import keep_alive_app

keep_alive_app()
```

### Endpoints

### `GET api/v1/videos?list=<ID-PLAYLIST>`

Este endpoint te permite obtener una lista de la información de cada video en la lista de reproducción especificada. Debes proporcionar el ID de la lista de reproducción de YouTube como parámetro list.

### `GET api/v1/channels?list=<ID-PLAYLIST>`

Este endpoint te permite obtener todos los canales encontrados en la lista de reproducción especificada.

### `GET api/v1/channels?list=<ID-PLAYLIST>&id_author=<ID-AUTHOR>`

Este endpoint te permite obtener información sobre un canal específico en la lista de reproducción especificada. Debes proporcionar el ID de la lista de reproducción de YouTube como parámetro list y el ID del autor como parámetro id_author.
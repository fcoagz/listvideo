from dataclasses import asdict
from flask import Blueprint, jsonify, request
from .utils.cache import cache
from ..data.metadata import MetaDataPlaylist

route = Blueprint('videos', __name__)

@route.route('/api/v1/videos')
def videos():
    try:
        id_list = request.args.get('list', None)

        if not id_list:
            return jsonify(error="Rellena el parametro list."), 400

        if not cache.get_data(f'{id_list}:videos'):
            metadata = MetaDataPlaylist(id_list)
            videos_list_class = metadata.videos
            videos_list = []

            for video in videos_list_class:
                video_dict = asdict(video)
                videos_list.append(video_dict)
            cache.set_data(f'{id_list}:videos', videos_list)

        return jsonify(cache.get_data(f'{id_list}:videos')), 200
    except Exception as e:
        return jsonify(error=e), 400
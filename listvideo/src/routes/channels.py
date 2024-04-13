from dataclasses import asdict
from flask import Blueprint, jsonify, request
from .utils.cache import cache
from ..data.metadata import MetaDataPlaylist

route = Blueprint('channels', __name__)

@route.route('/api/v1/channel')
def channel():
    try:
        id_list = request.args.get('list', None)
        id_author = request.args.get('id_author', None)

        if not all([id_list, id_author]):
            return jsonify(error="Rellena todos los parametros."), 400

        if not cache.get_data(f'{id_author}:author'):
            metadata = MetaDataPlaylist(id_list)
            channels_list_class = metadata.channels
            channel_dict = {}

            for channel in channels_list_class:
                if channel.videos[0].id_author == id_author:
                    channel_dict['author'] = channel.author
                    channel_dict['videos'] = [asdict(video) for video in channel.videos]
                    break
            cache.set_data(f'{id_author}:author', channel_dict)

            return jsonify(cache.get_data(f'{id_author}:author')), 200
    except Exception as e:
         return jsonify(error=e), 400

@route.route('/api/v1/channels')
def channels():
    try:
        id_list = request.args.get('list', None)

        if not id_list:
            return jsonify(error="Rellena el parametro list."), 400

        if not cache.get_data(f'{id_list}:channels'):
            metadata = MetaDataPlaylist(id_list)
            channels_list_class = metadata.channels
            channels_list = []

            for channel in channels_list_class:
                channel_dict = {}
                channel_dict['author'] = channel.author
                channel_dict['videos'] = [asdict(video) for video in channel.videos]
                channels_list.append(channel_dict)
            cache.set_data(f'{id_list}:channels', channels_list)

        return jsonify(cache.get_data(f'{id_list}:channels')), 200
    except Exception as e:
        return jsonify(error=e), 400
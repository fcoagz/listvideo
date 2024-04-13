from flask import Flask
from flask_cors import CORS
from threading import Thread
from .routes import videos, channels, index
from .exceptions import internal_server_error

app = Flask('')
CORS(app)

app.register_error_handler(500, internal_server_error)

app.register_blueprint(index.route)
app.register_blueprint(videos.route)
app.register_blueprint(channels.route)

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    """
    keep it alive as an app
    """
    t = Thread(target=run)
    t.start()
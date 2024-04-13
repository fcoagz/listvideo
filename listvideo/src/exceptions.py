from flask import jsonify

def internal_server_error(e):
    message = jsonify({"error": "Ha ocurrido un problema interno en el servidor. Por favor, inténtelo de nuevo más tarde."}), 500
    return message
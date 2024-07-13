import json
from flask import Response
from werkzeug.exceptions import Unauthorized

def register_error_handlers(app):
    @app.errorhandler(Unauthorized)
    def unauthorized_handler(error):
        return Response(json.dumps({
            'code': 'unauthorized',
            'message': "Unauthorized."
        }), status=401, content_type="application/json")
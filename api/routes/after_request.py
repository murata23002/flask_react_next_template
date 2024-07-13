import json
import os

from werkzeug.exceptions import Unauthorized

def register_after_request(app):
    @app.errorhandler(Unauthorized)
    def after_request(response):
        response.headers.add("X-Version", os.getenv("APP_VERSION", "1.0.0"))
        response.headers.add("X-Env", os.getenv("DEPLOY_ENV", "production"))
        return response

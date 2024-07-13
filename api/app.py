# app.py
import json
import logging
import os
import sys
from logging.handlers import RotatingFileHandler

from routes.after_request import register_after_request
from routes.error_handlers import register_error_handlers
from flask import Flask
from werkzeug.exceptions import Unauthorized


class Config:
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "app.log")
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOG_DATEFORMAT = "%Y-%m-%d %H:%M:%S"

class FlaskApp:
    def __init__(self, config_class=Config):
        self.app = Flask(__name__)
        self.app.config.from_object(config_class)
        self._init_extensions()
        self._setup_logging()
        self._register_blueprints()
        self._register_error_handlers()
        self._register_after_request()

    def _init_extensions(self):
        # Initialize your extensions here
        # For example:
        # db.init_app(self.app)
        # login_manager.init_app(self.app)
        pass

    def _setup_logging(self):
        if self.app.config["LOG_FILE"]:
            handler = RotatingFileHandler(
                filename=self.app.config["LOG_FILE"],
                maxBytes=10 * 1024 * 1024,  # 10MB
                backupCount=5,
            )
        else:
            handler = logging.StreamHandler(sys.stdout)

        formatter = logging.Formatter(
            fmt=self.app.config["LOG_FORMAT"], datefmt=self.app.config["LOG_DATEFORMAT"]
        )
        handler.setFormatter(formatter)

        self.app.logger.addHandler(handler)
        self.app.logger.setLevel(self.app.config["LOG_LEVEL"])

    def _register_blueprints(self):
        with self.app.app_context():
            from routes.external_api_blueprint import external_api_bp
            self.app.register_blueprint(external_api_bp)
            from routes.internal_api_blueprint import internal_api_bp
            self.app.register_blueprint(internal_api_bp)

    def _register_error_handlers(self):
        register_error_handlers(self.app)

    def _register_after_request(self):
        register_after_request(self.app)

    def run(self, host="0.0.0.0", port=None):
        if port is None:
            port = int(os.getenv("PORT", 5000))
        self.app.run(host=host, port=port)

flask_app_instance = FlaskApp()
app = flask_app_instance.app

if __name__ == "__main__":
    flask_app_instance.run()

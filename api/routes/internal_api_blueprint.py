import json
import os
from flask import Blueprint, Response, jsonify

bp = Blueprint('internal_api', __name__, url_prefix='/api')

@bp.route('/data')
def data():
    return jsonify({'data': 'Sample Data'})

@bp.route("/")
def index():
    return "Hello, World!"

internal_api_bp = bp
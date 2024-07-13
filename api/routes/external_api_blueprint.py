import json
import os
from flask import Blueprint, Response, jsonify

bp = Blueprint('external_api', __name__, url_prefix='/api')

@bp.route('/health')
def health():
    return Response(json.dumps({
        'status': 'ok',
        'version': os.getenv('APP_VERSION', '1.0.0')
    }), status=200, content_type="application/json")

external_api_bp = bp

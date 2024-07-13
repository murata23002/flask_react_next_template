#!/bin/bash

set -e
if [[ "${DEBUG}" == "true" ]]; then
    flask run --host=${APP_BIND_ADDRESS:-0.0.0.0} --port=${APP_PORT:-5001} --debug --reload
else
    gunicorn \
      --bind "${APP_BIND_ADDRESS:-0.0.0.0}:${APP_PORT:-5001}" \
      --workers ${SERVER_WORKER_AMOUNT:-1} \
      --worker-class ${SERVER_WORKER_CLASS:-gevent} \
      --timeout ${GUNICORN_TIMEOUT:-200} \
      --preload \
      app:app
  fi
fi
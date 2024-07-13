#!/bin/bash
set -e

export NEXT_PUBLIC_DEPLOY_ENV=${DEPLOY_ENV}
export NEXT_PUBLIC_EDITION=${EDITION}
export NEXT_PUBLIC_PUBLIC_API_PREFIX=${APP_API_URL}/api

pm2 start ./pm2.json --no-daemon

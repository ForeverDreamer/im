#!/bin/sh

set -x
set -eo pipefail

export PYTHONPATH=/data/im
export FLASK_ENV=development
export PYTHONUNBUFFERED=1
nohup python web/app.py &
tail -f nohup.out
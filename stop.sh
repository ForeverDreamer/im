#!/bin/sh

set -x
set -eo pipefail

lsof -t -i tcp:5000 | xargs kill -9
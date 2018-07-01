#!/usr/bin/env bash

python /opt/application/server.py 8001 > /var/log/face-detect 2>&1 &

cd /opt/application/demo/
python -m SimpleHTTPServer 8002 > /var/log/face-detect-demo 2>&1 &

tail -f /dev/null
import cgi
import json
import os
import sys
import urlparse
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from src.detector import detect
from src.formatter import group_by_context
from src.reader import get_image_from_base64


class HttpProcessor(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type', 'application/json')
        allow_origin_ = os.environ['ACCESS_CONTROL_ALLOW_ORIGIN'] \
            if 'ACCESS_CONTROL_ALLOW_ORIGIN' in os.environ \
            else 'http://localhost'
        self.send_header("Access-Control-Allow-Origin", allow_origin_)
        self.end_headers()

        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            post_vars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.getheader('content-length'))
            post_vars = urlparse.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            post_vars = {}

        im = get_image_from_base64(post_vars['image'][0])
        shapes = detect(im)

        result = []
        for s in shapes:
            result.append(group_by_context(s))

        self.wfile.write(json.dumps(result))


port = int(sys.argv[1]) if len(sys.argv) >= 2 else 8080
server = HTTPServer(("0.0.0.0", port), HttpProcessor)
server.serve_forever()

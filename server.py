from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import sys


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Blank server handler!")


port = int(sys.argv[1]) if len(sys.argv) >= 2 else 8080
server = HTTPServer(("0.0.0.0", port), HttpProcessor)
server.serve_forever()

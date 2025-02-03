import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/hello":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"hello world!")
        elif self.path == "/die":
            print("Application crashing!", flush=True)
            os._exit(1)
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"try /hello")


host = "0.0.0.0"
port = 1234

server = HTTPServer((host, port), SimpleHandler)
print(f"Server running on http://{host}:{port}")
server.serve_forever()

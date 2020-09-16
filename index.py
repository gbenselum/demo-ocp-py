import http.server
import socketserver
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello world')
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        self.wfile.write(local_ip)


httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()

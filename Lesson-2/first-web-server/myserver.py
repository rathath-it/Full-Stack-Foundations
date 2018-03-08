import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content/Type', 'application/json')
        self.end_headers()
        self.wfile.write('{"message": "Welcome"}')
        return




def main():
    host = os.environ.get('HOST', '0.0.0.0')
    port = os.environ.get('PORT', 19999)
    server = HTTPServer((host, port),MyHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()

# python 2.7
import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from string import Template


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content/Type', 'application/json')
        self.end_headers()
        self.wfile.write(Template('{"message": "$path"}').safe_substitute({'path': self.path[1:]}))
        return




def main():
    host = os.environ.get('HOST', '0.0.0.0')
    port = os.environ.get('PORT', 19999)
    server = HTTPServer((host, port), MyHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()

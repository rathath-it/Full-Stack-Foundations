import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    pass




def main():
    host = environ.get('HOST', '0.0.0.0')
    port = environ.get('PORT', 19900)
    server = HTTPServer((host, port),MyHandler)

if __name__ == '__main__':
    main()

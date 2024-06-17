from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
import json


class PingPongAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        request_path = parsed_path.path.strip('/')

        switch_request = {
            "ping": "pong",
            "pings": "pongs"
        }

        if request_path in switch_request:
            return_value = switch_request[request_path]
        else:
            return_value = f'pingpong {request_path}'

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = {"response": return_value}
        self.wfile.write(json.dumps(response).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=PingPongAPI):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print(f'Serving API on port 8000')
    httpd.serve_forever()


if __name__ == '__main__':
    run()

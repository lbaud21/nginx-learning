from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Backend Python 1\n")


HTTPServer(("", PORT), Handler).serve_forever()

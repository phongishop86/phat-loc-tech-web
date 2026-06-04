import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# ThreadingHTTPServer is available in Python 3.7+ and handles concurrent requests.
with http.server.ThreadingHTTPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()

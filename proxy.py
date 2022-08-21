import socketserver
import http.server
import urllib
import re

port = 9007

class Proxy(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # get url
        url = self.path
        regex = "*"
        # send request to url if url match regex
        if re.match(regex, url):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("<html><body><h1>Hello!</h1></body></html>", "utf8"))
            return

httpd = socketserver.TCPServer(("", port), Proxy)
print("serving at port", port)
# serve httpd
httpd.serve_forever()
httpd.server_close()
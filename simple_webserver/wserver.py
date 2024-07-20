from http.server import HTTPServer, SimpleHTTPRequestHandler

port = 3000  # You can change the port number here

httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
print(f"Serving at port {port}")
httpd.serve_forever()

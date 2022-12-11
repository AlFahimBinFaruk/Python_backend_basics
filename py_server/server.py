from http.server import HTTPServer,BaseHTTPRequestHandler


HOST = "192.168.0.109"
PORT = 8000

class ServerClass(BaseHTTPRequestHandler):
    # make a get request
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h4>Hi Python server</h4></body></html>","utf-8"))

    # make post req
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-tpye","application/joson")
        self.end_headers()

        self.wfile.write(bytes('{"msg":"Post not implemented!"}','utf-8'))    

    # make put req
    def do_PUT(self):
        self.send_response(200)
        self.send_header("Content-type","application/json")
        self.end_headers()

        self.wfile.write(bytes('{"msg":"PUT not implemented yet"}','utf-8')) 

    # make delete req
    def do_DELETE(self):
        self.send_response(200)
        self.send_header("Content-tpye","application/joson")
        self.end_headers()

        self.wfile.write(bytes('{"msg":"Delete not implemented!"}','utf-8'))         

server = HTTPServer((HOST,PORT),ServerClass)
print("server is running.")

server.serve_forever()
server.server_close()
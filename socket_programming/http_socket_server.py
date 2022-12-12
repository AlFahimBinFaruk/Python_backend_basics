import socket

HEADER = 1024

serverSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('localhost',8080))
serverSocket.listen()


while True:
    print('Server waiting for connections')
    (conn, address) = serverSocket.accept()

    print('HTTP server request received:')
    conn.recv(HEADER)
    conn.send(bytes("HTTP/1.1 200 OK\r\n\r\n<html><body><h6>Hello World From HTTP Server</h6></body></html>\r\n",'utf-8'))
    
    conn.close()
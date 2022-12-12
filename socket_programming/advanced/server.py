""""
This is based on many client to one server connection.
where clients can only communicate with the server not among themselves.
"""

import socket
# threading is a way of creating multiple threads withing one python program.
import threading

PORT = 8000

# if you want any device to access this
# SERVER = "YOUR PUBLIC IP ADDRESS"

# any device in this network can connect the server.
# SERVER = "192.168.0.110"
SERVER = socket.gethostbyname(socket.gethostname())

# port and server is our address so we have to bind it in a tuple
ADDR = (SERVER,PORT)

# encoding decoding format of msg
FORMAT = "utf-8"

# defining the size of header size.64 means every msg have to be 64 bits.
HEADER = 64

# when we get this msg we will close the client thread.
DISCONNECT_MSG = "!Disconnect"

# Creating the socket
# AF_INET = ipv4
# SOCK_STEAM = we are steaming data.
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Binding the socket to the server
server.bind(ADDR)


# Handle every client req
def handle_client(conn,addr):
    print(f"New connection {addr} connected")

    connected = True
    while connected:
        # this will wait untill a masg occurs
        msg_length = conn.recv(HEADER).decode(FORMAT)
        
        # we have to make sure that the msg that we are receiving is of valid length then we will do the rest
        if msg_length:
            # we will convert msg_length to int to see how many bites we are receiving as actual msg
            msg_length = int(msg_length)
            
            # now we will use that bites/length to know the actual msg
            msg = conn.recv(msg_length).decode(FORMAT)

            # abandon thread if msg match disconnect msg
            if msg == DISCONNECT_MSG:
                connected = False

            print(f"[{addr}] - [{msg}]")
            conn.send("Msg received".encode(FORMAT))

    # close the conn if it exits the loop    
    conn.close()  
    print(f"[Disconnected - {addr}]")  



# function to start the main server
def start():
    # start listen
    server.listen()
    print(f"Server is running on {SERVER}...")
    
    # we will continue to listen/running untill it stop or untill it crashes.
    while True:
        print("Waiting to connect.")
        # this line will wait untill a new conn occurs
        conn,addr = server.accept()
        # when a client req come handle it by creating a thread
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()

        print(f"[Active Thread] - {threading.active_count() - 1}")

# starting/listening the server
start()

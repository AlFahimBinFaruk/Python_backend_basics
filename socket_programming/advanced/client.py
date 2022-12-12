import socket

# defining the size of header size.64 means every msg have to be 64 bits.
HEADER = 64

# encoding decoding format of msg
FORMAT = "utf-8"

# which port of server we want to connect
PORT = 8000

# ip address of the server we want to connect
SERVER = "192.168.0.110"

# port and server is our address so we have to bind it in a tuple
ADDR = (SERVER,PORT)

# msg to close client thread.
DISCONNECT_MSG = "!Disconnect"

# Creating the socket
# AF_INET = ipv4
# SOCK_STEAM = we are steaming data.
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect to server
client.connect(ADDR)
print(f"client connected to server to disconnect enter {DISCONNECT_MSG}")

# function to send msg
def sendMsg(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    # make sure length match the header size(64 bits)
    send_len += b' ' * (HEADER - len(send_len))
    
    # at first we will send length of msg 
    client.send(send_len)
    # then we will send the actual msg
    client.send(message)
    # print the response that comes from server
    print(client.recv(HEADER).decode(FORMAT))
    
    if msg != DISCONNECT_MSG:
        # lisnen for another msg
        sendMsg(input())


print("Enter msgs:") 
sendMsg(input()) 

 

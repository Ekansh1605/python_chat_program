########### ports are used to identify application ## ip address are use to identify devices#######
import socket
chunk=65535## receive at most these size of data at once
port=3000
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)## create a socket a object
#socket.socket(family,type)
#AF_NET: family of ipv4 ip address
#SOCK_DGRAM: UDP,SOCK_STREAM:TCP

# some ip adress that the server will listen to when msg comes
hostname='127.0.0.1'#ip address of a local machine,same for everyone
#aka home,there is no place like 127.0.0.1

s.bind((hostname,port))# bind the socket with the host machine and on port 3000
print(f"server is live on {s.getsockname()}")

#run this server infinite times till i stop it manually
while True: #infinite loop
    data,client=s.recvfrom(chunk)
    message=data.decode('ascii')# data by default travels in bytes
    print(f"Rachit: {message}")
    message_send=input("Reply: ")
    data=message_send.encode('ascii')
    # send data to the ip add that send me the data
    s.sendto(data,client) # sending this data to client having client(that is address)
## ctrl+c se program terminate kar skte hai###
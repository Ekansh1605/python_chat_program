import socket
port=3000
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
chunk=65535
#instead of explicitly binding the object, i will let os do it.
# ephemeral ports: it is assign by the os
# OS will bind this for us
hostname='127.0.0.1'
while True:
    s.connect((hostname,port))
    message=input("Type message: ")
    data=message.encode('ascii')
    s.send(data)
    #data received
    data=s.recv(chunk)
    text=data.decode('ascii')
    print(f"Kunal: {text}")
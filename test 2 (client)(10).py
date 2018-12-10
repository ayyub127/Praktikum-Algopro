import socket
hostname ='localhost'
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((hostname,8089))
data=''
print 'ready'
while data.lower!= 'quit':
    data=raw_input('command : ')
    server.send(data)
    if data.lower() =='quit':
        print 'response : siap!!'
        break
    elif data.lower() !='quit':
        response= server.recv(1024)
        print 'response : ', response
server.close()

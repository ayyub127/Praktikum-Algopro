import socket
hostname ='localhost'
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((hostname,8087))
data=''
print 'ready'
while data.lower!= 'keluar':
    data=raw_input('Perintah : ')
    server.send(data)
    if data.lower() =='keluar':
        print 'Jawaban : siap!!'
        break
    elif data.lower() !='keluar':
        response= server.recv(1024)
        print 'Jawaban : ', response
server.close()

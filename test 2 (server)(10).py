import socket
import platform
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('',8089))
server.listen(5)
data=''
machine=platform.machine()
system=platform.system()
release=platform.release()
version=platform.version()
node=platform.node()
data1={'machine':machine,'system':system,'release':release,'vesion':version,'node':node}
while data.lower() != 'quit':
    komm, addr = server.accept()
    while data.lower() !='quit' :
        data = komm.recv(1024)
        if data.lower()=='quit':
            server.close()
            break
        print 'perintah : ', data
        if data1.has_key(data):
            komm.send(data1[data])
        else:
            komm.send('unknown command')

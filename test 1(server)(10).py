import socket
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('',8087))
server.listen(5)
data=''
data1={'nama':'Muhammad Ayyub Nasrullah','NIM':'L200183127','angkatan':'2018'}
while data.lower() != 'keluar':
    komm, addr = server.accept()
    while data.lower() !='keluar' :
        data = komm.recv(1024)
        if data.lower()=='keluar':
            x='Siap!!'
            komm.send(x)
            print 'siap!!'
            server.close()
            break
        print 'perintah : ', data
        if data1.has_key(data):
            komm.send(data1[data])
        else:
            komm.send('Maaf, perintah tidak dimengerti')

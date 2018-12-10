import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50005))
s.listen(5)
print"Server sudah siap"
perintah = "
r=0
t=0
while perintah !='keluar':
    komm, addr = s.accept()
    while perintah !='keluar':
        data = komm.recv(1024).lower().split("=")
        perintah = data[0]
        if perintah == 'keluar':
            s.close()
            break
        print 'Pesan:', perintah
        if len(data) == 2:
            if perintah == 'jari-jari':
                r = int(data[1])
                respon = "jari-jari dicatat"
                komm.send(respon)
            elif perintah == 'tinggi':
                t = int(data[1])
                respon = "tinggi dicatat"
                komm.send(respon)
            else:
                komm.send('pesan tidak diketahui')
        elif perintah == 'hitung':
            L = float(22/7*r*r*t)
            respon = "Luas tabung dengan jari-jari {} dan tinggi {} adalah {}".format(r,t,L)
            komm.send(respon)
        else:
            komm.send('pesan tidak diketahui')

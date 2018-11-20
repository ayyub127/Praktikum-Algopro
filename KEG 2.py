##Program Akun
##Dibuat oleh Fawwaz L200183143
import random
angka = random.randint(0,1000)

Nama = 'Fawwaz Haidar Abyansyah Kusuma'
TanggalLahir = '12 Juni 2000'
NamaSingkat = Nama[0] + '.' + Nama[8] + Nama[15:25]
Username = Nama[10] + TanggalLahir[0] + TanggalLahir[11:15]
Password = Nama[10:15] + str(angka)

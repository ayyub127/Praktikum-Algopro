##Program Akun
##Dibuat oleh Ayyub L200183127
import random
angka = random.randint(0,1000)

Nama = 'Muhammad Ayyub Nasrullah'
TanggalLahir = '4 Agustus 1999'
NamaSingkat = Nama[10] + '.' + Nama[11] + Nama[16:19]
Username = Nama[10] + TanggalLahir[0] + TanggalLahir[11:15]
Password = Nama[10:15] + str(angka)

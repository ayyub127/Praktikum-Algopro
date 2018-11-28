Data = {"NIM":"L200183127", "Nama":"Muhammad Ayyub Nasrullah", "Tempat/Tanggal_Lahir":"Dubai / 4 Agustus 1999", "Jenis_Kelamin":"Laki - laki", "Alamat":"DSN. Jomblang,Takeran,Magetan", "Agama":"Islam", "Pekerjaan":"Mahasiswa", "Kewarganegaraan":"Karifan Lokal"}
NIM = Data["NIM"]
Nama = Data["Nama"]
TTL = Data["Tempat/Tanggal_Lahir"]
JK = Data["Jenis_Kelamin"]
GD = Data["Golongan_Darah"]
Alamat = Data["Alamat"]
Agama = Data["Agama"]
Pekerjaan = Data["Pekerjaan"]
Kewarganegaraan = Data["Kewarganegaraan"]

print("Pilihan Yang Tersedia:")
print("j menampilkan bantuan ini")
print("i menampilkan NIM")
print("k menampilkan Nama")
print("c menampilkan Tempat/Tanggal Lahir")
print("v menampilkan Jenis Kelamin")
print("n menampilkan Alamat")
print("m menampilkan Agama")
print("s menampilkan Pekerjaan")
print("d menampilkan Kewarganegaraan")
print("g untuk keluar")
print(" ")

j ='''Pilihan Yang Tersedia:
j menampilkan bantuan ini
i menampilkan NIM
k menampilkan Nama
c menampilkan Tempat/Tanggal Lahir
v menampilkan Jenis Kelamin
n menampilkan Alamat
m menampilkan Agama
s menampilkan Pekerjaan
d menampilkan Kewarganegaraan
g untuk keluar'''

g = "Terima Kasih"
w = input("Masukkan huruf: ")
while w != "g":
    if w == "j":
        print(j)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "i":
        print(NIM)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "k":
        print(Nama)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "c":
        print(TTL)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "v":
        print(JK)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "n":
        print(Alamat)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "m":
        print(Agama)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "s":
        print(Pekerjaan)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "d":
        print(Kewarganegaraan)
        print(" ")
        w = input("Masukkan huruf: ")
    else:
        print("perintah tidak dikenal")
        print(" ")
        w = input("Masukkan huruf: ")
print(g)

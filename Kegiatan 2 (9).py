latihan = open("L200183127", "w")
latihan.write("L200184092 \n")
latihan.write("11/07/1999 \n")
latihan.write("Muhammad Ayyub Nasrullah \n")
latihan.write("Dubai")
latihan.close()

import shelve
data = open("L200183127", "r")
NIM = data.readline()
TL = data.readline()
Nama = data.readline()
Kota = data.readline()
data.close

data = shelve.open("Ayyub")
data["databaru"] = [Nama, Kota, TL, NIM]
data.close()

data = shelve.open("Ayyub")
print(data["databaru"][0])
print(data["databaru"][1])
print(data["databaru"][2])
print(data["databaru"][3])

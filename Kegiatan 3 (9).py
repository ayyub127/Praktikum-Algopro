import shelve

data = open("L200183127", "r")
NIM = data.readline()
TL = data.readline()
Nama = data.readline()
Kota = data.readline()
data.close()

data = shelve.open("Ayyub")
data["databaru"] = [NIM, TL, Nama, Kota]
data.close()

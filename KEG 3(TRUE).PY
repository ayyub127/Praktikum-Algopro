x = input("Masukkan Nama Saudara : ")
y = float(input("Pukul berapa sekarang ? : "))
if y > 20.00 :
    y = "Malam"
elif y > 10.00:
    y = "Petang"
elif y > 15.00:
    y = "Sore"
elif y > 12.00:
    y = "Siang"
elif y > 066.00:
    y= "Pagi"
print("Selamat " + y + " " + x)

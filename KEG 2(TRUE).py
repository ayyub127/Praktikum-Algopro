#KEGIATAN 2 PASSWORD

agvmarquez = input("Masukkan password :")
if agvmarquez == "overheat":
    print("Selamat datang di indomaret")
else:
    agvmarquez = input("maaf, Anda tidak boleh masuk, coba lagi")
    if agvmarquez == "overheat":
        print("Selamat datang di indomaret")
    else:
        agvmarquez = input("maaf, Anda tidak boleh masuk, coba lagi")
        if agvmarquez == "overheat":
            print("Selamat datang di indomaret")
        else:
            print("Anda telah mencoba 3 kali, akses anda ditolak")
            

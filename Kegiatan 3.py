from Tkinter import Tk, Label, Entry, Button, StringVar
from tkMessageBox import showinfo

my_app = Tk(className = 'Luas Tabung')

L1 = Label(my_app, text = 'Tinggi')
L1.grid(row=0, column=0)
str1 = StringVar( value = 0 )
E1 = Entry(my_app)
E1.grid(row=0 , column=1)

L2 = Label(my_app, text = "Jari-Jari")
L2.grid(row=1, column=0)
str2 = StringVar(value = 1 )
E2 = Entry(my_app)
E2.grid(row=1 , column=1)

L3 = Label(my_app, text = 'Hasil')
L3.grid(row=2 , column=0)

def luas():
    T = float(str1.get())
    R = float(str2.get())
    K = 3,14*R**2
    G = 2*3,14*R*T
    M = 3.14*R**2
    L = (K + G + M)

B1 = Button (my_app, text = 'Hitung Luas' , command = luas)
B1.grid(row=3 , column = 0)

    
str3 = StringVar(value=luas)
E3 = Entry(str3)
E3.grid(row=4, column=0)

my_app.mainloop()

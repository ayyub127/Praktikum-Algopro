Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Fawwaz Haidar Abyansyah Kusuma'
>>> NIM = 1143
>>> Tinggi = 1.76
>>> Berat = 66
>>> TahunLahir = 2000
>>> Saya = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(saya)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type(saya)
NameError: name 'saya' is not defined
>>> type(Saya)
<class 'tuple'>
>>> # Because 'Saya' is written in parentheses
>>> Saya[0]
2000
>>> # Because the first object in 'Saya' data is TahunLahir, value is 2000
>>> a = NIM % 4; Saya[a]
1143
>>> # Because remaining result of 1143 divided by 4 is 0, result Saya[0] is 1143
>>> type(Saya[a])
<class 'int'>
>>> # Because value of 'TahunLahir' is 0, 0 is an integer data type
>>> Saya[a:4]
(1143,)
>>> # Because first 4 object in the data is 'NIM'
>>> type(Saya[4])
<class 'str'>
>>> # Because the fifth data in Saya is 'Nama'
>>> Saya[0] = 'up'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    Saya[0] = 'up'
TypeError: 'tuple' object does not support item assignment
>>> # Because tuple element is cannot be changed
>>> type(Data)
<class 'list'>
>>> # Because the 'Data' is written in square brackets
>>> type(Data[4])
<class 'str'>
>>> # Because the fifth object in 'Data' is 'Nama'
>>> Data[4][5]
'z'
>>> # Because there is 'z' in sixth 'Nama' data
>>> Data[0] = 'up'; Data
['up', 66, 1.76, 1143, 'Fawwaz Haidar Abyansyah Kusuma']
>>> # Because the first object already changed with 'up'
>>> Data[-a]
1.76
>>> # Because third data in 'Data' is 1.76
>>> range(a)
range(0, 3)
>>> # Because in the 'a' data there is only 1 object

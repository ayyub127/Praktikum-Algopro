Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Muhammad Ayyub Nasrullah'
>>> NIM = 1127
>>> Tinggi = 1.65
>>> Berat = 51
>>> TahunLahir = 1999
>>> Saya = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Saya)
<class 'tuple'>
>>> #because 'Saya' is written in parentheses
>>> Saya[0]
1999
>>> #because the first object in 'Saya' data is TahunLahir, value is 1999
>>> a = NIM % 4; Saya[a]
1127
>>> #because remaining result of 1127 divided by 4 is 0, result Saya[0] is 1127
>>> type(Saya[a])
<class 'int'>
>>> #because value of 'TahunLahir' is 0, 0 is an integer data type
>>> Saya[a:4]
(1127,)
>>> #because first 4 object in the data is 'NIM'
>>> type(Saya[4])
<class 'str'>
>>> #because the fifth data in Saya is 'Nama'
>>> Saya[0] = 'jos'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Saya[0] = 'jos'
TypeError: 'tuple' object does not support item assignment
>>> #because tuple element is cannot be changed
>>> type(Data)
<class 'list'>
>>> #because 'Data' is written in square brackets
>>> type(Data[4])
<class 'str'>
>>> #because the fifth object in 'Data' is 'Nama'
>>> Data[4][5]
'm'
>>> #because there is 'm' in sixth 'Nama' data
>>> Data[0] = 'jos'; Data
['jos', 51, 1.65, 1127, 'Muhammad Ayyub Nasrullah']
>>> #because the first object already changed with 'jos'
>>> Data[-a]
1.65
>>> #because third data in 'Data' is 1.65
>>> range(a)
range(0, 3)
>>> #because in the 'a' data there is only 1 object

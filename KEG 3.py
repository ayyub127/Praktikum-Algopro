Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> Nama = "Fawwaz  Haidar Abyansyah Kusuma"
>>> NIM = "L200183143"
>>> X = "1" + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # Because the "X" data had changed to integerdata type
>>> type(b)
<class 'int'>
>>> # Because the "Nama" data has a "len" instruction
>>> a / b
36.87096774193548
>>> # Because the result of 1143 divided by 23 is 36.87096774193548
>>> a // b
36
>>> # Because the meaning of "//" is division with rounding down
>>> 10 * (a-999)
1440
>>> # Because the value of "a" minus 999 is 144
>>> # Because the value of "a" minus 999 is 144,after that it will multiplied by 10 and the result is 1440
>>> b ** 2
961
>>> # Because the meaning of "**" is square
>>> a % b
27
>>> # Because the meaning of "%" is remaining of the result
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> # Because "12.5" is a decimal number
>>> a / c
91.44
>>> # Because the result of 1143 divided by 12.5 is 91.44
>>> a /
SyntaxError: invalid syntax
>>> # Because the result of 1143 divided by 12.5 is 91.44
>>> a // c
91.0
>>> # Because the meaning of "//" is division with rounding down and the operand typeis writed in decimal number
>>> a % c
5.5
>>> # Because the meaning of "%" is remainingof the result
>>> c > b
False
>>> # Because the "b" data has a bigger value than the "c" data
>>> type(c > b)
<class 'bool'>
>>> # Because "True" or "False" is a boolean data type
>>> a > b and b > c
True
>>> # Because in "and" operator symbol, if "True" meet with "True", The result is "True"
>>> a > 1100 or b < 10
True
>>> # Because is "or" operator symbol, if "False" meet with "False", The result is "False"

Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Muhammad Ayyub Nasrullah'
>>> NIM = 'L200183127'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> #because 'X' data changed to integer data type
>>> type(b)
<class 'int'>
>>> #because 'Nama' data has a 'len' intrucsion
>>> a / b
46.958333333333336
>>> because result 1127 divided by 24 is 46.958333333333336
SyntaxError: invalid syntax
>>> #because result 1127 divided by 24 is 46.958333333333336
>>> a // b
46
>>> #because the meaning of '//' is division with rounding down
>>> 10 * (a - 999)
1280
>>> #because value 'a' minus 999 is 128, after multiplied by 10
>>> b ** 2
576
>>> #because meaning of '**' is square
>>> a % b
23
>>> #because '%' remaining the result
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> #because '12.5' is decimal number
>>> a / c
90.16
>>> #because result of 1127 divided by 12.5
>>> a // c
90.0
>>> #because the meaning '//' division with rounding down and operand types is writed decimal number
>>> a % c
2.0
>>> #because meaning of '%' remaining the result
>>> c > b
False
>>> #because 'b' is bigger than 'c' data
>>> type(c > b)
<class 'bool'>
>>> #because 'true' or 'false' is boolean data type
>>> a > b and b > c
True
>>> #because in 'and' operator symbol, if 'true' meet 'true', result 'true'
>>> a > 1100 or b < 10
True
>>> #because in 'or' operator symbol, if 'true' meet 'true, result 'true'

Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f=open('test.txt', 'r')
>>> body = f.read()
>>> f.close
<built-in method close of _io.TextIOWrapper object at 0x0000022F42FF2420>
>>> f.close()
>>> body = body.replace('java', 'python')
>>> f = open('test.txt', 'w')
>>> f.write(body)
18
>>> f.close()
>>> f=open('test.txt', 'r')
>>> body = f.read()
>>> f.close()
>>> body = body.replace('java', 'python')
>>> f = open('test.txt', 'w')
>>> f.write(body)
33
>>> f.close()
>>> # 경로가 특별히 지정하지 않으면 idle 경로에 있음.
>>> 
>>> #Q8 입력값을 모두 더해 출력하기.
>>> 
>>> C:\> cd doit
SyntaxError: unexpected character after line continuation character
>>> import sys
>>> numbers = sys.argv[1:]
>>> 
>>> result = 0
>>> for number in numbers:
...     result += int(number)
... 
>>> print(result)
0

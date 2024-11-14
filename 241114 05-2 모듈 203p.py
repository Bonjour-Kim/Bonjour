Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #241114 05-2 모듈 203p
>>> from mod1 import add
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    from mod1 import add
ModuleNotFoundError: No module named 'mod1'
>>> import sys
... sys.path.append(r'C:\doit')
... from mod1 import add
SyntaxError: multiple statements found while compiling a single statement
>>> import sys
>>> sys.path.append(r'C:\doit')
>>> from mod1 import add
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    from mod1 import add
  File "C:\doit\mod1.py", line 1
    >>> def add(a, b):
    ^^
SyntaxError: invalid syntax
>>> from mod11 import add
>>> add(3, 4)
7
>>> from mod11 import add, sub
>>> from mod11 import *
>>> import mod11
>>> mod1.__name__
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    mod1.__name__
NameError: name 'mod1' is not defined. Did you mean: 'mod11'?
>>> mod.__main__
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    mod.__main__
NameError: name 'mod' is not defined
>>> mod11.__name__
'mod11'
>>> import mod2
>>> print(mod2.PI)
3.141592
>>> a = mod2.Math()
>>> print(a.solv(2))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(a.solv(2))
  File "C:\doit\mod2.py", line 6, in solv
    return PI * (R**2)
NameError: name 'R' is not defined. Did you mean: 'r'?
>>> print(a.solv(2))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(a.solv(2))
  File "C:\doit\mod2.py", line 6, in solv
    return PI * (r**2)
NameError: name 'R' is not defined. Did you mean: 'r'?
import mod2
print(a.solv(2))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(a.solv(2))
  File "C:\doit\mod2.py", line 6, in solv
    return PI * (r**2)
NameError: name 'R' is not defined. Did you mean: 'r'?
a = mod2.Math()
print(a.solv(2))
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(a.solv(2))
  File "C:\doit\mod2.py", line 6, in solv
    return PI * (r**2)
NameError: name 'R' is not defined. Did you mean: 'r'?
import mod2
a = mod2.Math()
print(a.solv(2))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(a.solv(2))
  File "C:\doit\mod2.py", line 6, in solv
    return PI * (r**2)
NameError: name 'R' is not defined. Did you mean: 'r'?
print(a.solv(2))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(a.solv(2))
  File "C:\doit\mod2.py", line 6, in solv
    return PI * (r**2)
NameError: name 'R' is not defined. Did you mean: 'r'?
import mod2
print(mod2.add(3, 4))
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(mod2.add(3, 4))
AttributeError: module 'mod2' has no attribute 'add'
C:\doit>python
SyntaxError: unexpected character after line continuation character
r'C:\doit>python'
'C:\\doit>python'
import sys
sys.path
['', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\idlelib', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312\\DLLs', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312\\Lib', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages', 'C:\\doit']
sys.path.append("C:/doit/mymod")
sys.path
['', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\idlelib', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312\\DLLs', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312\\Lib', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages', 'C:\\doit', 'C:/doit/mymod']
import mod2
print(mod2.add(3, 4))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(mod2.add(3, 4))
AttributeError: module 'mod2' has no attribute 'add'
import mod2
print(mod2.add(3, 4))

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(mod2.add(3, 4))
AttributeError: module 'mod2' has no attribute 'add'
sys.path.append("C:/doit/mymod")

sys.path.append("C:/doit/mymod")
sys.path
['', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\idlelib', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312\\DLLs', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312\\Lib', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312', 'C:\\Users\\Bongju Kim\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages', 'C:\\doit', 'C:/doit/mymod', 'C:/doit/mymod', 'C:/doit/mymod']
import mod2
print(mod2.add(3, 4))
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(mod2.add(3, 4))
AttributeError: module 'mod2' has no attribute 'add'
import mod2.py
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    import mod2.py
ModuleNotFoundError: No module named 'mod2.py'; 'mod2' is not a package
import mod2
print(mod2.add(3, 4))
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(mod2.add(3, 4))
AttributeError: module 'mod2' has no attribute 'add'
import mod2
print(mod2.add(3,4))
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(mod2.add(3,4))
AttributeError: module 'mod2' has no attribute 'add'
print(mod2.add(3, 4))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print(mod2.add(3, 4))
AttributeError: module 'mod2' has no attribute 'add'
r'C:\doit>set PYTHONPATH=C:\doit\mymod'
'C:\\doit>set PYTHONPATH=C:\\doit\\mymod'
C:\doit>python
SyntaxError: unexpected character after line continuation character
r'C:\doit>python'
'C:\\doit>python'
import mod2
print(mod2.add(3, 4))
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print(mod2.add(3, 4))
AttributeError: module 'mod2' has no attribute 'add'
import mod2

print(mod2.add(3, 4))
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(mod2.add(3, 4))
AttributeError: module 'mod2' has no attribute 'add'

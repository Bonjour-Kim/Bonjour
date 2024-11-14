Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = FourCal()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a = FourCal()
NameError: name 'FourCal' is not defined
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

        
a = FourCal()
a.setdata(4, 2)
a.add()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.add()
AttributeError: 'FourCal' object has no attribute 'add'
class FourCal:
    def add(self):
    return self.first + self.second
SyntaxError: expected an indented block after function definition on line 2

class FourCal:
    def add(self):
    return self.first + self.second
SyntaxError: expected an indented block after function definition on line 2
class FourCal:
    def add(self):
        return self.first + self.second

    
a.add()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.add()
AttributeError: 'FourCal' object has no attribute 'add'
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    
a.add
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.add
AttributeError: 'FourCal' object has no attribute 'add'
a.setdata(4, 2)
a.add
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.add
AttributeError: 'FourCal' object has no attribute 'add'
a.add()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.add()
AttributeError: 'FourCal' object has no attribute 'add'
a.FourCal()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.FourCal()
AttributeError: 'FourCal' object has no attribute 'FourCal'
a = FourCal()
a.setdata(4, 2)
a.add()
6
class FourCal:
    def setdata(self, first, second):
    self.first = first
    
SyntaxError: expected an indented block after function definition on line 2
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(sefl):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result - self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

    
a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)
a.add()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.add()
  File "<pyshell#43>", line 6, in add
    result = self.first + self.second
NameError: name 'self' is not defined
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result - self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


a.add()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.add()
  File "<pyshell#43>", line 6, in add
    result = self.first + self.second
NameError: name 'self' is not defined
a = FourCal()
a.setdata(4, 2)
a.add
<bound method FourCal.add of <__main__.FourCal object at 0x0000026A66162600>>
a.add()
6
a.mul()
8
a.sub()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.sub()
  File "<pyshell#49>", line 12, in sub
    result - self.first - self.second
NameError: name 'result' is not defined
a.
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

    
a.sub()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.sub()
  File "<pyshell#49>", line 12, in sub
    result - self.first - self.second
NameError: name 'result' is not defined
a = FourCal()
a.setdata(4, 2)
a.sub()
2
a.div()
2.0
b = FourCal()
b.setdata(3, 8)
b.sub()
-5
def __init__(self, first, second):
    self.first = first
    self.second = second

    
a = FourCal()
Traceback (most recent call last):
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a = FourCal(4, 2)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a = FourCal(4, 2)
TypeError: FourCal() takes no arguments
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
SyntaxError: expected an indented block after function definition on line 5
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second

        
a = FourCal()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a = FourCal()
TypeError: FourCal.__init__() missing 2 required positional arguments: 'first' and 'second'
a = FourCal(4, 2)
a.first
4
a.second
2
a.div()
a= = FourCal(4, 2)
SyntaxError: invalid syntax
a = FourCal(4, 2)
a.div()
a.add()
6
a.div()
print(a.div())
None
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

    
a.div()
a = FourCal(4, 2)

a.div()
2.0
class MoreFourCal(FourCal):
    pass


a = MoreFourCal(4, 2)
>>> a.add()
6
>>> a.sub()
2
>>> a.div()
2.0
>>> class MoreFourCal(FourCal):
...     def pow(self):
...         result = self.first ** self.second
...         return result
... 
...     
>>> a = MoreFourCal(4, 2)
>>> a.pow()
16
>>> a.add()
6
>>> a = FourCal(4, 0)
>>> a.div()
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    a.div()
  File "<pyshell#94>", line 15, in div
    result = self.first / self.second
ZeroDivisionError: division by zero
>>> class SafeFourCal(FourCal):
...     def div(self):
...         if self.second == 0:
...             return 0
...         else:
...             return self.first / self.second
... 
>>> a = SafeFourCal(4, 0)
>>> a.div()
0
>>> class Family:
...     lastname =
...     
SyntaxError: invalid syntax
>>> 
>>> class Family:
...     lastname = "김"
... 
...     
>>> Family.lastname
'김'
>>> a = Family()
>>> a.lastname
'김'
>>> b = Family()
>>> b.lastname()
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    b.lastname()
TypeError: 'str' object is not callable
>>> b.lastname
'김'

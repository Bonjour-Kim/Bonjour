Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
"입력값과 리턴값"
'입력값과 리턴값'
def add(a, b):
    result = a + b
    return result

a= add(3, 4)
print(a)
7

def say():
    return 'Hi
SyntaxError: unterminated string literal (detected at line 2)
def say():
    return 'Hi'

print(say())
Hi

def add_many(*args):
    result = 0
    for i in args:
        result = result + i # *args에 입력받은 모든 값을 더한다.
    return result

# *args처럼 매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아 튜플로 만들어 주기 때문
result = add_many(1,2,3)
print(result)
6
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)
55

result = add_mul('add', 1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    result = add_mul('add', 1,2,3,4,5)
NameError: name 'add_mul' is not defined. Did you mean: 'add_many'?
def add/mul(choice, *args):
    
SyntaxError: expected '('
def add-mul(choice, *args):
    
SyntaxError: expected '('
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul"
    
SyntaxError: expected ':'
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
        return result

    
result = add_mul('add', 1,2,3,4,5)
print(result)
None
result = add_mul('mul', 1,2,3,4,5)
print(result)
120
result = add_mul('add', 1,2,3,4,5)
print(result)
None
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
...     elif choice == "mul":
...         result = 1
...         for i in args:
...             result = result * i
...     return result
... 
>>> result = add_mul('mul', 1,2,3,4,5)
... print(result)
SyntaxError: multiple statements found while compiling a single statement
>>> result = add_mul('mul', 1,2,3,4,5)
>>> print(result)
... 
120
>>> result = add_mul('add', 1,2,3,4,5)
>>> print(result)
15
>>> 
>>> 
>>> 
>>> def print_kwargs(**kwargs):
...     print(kwargs)
... 
...     
>>> print_kwargs(a=1)
{'a': 1}
>>> print_kwargs(name='foo', age=3)
{'name': 'foo', 'age': 3}
>>> #kwargs 는 ‘keyword arguments’ 의 약자이며 args 와 마찬가지로 관례적으로 사용한다.
>>> 
>>> 
>>> def add_and_mul(a,b):
...     return a+b, a*b
... 
>>> result = add_and_mul(3,4)
>>> print(result)
(7, 12)
>>> # 함수는 return 문을 만나는 순간, 리턴값을 돌려 준 다음 함수를 빠져나가게 된다.
>>> 
>>> 
>>> def say_nick(nick):
...     if nick == " 바 보 ":
...         return ... print(" 나 의 별 명 은 %s 입 니 다 ." % nick)
...     
SyntaxError: invalid syntax
>>> def say_nick(nick):
...     if nick == " 바 보 ":
...         return
...     print(" 나 의 별 명 은 %s 입 니 다 ." % nick)
... 
...     
>>> say_nick("야호")
 나 의 별 명 은 야호 입 니 다 .
>>> say_nick("바보")
 나 의 별 명 은 바보 입 니 다 .
>>> say_nick(" 바 보 ")
... 
>>> 

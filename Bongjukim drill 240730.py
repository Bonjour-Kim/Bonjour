Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
"hello"
'hello'
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a.keys()
dict_keys(['name', 'phone', 'birth'])
>>> for k in a.keys()
SyntaxError: expected ':'
>>> for k in a.keys():
...     print(k)
... 
...     
name
phone
birth
>>> 
>>> s1=set([1,2,3])
>>> s1
{1, 2, 3}
>>> s2=set("Hello")
>>> s2
{'e', 'l', 'H', 'o'}
>>> l1=list(s1)
>>> l1
[1, 2, 3]
>>> l1[0]
1
>>> t1=ti[;e)s1_
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> t1=tuple(s1)
>>> t1
(1, 2, 3)
>>> t1[0]
1
>>> s1 = set([1, 2, 3, 4, 5, 6])
>>> s2 = set([4, 5, 6, 7, 8, 9])
>>> s1&s2
{4, 5, 6}
>>> s1.intersection(s2)
{4, 5, 6}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> s1|s2
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> s1-s2
{1, 2, 3}
>>> s1.difference(s2)
{1, 2, 3}
>>> s2.difference(s1)
{8, 9, 7}
>>> s1.add(4)
>>> s1
{1, 2, 3, 4, 5, 6}
>>> s1.update([4,5,6,7])
>>> s1
{1, 2, 3, 4, 5, 6, 7}
>>> s1.remove(3)
>>> s1
{1, 2, 4, 5, 6, 7}
>>> 
>>> "Bool 불 자료형 "
'Bool 불 자료형 '

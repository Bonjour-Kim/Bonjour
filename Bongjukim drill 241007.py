Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
test list=['one', 'two', 'three']
SyntaxError: invalid syntax
test_list=['one', 'two', 'three']
for i in test_list:
    print(i)

    
one
two
three
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first+last)

    
3
7
11
marks = [90, 25, 67, 45, 80]
for marks:
    
SyntaxError: invalid syntax
number=0
for mark in marks:
    if mark>=60:
        print("Pass for %d student" %number)
    else:
        print("Fail for %d student" %number)

        
Pass for 0 student
Fail for 0 student
Pass for 0 student
Fail for 0 student
Pass for 0 student
for mark in marks:
    number=number+1
    if mark>=60:
         print("Pass for %d student" %number)
    else:
         print("Fail for %d student" %number)

         
Pass for 1 student
Fail for 2 student
Pass for 3 student
Fail for 4 student
Pass for 5 student
a=range(10)
a
range(0, 10)
sum(1:100)
SyntaxError: invalid syntax
m=1
sum(m)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    sum(m)
TypeError: 'int' object is not iterable
while m<=100
SyntaxError: expected ':'
while m<=100:
    m=m+1
    sum(m)

    
Traceback (most recent call last):
  File "<pyshell#33>", line 3, in <module>
    sum(m)
TypeError: 'int' object is not iterable
total=sum(range(1,101))
print(total)
5050
zcc=0
add=0]
SyntaxError: unmatched ']'
add=0
for i in range(1,11)"
SyntaxError: unterminated string literal (detected at line 1)
add=add+i
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    add=add+i
TypeError: unsupported operand type(s) for +: 'int' and 'str'
for i in range(1,11):
    add=add+1

    
print(add)
10
for i in range(1,11):
    add=add+i

    
print(add)
65

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("Congraturation, No.%d. You're in." %(number+1))

    
Congraturation, No.1. You're in.
Congraturation, No.3. You're in.
Congraturation, No.5. You're in.
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end="")
        print('')

        
2
4
6
8
10
12
14
16
18
3
6
9
12
15
18
21
24
27
4
8
12
16
20
24
28
32
36
5
10
15
20
25
30
35
40
45
6
12
18
24
30
36
42
48
54
7
14
21
28
35
42
49
56
63
8
16
24
32
40
48
56
64
72
9
18
27
36
45
54
63
72
81
for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end="")
    print('')

    
24681012141618
369121518212427
4812162024283236
51015202530354045
61218243036424854
71421283542495663
81624324048566472
91827364554637281
for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('.')

2 4 6 8 10 12 14 16 18 .
3 6 9 12 15 18 21 24 27 .
4 8 12 16 20 24 28 32 36 .
5 10 15 20 25 30 35 40 45 .
6 12 18 24 30 36 42 48 54 .
7 14 21 28 35 42 49 56 63 .
8 16 24 32 40 48 56 64 72 .
9 18 27 36 45 54 63 72 81 .
a = [1,2,3,4]
result=]\
        
SyntaxError: unmatched ']'
result=[]
for num in a:
    result.append(num*3)

    
print(result)
[3, 6, 9, 12]
a = [1,2,3,4]
result=[num*3 for num in a if num%2==0]
print(result)
[6, 12]
result=[num+1 for num in a if num>0]
print(result)
[2, 3, 4, 5]
result=[x*y for x in range(2,10)
            for y in range(1,10)]
print(result)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]
for i in <1,100>
SyntaxError: invalid syntax
for i in <1,100>:
    
SyntaxError: invalid syntax
for i in <1,100>:
    
SyntaxError: invalid syntax
for i in range<1,101>:
    
SyntaxError: invalid syntax
for i in range(1,101):
    print(i)

    
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
>>> A=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
>>> total=0
>>> for score in A:
...     total +=score
... average=total/num in A
SyntaxError: invalid syntax
>>> for score in A:
...     total +=score
... average=total/len(A)
SyntaxError: invalid syntax
>>> print(average)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    print(average)
NameError: name 'average' is not defined
>>> for score in A:
...     total+=socre
... 
...     
Traceback (most recent call last):
  File "<pyshell#97>", line 2, in <module>
    total+=socre
NameError: name 'socre' is not defined. Did you mean: 'score'?
>>> for score in A:
...     total += score
... average=total/len(A)
SyntaxError: invalid syntax
>>> A=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
... total=0
... 
... for score in A:
...     total += score
... average=total/len(A)
SyntaxError: multiple statements found while compiling a single statement
>>> A=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
... total=0
SyntaxError: multiple statements found while compiling a single statement
>>> A=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
>>> total=0
>>> A=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
>>> total = 0
>>> 
>>> for score in A:
...     total += score
... 
...     
>>> average = total / len(A)
>>> print(average)
79.0
>>> numbers = [1, 2, 3, 4, 5]
>>> result = [n*2 for n in numbers if n%2==1]
>>> print(result)
[2, 6, 10]

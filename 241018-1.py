Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# sys1.py
import sys

args = sys.argv[1:]
for i in args:
    print(i)

    
#argv는 argument vector의 약자, 명렬줄 인자를 의미. sys는 파이썬 표준 라이브러리의 일부로, 파이썬 인터프리터와 관련된 기능을 제공하는 모듈
    
# sys2.py
import sys
args = sys.argv[1:]
for i in args:
    print(i, upper(), end=' ')

    
# 명령프롬프트 안됨.

def is_odd(number):
    if number%2 == 0
    
SyntaxError: expected ':'
def is_odd(number):
    if number%2 == 0:
        return True
    else:
        return False

    
def is_odd(10)
SyntaxError: invalid syntax
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

    
is_odd(3)
True
is_odd(4)
False


# 4장 Q2 모든 입력의 평균값 구하기
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

avg_numbers(1,2)
1.5
avg_numbers(1,2,3,4,5,6,7,8,9,10)
5.5

# Q3 프로그램 오류 수정하기 1: 2개의 숫자를 입력받아 더한 후에 리턴하는 프로그램
input1 = input("첫번째 숫자를 입력하세요:")
첫번째 숫자를 입력하세요:
input2 = input("Input the second number:")
Input the second number:

total = input1 + input2
print("The sum of two numbers are %s" %total)
The sum of two numbers are 
input1 = input("첫번째 숫자를 입력하세요:")
첫번째 숫자를 입력하세요:3
input2 = input("Input the second number:")
Input the second number:6
print(" 두 수 의 합 은 %s 입 니 다 " % total)
 두 수 의 합 은  입 니 다 
total = input1 + input2
print("The sum of two numbers are %s" % total)
The sum of two numbers are 36
# 36이 아니라 9가 되어야하므로 입력된 문자열을 숫자로 바꾸어야한다, int()함수 사용.
#  숫자나 문자열을 정수형 (Integer)으로 변환할 수 있습니다.

total = int(input1) + int(input2)

print("The sum of two numbers are %s," %total)
The sum of two numbers are 9,
# >>> print("you" "need" "python") youneedpython
>>> print("you"+"need"+"python") youneedpython
>>> print("you", "need", "python") # 콤 마 가 있 는 경 우 공 백 이 삽 입 되 어 더 해 진 다 .
you need python >>> print("".join(["you", "need", "python"])) youneedpython
SyntaxError: invalid syntax


f1 = open("test.txt", 'w')
f1.write("Life is tooo short")
18

f2 = open("test.txt", 'r')
print(f2.read())

# Q5 위 코드의 오류를 수정해서 Life is tooo short를 출력시켜보자.
f1.close()
print(f2.read())
Life is tooo short
>>> #파일을 닫지 않은 상태에서 다시 열면 파일에 저장한 데이터를 읽을 수 없다. 따라서 열린 파일 객체를 close 로 닫아준 후 다시 열어서 파일의 내용을 읽어야 한다.
>>> #파일을 닫지 않은 상태에서 다시 열면 파일에 저장한 데이터를 읽을 수 없다. 따라서 열린 파일 객체를 close 로 닫아준 후 다시 열어서 파일의 내용을 읽어야 한다.
>>> 
>>> # Q6 사용자 입력 저장하기
>>> #사용자의 입력을 파일 (test.txt) 에 저장하는 프로그램을 작성해 보자. 단, 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.
>>> user_input = input("Input the content you want")
Input the content you want:Good
>>> f = open('test.txt', 'a')
>>> f.write(user_input)
5
>>> f.write("\n")
1
>>> f.close
<built-in method close of _io.TextIOWrapper object at 0x000002C7C7BF2420>
>>> 
>>> 
>>> #Q7 파일의 문자열 바꾸기
>>> # java라는 문자열을 python으로 바꾸기.
>>> 
>>> #Life is too short
>>> #you need java
>>> 
>>> f = open('test.txt', 'r')
>>> body = f.read()
>>> f.close() # test.txt의 내용을 body에 저장하고 닫음
>>> 
>>> body = body.replace('java', 'python') #바디 문자열에서 자바를 파이썬으로 변경
>>> 
>>> f = open('test.txt', 'w')
>>> f.write(body)
18
>>> f.close
<built-in method close of _io.TextIOWrapper object at 0x000002C7C80D3D80>
>>> f = open('test.txt', 'w')
>>> f.write(body)
18
>>> f.close()
>>> f = open('test.txt', 'r')
>>> body = f.read()
>>> print(body)
Life is tooo short

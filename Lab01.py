#1 print() 를 이용 다음 내용을 출력
from builtins import print

print("*   *    *    ****    ****    *   *     /////");
print("*   *   * *   *   *   *   *   *   *    │ o o │");
print("*****  *   *  ****    ****     * *    (│  ^  │)");
print("*   *  *****  *   *   *   *     *      │ [_] │");
print("*   *  *   *  *    *  *    *    *       -----");

print("            +---+");
print("            │   │");
print("        +---+---+");
print("        │   │   │");
print("    +---+---+---+     /\_/\      -----");
print("    │   │   │   │    ( ' ' )   / Hello \ ");
print("+---+---+---+---+    (  -  )  <  Junior │");
print("│   │   │   │   │    │  │  │   \ Coder!/");
print("+---+---+---+---+    (__│__)     -----");

#2
name = '헤교'
weight = 36.5
age = 35

print('이름 : {0}, 몸무게 : {1}, 나이 : {2}'.format(name, weight, age))
print(weight)
print(age)

#3
x = 2
y = 3
z = 4

print('3x = ', 3 * x)
print('3x + y = ', 3 * x + y)
print('(x + y) / 7 = ', (x + y) / 7)
print('(3x + y) / (z + 2) = ', (3 * x + y) / (z + 2))

#4
x, y = 4, 8

print(x) #4
print(y) #8

x *= y # x = x * y

print(x) #32
print(y) #8

x -= y

print(x) #24
print(y) #8

#5
x = 3 # 이 행을 수정하시오

print(x + 7 == 10) #True

#6
print((-32 + 95) * 12 / 3) #252.0

print((3 * 4 - (( -27 + 67 ) / 4)) ** 8) #256.0

print(((512 + 1968 - 432) / 2 ** 4) + 128) #256.0

print(256 == 2 **8) #True

print(50 + 50 <= 10 * 10) #True

print(99 != 10 ** 2 - 1) #False

#7
x = 2.5
y = -1.5
m = 18
n = 4

#7a.
print(x + n * y - (x + n) * y) #6.25

#7b.
print(m / n + m % n) #6.5

#7c.
print(5 * x - n / 5) #11.7

#7d.
print(1 - (1 - (1 - (1 - (1 - n))))) #-3

#8
a = 2.5 * 3 / 27
b = 4 * 2 / 30

print(a)
print(b)
print(a == b)
print(a > b)
print(a < b)

#8 생활속 문제를 파이썬으로 풀기
a = (2.5 * 3) / 27
b = (4 * 2) / 30

print(a)
print(b)

print('----------------')

age = 20
kor = 99
tot = 40
avg = 40
name ='swaroop'

print(
'{0}, {1}'.format(name, kor)
)

print(
'{0}, {1}'.format(tot, avg)
)

print(
'{0}, {1:.1f}'.format(tot, avg)
)

print( '{name}, {kor}' .format(name='혜교', kor=88) )

print( '이름=%s, 국어=%d ' % (name, kor) )

print("abc \n xyz \n 123")

print('a'); print('b');

x = 1
y = 2

x, y = 1, 2

print( '이름=%s, 국어=%d ' \
       % (name, kor) )

print(100 < 200) #True
print(100 > 200) #False
print(100 == 200) #False
print(100 != 200) #True
print('----------------')
print(1 is 2) #False
print(1 is not 1) #False
print(1 is not 2) #True
print(type(1) is type(2)) #True
print('----------------')
print(True or True) #True
print(True | False) #True
#print(True || False)
#print(True||False)
print(True&False) #False
print(True and False) #False
print(not True) #False
#print(! True)
print('-------69-------')
print(int(True)) #1
print(int(False)) #0

print('#9a.')
print((3 + 4.5 * 2 + 27) / 8) #4.875

print('#9b.')
print(((True or False) and 3) < (4 or (not (5 == 7)))) #True

print('#9c.')
print(True or ((3 < 5) and (6 >= 2))) #True

print('#9d.')
#print(not True > 'A') 실행안됨 문자에 비교연산자

print('#9e.')
#print(7 % 4 + 3 - 2 / 6 * 'Z') 실행안됨 문자에 산술연산자

print('#9f.')
#print('D' + 1 + 'M' % 2 / 3) 실행안됨 문자에 산술연산자

print('#9g.')
print(5.0 / 3 + 3 /3) #2.666666666666667

print('#9h.')
print(53 % 21 < 45 / 18) #False

print('#9i.')
print((4 < 6) or True and False or False and (2 > 3)) #True

print('#9j.')
print(7 - (3 + 8 * 6 + 3) - (2 + 5 * 2)) #-59

#10 이윤율 계산 - 도메인 문제
#지문만으로는 문제를 해결할 수 없음
#문제에 대한 배경 지식이 필요 - 이윤율 공식
가변자본 = 15
불변자본 = 30
잉여가치 = 45
이윤율 = 잉여가치 / (불변자본 + 가변자본)
print('이윤율 : ', 이윤율) #이윤율 :  1.0

#11 환율에 따른 노트북 구매
#달러 : 780, 유로 : 650
#달러 환율 : 1070.2
#유로 환율 : 1307.81
달러노트북 = 780 * 1070.2 #834,756
유로노트북 = 680 * 1307.81 #889,310.80

print('달러노트북 %d, 유로노트북 %d' % (달러노트북, 유로노트북))

#12
pi = 3.14
ins = (100 - 5*2) * pi
outs = 100 * pi

print(ins == outs) #False
print(ins > outs) #False
print(ins < outs) #True
print(ins) #298.3
print(outs) #314.0
print('더 달려 %d 미터' % (outs - ins)) #outs 더 달려 31 미터

print('#13a.')
print("Check out this line") #Check out this line

print('#13b.')
#print("//hello there " + '9' + 7) TypeError: Can't convert 'int' object to str implicitly 문자와 숫자 간 산술연산

print('#13c.')
#print('H' + 'I' + " is " + 1 + "more example") TypeError: Can't convert 'int' object to str implicitly

print('#13d.')
#print('H' + 6.5 + 'I' + " is " + 1 + "morn example") TypeError: Can't convert 'float' object to str implicitly

print('#13e.')
print("Print both of us", "Me too") #Print both of us Me too

print('#13f.')
print("Reverse" + 'I' + 'T') #ReverseIT

print('#13g.')
#print("Nonot Hrer is" + 1 + "more example") TypeError: Can't convert 'int' object to str implicitly

print('#13j.')
#print("Hrer is" + 10 * 10) TypeError: Can't convert 'int' object to str implicitly

print('#13k.')
#print("Not x is" + True) TypeError: Can't convert 'bool' object to str implicitly 문자와 블리언

print('#13l.')
print() #공백

print('#13m.')
print #아무것도 안나옴 (함수의 유형 출력)

print('#13n.')
#print("How about this one" ++ '?' + 'Huh?') TypeError: bad operand type for unary +: 'str' 증가연산자

print('#17')
print('*** 사칙연산 프로그램 ***')
num1 = int(input('첫번쨰 정수를 입력하세요\n'))
num2 = int(input('두번째 정수를 입력하세요\n'))

print('%d + %d = %d ' % (num1, num2, num1 + num2))
print('%d - %d = %d ' % (num1, num2, num1 - num2))
print('%d * %d = %d ' % (num1, num2, num1 * num2))
print('%d / %d = %d ' % (num1, num2, num1 / num2))


print('*** if / else ***')
flag = input('맘에 드는 옷을 골랐나요? (예/아니오)')

if flag == '예':
       print(':) 축하드려요~')
else:
       print(':( 어떻게요~')

flag = 1 # True 정수값 : 1
if flag:
       print(':)')

if flag == '예':
       print(':) 축하합니다!!')
elif flag == '아니요':
       print(':( 아쉽군요.')
else:
       print("'예' 또는 '아니요'로만 입력하세요.")

print('*** if / else ***')

flag = input('맘에 드는 옷을 골랐나요? (예/아니오)')

if flag == '예':
    print(':) 축하드려요~')
    price = int(input('옷 값은 얼마인가요?'))
    if price > 10000:
        print(':( 비싸네요~')
    else:
        print(':) 하나주세요~')

elif flag == '아니오':
    print(':( 어떻해요~')
else:
    print("'예/아니요'로만 입력하세요!")

print( ord('a')) #순번 문자에 대한 ASCII 코드값 출력 97
print( chr(65)) #캐릭터 숫자에 대한 ASCII 코드값 출력 A

# 난수 생성
import random
print( random.random() ) # 0 ~ 1 사이 실수 float 출력

print( random.randint(1,10) ) # 지정한 범위의 정수 int 출력


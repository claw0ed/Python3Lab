print('#18 연봉 계산')
salary = int(input('연봉을 입력하세요\n'))
isMarried = input('결혼여부를 입력하세요 (Y/N)\n')
tax = 0;

if isMarried.upper() == 'N':
    if salary < 3000:
        tax = salary * 0.1
    else:
        tax = salary * 0.25
else:
    if salary < 6000:
        tax = salary * 0.1
    else:
        tax = salary * 0.25

print(isMarried, salary, tax)

print('#19 윤년 계산')
#현재 연도가 4로 나눠 떨어지지만
#100으로는 나눠 떨어지지 않음
#현재 연도가 400으로 나눠 떨어짐
year = int(input("윤년여부를 알고 싶은 년도를 입력하세요\n"))
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print('%d년은 윤년입니다' % year)
else:
    print('%d년은 윤년이 아닙니다' % year)

print('#20 복권 발행')
import random

lotto = str(random.randint(100, 999))
print(lotto)
lucky = str(input('복권 숫자 3자리를 입력하세요\n'))

match = 0;

if lotto[0] == lucky[0] or lotto[0] == lucky[1] or lotto[0] == lucky[2]:
    match += 1
if lotto[1] == lucky[0] or lotto[1] == lucky[1] or lotto[1] == lucky[2]:
    match += 1
if lotto[2] == lucky[0] or lotto[2] == lucky[1] or lotto[2] == lucky[2]:
    match += 1

msg = '꽝이군요! 다음 기회에!'
if match == 3:
    msg = '모두 일치! 상금 1백만원!'
if match == 2:
    msg = '2개 일치! 상금 1만원!'
if match == 1:
    msg = '1개 일치! 상금 1천원!'

print(msg)

lotto = str(random.randint(100, 999))
lucky = input('복권번호를 입력하세요\n')
match = 0 # 일치여부

if lucky[0] == lotto[0] or lucky[0] == lotto[1] or lucky[0] == lotto[2]:
    match += 1
if lucky[1] == lotto[0] or lucky[1] == lotto[1] or lucky[1] == lotto[2]:
    match += 1
if lucky[2] == lotto[0] or lucky[2] == lotto[1] or lucky[2] == lotto[2]:
    match += 1

print(lotto, lotto, match)

if match == 3:
    msg = '1등 당첨 : 백만원!'
elif match == 2:
    msg = '2등 당첨 : 만원!'
elif match == 1:
    msg = '3등 당첨 : 천원!'
else:
    msg = '꽝@@ 다음 기회에!'


print('#21 구구단')
# 숫자만 입력받기
# 문자 - ASCII 코드값 : ord()
# ASCII 코드값 - 문자 : chr()
# 0 : ASCII - 48,9 : ASCII - 57
dan = input('출력할 단을 입력하세요\n')
#if ord(dan[0]) >= ord('0') and ord(dan[0]) <= ord('9'):
if not num.isnumeric(): # 위에꺼 대신 넘이라는 값이 숫자가 아니라면
    print('구구단 출력')
else:
    print('입력 오류 - 숫자만 입력하세요!')

print('#22 소문자를 대문자로 변환')
# 숫자나 대문자 입력시 오류메시지 출력
lower = input('소문자를 입력하세요~\n')
if ord(lower[0]) >= ord('a') and ord(lower[0]) <= ord('z'):
    print(lower.upper())
else:
    print('소문자만 입력가능!!')

print('#23 숫자 맞추기')
# 1 ~ 100 사이 난수 생성 후 맞추는 게임
key = random.randint(1, 100)

while True:
    lucky = int(input('1 - 100 사이 숫자를 입력하세요\n'))
    if key == lucky:
        print('빙고!! 숫자를 맞췄습니다 @@')
        break
    elif key < lucky:
        print('으음...숫자가 크네요 :(')
    else:
        print('으음...숫자가 작네요 :(')

for i in range(4):
    print('현재', i)
    continue
    print('다음', i + 1)

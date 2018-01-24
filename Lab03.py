# 이름 짓기
# 파스칼 표기법(클래스) : 첫단어를 대문자로 시작하며 이름을 지음
#               Employees, Department
#               RegisterEmployees, JoinMember
# 카멜 표기법 : 첫단어를 소문자로 시작하며 이름을 지음
#             registerEmployees, joinMember
# 스네이크 표기법(함수, 변수) : 소문자와 _ 기호를 이용해서 이름을 지음
#                register_employees, join_member
# 헝가리언 표기법 : 자료형을 의미하는 접두사를 이용해서 이름을 지음
#                strName, isMarried, boolMarried


# 지금까지 예제를 함수로 작성
# qna8, qna10, qna11, qna12, qna17, qna18, qna19, qna20


# qna8 자취방 구하기
def compareRoom(width, height, price):
    return (width * height) / price

roomA = compareRoom(2.5, 3, 27)
roomB = compareRoom(4, 2, 30)

if (roomA > roomB):
    print('방A가 낫네요')
else:
    print('방B가 낫네요')


# qna10
def computeProfit():
    c = int(input('불변자본을 입력하세요'))
    v = int(input('가변자본을 입력하세요'))
    s = int(input('잉여가치액을 입력하세요'))

    #constant capital, variable capital, surplus value
    return (c + v) / s

print( computeProfit() )


# qna11
#달러 환율 : 1071
#유로 환율 : 1309
def getExchageRate(country):
    rate = 0
    if country == 'us':
        rate = 1071
    elif country == 'euro':
        rate = 1309
    return rate

buyUS = 780 * getExchageRate('us')
buyEuro = 650 * getExchageRate('euro')

print(buyEuro, buyUS)

if buyUS > buyEuro:
    print('유로화로 구입하는게 더 싸네요')
else:
    print('달러로 구입하는게 더 싸네요')


# qna12
def howManyRun(radius):
    pi = 3.14

    return radius * pi

studentA = howManyRun(100)
studentB = howManyRun(90)

print('학생A는 학생B보다 %dm 만큼 더 뜀' % (studentA - studentB) )

# qna17 (제곱연산 추가)
def intCalu():
    num1 = int(input('좌변값을 하나 입력하세요'))
    num2 = int(input('우변값을 하나 입력하세요'))
    fmt = "%d + %d = %d\n%d - %d = %d\n"
    fmt += "%d * %d = %d\n%d / %d = %.5f\n"
    fmt += "%d ** %d = %d\n"

    print(fmt % (num1, num2, num1 + num2, \
                 num1, num2, num1 - num2, \
                 num1, num2, num1 * num2, \
                 num1, num2, num1 / num2, \
                 num1, num2, num1 ** num2,))

intCalu()


# qna18
def computeTax():
    salary = int(input('연봉을 입력하세요\n'))
    isMarried = input('결혼여부를 입력하세요 (Y/N)\n')
    tax = 0;

    if isMarried.upper() == 'N':
        if salary < 3000:
            tax = salary * 0.1
        else:
            tax = salary * 0.25
        isMarried = "아니오"
    else:
        if salary < 6000:
            tax = salary * 0.1
        else:
            tax = salary * 0.25
        isMarried = "예"

    fmt = "연봉 : %d, 결혼여부 : %s, 세금 : %.1f"
    print( fmt % (salary, isMarried, tax) )

computeTax()


# qna19
def isLeapYear():
    year = int(input("윤년여부를 알고 싶은 년도를 입력하세요\n"))
    isLeap = '윤년이 아닙니다'

    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        isLeap = '윤년입니다'

    print( "%d는 %s" % (year, isLeap) )

isLeapYear()


# qna20 복권발행
import random
def rouletteLotto():
    lotto = str(random.randint(100, 999))
    lucky = input('복권번호를 입력하세요\n')
    match = 0  # 일치여부

    for i in [0,1,2]:
        for j in [0,1,2]:
            if (lucky[i] == lotto[j]):
                match += 1

    if match == 3:
        prize = '1등 당첨! 상금 백만원!'
    elif match == 2:
        prize = '2등 당첨! 상금 만원!'
    elif match == 1:
        prize = '3등 당첨! 상금 천원!'

    print(lucky, lotto, prize)

rouletteLotto()


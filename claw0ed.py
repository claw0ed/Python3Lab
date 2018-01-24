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


# qna19
def isLeapYear():
    year = int(input("윤년여부를 알고 싶은 년도를 입력하세요\n"))
    isLeap = '윤년이 아닙니다'

    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        isLeap = '윤년입니다'

    print( "%d는 %s" % (year, isLeap) )


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


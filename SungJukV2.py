# 성적 처리 프로그램 v2
# 이름 name, 국어 kor, 영어 eng, 수학 mat
# 총점 tot ,평균 avg, 학점 grd
# getTotal, getAverage, getGrade

def getTotal():
    # pass : dummy code
    tot = kor + eng + mat
    return tot

def getAverage():
    avg = getTotal() / 3
    return avg

def getGrade():
    avg = getAverage()
    grd = '가'
    if avg >= 90:
        grd = '수'
    elif avg >= 80:
        grd = '우'
    elif avg >= 70:
        grd = '미'
    elif avg >= 60:
        grd = '양'
    return grd

print('-- 성적 처리 프로그램 v2 --')

name = input('이름을 입력하세요\n')
kor = int(input('국어 점수를 입력하세요\n'))
eng = int(input('영어 점수를 입력하세요\n'))
mat = int(input('수학 점수를 입력하세요\n'))

fmt = '%s %d %d %d %d %.2f %s'
print( fmt % (name, kor, eng, mat, getTotal(), getAverage(), getGrade() ) )

print('-- 성적 처리 프로그램 v1 --')

name = input('이름을 입력하세요\n')
kor = int(input('국어 점수를 입력하세요\n'))
eng = int(input('영어 점수를 입력하세요\n'))
mat = int(input('수학 점수를 입력하세요\n'))

tot = kor + eng + mat
avg = tot / 3
grd = '가'
if avg >= 90:
    grd = '수'
elif avg >= 80:
    grd = '우'
elif avg >= 70:
    grd = '미'
elif avg >= 60:
    grd = '양'

print(name, kor, eng, mat, tot, avg, grd)
print('{0} {1} {2} {3} {4} {5:.2f} {6}'.format(name, kor, eng, mat, tot, avg, grd))
print('%s %d %d %d %d %.2f %s' % (name, kor, eng, mat, tot, avg, grd))

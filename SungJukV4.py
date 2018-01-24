# 성적 처리 프로그램 v4
# 이름 name, 국어 kor, 영어 eng, 수학 mat
# 총점 tot ,평균 avg, 학점 grd
# getTotal, getAverage, getGrade
# 리스트 자료구조를 이용한다
class SungJukV0:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

class SungJukService:
    def getTotal(self, sj):
        tot = sj.kor + sj.eng + sj.mat
        return tot

    def getAverage(self, sj):
        avg = sj.getTotal(sj) / 3
        return avg

    def getGrade(self, sj):
        grdlist = '가가가가가가미양우수수'
        var = int(sj.getAverage(sj) / 10)
        grd = grdlist[var]
        return grd

sjsrv = SungJukService()
sj1 = SungJukV0('지현', 98, 45, 23)

print(sj1.name)
print(sj1.kor)
print(sj1.eng)
print(sj1.mat)

print(sjsrv.getTotal(sj1))
print(sjsrv.getAverage(sj1))
print(sjsrv.getGrade(sj1))
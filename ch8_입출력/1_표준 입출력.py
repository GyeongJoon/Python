# sep : 구분자 넣기
# end : 문장 끝 지정하기
print("Python", "Java", "Javascript", sep=" vs ")
print("Python", "Java", sep=",", end="?")
print("무엇이 더 재미있을까요?")

# file : 출력 위치 지정하기
import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# ljust, rlist : 공간 확보해 정렬하기
# 시험 성적
scores = {"수학": 0, "영어": 50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# zfill : 빈칸으로 0으로 채우기
# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))


answer = input("아무 값이나 입력하세요: ")
answer = 10
print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")
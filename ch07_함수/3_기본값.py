# 기본값
def get_price(is_vip = False): # True: 단골 손님, False: 일반 손님
	if is_vip == True:
		return 10000 # 단골 손님
	else:
		return 15000 # 일반 손님

price = get_price(True)
print(f'커트 가격은 {price}원입니다.') # 10000

price = get_price()
print(f'커트 가격은 {price}원입니다.') # 15000


def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name,age,main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학념 같은 반 같은 수업.
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name,age,main_lang))

profile("유재석")
profile("김태호")


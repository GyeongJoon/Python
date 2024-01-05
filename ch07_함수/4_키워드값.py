# 키워드값
def get_price(is_vip = False,
							is_birthday = False,
							is_membership = False,
							card = False,
							review = False,
							first_time = False):
	if is_vip == True:
		return 10000 # 단골 손님
	else:
		return 15000 # 일반 손님

price = get_price(review = Ture, is_vip = Ture)
print(f'커트 가격은 {price}원입니다.')

def profile(name,age,main_lang):
    print(name,age,main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=23, name="김태호")
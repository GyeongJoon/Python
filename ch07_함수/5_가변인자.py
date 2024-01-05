# 가변인자
def visit(today, *customers):
	print(today)
	for customer in customers:
		print(customer) # 고객 이름 출력

visit('24/01/24','장경준','장경원')



# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이:{1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)


def profile(name, age, *language):
    print("이름: {0}\t나이:{1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 23, "Python","Java","C","C++","C#","Javascript")
profile("김태호", 25, "Kotlin","Swift","","","")

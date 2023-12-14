# if / elif / else

weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather == "눈" : # if 조건:
    print("우산을 챙기세요.") # 실행명령문
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물 필요 없어요.")


temp = int(input("기온은 어때요?"))
if temp >= 30:
    print("너무 더워요.")
elif temp >= 10 and temp < 30:
    print("괜찮은 날씨에요.")
elif temp >= 0 and temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무 추워요.")






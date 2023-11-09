# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) #첫글자만 대문자
print(len(python)) # 문자의 개수
print(python.replace("Python", "Java")) # 문자 바꿈
print(python.index("n")) # 문자의 인덱스
index = python.index("n")
print(index)
index = python.index("n", index + 1) # 문자의 인덱스
print(index)
print(python.find("n")) # 문자의 인덱스
# print(python.index("Java"))
print(python.count("n")) # 문자의 개수
url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙 1
my_str = my_str[:my_str.index(".")] # 규칙 2
password = my_str[:3] + str(len(my_str)) + str(my_str.index("e")) + "!" # 규칙 3
print("{0}의 비밀번호는 {1} 입니다.".format(url,password))

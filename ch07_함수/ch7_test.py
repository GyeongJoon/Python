# def std_weight(height,gender):
#     if gender == "남자":
#         print("키 {0} {1}의 표준 체중은 {2}입니다.".format(height, gender, height*height*22))
#     elif gender == "여자":
#         print("키 {0} {1}의 표준 체중은 {2}입니다.".format(height, gender, height*height*21))

# std_weight(1.75, "남자")
# std_weight(1.56, "여자")

def std_weight(height,gender):
    if gender == "남자":
        return height*height*22
    elif gender == "여자":
        return height*height*21
    
height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))


def get_air_quality(air):
    if 0 <= air <= 30:
        print('좋음')
        return air
    elif 31 <= air <= 80:
        print('보통')
        return air
    elif 81 <= air <= 150:
        print('나쁨')
        return air
    elif 151 <= air:
        print('매우 나쁨')
        return air
    else:
        print('오류')

get_air_quality(15)
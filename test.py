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


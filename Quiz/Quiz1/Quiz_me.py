names = ["유튜버1", "유튜버2", "유튜버3", "유튜버4"]

def text(name=None):
    if name is None:
        name = ''
    return f'''
    안녕하세요? {name}님.

    (주)나도출판 편집자 나코입니다.
    현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
    {name}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
    자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

    좋은 하루 보내세요 ^^
    감사합니다.

    - 나코 드림.
    '''

# 각 name에 대해 텍스트 파일을 생성하고 내용을 쓰기
for name in names:
    filename = f"{name}.txt"  # 파일 이름 생성
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text(name))
    print(f"{filename} 파일이 생성되었습니다.")

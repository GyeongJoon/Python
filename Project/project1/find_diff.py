# 필요한 라이브러리와 모듈을 가져옵니다.
import os  # 운영 체제 관련 기능을 사용하기 위한 모듈
import time  # 시간과 관련된 기능을 사용하기 위한 모듈
import pyautogui  # 마우스와 키보드 제어를 위한 모듈
from PIL import ImageChops  # 이미지 비교를 위한 모듈
import cv2

while True:
    result = pyautogui.confirm('틀린 그림 찾기', buttons=['시작', '종료'])
    if result == '종료':
        break # 프로그램 종료
    
    # 왼쪽(원본) 이미지 캡처 및 저장
    width, height = 584, 468  # 이미지 크기
    x_pos = 667  # 시작 좌표 x

    src = pyautogui.screenshot(region=(x_pos, 0, width, height))
    # src.save('src.jpg')

    # 오른쪽(비교대상) 이미지 캡처 및 저장
    dest = pyautogui.screenshot(region=(x_pos, 473, width, height))
    # dest.save('dest.jpg')

    # 이미지 비교를 위한 차이 이미지 생성 및 저장
    diff = ImageChops.difference(src, dest)
    diff.save('diff.jpg')

    # 파일이 생성될 때까지 대기
    while not os.path.exists('diff.jpg'):
        time.sleep(1)

    # OpenCV를 사용하여 이미지 파일 로드

    # src_img = cv2.imread('src.jpg')
    # dest_img = cv2.imread('dest.jpg')
    diff_img = cv2.imread('diff.jpg')

    # 차이를 찾아 윤곽선 검출
    gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # 윤곽선에 녹색 사각형 그리기
    COLOR = (0, 200, 100)
    for cnt in contours:
        if 300 > cv2.contourArea(cnt) > 100:
            x, y, width, height = cv2.boundingRect(cnt)
            # cv2.rectangle(src_img, (x, y), (x + width, y + height), COLOR, 2)
            # cv2.rectangle(dest_img, (x, y), (x + width, y + height), COLOR, 2)
            cv2.rectangle(diff_img, (x, y), (x + width, y + height), COLOR, 2)

            # 마우스 이동 및 클릭 코드
            to_x = x + (width // 2) + x_pos
            to_y = y + (height // 2)
            pyautogui.moveTo(to_x, to_y, duration=0.5)
            pyautogui.click(to_x, to_y)

    # 이미지 창에 결과를 표시
    # cv2.imshow('src', src_img)
    # cv2.imshow('dest', dest_img)
    cv2.imshow('diff', diff_img)

    # 키 입력 대기 후 이미지 창 닫기
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# -*- coding: utf-8 -*-

import cv2
from PIL import Image
import drag_crop as dc

print("D조의 이미지 편집 툴 실행!!")
print("아래 해당하는 번호를 입력해 원하시는 기능을 선택해주세요.")

select = -1 #번호 입력 초기화

while True:
    print("1 : 이미지 색상 변경") #주연
    print("2 : 이미지 모자이크") #주연
    print("3 : 이미지 합성") #주연
    print("4 : 이미지 썸네일 생성") #주연
    print("5 : 이미지 드래그 크롭") #지혜
    print("6 : 이미지 배경색 변경") #기환
    print("7 : 이미지 텍스트 추가") #지원
    print("8 : 이미지 파일 이메일 전송") #상민
    select = input("원하시는 기능을 선택해주세요 : ")

    if select == '5':
        cv2.imshow('image', dc.img) #Window(사진) open
        cv2.setMouseCallback('image', dc.onMouse)
        cv2.waitKey(0) #키보드 두 번 누르면 윈도우 종료 
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    elif select == '0':
        print("Ver 1.0 End :)")
        break











#cv2.imshow('image', dc.img) #Window(사진) open
#cv2.setMouseCallback('image', dc.onMouse)
#cv2.waitKey(0) #키보드 두 번 누르면 윈도우 종료 
#cv2.waitKey(0)
#cv2.destroyAllWindows()
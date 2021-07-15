# -*- coding: utf-8 -*-

#1. 로컬에 저장된 이미지를 받아와서 화면에 띄우는 것 (O)
#2. 드래그로 크롭 이미지 영역 지정 (O)
#3. 받아온 좌표 기준으로 크롭 (O)
#4. 크롭된 결과 이미지 저장 (O)
#
#**찾아보아야 할 것**
#
#1. Python 드래그로 좌표 받아오는 것 확인 (OpenCV 활용)

#import OpenCV
import cv2

x0 = y0 = -1 #좌표 리셋
w = h = -1
isDragging = False



def onMouse(event, x, y, flags, param) :
    global isDragging, x0, y0 #, img
    # event는 마우스 동작 상수값, 클릭, 이동 등등
    # x, y는 내가 띄운 창을 기준으로 좌측 상단점이 0,0
    # flags는 마우스 이벤트가 발생할 때 키보드 또는 마우스 상태를 의미, Shif+마우스 등 설정가능
    # param은 영상이룻도 있도 전달하고 싶은 데이터, 안쓰더라도 넣어줘야함
    if event == cv2.EVENT_LBUTTONDOWN:
        isDragging = True
        x0 = x
        y0 = y
#    elif event == cv2.EVENT_MOUSEMOVE:
#        if isDragging:
#            copy_img = img.copy()
#            cv2.rectangle(img_draw, (oldx, oldy), (x, y), blue, 2)
#            cv2.imshow('img', img_draw)
    elif event == cv2.EVENT_LBUTTONUP:
        if isDragging:
            isDragging = False
            w = x - x0
            h = y - y0
            if w > 0 and h > 0:
                roi = img[y0:y0+h, x0:x0+w]
                cv2.imshow('cropped', roi)
                cv2.imwrite('./src/cropped_dog1.jpg', roi)
                print("모든 창을 닫으시거나 엔터를 두 번 누르면 종료됩니다.")
            else:
                print("왼쪽 위부터 오른쪽 아래로 드래그해주세요!")
            
img = cv2.imread('./src/dog1.jpg') #파일 객체 설정
cv2.imshow('image', img) #Window(사진) open
cv2.setMouseCallback('image', onMouse)
cv2.waitKey(0) #키보드 두 번 누르면 윈도우 종료 
cv2.waitKey(0)
cv2.destroyAllWindows()
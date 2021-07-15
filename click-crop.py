#1. 로컬에 저장된 이미지를 받아와서 화면에 띄우는 것 (O)
#2. 띄워진 이미지 4개 클릭 좌표 받아오기 (O)
#3. 받아온 좌표 기준으로 크롭
#4. 크롭된 결과 이미지 저장 (O)
#
#**찾아보아야 할 것**
#
#1. Pillow 라이브러리 파일 받아오기, 실행, 크롭, 저장 기능 확인 (O)
#2. Python 이미지 좌표 받아오는 방법 확인 (OpenCV 활용)

#import Pillow
from PIL import Image
#import OpenCV
import cv2

oldx1 = oldy1 = -1 #좌표 리셋
oldx2 = oldy1 = -1

img = cv2.imread('./src/dog1.jpg') #파일 객체 설정
copy_img = img.copy();
cv2.imshow('image', img) #Window(사진) open

def onMouse(event, x, y, flags, param) :
    # event는 마우스 동작 상수값, 클릭, 이동 등등
    # x, y는 내가 띄운 창을 기준으로 좌측 상단점이 0,0이 됌
    # flags는 마우스 이벤트가 발생할 때 키보드 또는 마우스 상태를 의미, Shif+마우스 등 설정가능
    # param은 영상이룻도 있도 전달하고 싶은 데이타, 안쓰더라도 넣어줘야함
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx = x
        oldy = y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))

cv2.setMouseCallback('image', onMouse)

cv2.waitKey(0) #키보드 두 번 누르면 윈도우 종료 
cv2.waitKey(0)
cv2.destroyAllWindows()


#파일 열기 
#img.show()

#(왼쪽위x,왼쪽위y,오른쪽아래x,오른쪽아래y)
#img_crop = img.crop((350, 120, 650, 467))
##크롭한 이미지를 해당 경로에 저장 
#img_crop.save('./src/dog1_crop.jpg')
#img_crop.show()
#
#img.close() 
#1. 로컬에 저장된 이미지를 받아와서 화면에 띄우는 것 (O)
#2. 띄워진 이미지 4개 클릭 좌표 받아오기
#3. 받아온 좌표 기준으로 크롭
#4. 크롭된 결과 이미지 저장 (O)
#
#**오늘 찾아보아야 할 것**
#
#1. Pillow 라이브러리 파일 받아오기, 실행, 크롭, 저장 기능 확인 (O)
#2. Python 이미지 좌표 받아오는 방법 확인

#import Pillow
from PIL import Image
#import OpenCV
import cv2

img=cv2.imread('./src/dog1.jpg') #파일 객체 설정
cv2.imshow('image', img) #Window(사진) open
cv2.waitKey(0) #키보드 두 번 누르면 윈도우 종료 
cv2.waitKey(0)
cv2.destroyAllWindows()

oldx = oldy = -1 #좌표 리셋
#파일 열기 
#img.show()

#(왼쪽위x,왼쪽위y,오른쪽아래x,오른쪽아래y)
img_crop = img.crop((350, 120, 650, 467))
#크롭한 이미지를 해당 경로에 저장 
img_crop.save('./src/dog1_crop.jpg')
img_crop.show()

img.close()
cv2.destroyAllWindows()
import cv2
import json

# 이미지 불러오기
image = cv2.imread('C:\Users\user\Desktop\23_kdt_hackathon\23-KDT-Hackerthon\hackathon_data\data\Training\01.원천데이터\TS_남자사람\남자사람_7_남_00572.jpg')

with open(file_path, "r", encoding="utf-8") as file:
    json_data = json.load(file)
    
    # 사람 전체~입까지 바운딩 박스 정보 탐색
    for cnt in range(0, 7):
        json_data_ele = json_data['annotations']['bbox'][cnt]
        width, height = json_data_ele['w'], json_data_ele['h']  #좌표 및 크기
        size = width * height


# Bounding box 좌표 (x, y, width, height)
x, y, width, height = (100, 100, 200, 200)  # 원하는 좌표 및 크기로 수정하세요

# Bounding box에 해당하는 이미지 추출
roi = image[y:y+height, x:x+width]

# 추출한 이미지를 저장할 경로 지정
output_path = 'output_image.jpg'

# 이미지 저장
cv2.imwrite(output_path, roi)

# 추출한 이미지를 화면에 표시 (선택사항)
cv2.imshow('Extracted Image', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
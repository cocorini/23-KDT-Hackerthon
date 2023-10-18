import cv2
import json
import numpy as np
import os
from tqdm import tqdm
import time

folder_path = r"C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\data\Training\01.원천데이터\TS_남자사람_얼굴"

# 지정한 폴더 내의 모든 파일과 폴더 목록을 가져옵니다.
contents = os.listdir(folder_path)

cnt=100

# 파일과 폴더 목록을 출력합니다.
for file_name in tqdm(contents):
    if cnt==0: 
        break
    
    file_path = os.path.join(folder_path, file_name)
    try:
        img_array = np.fromfile(file_path, np.uint8)
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)


        height, width, _ = image.shape

        # 이미지를 그레이, canny로 변경
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        canny = cv2.Canny(gray_image, 3000, 1000, apertureSize = 5, L2gradient = True)
        
        # 추출한 이미지를 저장할 경로 지정
        output_path = r"C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\data\Training\01.원천데이터\TS_남자사람_얼굴_canny_Thdown1"
        output_path = os.path.join(output_path, file_name)
        
        # 한글포함 경로에 넣기 위함..
        ret, img_arr = cv2.imencode('.jpg', canny)

        if ret:
            with open(output_path, mode='w+b') as f:
                img_arr.tofile(f)
        
        
        
        
        cnt-=1
        # # 결과 이미지
        # cv2.imshow('Image with Lines', canny)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # # 에지 이미지에서 선 찾기
        # lines = cv2.HoughLinesP(canny, 1, np.pi / 180, threshold=10, minLineLength=15)


        # for line in lines:
        #     x1, y1, x2, y2 = line[0]
        #     if y1 < height/2 or y2 < height/2: 
        #         continue
        #     angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
            
        #     cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)


        # # 결과 이미지
        # cv2.imshow('Image with Lines', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        
    except Exception as e:
        print(f"파일 읽기 및 JSON 파싱 오류: {file_name}, 오류 메시지: {str(e)}")
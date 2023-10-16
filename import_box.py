import cv2
import json
import numpy as np
import os

img_array = np.fromfile(r"C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\data\Training\01.원천데이터\TS_남자사람\남자사람_7_남_00572.jpg", np.uint8)
image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
file_path = r"C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\data\Training\02.라벨링데이터\TL_남자사람\남자사람_7_남_00572.json"

with open(file_path, "r", encoding="utf-8") as file:
    json_data = json.load(file)
    
    for cnt in range(1, 3):
        json_data_ele = json_data['annotations']['bbox'][cnt]
        x, y, width, height = json_data_ele['x'], json_data_ele['y'], json_data_ele['w'], json_data_ele['h']  #좌표

        # Bounding box에 해당하는 이미지 추출
        roi = image[y:y+height, x:x+width]

        # 추출한 이미지를 저장할 경로 지정
        output_path = r"C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\data\Training\01.원천데이터\TS_남자사람_"

        output_path += json_data['annotations']['bbox'][cnt]['label']
        
        file_name = json_data['meta']['img_path'].split('/')[-1]
        
        output_path = os.path.join(output_path, file_name)
         
        ret, img_arr = cv2.imencode('.jpg', roi)

        if ret:
            with open(output_path, mode='w+b') as f:
                img_arr.tofile(f)

        # 추출한 이미지를 화면에 표시 (선택사항)
        cv2.imshow('Extracted Image', roi)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
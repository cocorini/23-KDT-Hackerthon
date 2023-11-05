import cv2
import numpy as np
import os

folder_path = r"C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\data\Training\01.원천데이터\TS_남자사람_다리"

contents = os.listdir(folder_path)

for file_name in contents:
    file_path = os.path.join(folder_path, file_name)
    try:
        img_array = np.fromfile(file_path, np.uint8)
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        # 원하는 이미지 크기를 설정합니다.
        desired_width = 160
        desired_height = 120

        # 이미지 크기를 조절합니다.
        resized_image = cv2.resize(image, (desired_width, desired_height))
        
        output_path = os.path.join(r"C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\data\Training\01.원천데이터\TS_남자사람_다리", file_name)
                    
        # 한글포함 경로에 넣기 위함..
        ret, img_arr = cv2.imencode('.jpg', resized_image)

        if ret:
            with open(output_path, mode='w+b') as f:
                img_arr.tofile(f)
                
    except Exception as e:
        print(f"파일 읽기 및 JSON 파싱 오류: {file_name}, 오류 메시지: {str(e)}")
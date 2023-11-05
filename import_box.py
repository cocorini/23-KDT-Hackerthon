import cv2
import json
import numpy as np
import os


folder_path1 = r"C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\266.AI 기반 아동 미술심리 진단을 위한 그림 데이터 구축\01.데이터\Validation\01.원천데이터\VS_집"
folder_path2 = r"C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\266.AI 기반 아동 미술심리 진단을 위한 그림 데이터 구축\01.데이터\Validation\02.라벨링데이터\VL_집"

# 지정한 폴더 내의 모든 파일과 폴더 목록을 가져옵니다.
contents = os.listdir(folder_path1)

count=0

# 파일과 폴더 목록을 출력합니다.
for file_name in contents:
    if count==50:
        break
    count+=1
    file_path = os.path.join(folder_path1, file_name)
    json_path = os.path.join(folder_path2, file_name)
    try:
        img_array = np.fromfile(file_path, np.uint8)
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        json_path = json_path[:-2]+'son'
        
        with open(json_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)
            
            cnt = 2
            json_data_ele = json_data['annotations']['bbox'][cnt]
            if json_data_ele['label'] != '집벽':
                continue
            x, y, width, height = json_data_ele['x'], json_data_ele['y'], json_data_ele['w'], json_data_ele['h']  #좌표

            # Bounding box에 해당하는 이미지 추출
            roi = image[y:y+height, x:x+width]

            # 추출한 이미지를 저장할 경로 지정
            output_path = r"C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\266.AI 기반 아동 미술심리 진단을 위한 그림 데이터 구축\01.데이터\Validation\01.원천데이터\VS_집_"
            output_path += json_data['annotations']['bbox'][cnt]['label']
            file_name = json_data['meta']['img_path'].split('/')[-1]
            output_path = os.path.join(output_path, file_name)
            
            # 한글포함 경로에 넣기 위함..
            ret, img_arr = cv2.imencode('.jpg', roi)

            if ret:
                with open(output_path, mode='w+b') as f:
                    img_arr.tofile(f)
        
    except Exception as e:
        print(f"파일 읽기 및 JSON 파싱 오류: {file_name}, 오류 메시지: {str(e)}")
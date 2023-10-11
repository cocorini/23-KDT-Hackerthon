from skimage.metrics import structural_similarity as ssim
import os
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# boxplot 해석 함수
def boxplot_describe(Data, data_name):
    # Q1, Q3 계산
    Q1 = np.percentile(Data, 25)
    Q3 = np.percentile(Data, 75)

    # IQR 계산
    IQR = Q3 - Q1

    # 이상치 경계 계산
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # 이상치 식별
    outliers = [x for x in data if x < lower_bound or x > upper_bound]

    # 이상치를 벗어난 데이터 수 계산
    outliers_count = len(outliers)

    print(data_name, '해석')
    print("이상치 경계 (하단):", lower_bound)
    print("이상치 경계 (상단):", upper_bound)
    print("데이터 평균 값: ", Data.mean())
    print()
    print()

# 데이터 저장
data = []

# 라벨링 들어있는 폴더
folder_path_w = r"C:\Users\user\Downloads\hackathon_data\data\Training\02.라벨링데이터\TL_여자사람"
folder_path_m = r"C:\Users\user\Downloads\hackathon_data\data\Training\02.라벨링데이터\TL_남자사람"

# 지정한 폴더 내의 모든 파일과 폴더 목록을 가져옵니다.
contents_w = os.listdir(folder_path_w)
contents_m = os.listdir(folder_path_m)

body = []
head = []
face = []
eye = []
nose = []
mouth = []


# 여자그림: 파일과 폴더 목록을 출력합니다.
for file_name in contents_w:
    file_path = os.path.join(folder_path_w, file_name)
    try:
        # JSON 파일을 열어서 내용을 읽고 파싱합니다.
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)
            
            # 사람 전체~입까지 바운딩 박스 정보 탐색
            for cnt in range(0, 7):
                json_data_ele = json_data['annotations']['bbox'][cnt]
                width, height = json_data_ele['w'], json_data_ele['h']  #좌표 및 크기
                size = width * height
                
                if cnt==0:
                    body.append(size)
                elif cnt==1:
                    head.append(size)
                elif cnt==2:
                    face.append(size)
                elif cnt==3 or cnt==4:
                    eye.append(size)
                elif cnt==5:
                    nose.append(size)
                else:
                    mouth.append(size)
        
            
    except Exception as e:
        print(f"파일 읽기 및 JSON 파싱 오류: {file_name}, 오류 메시지: {str(e)}")
        break

body = np.array(body)
head = np.array(head)
face = np.array(face)
eye = np.array(eye)
nose = np.array(nose)
mouth = np.array(mouth)

## 그래프 그리기

plt.figure(figsize=(12,10))

plt.subplot(2, 3, 1)
plt.boxplot(body)
plt.title('body Box Plot')
plt.ylabel('val')

plt.subplot(2, 3, 2)
plt.boxplot(head)
plt.title('head Box Plot')
plt.ylabel('val')

plt.subplot(2, 3, 3)
plt.boxplot(face)
plt.title('face Box Plot')
plt.ylabel('val')

plt.subplot(2, 3, 4)
plt.boxplot(eye)
plt.title('eye Box Plot')
plt.ylabel('val')

plt.subplot(2, 3, 5)
plt.boxplot(nose)
plt.title('nose Box Plot')
plt.ylabel('val')

plt.subplot(2, 3, 6)
plt.boxplot(mouth)
plt.title('mouth Box Plot')
plt.ylabel('val')

plt.show()

boxplot_describe(body, 'body')
boxplot_describe(head, 'head')
boxplot_describe(face, 'face')
boxplot_describe(eye, 'eye')
boxplot_describe(nose, 'nose')
boxplot_describe(mouth, 'mouth')
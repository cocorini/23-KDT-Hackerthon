import os
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# 해석 함수
def describe(Data, data_name):
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
    print()
    print()
    
def compare():
    global w_body_w, w_body_h, w_head_w, w_head_h, w_face_w, w_face_h, w_eye_w, w_eye_h, w_nose_w, w_nose_h, w_mouth_w, w_mouth_h 
    global m_body_w, m_body_h, m_head_w, m_head_h, m_face_w, m_face_h, m_eye_w, m_eye_h, m_nose_w, m_nose_h, m_mouth_w, m_mouth_h 
    
    body = [w_body_w, m_body_w, w_body_h, m_body_h]
    head = [w_head_w, m_head_w, w_head_h, m_head_h]
    face = [w_face_w, m_face_w, w_face_h, m_face_h]
    eye =  [w_eye_w, m_eye_w, w_eye_h, m_eye_h]
    nose =  [w_nose_w, m_nose_w, w_nose_h, m_nose_h]
    mouth =  [w_mouth_w, m_mouth_w, w_mouth_h, m_mouth_h]
    
    plt.figure()
    plt.subplot(2,3,1)
    plt.boxplot(body)
    for i in range(1, len(body) + 1):
        y = body[i - 1]
        x = np.ones_like(y) * i
        plt.text(x[0], min(y), f"Median: {np.median(y):.2f}\nIQR: {np.percentile(y, 75) - np.percentile(y, 25):.2f}", verticalalignment="bottom")
    plt.xticks([1,2,3,4], ['w_body_w', 'm_body_w', 'w_body_h', 'm_body_h'])
    plt.xlabel('body')
    
    plt.subplot(2,3,2)
    plt.boxplot(head)
    for i in range(1, len(head) + 1):
        y = head[i - 1]
        x = np.ones_like(y) * i
        plt.text(x[0], min(y), f"Median: {np.median(y):.2f}\nIQR: {np.percentile(y, 75) - np.percentile(y, 25):.2f}", verticalalignment="bottom")
    plt.xticks([1,2,3,4], ['w_head_w', 'm_head_w', 'w_head_h', 'm_head_h'])
    plt.xlabel('head')
    
    plt.subplot(2,3,3)
    plt.boxplot(face)
    for i in range(1, len(face) + 1):
        y = face[i - 1]
        x = np.ones_like(y) * i
        plt.text(x[0], min(y), f"Median: {np.median(y):.2f}\nIQR: {np.percentile(y, 75) - np.percentile(y, 25):.2f}", verticalalignment="bottom")
    plt.xticks([1,2,3,4], ['w_face_w', 'm_face_w', 'w_face_h', 'm_face_h'])
    plt.xlabel('face')
    
    plt.subplot(2,3,4)
    plt.boxplot(eye)
    for i in range(1, len(eye) + 1):
        y = eye[i - 1]
        x = np.ones_like(y) * i
        plt.text(x[0], min(y), f"Median: {np.median(y):.2f}\nIQR: {np.percentile(y, 75) - np.percentile(y, 25):.2f}", verticalalignment="bottom")
    plt.xticks([1,2,3,4], ['w_eye_w', 'm_eye_w', 'w_eye_h', 'm_eye_h'])
    plt.xlabel('eye')
    
    plt.subplot(2,3,5)
    plt.boxplot(nose)
    for i in range(1, len(nose) + 1):
        y = nose[i - 1]
        x = np.ones_like(y) * i
        plt.text(x[0], min(y), f"Median: {np.median(y):.2f}\nIQR: {np.percentile(y, 75) - np.percentile(y, 25):.2f}", verticalalignment="bottom")
    plt.xticks([1,2,3,4], ['w_nose_w', 'm_nose_w', 'w_nose_h', 'm_nose_h'])
    plt.xlabel('nose')
    
    plt.subplot(2,3,6)
    plt.boxplot(mouth)
    for i in range(1, len(mouth) + 1):
        y = mouth[i - 1]
        x = np.ones_like(y) * i
        plt.text(x[0], min(y), f"Median: {np.median(y):.2f}\nIQR: {np.percentile(y, 75) - np.percentile(y, 25):.2f}", verticalalignment="bottom")
    plt.xticks([1,2,3,4], ['w_mouth_w', 'm_mouth_w', 'w_mouth_h', 'm_mouth_h'])
    plt.xlabel('mouth')
    
    plt.show()
    


def find_boundbox(content, woman):
    for file_name in content:
        if woman:
            file_path = os.path.join(folder_path_w, file_name)
        else:
            file_path = os.path.join(folder_path_m, file_name)    
        
        try:
            # JSON 파일을 열어서 내용을 읽고 파싱합니다.
            with open(file_path, "r", encoding="utf-8") as file:
                json_data = json.load(file)
                
                # 사람 전체~입까지 바운딩 박스 정보 탐색
                for cnt in range(0, 7):
                    json_data_ele = json_data['annotations']['bbox'][cnt]
                    width, height = json_data_ele['w'], json_data_ele['h']  #좌표 및 크기
                    size = width * height
                    
                    if woman:
                        if cnt==0:
                            w_body.append([width, height])
                        elif cnt==1:
                            w_head.append([width, height])
                        elif cnt==2:
                            w_face.append([width, height])
                        elif cnt==3 or cnt==4:
                            w_eye.append([width, height])
                        elif cnt==5:
                            w_nose.append([width, height])
                        else:
                            w_mouth.append([width, height])
                    else:
                        if cnt==0:
                            m_body.append([width, height])
                        elif cnt==1:
                            m_head.append([width, height])
                        elif cnt==2:
                            m_face.append([width, height])
                        elif cnt==3 or cnt==4:
                            m_eye.append([width, height])
                        elif cnt==5:
                            m_nose.append([width, height])
                        else:
                            m_mouth.append([width, height])
                    
                
        except Exception as e:
            print(f"파일 읽기 및 JSON 파싱 오류: {file_name}, 오류 메시지: {str(e)}")
            break



# 데이터 저장
data = []

# 라벨링 들어있는 폴더
folder_path_w = r"C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\data\Training\02.라벨링데이터\TL_여자사람"
folder_path_m = r"C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\data\Training\02.라벨링데이터\TL_남자사람"

# 지정한 폴더 내의 모든 파일과 폴더 목록 가져오기
contents_w = os.listdir(folder_path_w)
contents_m = os.listdir(folder_path_m)

w_body = []
w_head = []
w_face = []
w_eye = []
w_nose = []
w_mouth = []

m_body = []
m_head = []
m_face = []
m_eye = []
m_nose = []
m_mouth = []


# 여자그림: 파일과 폴더 목록 출력
find_boundbox(contents_w, True)

# 남자그림: 파일과 폴더 목록 출력
find_boundbox(contents_m, False)

w_body_w = np.array(w_body[:][0])
w_body_h = np.array(w_body[:][1])
w_head_w = np.array(w_head[:][0])
w_head_h = np.array(w_head[:][1])
w_face_w = np.array(w_face[:][0])
w_face_h = np.array(w_face[:][1])
w_eye_w = np.array(w_eye[:][0])
w_eye_h = np.array(w_eye[:][1])
w_nose_w = np.array(w_nose[:][0])
w_nose_h = np.array(w_nose[:][1])
w_mouth_w = np.array(w_mouth[:][0])
w_mouth_h = np.array(w_mouth[:][1])

m_body_w = np.array(m_body[:][0])
m_body_h = np.array(m_body[:][1])
m_head_w = np.array(m_head[:][0])
m_head_h = np.array(m_head[:][1])
m_face_w = np.array(m_face[:][0])
m_face_h = np.array(m_face[:][1])
m_eye_w = np.array(m_eye[:][0])
m_eye_h = np.array(m_eye[:][1])
m_nose_w = np.array(m_nose[:][0])
m_nose_h = np.array(m_nose[:][1])
m_mouth_w = np.array(m_mouth[:][0])
m_mouth_h = np.array(m_mouth[:][1])

compare()
import os
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

def find_boundbox(key):
    train_path = r"C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\266.AI 기반 아동 미술심리 진단을 위한 그림 데이터 구축\01.데이터\Training\02.라벨링데이터"
    dic = {'나무':'TL_나무', '남자':'TL_남자사람', '여자': 'TL_여자사람', '집': 'TL_집'}
    
    file_path = os.path.join(train_path, dic[key])
    files = os.listdir(file_path)
    
    for file_name in files:
        path = os.path.join(file_path, file_name)
        
        try:
            # JSON 파일을 열어서 내용을 읽고 파싱합니다.
            with open(path, "r", encoding="utf-8") as file:
                json_data = json.load(file)
                
                if key=='남자' or key=='여자':
                    body = json_data['annotations']['bbox'][0]
                    head = json_data['annotations']['bbox'][1]
                    face = json_data['annotations']['bbox'][2]
                    eye = json_data['annotations']['bbox'][3]
                    mouth = json_data['annotations']['bbox'][5]
                    ear = json_data['annotations']['bbox'][6]
                    neck = json_data['annotations']['bbox'][8]
                    upper_body = json_data['annotations']['bbox'][9]
                    foot = json_data['annotations']['bbox'][12]
                    leg = json_data['annotations']['bbox'][15]
                    shoes1 = json_data['annotations']['bbox'][16]
                    shoes2 = json_data['annotations']['bbox'][17]
                    
                elif key=='나무':
                    contents = json_data['annotations']['bbox']
                    for content in contents:
                        if content['label'] is '나무전체':
                            tree_h.append(content['h'])
                            tree_w.append(content['w'])
                        elif content['label'] is '기둥':
                            trunk_h.append(content['h'])
                            trunk_w.append(content['w'])
                        elif content['label'] is '수관':
                            crown_h.append(content['h'])
                            crown_w.append(content['w'])    
                        elif content['label'] is '나뭇잎':
                            leaf_h.append(content['h'])
                            leaf_w.append(content['w'])
                
        except Exception as e:
            print(f"파일 읽기 및 JSON 파싱 오류: {file_name}, 오류 메시지: {str(e)}")
            break
        

Tree = pd.DataFrame()
Man = pd.DataFrame()
House = pd.DataFrame()

tree_h = np.array()
tree_w = np.array()
trunk_h = np.array()
trunk_w = np.array()
branch_h = np.array()
branch_w = np.array()
leaf_h = np.array()
leaf_w = np.array()
crown_h = np.array()
crown_w = np.array()

find_boundbox('나무')

Tree['tree_h'] = tree_h
Tree['tree_w'] = tree_w
Tree['trunk_h'] = trunk_h
Tree['trunk_w'] = trunk_w
Tree['branch_h'] = branch_h
Tree['branch_w'] = branch_w
Tree['leaf_h'] = leaf_h
Tree['leaf_w'] = leaf_w
Tree['crown_h'] = crown_h
Tree['crown_w'] = crown_w
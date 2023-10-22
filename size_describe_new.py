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
                    contents = json_data['annotations']['bbox']
                    for content in contents:
                        if content['label'] == '사람전체':
                            body_h.append(content['h'])
                            body_w.append(content['w'])
                        elif content['label'] == '머리':
                            head_h.append(content['h'])
                            head_w.append(content['w'])
                        elif content['label'] == '얼굴':
                            face_h.append(content['h'])
                            face_w.append(content['w'])
                        elif content['label'] == '코':
                            nose_h.append(content['h'])
                            nose_w.append(content['w'])    
                        elif content['label'] == '눈':
                            eye_h.append(content['h'])
                            eye_w.append(content['w'])
                        elif content['label'] == '입':
                            mouth_h.append(content['h'])
                            mouth_w.append(content['w'])
                        elif content['label'] == '귀':
                            ear_h.append(content['h'])
                            ear_w.append(content['w'])    
                        elif content['label'] == '목':
                            neck_h.append(content['h'])
                            neck_w.append(content['w'])
                        elif content['label'] == '상체':
                            upper_body_h.append(content['h'])
                            upper_body_w.append(content['w'])
                        elif content['label'] == '발':
                            foot_h.append(content['h'])
                            foot_w.append(content['w'])    
                        elif content['label'] == '다리':
                            leg_h.append(content['h'])
                            leg_w.append(content['w'])    
                        elif content['label'] == '운동화':
                            shoes1_h.append(content['h'])
                            shoes_w.append(content['w'])
                            
                    if key=='여자':
                        if content['label'] == '여자구두':
                            shoes2_h.append(content['h'])
                            shoes2_w.append(content['w'])
                    else:
                        if content['label'] == '남자구두':
                            shoes2_h.append(content['h'])
                            shoes2_w.append(content['w'])
                            
                    
                elif key=='나무':
                    contents = json_data['annotations']['bbox']
                    for content in contents:
                        if content['label'] == '나무전체':
                            tree_h.append(content['h'])
                            tree_w.append(content['w'])
                        elif content['label'] == '기둥':
                            trunk_h.append(content['h'])
                            trunk_w.append(content['w'])
                        elif content['label'] == '가지':
                            branch_h.append(content['h'])
                            branch_w.append(content['w'])
                        elif content['label'] == '수관':
                            crown_h.append(content['h'])
                            crown_w.append(content['w'])    
                        elif content['label'] == '나뭇잎':
                            leaf_h.append(content['h'])
                            leaf_w.append(content['w'])
                
                elif key=='집':
                    contents = json_data['annotations']['bbox']
                    for content in contents:
                        if content['label'] == '지붕':
                            roof_h.append(content['h'])
                            roof_w.append(content['w'])
                        elif content['label'] == '문':
                            door_h.append(content['h'])
                            door_w.append(content['w'])
                        elif content['label'] == '창문':
                            window_h.append(content['h'])
                            window_w.append(content['w'])
                
        except Exception as e:
            print(f"파일 읽기 및 JSON 파싱 오류: {file_name}, 오류 메시지: {str(e)}")
            break

def make_df(key):
    dic={'나무': Tree, '남자': Man, '여자': Woman, '집': House}
    
    if key=='나무':
        find_boundbox(key)
        
        # 사이즈 11200개로 동일하게 제작
        dic[key]['tree_h'] = tree_h[:11200]
        dic[key]['tree_w'] = tree_w[:11200]
        dic[key]['trunk_h'] = trunk_h[:11200]
        dic[key]['trunk_w'] = trunk_w[:11200]
        dic[key]['branch_h'] = branch_h[:11200]
        dic[key]['branch_w'] = branch_w[:11200]
        dic[key]['leaf_h'] = leaf_h[:11200]
        dic[key]['leaf_w'] = leaf_w[:11200]
        dic[key]['crown_h'] = crown_h[:11200]
        dic[key]['crown_w'] = crown_w[:11200]
        
    elif key=='남자' or key=='여자':
        find_boundbox(key)
        
        # 사이즈 11200개로 동일하게 제작
        dic[key]['body_h']=body_h[:11200]
        dic[key]['body_w']=body_w[:11200]
        dic[key]['head_h']=head_h[:11200]
        dic[key]['head_w']=head_w[:11200]
        dic[key]['face_h']=face_h[:11200]
        dic[key]['face_w']=face_w[:11200]
        dic[key]['eye_h']=eye_h[:11200]
        dic[key]['eye_w']=eye_w[:11200]
        dic[key]['nose_h']=nose_h[:11200]
        dic[key]['nose_w']=nose_w[:11200]
        dic[key]['mouth_h']=mouth_h[:11200]
        dic[key]['mouth_w']=mouth_w[:11200]
        dic[key]['ear_h']=ear_h[:11200]
        dic[key]['ear_w']=ear_w[:11200]
        dic[key]['neck_h']=neck_h[:11200]
        dic[key]['neck_w']=neck_w[:11200]
        dic[key]['upper_body_h']=upper_body_h[:11200]
        dic[key]['upper_body_w']=upper_body_w[:11200]
        dic[key]['foot_h']=foot_h[:11200]
        dic[key]['foot_w']=foot_w[:11200]
        dic[key]['leg_h']=leg_h[:11200]
        dic[key]['leg_w']=leg_w[:11200]
        dic[key]['shoes1_h']=shoes1_h[:11200]
        dic[key]['shoes_w']=shoes_w[:11200]
        dic[key]['shoes2_h']=shoes2_h[:11200]
        dic[key]['shoes2_w']=shoes2_w[:11200]
    
    elif key=='집':
        find_boundbox(key)
        
        # 사이즈 11300개로 동일하게 제작
        dic[key]['roof_h']= roof_h[:11300]
        dic[key]['roof_w']= roof_w[:11300]
        dic[key]['door_h']= door_h[:11300]
        dic[key]['door_w']= door_w[:11300]
        dic[key]['window_h']= window_h[:11300]
        dic[key]['window_w']= window_w[:11300]
        
Tree = pd.DataFrame()
Man = pd.DataFrame()
Woman = pd.DataFrame()
House = pd.DataFrame()

tree_h = []
tree_w = []
trunk_h = []
trunk_w = []
branch_h = []
branch_w = []
leaf_h = []
leaf_w = []
crown_h = []
crown_w = []
make_df('나무')

body_h = []
body_w = []
head_h = []
head_w = []
face_h = []
face_w = []
eye_h = []
eye_w = []
nose_h = []
nose_w = []
mouth_h = []
mouth_w = []
ear_h = []
ear_w = []
neck_h = []
neck_w = []
upper_body_h = []
upper_body_w = []
foot_h = []
foot_w = []
leg_h = []
leg_w = []
shoes1_h = []
shoes_w = []
shoes2_h = []
shoes2_w = []
make_df('남자')

body_h = []
body_w = []
head_h = []
head_w = []
face_h = []
face_w = []
eye_h = []
eye_w = []
nose_h = []
nose_w = []
mouth_h = []
mouth_w = []
ear_h = []
ear_w = []
neck_h = []
neck_w = []
upper_body_h = []
upper_body_w = []
foot_h = []
foot_w = []
leg_h = []
leg_w = []
shoes1_h = []
shoes_w = []
shoes2_h = []
shoes2_w = []
make_df('여자')

roof_h = []
roof_w = []
door_h = []
door_w = []
window_h = []
window_w = []
make_df('집')

Tree.to_csv(r'C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\tree.csv')
Man.to_csv(r'C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\man.csv')
Woman.to_csv(r'C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\woman.csv')
House.to_csv(r'C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\house.csv')
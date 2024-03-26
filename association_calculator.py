import pandas as pd

num_tags = 12  # 전체 태그 수

def calculate_association(userInfos, exhibitionInfos):
    association_list = []

    if userInfos is not None and exhibitionInfos is not None:
        for userInfo in userInfos:
            user_id = userInfo['userId']
            user_tags = userInfo['userTagNames']
            for exhibitionInfo in exhibitionInfos:
                exhibition_id = exhibitionInfo['exhibitionId']
                exhibition_tags = exhibitionInfo['exhibitionTagNames']
                
                # 선택된 태그의 가중치 계산
                weight = sum(1 for tag in user_tags if tag in exhibition_tags) / num_tags

                # 결과를 리스트에 저장
                association_list.append({'userId': user_id, 'exhibitionId': exhibition_id, 'weight': weight})

    else:
        print("Unable to calculate association between users and exhibitions.") 

    # DataFrame으로 변환하여 반환
    return pd.DataFrame(association_list)
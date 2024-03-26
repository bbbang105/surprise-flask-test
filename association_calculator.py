num_tags = 12  # 전체 태그 수

def calculate_association(userInfos, exhibitionInfos):
    if userInfos is not None and exhibitionInfos is not None:
        for userInfo in userInfos:
            user_id = userInfo['userId']
            user_tags = userInfo['userTagNames']
            for exhibitionInfo in exhibitionInfos:
                exhibition_id = exhibitionInfo['exhibitionId']
                exhibition_tags = exhibitionInfo['exhibitionTagNames']
                
                # 선택된 태그의 가중치 계산
                weight = sum(1 for tag in user_tags if tag in exhibition_tags) / num_tags
                print(f"User ID: {user_id}, Exhibition ID: {exhibition_id}, Weight: {weight:.3f}")
    else:
        print("Unable to calculate association between users and exhibitions.") 
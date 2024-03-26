from surprise import Reader, Dataset
from surprise import KNNBasic
import heapq
from collections import defaultdict

# ratings.csv 파일을 읽어 Surprise 데이터셋 생성
reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)
data = Dataset.load_from_file("ratings.csv", reader=reader)

# Surprise 데이터셋을 훈련셋으로 변환
trainSet = data.build_full_trainset()

# 유사도 옵션 설정
sim_options = {
    'name': 'cosine',
    'user_based': True
}

# KNNBasic 모델 초기화 및 훈련
model = KNNBasic(sim_options=sim_options)
model.fit(trainSet)

# 유사도 행렬 계산
simsMatrix = model.compute_similarities()

def recommendForUser(userID, k=10):
    testUserInnerID = trainSet.to_inner_uid(userID)
    similarityRow = simsMatrix[testUserInnerID]

    users = []
    for innerID, score in enumerate(similarityRow):
        if innerID != testUserInnerID:
            users.append((innerID, score))

    kNeighbors = heapq.nlargest(k, users, key=lambda t: t[1])

    candidates = defaultdict(float)
    for similarUser in kNeighbors:
        innerID = similarUser[0]
        userSimilarityScore = similarUser[1]
        theirRatings = trainSet.ur[innerID]
        for rating in theirRatings:
            candidates[rating[0]] += rating[1] * userSimilarityScore

    watched = {}
    for itemID, rating in trainSet.ur[testUserInnerID]:
        watched[itemID] = 1

    recommendedItems = []
    for itemID, ratingSum in sorted(candidates.items(), key=lambda k: k[1], reverse=True):
        if not itemID in watched:
            movieID = trainSet.to_raw_iid(itemID)
            recommendedItems.append((movieID, ratingSum))

    return recommendedItems

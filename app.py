from request_sender import send_get_request
from association_calculator import calculate_association
from surprise_model import build_collaborative_filtering_model, recommend_exhibitions_for_user
import configparser

# 설정 파일 읽기
config = configparser.ConfigParser()
config.read('config.ini')

# 사용자 정보 가져오기
users_url = config['Endpoints']['users_url']
user_infos = send_get_request(users_url)

# 전시회 정보 가져오기
exhibitions_url = config['Endpoints']['exhibitions_url']
exhibition_infos = send_get_request(exhibitions_url)

# 유저와 전시회 간의 연관성 계산
association_infos = calculate_association(user_infos, exhibition_infos)

# 협업 필터링 모델 훈련
collaborative_filtering_model = build_collaborative_filtering_model(association_infos)

# 사용자에게 전시회 추천 받기
user_id = 100  # 사용자 ID 입력
recommended_exhibitions = recommend_exhibitions_for_user(collaborative_filtering_model, user_id)

# 전시회 추천 결과 출력
print("Recommended Exhibitions for User", user_id, ":")
for exhibition_id, weight in recommended_exhibitions:
    print("- Exhibition ID:", exhibition_id, "|", "Weight:", weight)
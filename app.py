from request_sender import send_get_request
from association_calculator import calculate_association

# Spring Boot 애플리케이션의 엔드포인트 URL
users_url = "http://localhost:8080/api/flask/users"
exhibitions_url = "http://localhost:8080/api/flask/exhibitions"
num_tags = 12  # 태그의 총 개수

# 사용자 정보 가져오기
userInfos = send_get_request(users_url)

# 전시회 정보 가져오기
exhibitionInfos = send_get_request(exhibitions_url)

# 유저와 전시회 간의 연관성 계산
calculate_association(userInfos, exhibitionInfos)
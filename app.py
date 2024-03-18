import ssl
ssl._create_default_https_context = ssl._create_unverified_context # SSL 인증 비활성화 : 테스트 환경에서만 사용❗️

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # 데이터 불러오기
    movies = pd.read_csv("https://grepp-reco-test.s3.ap-northeast-2.amazonaws.com/movielens/movies.csv")
    ratings = pd.read_csv("https://grepp-reco-test.s3.ap-northeast-2.amazonaws.com/movielens/ratings.csv")
    
    # 영화 정보 출력
    movies_html = movies.head().to_html()

    return render_template('index.html', movies_html=movies_html)

if __name__ == '__main__':
    app.run(debug=True)
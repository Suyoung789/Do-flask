from flask import Flask
#Flask 모듈 임포트
 
app = Flask(__name__)
#Flaks 객체를 app에 할당

@app.route('/')
#라우팅 경로를 '/'로 설정
def hello():
     return 'Hi flask'

if __name__ == "__main__":
    app.run()
#메인 모듈로 실행될 때 플라스크 서버 구동
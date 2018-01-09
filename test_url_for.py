from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

@app.route('/profile/<user>')
#동적으로 URI를 적용할 수도 있다. user가 동적으로 변경되는 부분이며 변환타입을 명시해 문자열이 아닌 다른 형태도 가능
def profile(user):
    return 'hello' + user
#user가 profile함수의 인자로 사용

if __name__ == '__main__':  
    with app.test_request_context():
        print (url_for('hello'))
        print (url_for('profile', user="flask"))
        #url_for함수를 이용해 함수명으로 URI를 얻을 수 있다
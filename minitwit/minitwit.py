from flask import Flask, session, g
from sqlite3 import dbapi2 as sqlite3

#configuration
DATABASE = '/minitwit.db'
PER_PAGE = 30
DEBUG = True
SECERET_KEY = 'development key'

#플라스크 애플리케이션 생성 및 데이터베이스 초기화
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('MINITWIT_SETTINGS',silent=True)

def connet_db():
    return sqlite3.connect(app.config[DATABASE])

@app.before_request
def before_request():
    g.db = connet_db()
    g.user = None
    if 'user_id' in session:
        g.user = query('select * from user where user_id= ?', [session['user_id']], one=True)

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0],value)for idx, value in enumerate(row))for row in cur.fetchall()]

    return  (rv[0] if rv else None) if one else rv

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()
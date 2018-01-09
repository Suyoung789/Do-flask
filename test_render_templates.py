from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello():
    return render_template('hello.html', name='flask')

if __name__ == "__main__":
    app.run()
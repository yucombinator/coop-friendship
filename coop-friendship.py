from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def nye_world():
    return 'Bye World!'

if __name__ == '__main__':
    app.run(debug=True)

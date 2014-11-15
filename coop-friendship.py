from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def nye_world():
    return 'Bye World!'

@app.route('/test/inner')
def inner():
    return "You've reached the inside."

@app.route('/test/inner2')
def inner2():
    return "The second inside."

if __name__ == '__main__':
    app.run(debug=True)

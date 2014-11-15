from flask import Flask, render_template

app = Flask(__name__)

def arrayTest():
    return str(2)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/test')
def nye_world():
    return 'Bye World!'

@app.route('/test/inner')
def inner():
    return "You've reached the inside."

@app.route('/test/inner2')
def inner2():
    return "The second inside."

@app.route('/array')
def test():
    return arrayTest()

if __name__ == '__main__':
    app.run(debug=True)

dict = {"8":["1A", "1B", "COOP", "2A", "OFF"]}
def compareArrays(array1, array2):

    pass
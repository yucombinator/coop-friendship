import json
from flask import Flask,render_template, request
import os
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/getPrograms")
def getPrograms():
    return render_template('index.html')

@app.route("/postSubmit", methods=['POST'])
def postSubmit():
    my_program = str(request.form['my_program'])
    my_stream = str(request.form['my_stream'])
    my_term = str(request.form['my_term'])
    friend_program = str(request.form['friend_program'])
    friend_stream = str(request.form['friend_stream'])
    friend_term = str(request.form['friend_term'])
    response = json.dumps({'status': "OK"}, sort_keys=True,indent=4, separators=(',', ': '))
    return response

if __name__ == "__main__":
    app.run(debug=True,host='localhost',port=int(os.environ.get("PORT", 5000)))
import json
from flask import Flask,render_template, request
import os
import logic


app = Flask(__name__)
programs = []
import csv

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/getPrograms")
def getPrograms():
    response = json.dumps(programs, sort_keys=True,indent=4, separators=(',', ': '))
    return response

@app.route("/postSubmit", methods=['POST'])
def postSubmit():
    my_faculty = str(request.form['my_faculty'])
    my_program = str(request.form['my_program'])
    my_stream = str(request.form['my_stream'])
    my_term = str(request.form['my_term'])
    friend_faculty = str(request.form['friend_faculty'])
    friend_program = str(request.form['friend_program'])
    friend_stream = str(request.form['friend_stream'])
    friend_term = str(request.form['friend_term'])
    dict = logic.takeInput(my_faculty, my_program, my_term,friend_faculty,
                           friend_program, friend_term,my_stream,friend_stream)
    response = json.dumps(['response',{'dates':dict["terms"],
                                       'my_array':dict["array1"],
                                       'friend_array':dict["array2"],
                                       'result':dict["results"]}],
                          sort_keys=True,indent=4, separators=(',', ': '))
    return response

@app.route("/postSuggestion", methods=['POST'])
def postSuggestion():
    program = str(request.form['my_program'])
    faculty = str(request.form['my_stream'])
    response = json.dumps({}, sort_keys=True,indent=4, separators=(',', ': '))
    return response

if __name__ == "__main__":
    f = open('programs.csv')
    csv_f = csv.reader(f)
    for row in csv_f:
      programs.append({'program':row[0],'faculty':row[1],'require_stream':row[2]})
    app.run(debug=True,host='localhost',port=int(os.environ.get("PORT", 5000)))


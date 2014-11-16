import json
from flask import Flask,render_template, request
import os
import logic
import programs as program_helper
import csv

app = Flask(__name__)
programs = []


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/getPrograms")
def getPrograms():
    response = json.dumps(programs, sort_keys=True, indent=4, separators=(',', ': '))
    return response

@app.route("/postSubmit", methods=['POST'])
def postSubmit():
    post = request.get_json()
    app.logger.debug(post)
    my_program = post.get('my_program')
    my_stream = post.get('my_stream')
    my_term = post.get('my_term').upper()
    my_faculty = post.get('my_faculty')
    friend_program = post.get('friend_program')
    friend_stream = post.get('friend_stream')
    friend_term = post.get('friend_term').upper()
    friend_faculty = post.get('friend_faculty')

    dict = logic.takeInput(my_faculty, my_program, my_term, friend_faculty,
                           friend_program, friend_term, my_stream, friend_stream)
    app.logger.debug(dict)

    response = json.dumps(['response',{'dates':dict["terms"],
                                       'my_array':dict["array1"],
                                       'friend_array':dict["array2"],
                                       'result':dict["results"]}],
                          sort_keys=True,indent=4, separators=(',', ': '))
    return response

def parseColor(param):
    if param == "science":
        return "blue"
    elif param == "math":
        return "violet"
    elif param == "environment":
        return "green"
    elif param == "arts":
        return "orange"
    elif param == "engineering":
        return "purple"
    elif param == "health":
        return "blue"
    else:
        return "black"

@app.route("/postSuggestion", methods=['POST'])
def postSuggestion():
    post = request.get_json()
    program = post.get('program')
    faculty = post.get('faculty')
    app.logger.debug(program)
    app.logger.debug(faculty)
    array = program_helper.suggestProgram(faculty, program)
    app.logger.debug(array)
    response = json.dumps(array, sort_keys=True,indent=4, separators=(',', ': '))
    return response

@app.route("/postTerms", methods=['POST'])
def postTerms():
    post = request.get_json()
    app.logger.debug(post)
    program = post.get('program')
    faculty = post.get('faculty')
    stream = post.get('stream')
    app.logger.debug(program)
    app.logger.debug(faculty)
    app.logger.debug(stream)
    array = program_helper.returnTerms(faculty, program, stream)
    app.logger.debug(array)
    response = json.dumps(array, sort_keys=True,indent=4, separators=(',', ': '))
    return response

if __name__ == "__main__":
    f = open('programs.csv')
    csv_f = csv.reader(f)
    for row in csv_f:
      color = parseColor(row[1])
      programs.append({'name':row[0],'faculty':row[1],'require_stream':row[2],'color':color})
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get("PORT", 5000)))


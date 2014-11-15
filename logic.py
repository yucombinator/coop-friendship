import data, datetime

def detFaculty(faculty):
    if faculty == "AHS":
        return data.AHS
    elif faculty == "ENG":
        return data.ENG
    elif faculty == "SCI":
        return data.SCI
    elif faculty == "MATH":
        return data.MATH
    elif faculty == "ARTS":
        return data.ARTS
    else:
        return data.ENV


def ahsProgram(program):
    if program == "Health Promotion":
        return "HPROMO"
    elif program == "Health Studies":
        return "HSTUDY"
    elif program == "Kinesiology":
        return "KIN"
    else:
        return "RLS"

def artsProgram(program, stream=None):
    if program == "Accounting and Financial Management":
        return ("AFM" + stream)
    elif program == "Anthropology" or program == "Political Science" or program == "Psychology" or program == "Sociology":
        return "ANTHRO"
    elif program == "Arts and Business with Digital Arts Communication Specialization or International Trade Specialization":
        return "GENSPEC"
    elif program == "Computing and Financial Management":
        return "CFM"
    elif program == "Economics":
        return "ECON"
    elif program == "English":
        return "ENGLISH"
    else:
        return "GEN"

def engProgram(program, stream = None):
    if program == "Architecture Engineering":
        return "ARCH"
    elif program == "Biomedical Engineering":
        return "BIOMED"
    elif program == "Nanotechnology Engineering":
        return "NANO"
    elif program == "Software Engineering":
        return "SE"
    elif (program == "Electrical Engineering" or program == "Computer Engineering") and stream == "4":
        return "ECE4"
    elif stream == "4":
        return "4"
    elif stream == "8":
        return "8"

def envProgram(program):
    if program == "Environment and Business":
        return "BUSINESS"
    elif program == "Environment and Resource Studies":
        return "RESOURCE"
    elif program == "Geography and Environmental Management":
        return "GEMGMT"
    elif program == "Geomatics":
        return "GEOMATICS"
    elif program == "Planning":
        return "PLANNING"

def sciProgram(program):
    if program == "Pharmacy (Doctor of Pharmacy":
        return "PHARM"
    elif program == "Psychology":
        return "PSYCH"
    elif program == "Materials and Nanosciences":
        return "MAT"
    elif program == "Biotechnology/Chartered Professional Accountancy":
        return "BIOT"
    elif program == "Physics" or program == "Mathematical Physics" or program == "Life Physics" or program == "Physics and Astronomy":
        return "PHYS"
    else:
        return "BIOC"

def findProgram(facultyString, programString, stream=None):
    faculty = detFaculty(facultyString)
    program = ""
    if faculty == data.ARTS:
        program == artsProgram(programString, stream)
    elif faculty == data.AHS:
        program = ahsProgram(programString)
    elif faculty == data.ENG:
        program = engProgram(programString, stream)
    elif faculty == data.SCI:
        program == sciProgram(programString)
    elif faculty == data.ENV:
        program = envProgram(programString)
    else:
        program = mathProgram(programString, stream)

    return faculty[program]

def generateTerms(length):
    #CREATE ARRAY OF TERMS
    #Keeping track of dates.
    date = str(datetime.date.today()).split("-")
    for element in range(len(date)):
        date[element] = int(date[element])

    #Append term to array
    terms = []
    for index in range(length):
        currentTerm = str(date[0])
        if 1 <= date[1] <= 4:
            currentTerm += "W"
        elif 5 <= date[1] <= 8:
            currentTerm += "S"
        else:
            currentTerm += "F"
        terms.append(currentTerm)

        #Shift to next term and wrap
        date[1] += 4
        if date[1] > 12:
            date[0] += 1
            date[1] -= 12
    return terms

def comparePrograms(array1, array2, term1="1A", term2="1A"):
    #SHIFTING THE ARRAYS
    array1 = array1[array1.index(term1):]
    array2 = array2[array2.index(term2):]

    #PRINTING STUFF
    results = []
    length = min(len(array1), len(array2))
    for index in range(length):
        if "COOP" not in array1[index] and "OFF" not in array1[index] and "COOP" not in array2[index] and "OFF" not in array2[index]:
            results.append("ON CAMPUS")
        elif ("COOP" in array1[index] or array1[index] == "OFF") and ("COOP" in array2[index] or array2[index] == "OFF"):
            results.append("OFF CAMPUS")
        else:
            results.append("NO MATCH")

    #PAD "NO MATCH" to the end.
    padding = abs(len(array1)-len(array2))
    for index in range(padding):
        results.append("NO MATCH")

    terms = generateTerms(max(len(array1), len(array2)))

    return {"terms":terms,
            "array1":array1,
            "array2":array2,
            "results":results
    }

def takeInput(my_faculty, my_program, my_stream_code = None, my_term, friend_faculty, friend_program, friend_stream_code = None, friend_term):
    myProgram = findProgram(my_faculty, my_program, my_stream_code)
    friendProgram = findProgram(friend_faculty, friend_program, friend_stream_code)

    results = comparePrograms(myProgram, friendProgram, my_term, friend_term)
    print (results)

takeInput("Engineering", "Software Engineering", None, "1A", "Math", "Computer Science", "1", "1A")


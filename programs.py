import data

def detFaculty(faculty):
    if faculty == "health":
        return data.AHS
    elif faculty == "engineering":
        return data.ENG
    elif faculty == "science":
        return data.SCI
    elif faculty == "math":
        return data.MATH
    elif faculty == "arts":
        return data.ARTS
    else:
        return data.ENV

def mathProgram(program, stream = None):
    if program == 'Bioinformatics':
        return 'BIO'
    elif program == 'Mathematical Physics':
        return 'PHYS'
    elif program == 'Business Administration and Computer Science':
        if stream == "Sequence 1":
            return 'DD1'
        elif stream == "Sequence 2":
            return 'DD2'
        else:
            return 'DD3'
    elif program == 'Business Administration and Mathematics':
        if stream == "Sequence 1":
            return 'DD1'
        elif stream == "Sequence 2":
            return 'DD2'
        else:
            return 'DD3'
    elif program == 'Mathematics/Teaching' or program == 'Pure Mathematics/Teaching':
        if stream == "Sequence 1":
            return 'T1'
        else :
            return 'T2'
    elif program == 'Mathematics/Chartered Professional Accountancy':
        if stream == "Sequence 1":
            return 'CPA1'
        elif stream == "Sequence 2":
            return 'CPA2'
        else:
            return 'CPA3'
    else:
        if stream == "Sequence 1":
          return '1'
        elif stream == "Sequence 2":
            return '2'
        elif stream == "Sequence 3":
            return '3'
        else :
            return '4'




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
        if stream == "Sequence 1":
            return "AFM1"
        elif stream == "Sequence 2":
            return "AFM2"
        else:
            return "AFM3"
    elif program == "Anthropology" or program == "Political Science" or program == "Psychology" or \
                    program == "Sociology":
        return "ANTHRO"
    elif program == "Arts and Business with Digital Arts Communication Specialization":
        return "GENSPEC"
    elif program == "Arts and Business with International Trade Specialization":
        return "GENSPEC"
    elif program == "Computing and Financial Management":
        return "CFM"
    elif program == "Economics":
        return "ECON"
    elif "English" in program:
        return "ENGLISH"
    else:
        return "GEN"

def engProgram(program, stream):
    if program == "Architecture":
        return "ARCH"
    elif program == "Biomedical Engineering":
        return "BIOMED"
    elif program == "Nanotechnology Engineering":
        return "NANO"
    elif program == "Software Engineering":
        return "SE"
    elif (program == "Electrical Engineering" or program == "Computer Engineering") and stream == "Stream 4":
        return "ECE4"
    elif program == "Civil Engineering" or program == "Management Engineering":
        return "8"
    elif program == "Environmental Engineering" or program == "Geological Engineering" \
            or program == "Systems Design Engineering":
        return "4"
    elif stream == "Stream 4":
        return "4"
    elif stream == "Stream 8":
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
    if program == "Pharmacy":
        return "PHARM"
    elif program == "Psychology":
        return "PSYCH"
    elif program == "Materials and Nanosciences":
        return "MAT"
    elif program == "Biotechnology/Chartered Professional Accountancy":
        return "BIOT"
    elif program == "Physics" or program == "Mathematical Physics" or program == "Life Physics" \
            or program == "Physics and Astronomy":
        return "PHYS"
    else:
        return "BIOC"

def findProgram(facultyString, programString, stream=None):
    faculty = detFaculty(facultyString)
    program = ""
    if faculty == data.ARTS:
        program = artsProgram(programString, stream)
    elif faculty == data.AHS:
        program = ahsProgram(programString)
    elif faculty == data.ENG:
        program = engProgram(programString, stream)
    elif faculty == data.SCI:
        program = sciProgram(programString)
    elif faculty == data.ENV:
        program = envProgram(programString)
    else:
        program = mathProgram(programString, stream)
    return faculty[program]


def suggestMath(programString):
    if programString == "Mathematics/Chartered Professional Accountancy" \
            or programString == 'Business Administration and Computer Science (Double Degree)':
        return ["Sequence 1", "Sequence 2", "Sequence 3"]
    elif programString == 'Mathematics/Teaching' or programString == 'Pure Mathematics/Teaching':
        return ["Sequence 1", "Sequence 2"]
    else:
        return ["Sequence 1", "Sequence 2", "Sequence 3", "Sequence 4"]

def suggestProgram(facultyString, programString):
    faculty = detFaculty(facultyString)
    if faculty == data.ARTS:
        return ["Sequence 1", "Sequence 2", "Sequence 3"]
    elif faculty == data.ENG:
        return ["Stream 4", "Stream 8"]
    elif faculty == data.MATH:
        return suggestMath(programString)

def returnTerms(facultyString, programString, stream = None):
    faculty = detFaculty(facultyString)
    program = findProgram(facultyString, programString, stream)
    return program

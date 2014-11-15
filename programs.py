import data

def mathProgram(program, stream = None):
    if program == 'Bioinformatics':
        return 'BIO'
    elif program == 'Mathematical Physics':
        return 'PHYS'
    elif program == 'Business Administration and Computer Science (Double Degree)':
        if stream == 1:
            return 'DD1'
        elif stream == 2:
            return 'DD2'
        else:
            return 'DD3'
    elif program == 'Business Administration and Computer Science (Double Degree)':
        if stream == 1:
            return 'DD1'
        elif stream == 2:
            return 'DD2'
        else:
            return 'DD3'
    elif program == 'Mathematics/Teaching' or 'Pure Mathematics/Teaching':
        if stream == 1:
            return 'T1'
        else :
            return 'T2'
    elif program == 'Mathematics/Chartered Professional Accountancy':
        if stream == 1:
            return 'CPA1'
        elif stream == 2:
            return 'CPA2'
        else:
            return 'CPA3'
    else:
        if stream == 1:
          return '1'
        elif stream == 2:
            return '2'
        elif stream == 3:
            return '3'
        else :
            return '4'

def detFaculty(faculty):
    if faculty == "Applied Health Sciences":
        return data.AHS
    elif faculty == "Engineering":
        return data.ENG
    elif faculty == "Science":
        return data.SCI
    elif faculty == "Math":
        return data.MATH
    elif faculty == "Arts":
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

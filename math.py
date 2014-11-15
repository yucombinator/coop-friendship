import logic
import data
import datetime

def convert(program, stream = None):
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

convert();
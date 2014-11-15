from flask import Flask, render_template
import datetime
app = Flask(__name__)



eng = {"8": ["1A", "1B", "COOP1", "2A", "COOP2"], "4": ["1A", "COOP1", "1B", "COOP2"],
       "ARCH": ["1A", "1B", "OFF", "2A", "2B"]}

def compareArrays(array1, array2, term1 = "1A", term2 = "1A"):
    #SHIFTING THE ARRAYS
    shift1 = array1.index(term1)
    shift2 = array2.index(term1)

    #PRINTING STUFF
    results = []
    length = min(len(array1), len(array2))
    print (term1 ,term2)
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

    #Create array of terms.
    date = str(datetime.date.today()).split("-")
    for element in range (len(date)):
        date[element] = int(date[element])
    terms = []
    for index in range(length):
        currentTerm = str(date[0])
        if date[1] >= 1 and date[1] <= 4:
            currentTerm += "W"
        elif date[1] >= 5 and date[2] <= 8:
            currentTerm += "S"
        else:
            currentTerm += "F"
        terms.append(currentTerm)
        date[1]+= 4
        if date[1] > 12:
            date[0] += 1
            date[1] -= 12


    print(terms)
    print(array1)
    print(array2)
    print(results)


compareArrays(eng["8"], eng["ARCH"])

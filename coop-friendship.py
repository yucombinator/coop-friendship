from flask import Flask, render_template
import datetime
app = Flask(__name__)



eng = {"8": ["1A", "1B", "COOP1", "2A", "COOP2", "2B", "COOP3", "3A", "COOP4", "3B", "COOP5", "4A", "COOP6", "4B"],
       "4": ["1A", "COOP1", "1B", "COOP2","2A", "COOP3", "2B", "COOP4", "3A", "COOP5", "3B", "COOP6", "4A", "4B"],
       "ARCH": ["1A", "1B", "OFF", "2A", "COOP1", "2B", "COOP2", "3A", "COOP3", "3B", "COOP4", "COOP5", "4A", "COOP6", "4B"]}

def compareArrays(array1, array2, term1="1B", term2="1A"):
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

    #CREATE ARRAY OF TERMS
    #Keeping track of dates.
    date = str(datetime.date.today()).split("-")
    for element in range(len(date)):
        date[element] = int(date[element])

    #Append term to array
    terms = []
    for index in range(length + padding):
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


    print(terms)
    print(array1)
    print(array2)
    print(results)


compareArrays(eng["8"], eng["4"], "2A", "1A")

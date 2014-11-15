import data, datetime
def detFaculty(faculty):
    switch(s)

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

def compareArrays(array1, array2, term1="1A", term2="1A"):
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

results = compareArrays(data.ARTS["AFM1"], data.ENG["BIOMED"], "1A", "1A")
print (results)
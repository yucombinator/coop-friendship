import programs, datetime


def generateTerms(length):
    #CREATE ARRAY OF TERMS
    #Keeping track of dates.
    date = str(datetime.date.today()).split("-")
    for element in range(len(date)):
        date[element] = int(date[element])

    #Appendz term to array
    terms = []
    for index in range(length):
        currentTerm = ""
        if 1 <= date[1] <= 4:
            currentTerm = "Winter "
        elif 5 <= date[1] <= 8:
            currentTerm = "Spring "
        else:
            currentTerm = "Fall "
        currentTerm += str(date[0])
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
            results.append("No")
        elif ("COOP" in array1[index] or array1[index] == "OFF") and ("COOP" in array2[index] or array2[index] == "OFF"):
            results.append("Off Campus")
        else:
            results.append("Yes")

    #PAD "Mismatch" to the end.
    padding = abs(len(array1)-len(array2))
    for index in range(padding):
        results.append("Mismatch")

    terms = generateTerms(max(len(array1), len(array2)))

    return {"terms": terms,
            "array1": array1,
            "array2": array2,
            "results": results
    }

def takeInput(my_faculty, my_program, my_term, friend_faculty, friend_program, friend_term, my_stream_code, friend_stream_code):

    myProgram = programs.findProgram(my_faculty, my_program, my_stream_code)
    friendProgram = programs.findProgram(friend_faculty, friend_program, friend_stream_code)
    results = comparePrograms(myProgram, friendProgram, my_term, friend_term)
    print (results)
    return results

#takeInput("engineering", "Software Engineering", "1A", "arts", "English", "1A", None, None)


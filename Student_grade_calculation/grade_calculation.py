def calculate_note(line):
    line = line[:-1]
    parts = line.split(":")
    
    if len(parts) != 2:
        return "Invalid format"
    
    studentName = parts[0]
    notes_str = parts[1].strip()
    notes = notes_str.split(',')
    
    if len(notes) != 3:
        return "Invalid notes format"
    
    try:
        note1 = int(notes[0])
        note2 = int(notes[1])
        note3 = int(notes[2])
        
        average = (note1 + note2 + note3) / 3
        
        if average >= 90 and average <= 100:
            char = "AA"
        elif average >= 85 and average <= 89:
            char ="BA"
        elif average >= 80 and average <= 84:
            char = "BB"
        elif average >= 75 and average <= 79:
            char = "CB"
        elif average >= 70 and average <= 74:
            char = "CC"
        elif average >= 65 and average <= 69:
            char = "DC"
        elif average >= 60 and average <= 64:
            char = "DD"
        elif average >= 50 and average <= 59:
            char = "FD"
        elif average < 49:
            char = "FF"
        else:
            print("Invalid note")
        return f"{studentName}: Average: {average:.2f}, Char Note: {char}\n"
        
    except ValueError:
        return "Invalid note values"
        
 # return studentName + ": " + char + "\n"
def readNotes():
    with open("quiz_notes.txt","r",encoding="UTF-8") as file:
        for line in file:
            print(calculate_note(line))

def writeNotes():
    fname = input("Student first name: ")
    lname = input("Student last name: ")
    n1 = input("Student note 1: ")
    n2 = input("Student note 2: ")
    n3 = input("Student note 3: ")
    with open("quiz_notes.txt","a",encoding="UTF-8") as file:
        file.write(fname+' '+lname+":"+n1+','+n2+','+n3+'\n')

      

def saveNotes():
    with open("quiz_notes.txt","r",encoding="UTF-8") as file:
        result_list = []
        for line in file:
            result = calculate_note(line)
            result_list.append(result)
            
        with open("results.txt","w",encoding="UTF-8") as file2:
            for item in result_list:
                file2.write(item)
            
            
            

    



while True:
    menu = input("1- Read Notes \n2- Write Notes\n3- Save Note\n4- Exit\n")
    
    if menu == "1":
        readNotes()
    elif menu == "2":
        writeNotes()
    elif menu == "3":
        saveNotes()
    elif menu == "4":
        print("Power off")
        break
    else:
        print("Invalid enter")
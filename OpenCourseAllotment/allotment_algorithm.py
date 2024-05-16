import csv

def allotStudents(file):
    """Input a csv of all students and their choices, allots them to classes"""
    
    classes = {
        "Malayalam": 4,
        "English": 4,
        "Hindi": 4,
        "Tamil": 4,
        "Physics": 4,
        "Chemistry": 4,
        "Botany": 4,
        "Zoology": 4,
        "Mathematics": 4,
        "Economics": 4,
        "History": 4,
        "Philosophy": 4
    }
    # Read the file and store the data as a list of dictionaries
    students = []
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            name, admn_no, percentage, c1, c2, c3, c4, c5 = row[0], row[1], row[2], row[3].strip(), row[4].strip(), row[5].strip(), row[6].strip(), row[7].strip()
            student  = {"name": name, "admn_no": admn_no, "percentage": percentage, "choices": [c1, c2, c3, c4, c5]}
            students.append(student)

    # Sort the students according to their percentage
    students.sort(key=lambda x: x["percentage"], reverse = True)
    
    # Allot the students to their choices
    allotment = {}
    for student in students:
        for choice in student["choices"]:
            if classes[choice] > 0:
                classes[choice] -= 1
                print(f"{student['name']} ({student['admn_no']}) allotted to {choice}")
                allotment[choice] = allotment.get(choice, []) + [(student['name'], student['admn_no'])]
                break
            else:
                print(f"{student['name']} ({student['admn_no']}) not allotted to {choice}")
        
    return allotment
            

if __name__ == "__main__":
    print(allotStudents("file.txt"))
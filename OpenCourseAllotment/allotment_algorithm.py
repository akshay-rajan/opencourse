import csv

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

def allotStudents(file):
    """Input a csv of all students and their choices, allots them to classes"""
    
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    
    return {}
            

if __name__ == "__main__":
    allotStudents("file.txt")
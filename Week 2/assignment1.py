#code used to load in the csv file
file_path = input("Enter the path to the CSV file: ")
records = []
with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        records.append(row)

#function return the average grade of all students from the input list
def avg_grade(inpt):
    total = sum(float(record['Grade']) for record in inpt)
    return total / len(records)

def avg_grade_print(inpt):
    print(f"Average Grade: {inpt}")
    print("--------------------")

#function return a list of all students who achieved a grade higher then 80.0
def starstudents(inpt):
    return [item for item in inpt if float(item['Grade']) >= 80.0]

#function prints the name and grade of all students in the input list
def student_report_print(inpt):
    print("Student Report")
    print("--------------")
    for record in inpt:
        print(f"Name: {record['Name']}")
        print(f"Grade: {record['Grade']}")
        print("--------------------")

#helps find the desired values in the records to be found
filtered_records = starstudents(records)
average = avg_grade(records)

#prints the desired values
avg_grade_print(average)
student_report_print(filtered_records)
# data_analysis.py (basic analysis script)

import os

# load the student data from the csv file
def load_students(filename='data/students.csv'):
    with open(filename, 'r') as f:
        lines = f.readlines()[1:]
    students = [line.strip().split(',') for line in lines]
    return students

# calculate the average grades
def calculate_average_grade(students):
    grades = [int(s[2]) for s in students]
    return sum(grades) / len(grades)

# count how many students are in math
def count_math_students(students):
    return sum(1 for s in students if s[3].strip() == 'math')

# create a report with total, average, and math count
def generate_report(students):
    total = len(students)  # number of rows
    avg = calculate_average_grade(students)  # average grade
    math_count = count_math_students(students)  # math count

    report = (
        f"total students: {total}\n"
        f"average grade: {avg:.1f}\n"  # one decimal place
        f"math students: {math_count}\n"
    )
    return report

# save the report to a text file
def save_report(report, filename='output/basic_analysis_report.txt'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f: 
        f.write("basic analysis report\n")
        f.write(report)

# main function that runs everything in order
def main():
    students = load_students('data/students.csv')
    report = generate_report(students)
    save_report(report, 'output/basic_analysis_report.txt')
    print("basic analysis complete. report saved to output/basic_analysis_report.txt")

# only run main if this file is executed directly
if __name__ == '__main__':
    main()

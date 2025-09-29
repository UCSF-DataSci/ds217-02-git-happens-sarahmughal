# data_analysis.py
import os

def load_students(filename):
    with open(filename, "r") as f:
        lines = f.readlines()[1:]  # skip header
    students = [line.strip().split(",") for line in lines]
    return students

def calculate_average_grade(students):
    grades = [int(s[2]) for s in students]
    return sum(grades) / len(grades)

def count_math_students(students):
    return sum(1 for s in students if s[3].strip() == "math")

def generate_report(students):
    total = len(students)
    avg = calculate_average_grade(students)
    math_count = count_math_students(students)

    report = (
        f"Total students: {total}\n"
        f"Average grade: {avg:.1f}\n"
        f"Math students: {math_count}\n"
    )
    return report

def save_report(report, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(report)

def main():
    students = load_students("data/students.csv")
    report = generate_report(students)
    save_report(report, "output/analysis_report.txt")
    print("basic analysis complete. report saved to output/analysis_report.txt")

if __name__ == "__main__":
    main()
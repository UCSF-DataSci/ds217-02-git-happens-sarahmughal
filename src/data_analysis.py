# data_analysis.py (basic analysis script)

# load csv data, skip header row
def load_students(filename="data/students.csv"):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()[1:]
    return [line.strip().split(",") for line in lines]


# calculate average grade
def calculate_average_grade(students):
    grades = [int(s[2]) for s in students]
    return sum(grades) / len(grades)


# count how many students take math
def count_math_students(students):
    return sum(1 for s in students if s[3].strip().lower() == "math")


# create a simple report string
def generate_report(students):
    total = len(students)
    avg = calculate_average_grade(students)
    math_count = count_math_students(students)

    report = []
    report.append("basic analysis report")
    report.append(f"total students: {total}")
    report.append(f"average grade: {avg:.1f}")
    report.append(f"math students: {math_count}")
    return "\n".join(report)


# save report to output file
def save_report(report, filename="output/analysis_report.txt"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report + "\n")
    print(f"report saved to {filename}")


# main workflow
def main():
    students = load_students()
    report = generate_report(students)
    save_report(report)


if __name__ == "__main__":
    main()

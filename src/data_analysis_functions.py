# data_analysis_functions.py
import os

def load_data(filename):
    if filename.endswith(".csv"):
        return load_csv(filename)
    else:
        raise ValueError("unsupported file format")

def load_csv(filename):
    with open(filename, "r") as f:
        lines = f.readlines()[1:]  # skip header
    students = [line.strip().split(",") for line in lines]
    return students

def analyze_data(students):
    grades = [int(s[2]) for s in students]
    subjects = {}
    for s in students:
        subj = s[3].strip()
        subjects[subj] = subjects.get(subj, 0) + 1

    return {
        "total": len(students),
        "average": sum(grades) / len(grades),
        "highest": max(grades),
        "lowest": min(grades),
        "subjects": subjects,
        "distribution": analyze_grade_distribution(grades),
    }

def analyze_grade_distribution(grades):
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for g in grades:
        if g >= 90:
            dist["A"] += 1
        elif g >= 80:
            dist["B"] += 1
        elif g >= 70:
            dist["C"] += 1
        elif g >= 60:
            dist["D"] += 1
        else:
            dist["F"] += 1
    total = len(grades)
    return {k: f"{v} ({(v/total)*100:.1f}%)" for k, v in dist.items()}

def save_results(results, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write("Detailed Analysis Report\n")
        f.write(f"Total students: {results['total']}\n")
        f.write(f"Average grade: {results['average']:.1f}\n")
        f.write(f"Highest grade: {results['highest']}\n")
        f.write(f"Lowest grade: {results['lowest']}\n")
        f.write("\nStudents by subject:\n")
        for subj, count in results["subjects"].items():
            f.write(f"- {subj}: {count}\n")
        f.write("\nGrade distribution:\n")
        for grade, val in results["distribution"].items():
            f.write(f"- {grade}: {val}\n")

def main():
    students = load_data("data/students.csv")
    results = analyze_data(students)
    save_results(results, "output/advanced_analysis_report.txt")
    print("advanced analysis complete. report saved to output/analysis_report.txt")

if __name__ == "__main__":
    main()

# data_analysis_functions.py (advanced analysis script)

import os

# check file type
def load_data(filename='data/students.csv'):
    if filename.endswith('.csv'):
        return load_csv(filename)
    else:
        raise ValueError('unsupported file format')

# load csv data just like the basic script
def load_csv(filename='data/students.csv'):
    with open(filename, 'r') as f:
        lines = f.readlines()[1:] 
    students = [line.strip().split(',') for line in lines]
    return students

# analyze student data and return results in a dictionary
def analyze_data(students):
    grades = [int(s[2]) for s in students]  # all grades as integers

    # calculate average, highest, and lowest
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)

    # count students by subject
    subjects = {}
    for s in students:
        subject = s[3].strip()
        if subject in subjects:
            subjects[subject] += 1
        else:
            subjects[subject] = 1

    # get grade distribution (a, b, c, d, f)
    distribution = analyze_grade_distribution(grades)

    # store everything in a dictionary
    results = {
        'total': len(students),
        'average': average,
        'highest': highest,
        'lowest': lowest,
        'subjects': subjects,
        'distribution': distribution
    }
    return results

# make grade distribution with counts and percentages
def analyze_grade_distribution(grades):
    dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for g in grades:
        if g >= 90:
            dist['A'] += 1
        elif g >= 80:
            dist['B'] += 1
        elif g >= 70:
            dist['C'] += 1
        elif g >= 60:
            dist['D'] += 1
        else:
            dist['F'] += 1
    return dist

# save the advanced analysis results to a file
def save_results(results, filename='output/advanced_analysis_report.txt'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)  
    with open(filename, 'w') as f: 
        f.write("advanced analysis report\n")
        f.write(f"total students: {results['total']}\n")
        f.write(f"average grade: {results['average']:.1f}\n")
        f.write(f"highest grade: {results['highest']}\n")
        f.write(f"lowest grade: {results['lowest']}\n")

        f.write("\nstudents by subject:\n")
        for subject, count in results['subjects'].items():
            f.write(f"- {subject}: {count}\n")

        f.write("\ngrade distribution:\n")
        total = results['total']
        for grade, count in results['distribution'].items():
            percent = (count / total) * 100
            f.write(f"- {grade}: {count} ({percent:.1f}%)\n")

    print(f"results saved to {filename}")

# main function to run the whole workflow
def main():
    students = load_data('data/students.csv')
    results = analyze_data(students)
    save_results(results, 'output/advanced_analysis_report.txt')

# only run main if this file is executed directly
if __name__ == '__main__':
    main()

import random
import numpy as np
import matplotlib.pyplot as plt

# ---------- Step 1: Generate Random Data ----------
def generate_student_data(n=10):
    students = []
    subjects = ["Math", "Physics", "Chemistry", "English", "CS"]

    for i in range(1, n+1):
        student = {
            "Name": f"Student_{i}",
            "Marks": {sub: random.randint(40, 100) for sub in subjects},
            "Attendance": random.randint(60, 100)  # percentage
        }
        students.append(student)
    return students, subjects

# ---------- Step 2: Analyze Data ----------
def analyze_students(students, subjects):
    print("\nStudent Performance Analysis:")

    # Average per subject
    print("\nAverage Marks per Subject:")
    for sub in subjects:
        avg = np.mean([s["Marks"][sub] for s in students])
        print(f" - {sub}: {avg:.2f}")

    # Top 3 students by total marks
    totals = [(s["Name"], sum(s["Marks"].values())) for s in students]
    top_students = sorted(totals, key=lambda x: x[1], reverse=True)[:3]
    print("\nTop 3 Students:")
    for name, score in top_students:
        print(f" - {name}: {score} marks")

    # Correlation between attendance and average marks
    avg_marks = [np.mean(list(s["Marks"].values())) for s in students]
    attendance = [s["Attendance"] for s in students]
    correlation = np.corrcoef(attendance, avg_marks)[0,1]
    print(f"\n Correlation (Attendance vs Marks): {correlation:.2f}")

    return avg_marks, attendance, top_students

# ---------- Step 3: Visualize ----------
def visualize_data(students, subjects, avg_marks, attendance):
    # 1. Average marks per subject
    plt.figure(figsize=(12,4))

    plt.subplot(1,3,1)
    subject_avgs = [np.mean([s["Marks"][sub] for s in students]) for sub in subjects]
    plt.bar(subjects, subject_avgs, color="skyblue")
    plt.title("Average Marks per Subject")
    plt.ylabel("Marks")

    # 2. Attendance vs Average Marks
    plt.subplot(1,3,2)
    plt.scatter(attendance, avg_marks, color="red")
    plt.title("Attendance vs Marks")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Average Marks")

    # 3. Marks distribution of one student
    plt.subplot(1,3,3)
    student = random.choice(students)
    plt.bar(student["Marks"].keys(), student["Marks"].values(), color="green")
    plt.title(f"Marks of {student['Name']}")
    plt.ylabel("Marks")

    plt.tight_layout()
    plt.show()

# ---------- Step 4: Main ----------
def main():
    students, subjects = generate_student_data(15)
    avg_marks, attendance, top_students = analyze_students(students, subjects)
    visualize_data(students, subjects, avg_marks, attendance)

if __name__ == "__main__":

    main()

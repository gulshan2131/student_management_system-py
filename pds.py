import math
import numpy as np
import pandas as pd
from scipy import stats
from bs4 import BeautifulSoup

# 1. Libraries / Environment
def practical1():
    print("Python Environment Ready")
    print("NumPy, Pandas, SciPy, Seaborn, Plotly installed")


# 2. Student Details
def practical2():
    r = input("Roll No: ")
    n = input("Name: ")
    b = input("Branch: ")
    s = input("Semester: ")
    e = input("Email: ")
    m = input("Mobile: ")

    print("\nStudent Details:")
    print(r, n, b, s, e, m)


# 3. Marks, Percentage, Grade
def practical3():
    marks = [float(input(f"Subject {i+1}: ")) for i in range(5)]

    total = sum(marks)
    per = total / 5

    if per >= 90:
        grade = "A"
    elif per >= 80:
        grade = "B"
    elif per >= 70:
        grade = "C"
    elif per >= 40:
        grade = "D"
    else:
        grade = "F"

    print("Total:", total)
    print("Percentage:", per)
    print("Grade:", grade)
    print("Status:", "Pass" if per >= 40 else "Fail")


# 4. Membership and Bitwise Operators
def practical4():
    club = input("Club: ")
    hostel = input("Hostel Required (Yes/No): ")

    clubs = ["Coding", "Robotics", "Sports", "Music"]

    print("Club Eligible:", club in clubs)

    lib, lab, host = 1, 2, 4

    if hostel.lower() == "yes":
        permission = lib | lab | host
    else:
        permission = lib | lab

    print("Permission Code:", permission)
    print("Library:", bool(permission & lib))
    print("Laboratory:", bool(permission & lab))
    print("Hostel:", bool(permission & host))


# 5. Data Structures
def practical5():
    subjects = ["Python", "DBMS", "OS"]
    semesters = (3, 4, 5)
    clubs = {"Coding", "Sports"}
    student = {"Roll": 101, "Branch": "CE"}
    marks = np.array([75, 80, 70])
    name = "Neel"

    subjects.append("AI")
    clubs.add("Music")
    student["Roll"] = 102

    print("Subjects:", subjects)
    print("Semesters:", semesters)
    print("Clubs:", clubs)
    print("Student:", student)
    print("Marks:", marks)
    print("Name:", name)


# 6. Attendance Function
def practical6():
    a = [
        int(input(f"Day {i+1} (1=Present, 0=Absent): "))
        for i in range(5)
    ]

    def attendance(x):
        return sum(x) / len(x) * 100

    p = attendance(a)

    print("Attendance:", p)
    print("Rounded Up:", math.ceil(p))


# 7. Pickle / Exception
def practical7():
    import pickle

    data = {
        "Roll": 101,
        "Name": "Neel"
    }

    try:
        with open("student.dat", "wb") as f:
            pickle.dump(data, f)

        with open("student.dat", "rb") as f:
            print("Record:", pickle.load(f))

    except Exception as e:
        print("Error:", e)


# 8. Text File CRUD
def practical8():
    file = "student.txt"

    r = input("Roll: ")
    n = input("Name: ")

    with open(file, "a") as f:
        f.write(r + "," + n + "\n")

    print("\nRecords:")

    with open(file) as f:
        data = f.readlines()
        print("".join(data))

    search = input("Search Roll: ")

    print(
        "Found:",
        any(x.startswith(search + ",") for x in data)
    )


# 9. CSV File CRUD
def practical9():
    import csv

    file = "student.csv"

    r = input("Roll: ")
    n = input("Name: ")

    with open(file, "a", newline="") as f:
        csv.writer(f).writerow([r, n])

    with open(file) as f:
        rows = list(csv.reader(f))

    print("Records:", rows)

    search = input("Search Roll: ")

    print(
        [x for x in rows if x[0] == search]
    )


# 10. MySQL CRUD
def practical10():
    try:
        import mysql.connector

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="college"
        )

        c = db.cursor()

        c.execute("""
            CREATE TABLE IF NOT EXISTS student (
                roll INT,
                name VARCHAR(30)
            )
        """)

        c.execute(
            "INSERT INTO student VALUES(101, 'Neel')"
        )

        db.commit()

        c.execute("SELECT * FROM student")

        print("Records:", c.fetchall())

        c.execute(
            "UPDATE student SET name='ABC' WHERE roll=101"
        )

        c.execute(
            "DELETE FROM student WHERE roll=101"
        )

        db.commit()
        db.close()

        print("MySQL CRUD completed.")

    except Exception as e:
        print("MySQL Error:", e)


# 11. NumPy Marks
def practical11():
    a = np.array([70, 80, 60, 90, 75])

    print("Marks:", a)
    print("Total:", np.sum(a))
    print("Percentage:", np.mean(a))
    print(
        "Percentile of 75:",
        stats.percentileofscore(a, 75)
    )


# 12. SciPy Statistics
def practical12():
    a = np.array([50, 60, 70, 70, 80, 90])

    print("Mean:", np.mean(a))
    print("Median:", np.median(a))
    print(
        "Mode:",
        stats.mode(a, keepdims=True).mode[0]
    )
    print("Std:", np.std(a))
    print("Variance:", np.var(a))
    print("Skewness:", stats.skew(a))
    print("Kurtosis:", stats.kurtosis(a))

    ci = stats.t.interval(
        0.95,
        len(a) - 1,
        loc=np.mean(a),
        scale=stats.sem(a)
    )

    print("Confidence Interval:", ci)


# 13. Pandas Statistics
def practical13():
    df = pd.DataFrame({
        "Python": [70, 80, 60, 90, 75],
        "DBMS": [65, 75, 70, 85, 80]
    })

    print("Data:")
    print(df)

    print("\nMean:")
    print(df.mean())

    print("\nMedian:")
    print(df.median())

    print("\nMode:")
    print(df.mode().iloc[0])

    print("\nStandard Deviation:")
    print(df.std())

    print("\nVariance:")
    print(df.var())

    print("\nSkewness:")
    print(df.skew())


# 14. BeautifulSoup + Pandas Merge
def practical14():
    html = """
    <table>
        <tr><th>Roll</th><th>Name</th></tr>
        <tr><td>101</td><td>Neel</td></tr>
        <tr><td>102</td><td>Rahul</td></tr>
    </table>
    """

    soup = BeautifulSoup(html, "html.parser")

    rows = soup.find_all("tr")[1:]

    info = [
        [
            r.find_all("td")[0].text,
            r.find_all("td")[1].text
        ]
        for r in rows
    ]

    students = pd.DataFrame(
        info,
        columns=["Roll", "Name"]
    )

    marks = pd.DataFrame({
        "Roll": ["101", "102"],
        "Marks": [80, 75]
    })

    print("Merged Data:")

    print(
        pd.merge(
            students,
            marks,
            on="Roll"
        )
    )


# 15. Interactive Data Visualization using Plotly
def practical15():
    import plotly.express as px

    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Sales": [100, 150, 130, 180, 220]
    }

    fig = px.line(
        data,
        x="Month",
        y="Sales",
        title="Monthly Sales"
    )

    fig.show()


functions = {
    1: practical1,
    2: practical2,
    3: practical3,
    4: practical4,
    5: practical5,
    6: practical6,
    7: practical7,
    8: practical8,
    9: practical9,
    10: practical10,
    11: practical11,
    12: practical12,
    13: practical13,
    14: practical14,
    15: practical15
}


while True:

    print("\n========== PDS PRACTICALS ==========")

    print("1. Libraries / Environment")
    print("2. Student Details")
    print("3. Marks, Percentage and Grade")
    print("4. Membership and Bitwise Operators")
    print("5. Data Structures")
    print("6. Attendance")
    print("7. Pickle / Exception")
    print("8. Text File CRUD")
    print("9. CSV File CRUD")
    print("10. MySQL CRUD")
    print("11. NumPy Marks")
    print("12. SciPy Statistics")
    print("13. Pandas Statistics")
    print("14. BeautifulSoup + Pandas")
    print("15. Interactive Data Visualization using Plotly")
    print("0. Exit")

    try:

        ch = int(input("\nEnter your choice: "))

        if ch == 0:
            print("Program Ended")
            break

        if ch in functions:
            functions[ch]()

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please enter a valid number.")

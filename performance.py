import mysql.connector as myconn

mydb = myconn.connect(
    host="localhost",
    user="root",
    password="A@y@n#786",
    database="Tracker"
)

cursor = mydb.cursor()


# ---------- Attendance Insert (Teacher) ----------
def attendance():
    user_id = int(input("Enter Student User ID: "))
    date = input("Enter date (YYYY-MM-DD): ")
    status = input("Enter status (Present/Absent): ")

    query = "INSERT INTO attendance (user_id, date, status) VALUES (%s, %s, %s)"
    cursor.execute(query, (user_id, date, status))
    mydb.commit()

    print("Attendance added successfully\n")


# ---------- Performance Insert (Teacher) ----------
def performance():
    user_id = int(input("Enter Student User ID: "))
    score = int(input("Enter score (0-100): "))

    query = "INSERT INTO performance (user_id, score) VALUES (%s, %s)"
    cursor.execute(query, (user_id, score))
    mydb.commit()

    print("Performance added successfully\n")


# ---------- View Attendance ----------
def view_attendance(user_id):
    cursor.execute(
        "SELECT date, status FROM attendance WHERE user_id=%s",
        (user_id,)
    )

    records = cursor.fetchall()

    print("\nAttendance Records:")
    for r in records:
        print("Date:", r[0], "| Status:", r[1])
    print()


# ---------- View Performance ----------
def view_performance(user_id):
    cursor.execute(
        "SELECT score FROM performance WHERE user_id=%s",
        (user_id,)
    )

    records = cursor.fetchall()

    print("\nPerformance Records:")
    for r in records:
        print("Score:", r[0])
    print()


# ---------- Teacher Menu ----------
def teacher_menu():
    while True:
        print("\n--- Teacher Menu ---")
        print("1. Add Attendance")
        print("2. Add Performance")
        print("3. View Student Attendance")
        print("4. View Student Performance")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            attendance()
        elif choice == "2":
            performance()
        elif choice == "3":
            uid = int(input("Enter Student User ID: "))
            view_attendance(uid)
        elif choice == "4":
            uid = int(input("Enter Student User ID: "))
            view_performance(uid)
        elif choice == "5":
            break
        else:
            print("Invalid choice\n")


# ---------- Student Menu ----------
def student_menu():
    user_id = int(input("Enter your User ID: "))

    while True:
        print("\n--- Student Menu ---")
        print("1. View My Attendance")
        print("2. View My Performance")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            view_attendance(user_id)
        elif choice == "2":
            view_performance(user_id)
        elif choice == "3":
            break
        else:
            print("Invalid choice\n")


# ---------- Main Role Menu ----------
def main_menu():
    while True:
        print("\n==== College Tracker System ====")
        print("1. Teacher Login")
        print("2. Student Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            teacher_menu()
        elif choice == "2":
            student_menu()
        elif choice == "3":
            print("Exiting system...")
            break
        else:
            print("Invalid choice\n")


# ---------- Start Program ----------
main_menu()

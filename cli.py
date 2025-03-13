import student, course, enrollment

def main_menu():
    while True:
        print("\n🎓 Student-Course Enrollment System")
        print("1️⃣  ➕ Add Student")
        print("2️⃣  ❌ Remove Student")
        print("3️⃣  👥 View Students")
        print("4️⃣  🔍 Find Student")
        print("5️⃣  📚➕ Add Course")
        print("6️⃣  🗑️ Remove Course")
        print("7️⃣  📖 View Courses")
        print("8️⃣  🔎 Find Course")
        print("9️⃣  📝 Enroll Student")
        print("🔟  📤 Drop Course")
        print("11  📖 View Enrollments")
        print("0️⃣  🚪 Exit")


        choice = input("Enter your choice: ")

        if choice == "1":
            student.add_student(input("Name: "), input("Email: "), input("Phone: "))
        elif choice == "2":
            student.remove_student(int(input("Student ID: ")))
        elif choice == "3":
            student.view_students()
        elif choice == "4":
            student.find_student(input("Name or Email: "))
        elif choice == "5":
            course.add_course(input("Course Name: "), int(input("Credits: ")))
        elif choice == "6":
            course.remove_course(int(input("Course ID: ")))
        elif choice == "7":
            course.view_courses()
        elif choice == "8":
            course.find_course(input("Name or Code: "))
        elif choice == "9":
            enrollment.enroll_student(int(input("Student ID: ")), int(input("Course ID: ")))
        elif choice == "10":
            enrollment.drop_course(int(input("Student ID: ")), int(input("Course ID: ")))
        elif choice == "0":
            break

if __name__ == "__main__":
    main_menu()

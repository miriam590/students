from models import session, Student

def add_student(name, email, phone):
    student = Student(name=name, email=email, phone=phone)
    session.add(student)
    session.commit()
    print(f"Student {name} added successfully!")

def remove_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Student {student.name} removed successfully!")
    else:
        print("Student not found.")

def view_students():
    students = session.query(Student).all()
    for student in students:
        print(student)

def find_student(identifier):
    student = session.query(Student).filter((Student.name == identifier) | (Student.email == identifier)).first()
    if student:
        print(student)
    else:
        print("Student not found.")

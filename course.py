import random
from models import session, Course

def generate_course_code(name):
    return name[:2].upper() + str(random.randint(100, 999))

def add_course(name, credits):
    course_code = generate_course_code(name)
    course = Course(name=name, course_code=course_code, credits=credits)
    session.add(course)
    session.commit()
    print(f"Course {name} added successfully with code {course_code}!")

def remove_course(course_id):
    course = session.query(Course).filter_by(id=course_id).first()
    if course:
        session.delete(course)
        session.commit()
        print(f"Course {course.name} removed successfully!")
    else:
        print("Course not found.")

def view_courses():
    courses = session.query(Course).all()
    if not courses:
        print("No courses found!.")
    else:
        for course in courses:
            print(f"{course.name} - {course.course_code}")

      
        

def find_course(identifier):
    course = session.query(Course).filter((Course.name == identifier) | (Course.course_code == identifier)).first()
    if course:
        print(course)
    else:
        print("Course not found.")

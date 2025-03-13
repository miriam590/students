from models import session, Course

def seed_data():
    # Check if there are already courses in the database
    existing_courses = session.query(Course).all()
    if existing_courses:
        print("Courses already exist in the database. Seeding skipped.")
        return

    # Sample courses to add with course codes
    courses = [
        Course(name="Introduction to Programming", course_code="CS101", credits=3),
        Course(name="Data Structures", course_code="CS102", credits=4),
        Course(name="Web Development", course_code="CS103", credits=3),
        Course(name="Database Management", course_code="CS104", credits=3),
        Course(name="Software Engineering", course_code="CS105", credits=4)
    ]
    
    # Add courses to the session
    session.add_all(courses)
    session.commit()
    print("Seed data added successfully!")

if __name__ == "__main__":
    try:
        seed_data()
    except Exception as e:
        print(f"An error occurred while seeding data: {e}")

from models import session, Enrollment, Student, Course

def enroll_student(student_id, course_id):
    """Enrolls a student in a course if not already enrolled."""
    student = session.query(Student).get(student_id)
    course = session.query(Course).get(course_id)

    if not student or not course:
        print("❌ Invalid Student ID or Course ID. Please check and try again.")
        return

    existing_enrollment = session.query(Enrollment).filter_by(student_id=student_id, course_id=course_id).first()
    if existing_enrollment:
        print(f"⚠️ {student.name} is already enrolled in {course.name}.")
        return

    enrollment = Enrollment(student_id=student_id, course_id=course_id, status="Enrolled")
    session.add(enrollment)
    session.commit()
    print(f"✅ {student.name} successfully enrolled in {course.name}!")

def drop_course(student_id, course_id):
    """Removes a student’s enrollment from a course."""
    student = session.query(Student).get(student_id)
    course = session.query(Course).get(course_id)

    if not student or not course:
        print("❌ Invalid Student ID or Course ID. Please check and try again.")
        return

    enrollment = session.query(Enrollment).filter_by(student_id=student_id, course_id=course_id).first()
    if enrollment:
        session.delete(enrollment)
        session.commit()
        print(f"✅ {student.name} successfully dropped {course.name}.")
    else:
        print(f"⚠️ {student.name} is not enrolled in {course.name}.")

def view_enrollments():
    """Displays all student-course enrollments."""
    enrollments = session.query(Enrollment).all()
    if not enrollments:
        print("📭 No enrollments found.")
        return

    print("📜 Student Enrollment List:")
    for enrollment in enrollments:
        student = session.query(Student).get(enrollment.student_id)
        course = session.query(Course).get(enrollment.course_id)
        print(f"🎓 {student.name} → 📚 {course.name} | Status: {enrollment.status}")

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# 📌 Database setup
DATABASE_URL = "sqlite:///enrollment.db"
engine = create_engine(DATABASE_URL, echo=True)  # Set echo=False in production
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# 🎓 Student Model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)

    # Relationship with Enrollment
    enrollments = relationship("Enrollment", back_populates="student", cascade="all, delete")

    def __repr__(self):
        return f"👤 Student(ID={self.id}, Name={self.name}, Email={self.email})"

# 📚 Course Model
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    course_code = Column(String, unique=True, nullable=False)
    credits = Column(Integer, nullable=False)

    # Relationship with Enrollment
    enrollments = relationship("Enrollment", back_populates="course", cascade="all, delete")

    def __repr__(self):
        return f"📖 Course(ID={self.id}, Name={self.name}, Code={self.course_code}, Credits={self.credits})"

# ✅ Enrollment Model (Many-to-Many Link)
class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id', ondelete="CASCADE"), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id', ondelete="CASCADE"), nullable=False)
    status = Column(String, default="Enrolled")

    # Relationships
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

    def __repr__(self):
        return f"✅ Enrollment(Student_ID={self.student_id}, Course_ID={self.course_id}, Status={self.status})"

# 🚀 Initialize Database
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("✅ Database tables created successfully!")

# 🎓 Student Enrollment System

Welcome to the **Student Enrollment System**:
This command-line application is designed to make managing students and courses a breeze. Whether you're an administrator, a teacher, or just someone passionate about education, this system helps you keep everything organized and efficient.

## What is This System All About?
The Student Enrollment System is your go-to tool for managing students, courses, and enrollments. With a straightforward interface, you can easily add, remove, view, and find students and courses as well as enroll students in their desired classes.

## Key Features
Here is what you can do with the Student Enrollment System:

### Student Management
- **Create**: Add new students to the system with just a few details.
- **Read**: View all your students or search for a specific student by name or email.
- **Update**: Modify a student's information whenever necessary.
- **Delete**: Easily remove students who are no longer enrolled.

### Course Management
- **Create**: Add new courses to your offerings.
- **Read**: View all available courses or search for a specific one by name or code.
- **Update**: Modify course details as needed, ensuring your offerings are always up to date.
- **Delete**: Remove courses that are no longer being offered.

### Enrollment Management
- Enroll students in courses and drop them from courses as needed, making it easy to keep track of who is taking what.

### View Enrollments
- Get a comprehensive list of all student enrollments to see who is taking which courses at a glance.

## How Does the Database Work?
The system uses a SQLite database to store all the important information about students, courses, and enrollments. Here’s a quick overview of the models:
- **Student**: Each student has a name, email, and phone number.
- **Course**: Each course has a name, a unique course code, and the number of credits it offers.
- **Enrollment**: This model links students to the courses they are enrolled in, allowing for easy tracking of their academic progress.

## Getting Started
 Here is  how to set up the Student Enrollment System on your machine:
1. **Clone the repository**:
   ```bash
   git clone <git@github.com:miriam590/students.git>
   ```
2. **Navigate to the project directory**:
   ```bash
   cd Student_course
   ```
3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the System
To run the application, simply execute the following command in your terminal:
```bash
python cli.py
```
Follow the on-screen prompts to navigate through the menu and manage students and courses effortlessly. 

##  Contributions
If you have suggestions for improvements or would like to add new features, please feel free to submit a pull request .


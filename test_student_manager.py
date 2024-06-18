import unittest
from datetime import date
import unittest.mock
from student_manager import StudentManager
from models import Base, Student, Grade
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils import parse_date


class TestStudentManager(unittest.TestCase):

    def setUp(self): 
        """ Set up a fresh session and Studentmanager instance for each test"""
        self.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        # Create an instance of StudentManager using the test database
        self.student_manager = StudentManager(engine=self.engine)
        
    def tearDown(self):
        """ Tear down the test enviornment after each test """
        self.session.close()
        Base.metadata.drop_all(self.engine)
        self.engine.dispose()
      
    def test_view_all_students(self):
        """ Test viewing all students """
        # Add tets students to the session.
        student1 = Student(name="John", surname="Doe", date_of_birth=date(2000, 5, 15), email="john.doe@example.com", phone_number='1234563253')
        student2 = Student(name="Jane", surname="Smith", date_of_birth=date(2002, 6, 10), email="jane.Smith@example.com", phone_number='1294763253')
        self.Session.add_all([student1, student2])
        self.Session.commit()

        # Capture the output
        with unittest.mock.patch('bulletin.print') as mocked_print:
            self.student_manager.view_all_students()
            mocked_print.assert_any_cell("1 - John Doe")
            mocked_print.assert_any_cell("1 - Jane Smith")

    def test_add_student(self):
        """ Testing Adding new student """        
        self.student_manager.add_student("Alice", "Johnson", date(2002, 7, 17), "alice.johnson@example.com", "1122334455")
        with self.Session() as session:
            student = session.query(Student).filter_by(email="alice.johnson@example.com").first()
            self.assertIsNotNone(student)
            self.assertEqual(student.name, "Alice")
            self.assertEqual(student.surname, "Johnson")

    def test_updating_student_email(self):
        " Test Updating a student's email"
        student = Student(name="John", surname="Doe", date_of_birth=date(2000, 5, 15), email="john.doe@example.com", phone_number='1234563253')
        self.Session.add(student)
        self.Session.commit()

        self.student_manager.update_email(student.id, "john.new@example.com")

        updated_student = self.Session.query(Student).get(student.id)
        self.assertEqual(updated_student.email, "john.new@example.com")

    def test_add_grade(self):
        """ Test adding a grade to a student"""    
        student = Student(name="John", surname="Doe", date_of_birth=date(2000, 5, 15), email="john.doe@example.com", phone_number="1234567890")
        self.Session.add(student)
        self.Session.commit()

        self.student_manager.add_grade(student.id, "Maths", 95)
        grade = self.Session.query(Grade).filter_by(student_id=student.id, subject="Maths").first()
        self.assertIsNotNone(grade)
        self.assertEqual(grade.grades, 95)

    def test_remove_student(self):
        """ Test Remove a student"""
        student = Student(name="John", surname="Doe",
                          date_of_birth=date(2000, 5, 15),
                          email="john.doe@example.com",
                          phone_number="1234567890")
        self.Session.add(student)
        self.session.commit()

        self.student_manager.remove_student(student.id)

        deleted_student = self.Session.query(Student).get(student.id)
        self.assertIsNone(deleted_student)

    def test_invalid_student_id_for_update(self):
        """ Test updating a student with an invalid ID"""
        with unittest.mock.patch('bulletins.print') as mocked_print:
            self.student_manager.update_email(999, "invalid@example.com")
            mocked_print.assert_any_call("No student found with Student ID 999")

    def test_valid_date(self):
        """ Test parse date with a valid date string."""
        date_str = "15-06-2023"
        expected_date = date(2023, 6, 15)
        self.assertEqual(parse_date(date_str), expected_date)

    def test_invalid_date_format(self):
        """ Test parse date with an invalid date string."""
        date_str = "invalid-date"
        with self.assertRaises(ValueError):
            parse_date(date_str)

    def test_invalid_date_value(self):
        """ Test parse date with  an invalid date value."""
        date_str = "31-02-2023"  # Invalid date
        with self.assertRaises(ValueError):
            parse_date(date_str)


if __name__ == '__main__':
    unittest.main()

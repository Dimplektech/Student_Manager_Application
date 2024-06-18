from sqlalchemy import create_engine
import settings
from sqlalchemy.orm import sessionmaker
from models import Student, Grade


class StudentManager:

    def __init__(self, engine=None):
        """Initialize the StudentManager with database engine"""
        if engine:
            self.engine = engine
        else:    
            self.engine = create_engine(settings.DB_ADDRESS)  # Creare engine.
        self.Session = sessionmaker(bind=self.engine)
    
    #  we will use this engine to create sesssion
    @property
    def get_session(self):
        """
        Create and return a new session bound to the engine.
        """
        # Bind session with engine and create instance or object of class 
        # 'sessionmaker(bind=self.engine)'
        return self.Session()
    
    # You can define a setter if needed:
    @get_session.setter
    def get_session(self, value):
        # Optionally define a setter if you need to modify behavior
        pass
     
    def add_student(self, name, surname, date_of_birth, email, phone_number):
        """ Add a new student to the database.
        
            Args:
                name(str): The student's first name
                surname(str): The Student's last name
                Date_of_birth(date: The Student' date of birth
                email(str): The student's email address
                phone_number(str): The student's phone number)"""
        # Create a new  object of student
        new_student = Student(name=name,
                              surname=surname,
                              date_of_birth=date_of_birth,
                              email=email,
                              phone_number=phone_number
                              )
        # When we have a sesssion we neede to open session ,iteract with
        # database,and the close the session Like text file ( we  open it 
        # and close it at the end.
        with self.get_session as session:
            try:
                session.add(new_student)  # Add new student to the session.
                session.commit()  # Commit the transaction.
                print(f"Added student: {name} {surname}")
            except Exception as e:
                session.rollback()  # Rollback the transaction on error.
                print(f"Failed to add Student: {e}")
            finally:
                session.close()  # Ensure the session is closed.

    def remove_student(self, student_id):
        """Remove a Student from the database by ID.
        Args:
            student_id(int): The Id of the student to be removed
        """    
        # Open a sessiom, find the student by ID , delete if found,
        # commit the transaction, and close the session
        with self.get_session as session:
            try:
                student = session.query(Student).filter(Student.id ==
                                                        student_id).first()
                if student:
                    # delete the student from the session.
                    session.delete(student)
                    session.commit()  # Commit the transaction.
                    print(f"{student.name} has been Deleted !!")
                else:
                    print(f"No student found with ID {student_id}")
            except Exception as e:
                session.rollback()  # Rollback the transaction on error.
                print(f"Failed to delete student : {e}")
            finally:
                session.close()  # Ensure the session is closed.

    def get_student(self, student_id):
        """
        Retrieve a student by ID.
        Args:
            student_id(int): The ID of the student to be removed.

        Returns:
            str: Student's deails if found, otherwise a not found message.
        """
        # Open a session, find the student by ID, return the student deatils
        # or an error message, and close the session.
        with self.get_session as session:
            try:
                result = session.query(Student).filter(Student.id ==
                                                       student_id).first()
                if result:
                    # Return the student details as a string.
                    return str(result) 
                else:
                    return f"No Student found with ID {student_id}"
            except Exception as e:
                print(f"Failed to retrieve student: {e}")
            finally:
                session.close()  # Ensure the session is closed.
            
    def view_all_students(self):
        """
        Print all students in the database.
        """
        #  Open a session ,retrive all the stdents, print the deatials and
        #  close the session.
        with self.get_session as session:
            try:
                result = session.query(Student).all()
                for student in result:
                    print(f"{student.id} - {student.name} {student.surname}")
            except Exception as e:
                print(f"Failed to retrive students: {e}")
            finally:
                session.close()  # Ensure the session is closed.

    def add_grade(self, student_id, subject, grades):
        """
        Add a grade for the Student.
        Args:
          student_id(int): The Id of the Student.
          subject(str): The subject of the grade.
          grades(int): The grade score
        """
        # Create a new grade object.
        new_grade = Grade(student_id=student_id,
                          subject=subject,
                          grades=grades)
        
        # Open a session, add the new grade if student is found,commit
        # the transaction, and close the session.
        with self.get_session as session:
            try:
                result = session.query(Student).filter(student_id ==
                                                       student_id).first()
                if result:
                    session.add(new_grade)  # Add new grade to the session.
                    session.commit()  # Commit the transaction.
                    print(f"Grades has been added to student ID {student_id}")
                else:
                    print(f"No Student found with ID {student_id}")
            except Exception as e:
                session.rollback()  # Rollback the Transaction on error.
                print(f"Failed to add grade: {e}")
            finally:
                session.close()  # Ensure the session is closed.

    def update_email(self, student_id, new_email):
        """
        Update a student's email address.

        Args:
            student_id (int): The ID of the student.
            new_email (str): The new email address.
        """
        # Open a session , find the student by ID, update the email if student
        # is found, commit the transaction and close the session.
        with self.get_session as session:
            try:
                result = session.query(Student).filter(Student.id ==
                                                       student_id).first()
                if result:
                    result.email = new_email  # Update the student's email.
                    session.commit()  # Commit  the transaction.
                    print(f"{result.name}'s Email Address Has been updated!!!")
            except Exception as e:
                session.rollback()  # Rollback the session on error.
                print(f" Failed to update email: {e}")
            finally:
                session.close()

    def update_phone_no(self, student_id, new_phone_no):
        """
        Update a student's Phone number.

        Args:
            student_id (int): The ID of the student.
            phone_number (str): The new phone number.
        """
        # Open a session , find the student by ID, update the phone number
        # if student is found, commit the transaction and close the session.
        with self.get_session as session:
            try:
                result = session.query(Student).filter(Student.id ==
                                                       student_id).first()
                if result:
                    result.phone_number = new_phone_no
                    session.commit()  # Commit the transaction.
                    print(f"{result.name}'s Phone Number Has been updated!!")
                else:
                    print(f"No student found with Student ID {student_id}")
            except Exception as e: 
                session.rollback()  # Rollback the session on error.
                print(f"Failed to update Phone number:{e}")
            finally:
                session.close()

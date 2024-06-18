from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base


#  Intitialize the base class for declarative class defination.
Base = declarative_base()


class BaseModel(Base):
    """
    A base model that the other model will inherit from.
    Contains common attributes like 'id'.
    """
    # Mark this class as abstract, no table will be  created for this class.
    __abstract__ = True  
    # Allow this base class to be used in mapped realtionship.
    __allow_mapped__ = True  
    #  Primary key for all derieved models.
    id = Column(Integer, autoincrement=True, primary_key=True) 


class Grade(BaseModel):
    """
    Grade model representing a grade for a student in a perticular subject.
    
    Attributes:
        student_id(int): Foreign key referring to the student's ID.
        subject(str): The subject name.
        grades(int): The grade score.
    """
    __tablename__ = "Grades"  # Define the table name for this model.
    # Foreign key referring to the Students table.
    student_id = Column(ForeignKey('Students.id'))  
    subject = Column(String)  # Subject name
    grades = Column(Integer)  # Grade score

    def __repr__(self):
        """
        Return a string reperesentation of the Grade object.
        """
        return f"<{self.subject} - {self.grades}"
    

class Student(BaseModel):
    """
    Student model representing a student with personal details and grades.
    
    Attributes:
        name (str): The student's first name.
        surname (str): The student's last name.
        date_of_birth (date): The student's date of birth.
        email (str): The student's email address.
        phone_number (str): The student's phone number.
        grades (list of Grade): List of grades associated with the student.
    """
    __tablename__ = "Students"  # Define the table name for this model.
    name = Column(String)  # Student's first name.
    surname = Column(String)  # Student's last name.
    date_of_birth = Column(Date)  # Student's date of birth.
    email = Column(String)  # Student's email address.
    phone_number = Column(String)  # # Student's phone number
    grades = relationship(Grade)  # Relationship to the Grade model

    def __str__(self):
        """
        Return a string representation of the Student object.
        """
        output = f"Student ID:\t {self.id}\n Full Name:\t{self.name} {self.surname}\n"
        output += f"Date of Birth:\t {self.date_of_birth}\nEmail:\t{self.email}\n"
        output += f"Phone Number:\t{self.phone_number}\n\nGrades:\n"
        for grade in self.grades:
            output += f"{grade.subject} : {grade.grades}% \n"
        return str(output)

    def __repr__(self):
        """
        Return a brief string representation of the Student object.
        """
        return f"<{self.id} - {self.name} {self.surname}- {self.grades}%"
    


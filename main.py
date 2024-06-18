from student_manager import StudentManager
from utils import draw_line, parse_date

MAIN_MENU = """Student Manager

1. View All Students
2. Update Student
3. Add Student
4. Delete Student

0. Quit"""

STUDENT_EDIT_MENU = """Please Select an option Below

1. Add Grade
2. Change Email
3. Change Phone Number

0. Back"""


def main():
    """
    Main function to manage Student's Database. It provides a command line
    interface for viewing, updating, adding and deleting Students.
    """
    student_manager = StudentManager()

    while True:
        # Display Main Menu.
        draw_line()
        print(MAIN_MENU)
        draw_line()
        user_option = input(": ")

        if user_option == "0":
            # Exit the program.
            break
        if user_option == "1":
            # View all Students.
            draw_line()
            print("Students: ")
            draw_line()
            student_manager.view_all_students()
        
        elif user_option == "2":
            # Update Student Information.
            student_id = int(input("Please Enter the ID of the Student you "
                                   "would like to edit: "))
            while True:
                student = student_manager.get_student(student_id)
                draw_line()
                print(student)
                print(STUDENT_EDIT_MENU)
                draw_line()
                edit_option = input(": ")
                if edit_option == "0":
                    # Return to the main Menu.
                    break
                elif edit_option == "1":
                    # Add grade for student for perticular subject.
                    subject = input("Please enter the subject name :")
                    grade = int(input("Please Enter the Grade score : "))
                    student_manager.add_grade
                    (student_id, subject, grade)
                elif edit_option == "2":
                    # Change the student's email address.
                    new_email = input("Enter New Email address: ")
                    student_manager.update_email(student_id, new_email)
                elif edit_option == "3":
                    # Change the student's phone number.
                    new_phone_num = input("Enter New phone Number : ")
                    student_manager.update_phone_no(student_id, new_phone_num)
   
        elif user_option == "3":
            # Add a new Student
            print("Please enter the follwing data to add a student:")          
            name = input("Name: ")
            surname = input("Surname : ")
            date_of_birth_str = input("Date of Birth(DD-MM-YYYY): ")
            try:
                date_of_birth = parse_date(date_of_birth_str)
            except ValueError as e:
                print(e)
                # Skip the rest of the loop iterarion if the date is invalid.
                continue  
            # day, month, year = date_of_birth.split("-")
            # date_of_birth = date(int(year), int(month), int(day))
            email = input("Email: ")
            phone_number = input("Phone Number: ")
            student_manager.add_student(name, surname, date_of_birth, email,
                                        phone_number)

        elif user_option == "4":
            # Delete a a student.
            student_id = int(input("Enter the Id of the student which You would like to Delete : "))
            student_manager.remove_student(student_id)


if __name__ == "__main__":
    main()
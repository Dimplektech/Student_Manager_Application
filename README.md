# Student_Manager_Application

## Description

The Student Manager Application is a command-line tool for managing student records, including their personal details and grades. It allows users to view, add, update, and delete student information.

## Features

- View all students
- Add a new student
- Update student information (email, phone number, and grades)
- Delete a student
- Parse and validate dates

## Technologies Used

- Python 3.7+
- SQLAlchemy (ORM for database interaction)
- SQLite (default database, configurable)
- Unittest

## Installation

1. **Clone the repository**:

    ```bash
    git clone [https://github.com/your-username/student-manager.git](https://github.com/Dimplektech/Student_Manager_Application.git)
    cd student-manager
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the database settings**:

    - Create a `settings.py` file in the project root with the following content:

        ```python
        DB_ADDRESS = 'sqlite:///my_db.db'  # Update with your database URL if using a different database
        ```

5. **Initialize the database**:

    - Run the following command to create the database tables:

        ```bash
        python init_db.py
        ```

## Usage

1. **Run the application**:

    ```bash
    python main.py
    ```

2. **Follow the on-screen menu to manage students**.

## Project Structure

- `main.py`: Entry point of the application
- `student_manager.py`: Contains the `StudentManager` class for handling database operations
- `models.py`: Defines the database models (`Student` and `Grade`)
- `settings.py`: Configuration file for database settings
- `utils.py`: Utility functions (e.g., for drawing lines in the menu, for checking Date format)
- `requirements.txt`: List of required Python packages

## Models

### Student

- `id` (int): Primary key
- `name` (str): First name
- `surname` (str): Last name
- `date_of_birth` (date): Date of birth
- `email` (str): Email address
- `phone_number` (str): Phone number
- `grades` (relationship): List of grades associated with the student

### Grade

- `id` (int): Primary key
- `student_id` (int): Foreign key referring to the `Student` model
- `subject` (str): Subject name
- `grades` (int): Grade score


## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request

## Acknowledgements

- [SQLAlchemy](https://www.sqlalchemy.org/) for the ORM
- [SQLite](https://www.sqlite.org/) for the database

## Contact

### Dimpal Kaware (https://github.com/Dimplektech)

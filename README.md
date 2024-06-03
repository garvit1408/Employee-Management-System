# Employee Management System

Welcome to the Employee Management System! This is a simple yet powerful application developed using Python, customTkinter for the GUI, and MySQL for the database management. This system allows you to manage employee records efficiently, including adding, updating, deleting, and viewing employee details.

## Features

- **Add Employee**: Add new employee records to the database.
- **Update Employee**: Modify existing employee details.
- **Delete Employee**: Remove employee records from the database.
- **View Employees**: Display all employee records in a tabular format.

## Technologies Used

- **Python**: The core programming language used for developing the application.
- **customTkinter**: A modern and customizable Tkinter library used for building the graphical user interface.
- **MySQL**: The relational database management system used for storing and managing employee data.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- MySQL server installed and running.
- Required Python libraries installed. You can install them using:
  
    ```bash
    pip install customtkinter mysql-connector-python

## Installation

Follow these steps to set up the Employee Management System on your local machine:

1. **Clone the Repository**:

     ```bash
     git clone https://github.com/your-username/employee-management-system.git
     cd employee-management-system

3. **Setup Database**:
    - Log in to your MySQL server and create a new database:

      ```sql
      CREATE DATABASE employee_management;
      USE employee_management;
      
      CREATE TABLE employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        position VARCHAR(50),
        salary DECIMAL(10, 2)
      );

3. **Configure Database Connection**:
    - Open the config.py file (or the relevant Python script) and update the database connection settings with your MySQL credentials:

      ```python
        db_config = {
        'host': 'localhost',
        'user': 'your-username',
        'password': 'your-password',
        'database': 'employee_management'
      }
    
4. **Install Required Libraries:**
    - Install the necessary Python libraries using pip:

      ```bash
         pip install customtkinter mysql-connector-python

## Screenshots:


# Bank Management System

## Description
This project is a simple banking system implemented in Python. It provides basic functionalities such as user registration with secure password creation, login, balance inquiry, cash deposit, cash withdrawal, and fund transfer. The project uses MySQL for data storage and demonstrates object-oriented programming concepts.

## Features
- User registration with strong password policy
- Secure user login
- Balance inquiry
- Cash deposit with input validation
- Cash withdrawal
- Fund transfer between accounts with transaction recording for both sender and receiver
- Transaction history

## Technologies Used
- Python
- MySQL
- Regular Expressions (for password validation)

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/your-username/python-bank-project.git
   ```
2. Install the required dependencies:
   ```
   pip install mysql-connector-python
   ```
3. Set up a MySQL database and update the connection details in `database.py`.

## Usage
Run the `main.py` file to start the application:
```
python main.py
```
Follow the on-screen prompts to navigate through the banking system.

## Project Structure
- `main.py`: The main entry point of the application
- `bank.py`: Contains the `Bank` class with core banking operations
- `customer.py`: Defines the `Customer` class for user management
- `database.py`: Handles database connections and operations
- `register.py`: Manages user registration and sign-in processes
- `passwords.py`: Implements secure password creation and validation

## Security Features
- Strong password policy enforcing length, complexity, and character variety
- Input validation to prevent negative deposits
- Separate transaction recording for both sender and receiver in fund transfers


##  Acknowledgement
- This project was created as part of my journey to learn Python programming and basic banking system implementation.

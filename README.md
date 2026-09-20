# Data Redundancy Removal System

## Overview

The Data Redundancy Removal System (DRRS) is a Flask-based web application designed to reduce duplicate records in a database.

The system validates user input, checks email uniqueness, generates a SHA-256 hash for each record, and stores valid data in a MySQL database.

## Features

- User-friendly web interface
- Name, email, and phone number validation
- Email uniqueness checking
- SHA-256 data hashing
- MySQL database integration
- Database-level unique constraints
- Success and error messages
- Environment variables for database credentials

## Technologies Used

- Python
- Flask
- MySQL
- HTML
- CSS
- Git and GitHub

## Project Structure

```text
drs/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── .gitignore
└── README.md
```

## Validation Rules

- All fields are required.
- Email must follow a valid email format.
- Phone number must contain 10 digits and start with 6–9.
- Email addresses must be unique.
- Names can be repeated.
- Phone numbers can be repeated.

## Security

Database credentials are stored in a `.env` file and excluded from Git using `.gitignore`.

## How to Run

1. Activate the virtual environment:

```bash
source venv/bin/activate
```

2. Install the required packages:

```bash
pip install flask mysql-connector-python python-dotenv
```

3. Start the Flask application:

```bash
python app.py
```

4. Open the application in your browser:

```text
http://127.0.0.1:5000
```

## Future Improvements

- Email domain/existence verification
- Cloud deployment
- Additional database management features
- Improved user interface

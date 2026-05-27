# College Data - Student CRUD App

A simple Flask + MySQL web app to manage student records.

## Features
- Add a student name
- View all saved students
- Edit a student
- Delete a student

## Tech Stack
- Python
- Flask
- MySQL
- HTML (Jinja templates)

## Project Structure
```text
college_data/
|-- app.py
|-- .env
|-- .gitignore
|-- templates/
|   |-- index.html
|   `-- edit.html
`-- README.md
```

## Prerequisites
- Python 3.8+
- MySQL Server running locally
- A MySQL database named `college`

## Database Setup
Run the following SQL in MySQL:

```sql
CREATE DATABASE IF NOT EXISTS college;
USE college;

CREATE TABLE IF NOT EXISTS studenttbl (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(255) NOT NULL
);
```

Note:
- In your code, both `Studenttbl` and `studenttbl` are used in queries.
- On most local Windows MySQL setups this still works, but using one consistent table name is recommended.

## Installation
1. Clone the repository:
```bash
git clone <your-repo-url>
cd college_data
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
```

Windows (PowerShell):
```bash
.venv\Scripts\Activate.ps1
```

3. Install dependencies:
```bash
pip install flask mysql-connector-python
```

## Configuration
Update DB credentials in `app.py` if needed:
- `host`
- `user`
- `password`
- `database`

Current app expects:
- Host: `127.0.0.1`
- User: `root`
- Database: `college`

## Run the App
```bash
python app.py
```

Then open:
- `http://127.0.0.1:5000/`
<img width="1920" height="1032" alt="image" src="https://github.com/user-attachments/assets/56887b9a-ec58-479c-9212-c83762ad1646" />
<img width="1920" height="1032" alt="image" src="https://github.com/user-attachments/assets/dd249e4b-60e1-449a-887a-74d280d066be" />

## Routes
- `GET /` - Show form and student list
- `POST /` - Add new student
- `GET /edit/<id>` - Open edit form
- `POST /update/<id>` - Update student name
- `GET /delete/<id>` - Delete student

## Notes
- App runs in debug mode (`debug=True`) for development.
- Avoid committing real DB passwords to source control.

# Task Manager Web Application

A RESTful task management backend built with **Python**, **FastAPI**, **Pydantic**, and **MySQL** (`mysql-connector-python`). The application provides complete CRUD endpoints for creating, viewing, updating, and deleting tasks with request payload validation and parameterized SQL queries to prevent SQL injection.

---

## Features

- **Complete CRUD Operations:** Create new tasks, retrieve all tasks, fetch a single task by ID, update existing tasks, and delete tasks via clean REST endpoints.
- **Pydantic Request Validation:** Validates incoming task payloads using a structured `Taskrequest` Pydantic model before executing database operations.
- **SQL Injection Protection:** Uses parameterized SQL queries with `mysql-connector-python` for secure relational database interactions.
- **Interactive API Docs:** Automatically generated Swagger UI (`/docs`) and ReDoc (`/redoc`) endpoints provided by FastAPI for testing API routes directly in the browser.

---

## Tech Stack

- **Backend Framework:** Python, FastAPI
- **Data Validation:** Pydantic
- **Database & Driver:** MySQL, `mysql-connector-python`
- **Server:** Uvicorn

---

## Project Structure

```text
taskmanager_fastapi_application/
├── main.py                   # FastAPI application, Pydantic models, MySQL connection, and CRUD routes
├── requirements.txt          # Python project dependencies
├── .gitignore                # Git ignore rules for virtual environments and cache files
└── README.md                 # Project documentation
```

---

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/create` | Validate task payload via `Taskrequest` and insert a new task into MySQL |
| `GET` | `/show` | Retrieve all tasks from the database |
| `GET` | `/showonetask` | Retrieve a single task record by task ID |
| `PUT` | `/update` | Update an existing task's details in MySQL |
| `DELETE` | `/delete` | Delete a specific task record from the database |

---

## Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/varshitha17041943/](https://github.com/varshitha17041943/)<your-task-manager-repo-name>.git
cd <your-task-manager-repo-name>
```

### 2. Create & Activate a Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn pydantic mysql-connector-python
```

### 4. Configure MySQL Database
1. Start your local MySQL server and create your database and tasks table.
2. Update the MySQL connection credentials (`host`, `user`, `password`, `database`) in `main.py` (or load them via environment variables).

### 5. Run the Application
```bash
uvicorn main:app --reload
```

Open your browser and navigate to:
- **Interactive Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc Documentation:** `http://127.0.0.1:8000/redoc`

---

## Author

**Varshitha Reddy**  
- GitHub: [@varshitha17041943](https://github.com/varshitha17041943)  
- LinkedIn: [N Varshitha](https://www.linkedin.com/in/n-varshitha)

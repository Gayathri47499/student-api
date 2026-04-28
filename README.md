# 🎓 Student Management REST API

A simple and scalable RESTful API built using **Flask** and **SQLite** to manage student records. This project demonstrates core backend development concepts including API design, database integration, and clean project structuring.

---

## 🚀 Features

* Retrieve all student records
* Add a new student
* Delete an existing student
* Lightweight database integration using SQLite
* Clean and modular code structure

---

## 🛠️ Tech Stack

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Core programming language |
| Flask      | Backend web framework     |
| SQLite     | Lightweight database      |
| Postman    | API testing               |

---

## 📂 Project Structure

```
student-api/
│
├── app.py              # Main application file
├── database.db        # SQLite database (auto-generated)
├── requirements.txt   # Project dependencies
└── README.md          # Documentation
```

---

## ⚙️ Setup & Installation

Follow these steps to run the project locally:

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/student-api.git
cd student-api
```

### 2️⃣ Create virtual environment

```
python -m venv venv
```

### 3️⃣ Activate environment

```
venv\Scripts\activate
```

### 4️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 5️⃣ Run the application

```
python app.py
```

### 6️⃣ Access API

```
http://127.0.0.1:5000/
```

---

## 🔗 API Endpoints

### 📌 Get All Students

**GET /students**

Returns a list of all students.

---

### 📌 Add a Student

**POST /students**

**Request Body:**

```json
{
  "name": "Gayathri",
  "age": 20
}
```

---

### 📌 Delete a Student

**DELETE /students/{id}**

Deletes a student based on ID.

---

## 🧪 Testing

All endpoints were tested using **Postman** to ensure correct functionality and responses.

---

## 🗄️ Database

* SQLite is used as a lightweight relational database
* Database file: `database.db`
* Table: `students (id, name, age)`

---

## 📌 Key Highlights

* Demonstrates REST API fundamentals
* Uses real database integration (not in-memory)
* Follows clean and readable code practices
* Beginner-friendly but structured like production code

---

## 👩‍💻 Author

**Gayathri Sanjana**
Backend Intern Applicant

---

## 📬 Submission Note

This project was completed as part of the backend internship evaluation task. It focuses on clarity, correctness, and clean implementation of REST API principles.

---

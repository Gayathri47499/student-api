from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Create DB connection
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# Create table
def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    """)
    conn.commit()
    conn.close()

init_db()

# 1. GET all students
@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()

    return jsonify([dict(row) for row in students])


# 2. POST new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    name = data.get('name')
    age = data.get('age')

    conn = get_db()
    conn.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

    return jsonify({"message": "Student added"}), 201


# 3. DELETE student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    conn = get_db()
    conn.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Student deleted"})


if __name__ == '__main__':
    app.run(debug=True)
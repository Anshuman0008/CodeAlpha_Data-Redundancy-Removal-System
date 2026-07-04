from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# -----------------------------
# Database Connection Function
# -----------------------------
def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="Anshu#12345",
        database="data_redundancy"
    )


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Add Record Page
# -----------------------------
@app.route("/add")
def add():
    return render_template("add_record.html")


# -----------------------------
# Save Employee
# -----------------------------
@app.route("/save", methods=["POST"])
def save():

    employee_id = request.form["employee_id"]
    full_name = request.form["full_name"]
    email = request.form["email"]
    phone = request.form["phone"]
    department = request.form["department"]
    address = request.form["address"]

    db = get_connection()
    cursor = db.cursor()

    # Duplicate Check
    sql = """
    SELECT * FROM employee
    WHERE employee_id=%s
    OR email=%s
    OR phone=%s
    """

    cursor.execute(sql, (employee_id, email, phone))

    record = cursor.fetchone()

    if record:
        cursor.close()
        db.close()
        return "<h2 style='color:red;'>Duplicate Record Found!</h2>"

    # Insert Data
    sql = """
    INSERT INTO employee
    (employee_id, full_name, email, phone, department, address)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (
        employee_id,
        full_name,
        email,
        phone,
        department,
        address
    )

    cursor.execute(sql, values)

    db.commit()

    cursor.close()
    db.close()

    return "<h2 style='color:green;'>Record Added Successfully!</h2>"


# -----------------------------
# Run Flask
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
import mysql.connector
import hashlib
import re
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


@app.route("/", methods=["GET", "POST"])
def index():

    message = ""
    message_type = ""

    if request.method == "POST":

        name = request.form["name"].strip()
        email = request.form["email"].strip()
        phone = request.form["phone"].strip()

        if not name or not email or not phone:
            message = "All fields are required."
            message_type = "error"

        elif not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            message = "Please enter a valid email address."
            message_type = "error"

        elif not re.match(r"^[6-9]\d{9}$", phone):
            message = "Please enter a valid 10-digit phone number."
            message_type = "error"

        else:
            db = get_db_connection()
            cursor = db.cursor()

            data_string = name + email + phone
            data_hash = hashlib.sha256(
                data_string.encode()
            ).hexdigest()

            email_query = """
            SELECT id FROM data
            WHERE email = %s
            """

            cursor.execute(email_query, (email,))
            email_result = cursor.fetchone()

            if email_result:
                message = "Email already taken. An account with this email already exists."
                message_type = "error"

            else:
                insert_query = """
                INSERT INTO data (name, email, phone, data_hash)
                VALUES (%s, %s, %s, %s)
                """

                cursor.execute(
                    insert_query,
                    (name, email, phone, data_hash)
                )

                db.commit()

                message = "Data added successfully!"
                message_type = "success"

            cursor.close()
            db.close()

    return render_template(
        "index.html",
        message=message,
        message_type=message_type
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)

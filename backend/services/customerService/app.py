import mysql.connector
from flask import Flask, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.getenv('MYSQL_HOST'),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DB")
)

# Use dictionary=True to get column names
cursor = db.cursor(dictionary=True)

@app.route("/customers")
def get_users():
    cursor.execute("SELECT * FROM customers")
    users = cursor.fetchall()  # Each row is now a dict
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True,port=5002)

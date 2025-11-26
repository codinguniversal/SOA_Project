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


@app.route("/inventory")
def get_inventory():
    cursor.execute("SELECT * FROM inventory")
    inventory = cursor.fetchall()  # Each row is now a dict
    return jsonify(inventory)

if __name__ == "__main__":
    app.run(port=5002, debug=True)
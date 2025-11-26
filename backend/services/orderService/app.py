from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/orders")
def get_orders():
    orders = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]
    return jsonify(orders)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
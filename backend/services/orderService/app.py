from flask import Flask,request, jsonify

app = Flask(__name__)

@app.route("/orders")
def get_orders():
    orders = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]
    return jsonify(orders)

@app.route("/api/orders/create", methods=["POST"])
def create_order():
    data  = request.get_json() # To access the request body
    customerId = data.get('customer_id') # access the parameter 'customer_id'
    products = data.get('products')
    total_amount = data.get('total_amount')
    order = {"customer_id":customerId,"products":products,"total_amount":total_amount}
    return jsonify({"message": "Order created successfully","data":order})

if __name__ == "__main__":
    app.run(port=5001, debug=True)
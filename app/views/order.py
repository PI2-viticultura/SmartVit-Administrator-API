from flask import Blueprint, request
from flask_cors import CORS
import controllers.order as order_controller

app = Blueprint('order', __name__)
CORS(app)


@app.route("/order", methods=["POST"])
def order():
    return order_controller.register_order_request(request.json)


@app.route("/orders", methods=["GET"])
def orders():
    return order_controller.get_orders()


@app.route("/orders/<string:order_id>", methods=["PATCH"])
def orders_update_status(order_id):
    return order_controller.change_status(order_id)

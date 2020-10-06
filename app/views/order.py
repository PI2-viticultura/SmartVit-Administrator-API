from flask import Blueprint, request
from flask_cors import CORS
import controllers.order as order_controller

app = Blueprint('order', __name__)
CORS(app)


@app.route("/order", methods=["POST"])
def order():
    return order_controller.register_order_request(request.json)

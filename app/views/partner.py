from flask import Blueprint, request
from flask_cors import CORS
import controllers.partner as partner_controller


app = Blueprint('partner', __name__)
CORS(app)


@app.route("/partner", methods=["POST"])
def partner():
    return partner_controller.register_partner_request(request.json)


@app.route("/partners", methods=["GET"])
def partners():
    return partner_controller.get_partners()

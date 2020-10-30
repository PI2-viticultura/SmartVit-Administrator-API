from flask import Blueprint, request
from flask_cors import CORS
import controllers.contract as contract


app = Blueprint('contract', __name__)
CORS(app)


@app.route("/contracts", methods=["POST"])
def contrato():
    return contract.register_contract_request(request.json)


@app.route("/contracts", methods=["GET"])
def contrato():
    return contract_controller.get_contracts()


@app.route("/contract/<string:contract_id>", methods=["PATCH"])
def contrato_update_status(contract_id):
    return contract_controller.change_status(contract_id)

from flask import Blueprint, request
from flask_cors import CORS
import controllers.contract as contract


app = Blueprint('contract', __name__)
CORS(app)


@app.route("/contract", methods=["POST"])
def contrato():
    return contract.register_contract_request(request.json)

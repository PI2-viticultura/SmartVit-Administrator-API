from flask import Blueprint, request, jsonify
from flask_cors import CORS
import controllers.contrato as controller


app = Blueprint('contrato', __name__)
CORS(app)

@app.route("/contrato", methods=["POST"])
def contrato():
    return controller.register_contract_request(request.json)

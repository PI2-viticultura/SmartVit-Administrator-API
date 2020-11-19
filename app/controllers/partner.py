from models.db import MongoDB
from bson.json_util import dumps

def register_partner_request(request):
    fields = [
        'name', 'address',
        'phoneNumber', 'type'
    ]

    if not all(field in request.keys() for field in fields):
        return {
            "Erro":
            "Por gentileza, preencha todos os campos"
        }, 400

    if not request["name"]:
        return {"erro": "Informe o nome do Parceiro"}, 400
    if not request["address"]:
        return {"erro": "Informe o endereço do parceiro"}, 400
    if not request["phoneNumber"]:
        return {"erro": "Informe o telefone do parceiro"}, 400
    if not request["type"]:
        return {"erro": "Informe a especialidade do parceiro"}, 400

    db = MongoDB()

    connection_is_alive = db.test_connection()
    if connection_is_alive:
        partner = db.insert_one(request, 'partners')
        if not partner:
            return {'error': 'Something gone wrong'}, 500
        return {"message": "Sucess"}, 200

    return {'error': 'Something gone wrong'}, 500

def get_partners():
    db = MongoDB()

    connection_is_alive = db.test_connection()
    if connection_is_alive:
        partners = db.get_all('partners')
        if(partners):
            return dumps(partners), 200

    return {'error': 'Something gone wrong'}, 500
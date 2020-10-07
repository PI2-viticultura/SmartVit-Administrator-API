from models.db import MongoDB
from bson.json_util import dumps


def register_order_request(request):
    fields = [
        'description', 'name', 'email',
        'phoneNumber', 'status'
    ]

    if not all(field in request.keys() for field in fields):
        return {
            "Erro":
            "Por gentileza, preencha os campos obrigatórios!"
        }, 400

    if not request["description"]:
        return {"erro": "Descreva a sua solicitação"}, 400
    if not request["name"]:
        return {"erro": "Informe o nome"}, 400
    if not request["email"]:
        return {"erro": "Informe o email"}, 400
    if not request["phoneNumber"]:
        return {"erro": "Informe o telefone"}, 400

    db = MongoDB()

    connection_is_alive = db.test_connection()
    if connection_is_alive:
        if(db.insert_one(request, 'orders')):
            return {"message": "Sucess"}, 200

    return {'error': 'Something gone wrong'}, 500


def get_orders():
    db = MongoDB()

    connection_is_alive = db.test_connection()
    if connection_is_alive:
        orders = db.get_all('orders')
        if(orders):
            return dumps(orders), 200

    return {'error': 'Something gone wrong'}, 500
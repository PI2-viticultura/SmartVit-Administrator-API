from models.db import MongoDB
from bson.json_util import dumps
from bson import ObjectId


def register_contract_request(request):
    fields = [
        'contractor', 'cpf_cnpj', 'address',
        'phoneNumber', 'initialDate', 'status',
        'endDate', 'winery'
    ]

    if not all(field in request.keys() for field in fields):
        return {
            "Erro":
            "Por gentileza, preencha todos os campos"
        }, 400

    if not request["contractor"]:
        return {"erro": "Informe o contratante do contrato"}, 400
    if not request["cpf_cnpj"]:
        return {"erro": "Informe o CPF/CNPJ do contratante"}, 400
    if not request["address"]:
        return {"erro": "Informe o endereco do contratante"}, 400
    if not request["phoneNumber"]:
        return {"erro": "Informe o telefone do contratante"}, 400
    if not request["initialDate"]:
        return {"erro": "Informe a data de inicio do contrato"}, 400
    if not request["status"]:
        return {"erro": "Informe o status do contrato"}, 400
    if not request["endDate"]:
        return {"erro": "Informe a data final do contrato"}, 400
    if not request["winery"]:
        return {"erro": "Informe os dados da vinicola"}, 400

    db = MongoDB()

    connection_is_alive = db.test_connection()
    if connection_is_alive:
        winery = db.insert_one(request['winery'], 'winery')
        if not winery:
            return {'error': 'Something gone wrong'}, 500

        winery = db.get_one(winery.inserted_id, 'winery')
        request["winery"] = winery
        if(db.insert_one(request, 'contracts')):
            return {"message": "Sucess"}, 200

    return {'error': 'Something gone wrong'}, 500


def get_contracts():
    db = MongoDB()

    connection_is_alive = db.test_connection()
    if connection_is_alive:
        contracts = db.get_all('contracts')
        if(contracts):
            return dumps(contracts), 200

    return {'error': 'Something gone wrong'}, 500


def change_status(contract_id):
    id_transformed = ObjectId(contract_id)
    db = MongoDB()

    connection_is_alive = db.test_connection()
    if connection_is_alive:
        contract = db.get_one(id_transformed, 'contracts')

        if contract:
            if (contract['status'] == 1):
                contract['status'] = 0
            else:
                contract['status'] = 1

        retorno = db.update_one(contract, 'contracts')

        if retorno:
            return {'message': 'Success'}, 200

    return {'message': 'Something gone wrong'}, 500

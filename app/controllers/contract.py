from models.db import MongoDB


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

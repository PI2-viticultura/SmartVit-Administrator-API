from models.db import MongoDB


def register_contract_request(request):
    fields = [
        'contratante', 'cpf_cnpj', 'endereco',
        'telefone', 'dataInicio', 'status',
        'dataFim', 'vinicola'
    ]

    if not all(field in request.keys() for field in fields):
        return {
            "Erro":
            "Por gentileza, preencha todos os campos"
        }, 400

    if not request["contratante"]:
        return {"erro": "Informe o contratante do contrato"}, 400
    if not request["cpf_cnpj"]:
        return {"erro": "Informe o CPF/CNPJ do contratante"}, 400
    if not request["endereco"]:
        return {"erro": "Informe o endereco do contratante"}, 400
    if not request["telefone"]:
        return {"erro": "Informe o telefone do contratante"}, 400
    if not request["dataInicio"]:
        return {"erro": "Informe a data de inicio do contrato"}, 400
    if not request["status"]:
        return {"erro": "Informe o status do contrato"}, 400
    if not request["dataFim"]:
        return {"erro": "Informe a data final do contrato"}, 400
    if not request["vinicola"]:
        return {"erro": "Informe os dados da vinicola"}, 400

    db = MongoDB()

    connection_is_alive = db.test_connection()
    if connection_is_alive:
        if(db.insert_one(request, 'contracts')):
            return {"message": "Sucess"}, 200

    return {'error': 'Something gone wrong'}, 500

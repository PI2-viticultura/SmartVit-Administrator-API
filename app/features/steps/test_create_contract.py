from behave import given, when, then
import requests

request_headers = {}
request_bodies = {}
api_url = None


@given('a pagina de criar novo contrato')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-admin-dev.herokuapp.com/contracts'
    print('url :'+api_url)


@when('ele regista novo conteudo do contrato da solicitacao')
def step_impl_when(context):
    request_bodies['POST'] = {"contractor": "Joao Alves",
                              "cpf_cnpj": "45212563455",
                              "address": "rua Sao Paulo",
                              "phoneNumber": "61996853214", 
                              "initialDate": "25-01-2020",
                              "status": "1",
                              "endDate": "25-01-2021",
                              "winery": "5fa0c880d578d4bc349dc376"}
    response = requests.post(
                            'https://smartvit-admin-dev.herokuapp.com//contracts',
                            json=request_bodies['POST']
                            )
    assert response.status_code == 200


@then('o bff requisita o microsservico para criar contrato')
def step_impl_then(context):
    api_bff_url = 'https://smartvit-admin-bff-dev.herokuapp.com/contracts'
    response = requests.post(
                            api_bff_url,
                            json=request_bodies['POST']
                            )
    assert response.status_code == 200
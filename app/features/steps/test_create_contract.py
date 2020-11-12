from behave import given, when, then
import requests

request_headers = {}
request_bodies = {}
response_codes = {}
api_url = None


@given('a pagina de criar novo contrato')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-admin-stg.herokuapp.com/contracts'
    print('url :'+api_url)


@when('ele regista novo conteudo do contrato da solicitacao')
def step_impl_when(context):
    request_bodies['POST'] = {"address": "rua Sao Paulo",
                              "contractor": "unb@unb.com.br",
                              "cpf_cnpj": "45212563455",
                              "initialDate": "2020-11-09",
                              "phoneNumber": "61996853214",
                              "status": "1",
                              "endDate": "2021-11-09",
                              "winery": "5fad331b38b2670687db57e2"}
    response = requests.post(
                            api_url,
                            json=request_bodies['POST']
                            )
    statuscode = response.status_code
    response_codes['POST'] = statuscode


@then('certifica que o contrato foi feito')
def step_impl_then(context):
    print('Post rep code ;'+str(response_codes['POST']))
    assert response_codes['POST'] != 200

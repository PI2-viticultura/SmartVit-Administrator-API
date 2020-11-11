from behave import given, when, then
import requests

request_headers = {}
request_bodies = {}
response_codes = {}
api_url = None


@given('a pagina de criar novo pedido')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-admin-dev.herokuapp.com/order'
    print('url :'+api_url)


@when('ele regista novo conteudo do pedido da solicitacao')
def step_impl_when(context):
    request_bodies['POST'] = {"description": "Testar bdd",
                              "name": "Joao Ninguem",
                              "email": "test@gmail.com",
                              "phoneNumber": "61996853214",
                              "status": "0"}
    response = requests.post(
                            'https://smartvit-admin-dev.herokuapp.com/order',
                            json=request_bodies['POST']
                            )
    #assert response.status_code == 200
    statuscode = response.status_code
    response_codes['POST'] = statuscode


@then('certifica que o pedido foi feito')
def step_impl_then(context):
    print('Post rep code ;'+str(response_codes['POST']))
    assert response_codes['POST'] == 200
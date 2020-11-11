from behave import given, when, then
import requests

request_headers = {}
request_bodies = {}
response_codes = {}
api_url=None

@given('a pagina de gerenciar contratos')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-admin-dev.herokuapp.com/contracts'
    print('url :'+api_url)

@when('ele visualizar os contratos desejados')
def step_impl_when(context):
    response = requests.get('https://smartvit-admin-dev.herokuapp.com/contracts')
    #assert response.status_code == 200
    statuscode = response.status_code
    response_codes['GET'] = statuscode


@then('pega os contratos cadastrados')
def step_impl_then(context):
    print('GET rep code ;'+str(response_codes['GET']))
    assert response_codes['GET'] == 200
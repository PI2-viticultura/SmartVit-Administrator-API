from behave import given, when, then
import requests

api_url = None
bff_url = None


@given('a pagina de gerenciar pedidos')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-admin-dev.herokuapp.com/orders'
    print('url :'+api_url)


@when('ele visualizar os pedidos desejados')
def step_impl_when(context):
    response = requests.get('https://smartvit-admin-dev.herokuapp.com/orders')
    assert response.status_code == 200


@then('pega os pedidos registrados')
def step_impl_then(context):
    global bff_url
    bff_url = 'https://smartvit-admin-bff-dev.herokuapp.com/orders'
    response = requests.get(bff_url)
    assert response.status_code == 200

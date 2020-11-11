from behave import given, when, then
import requests

api_url=None

@given('a pagina de gerenciar pedidos')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-admin-dev.herokuapp.com/orders'
    print('url :'+api_url)

@when('ele visualizar os pedidos desejados')
def step_impl_when(context):
    response = requests.get('https://smartvit-admin-dev.herokuapp.com/orders')
    assert response.status_code == 200


@then('o bff requisita o microsservico com os pedidos')
def step_impl_then(context):
    response = requests.get('https://smartvit-admin-bff-dev.herokuapp.com/orders')
    assert response.status_code == 200
from behave import *
import requests
from API.utilities.configurations import *
from API.utilities.Resources import *
from API.payload import *


@given('the user details which are need to be added to Library')
def step_imp(context):
    context.url = getconfig()['API']['endpoint'] + Apiresources.add_user
    context.headers = {"Content-Type": "application/json"}
    context.payload = addpayload('basavana')


@when('we execute the addUser PostAPI Method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload, headers=context.headers, )


@then('user is successfully added')
def step_impl(context):
    print(context.response.status_code)
    print(context.response.json())
    context.response = context.response.json()
    print(type(context.response))
    context.user_id = context.response['id']
    print(context.user_id)
    print(context.response['name'])


@given("the user details which is given {user}")
def step_impl(context, user):
    context.url = getconfig()['API']['endpoint'] + Apiresources.add_user
    context.headers = {"Content-Type": "application/json"}
    context.payload = addpayload(user)


@given('I have gitHub auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('basavangouda', 'abc9741090584@J')


@when('I hit gitRepo API of github')
def step_impl(context):
    context.response = context.se.get(Apiresources.GitRepo)


@then('status code of the response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response)
    assert context.response.status_code == statusCode

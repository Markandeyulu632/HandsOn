import requests
import json
from django import urls
import pytest


@pytest.mark.parametrize('param', ['home'])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200


user_data = ["1;21;12", "2;51;15", "3;11;11", "4;81;18", "5;1;1", "3;A;A", "A;A;A", "4;1;0"]


@pytest.mark.parametrize('user_data', user_data)
def test_calc_all(client, user_data):
    option, num1, num2 = user_data.split(';')
    in_data = {'option': option, 'num1': num1, 'num2': num2}
    home_url = urls.reverse('home')
    resp = client.post(home_url, in_data)
    assert resp.status_code == 200


url = "http://127.0.0.1:8000/"


def test_addition():
    file = open("C:\\Users\\mark\\PycharmProjects\\WebCalculator\\addition.json", 'r')
    json_input = file.read()
    request_jon = json.loads(json_input)
    response = requests.post(url, request_jon)
    result = response.text
    assert result[1642:1646] == '2.00'


def test_subtraction():
    file = open("C:\\Users\\mark\\PycharmProjects\\WebCalculator\\subtraction.json", 'r')
    json_input = file.read()
    request_jon = json.loads(json_input)
    response = requests.post(url, request_jon)
    result = response.text
    assert result[1646:1651] == '22.00'


def test_multiply():
    file = open("C:\\Users\\mark\\PycharmProjects\\WebCalculator\\multiply.json", 'r')
    json_input = file.read()
    request_jon = json.loads(json_input)
    response = requests.post(url, request_jon)
    result = response.text
    assert result[1649:1654] == '50.00'


def test_division():
    file = open("C:\\Users\\mark\\PycharmProjects\\WebCalculator\\division.json", 'r')
    json_input = file.read()
    request_jon = json.loads(json_input)
    response = requests.post(url, request_jon)
    result = response.text
    assert result[1643:1648] == '31.33'


def test_division0():
    file = open("C:\\Users\\mark\\PycharmProjects\\WebCalculator\\div0_mes.json", 'r')
    json_input = file.read()
    request_jon = json.loads(json_input)
    response = requests.post(url, request_jon)
    result = response.text
    assert result[1627:1649] == "Can't divide with zero"


def test_inv_opt():
    file = open("C:\\Users\\mark\\PycharmProjects\\WebCalculator\\inv_opt_mes.json", 'r')
    json_input = file.read()
    request_jon = json.loads(json_input)
    response = requests.post(url, request_jon)
    result = response.text
    assert result[1571:1585] == 'Invalid option'


def test_inv_val():
    file = open("C:\\Users\\mark\\PycharmProjects\\WebCalculator\\inv_val_mes.json", 'r')
    json_input = file.read()
    request_jon = json.loads(json_input)
    response = requests.post(url, request_jon)
    result = response.text
    assert result[1571:1585] == 'Invalid values'


def test_inv_opt_val():
    file = open("C:\\Users\\mark\\PycharmProjects\\WebCalculator\\inv_opt_val_mes.json", 'r')
    json_input = file.read()
    request_jon = json.loads(json_input)
    response = requests.post(url, request_jon)
    result = response.text
    assert result[1571:1596] == 'Invalid option and values'

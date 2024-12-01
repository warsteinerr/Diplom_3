import pytest
from selenium import webdriver
from data import *
from helper import *
import requests

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.get(URL.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def create_user():
    payload, response = get_users_info()
    email = payload.get('email')
    password = payload.get('password')
    yield email, password
    access_token = response.json().get('accessToken')
    requests.delete(f'{URL.BASE_URL}{URL.DELETE_URL}', headers={'Authorization': access_token})
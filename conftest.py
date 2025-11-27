import pytest
from selenium import webdriver
from pages.login_pages import LoginPage
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield  driver               ## devuelve un valor // pausa el fixture y permite que todo el test se corra
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    LoginPage(driver).abrir_pagina().login_completo("standard_user","secret_sauce")
    return driver

@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def header_request():
    return {"x-api-key": "reqres-free-v1"}
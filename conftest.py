import pytest
from selenium import webdriver
from pages.login_pages import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield  driver               ## devuelve un valor // pausa el fixture y permite que todo el test se corra
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    LoginPage(driver).abrir_pagina().login_completo("standard_user","secret_sauce")
    return driver

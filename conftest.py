import pytest
from selenium import webdriver
from utils import login

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield  driver               ## devuelve un valor // pausa el fixture y permite que todo el test se corra
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver
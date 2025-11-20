from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from utils.lector_json import leer_json_productos
from pages.inventory_page import inventoryPage
import time


RUTA_JSON= "datos/productos.json"

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
@pytest.mark.parametrize("nombre_producto",leer_json_productos(RUTA_JSON))

def test_inventory(login_in_driver,usuario,password,nombre_producto):
    try:
        driver = login_in_driver
        inventory_page = inventoryPage(driver)

        #agregar al carrito el producto
        inventory_page.agregar_producto_por_nombre(nombre_producto)

        #abrir el carrito
        inventory_page.abrir_carrito()
        time.sleep(2)

        #validar el producto 
        cartPage = cartPage(driver)

        assert cartPage.obtener_nombre_producto_carrito() == nombre_producto


    except Exception as e:
        print(f"Error en test_login: {e}")
        raise 
    finally:
        driver.quit()
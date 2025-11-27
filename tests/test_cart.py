from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from pages.inventory_page import inventoryPage
from pages.cart_page import CartPage

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver,usuario,password):
    try:
        driver = login_in_driver
        inventory_page = inventoryPage(driver)

        #agregar al carrito el producto
        inventory_page.agregar_primer_producto()

        #abrir el carrito
        inventory_page.abrir_carrito()

        #validar el producto
        cartPage = cartPage(driver)

        productos_en_carrito = cartPage.obtener_productos_carrito()
        assert len(productos_en_carrito)==1



    except Exception as e:
        print(f"Error en test_login: {e}")
        raise 
    finally:
        driver.quit()
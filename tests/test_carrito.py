from selenium.webdriver.common.by import By
from selenium import webdriver

def test_productos(login_in_driver):
    try:
        driver = login_in_driver
        
        # Busco nuevamente todos los productos
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        
        #Añadimos un productos al carrito con el primero producto
        products[0].find_element(By.TAG_NAME,"button").click()
        
        # Verificamos el texto del carrito
        carro = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
        carro_esperado = "1"
        
        #Validamos que contador del carrito cambio
        assert carro == carro_esperado,f"Fallo la Validacion. Esperado: {carro_esperado}, Actual {carro}"
        
        #Hacemos click en el carrito entrar a la misma
        carrito = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").click()
        
        # Verificamos que entro a cart
        assert "/cart.html" in driver.current_url,"No se Redirigio al inventario"
        
        # Busco un Elemento que esten dentro de la estructura con el nombre guardado
        producto_item_name = "Sauce Labs Backpack"
        carro_item = driver.find_element(By.XPATH,f"//div[@class='inventory_item_name']").text
        
        # Verificamos que en el XPATH exista ese nombre que corresponde al nombre del producto
        assert carro_item.startswith(producto_item_name),f"Fallo la verificacion. El producto {producto_item_name} no se encuentra"
        
    except Exception as e:
        print(f"El error fue: {e}")
        raise
    finally:
        driver.quit();       
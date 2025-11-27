import pytest


#Lista de archivos de pruebas a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_inventory.py",
    "tests/test_cart.py",
    "tests/test_cart_json.py"
    "tests/test_api_reqres.py"
]

#argumentos para ejecutar las pruebas: archivos + reporte html
pytest_args = test_files + ["--html=reportes/report.html", "--self-contained-html","-v"] # lo que genera lo hace adentro del html el scc

pytest.main(pytest_args)

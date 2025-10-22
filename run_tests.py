import pytest


#Lista de archivos de pruebas a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_inventory.py"
]

#argumentos para ejecutar las pruebas: archivos + reporte html
pytest_args = test_files + ["--html=report.html", "--self-contained-html","-v"] # lo que genera lo hace adentro del html el scc

pytest.main(pytest_args)

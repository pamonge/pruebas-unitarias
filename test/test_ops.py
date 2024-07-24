import allure
from src.ops import sumar, restar, promedio

@allure.description('Testeo de calculo de suma')
@allure.feature('Testeo de suma')
@allure.epic('Operaciones matematicas')
def test_sumar():
    res = sumar(2, 2)
    assert res == 4

@allure.description('Testeo de calculo de resta')
@allure.feature('Testeo de resta')
@allure.epic('Operaciones matematicas')
def test_restar():
    res = restar(2, 2)
    assert res == 0

@allure.description('Testeo de calculo de Promedio')
@allure.feature('Testeo de promedio')
@allure.epic('Operaciones matematicas')
def test_promedio():
    num = [1, 2, 3, 4, 5]
    res= promedio(num)
    assert res == 3

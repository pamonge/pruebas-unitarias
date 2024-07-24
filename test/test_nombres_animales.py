import allure
from src.animales import obtener_nombres_animales


@allure.description('Test para retornar una lista de nombres de animales')
@allure.feature('Animales')
@allure.epic('Lista de nombres')
def test_obtener_nombres ():
    nombres = obtener_nombres_animales()
    assert isinstance(nombres, list)

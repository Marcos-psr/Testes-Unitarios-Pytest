from codigo.bytebank import Funcionario
import pytest
from pytest import mark


class TestClass:

    @pytest.fixture
    def funcionario(self):
        return Funcionario("Lucas Carvalho", "13/03/2000", 1000)

    @pytest.fixture
    def socio(self):
        return Funcionario("Paulo Bragança", "10/10/1980", 100000)

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self, funcionario):
        esperado = 22
        resultado = funcionario.idade()

        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self, funcionario):
        esperado = "Carvalho"
        resultado = funcionario.sobrenome()

        assert resultado == esperado

    def test_quando_decresimo_salario_recebe_100000_deve_retornar_90000(self, socio):
        esperado = 90000

        socio.decresimo_salario()
        resultado = socio.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self, funcionario):
        esperado = 100
        resultado = funcionario.calcular_bonus()

        assert  resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self, socio):
        with pytest.raises(Exception):
            resultado = socio.calcular_bonus()

            assert resultado

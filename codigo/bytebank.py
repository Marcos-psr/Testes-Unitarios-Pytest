from datetime import date

class Funcionario:
    def __init__(self, nome: str, data_nascimento: str, salario: float):
        self.__nome = nome.capitalize()
        self.__data_nascimento = data_nascimento
        self.__salario = salario

    def __str__(self):
        return f'Funcionario({self.__nome}, {self.__data_nascimento}, {self.__salario})'

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def salario(self) -> float:
        return self.__salario

    def calcular_bonus(self) -> float:
        valor = self.__salario * 0.1
        if valor > 1000:
            raise Exception("O salário é muito alto para receber um bônus!")
        return valor

    def idade(self) -> int:
        datas = self.__data_nascimento.split("/")
        ano_nascimento = datas[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self) -> str:
        nome_completo = self.nome.strip()
        nome_sepearado = nome_completo.split(" ")
        return nome_sepearado[-1].capitalize()

    def _status_socio(self):
        sobrenomes_diretores = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return self.__salario >= 100000 and self.sobrenome() in sobrenomes_diretores

    def decresimo_salario(self):
        if self._status_socio():
            self.__salario -= (self.__salario * 0.1)


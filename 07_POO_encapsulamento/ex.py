# 1. Encapsulamento
# Proteger o salário para que só mude seguindo regras
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

        # Método para exibir informações do funcionário

    def apresentar(self):
        print(f"Sou {self.nome} e ganho R${self.__salario:.2f}")

    # Permite ler o salário como se fosse um atributo público
    @property
    def salario(self):
        return self.__salario

    def dar_aumento(self, porcentagem):
        if porcentagem <= 0:
            print(f"Aumento inválido para {self.nome}")
            return

        self.__salario = self.__salario * (1 + porcentagem / 100)
        print(f"{self.nome} recebeu {porcentagem}% de aumento.")


##################################################################################
ana = Funcionario(nome='Ana', salario=3000)
print(f"Salário inicial de {ana.nome}: R${ana.salario:.2f}")
ana.apresentar()
ana.dar_aumento(20)
ana.apresentar()
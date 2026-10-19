#A CLASSE: O modelo(a planta)
from types import coroutine


class Cachorro:
    def __init__(self, nome ,raça,idade = 8):
        self.nome = nome
        self.raça = raça
        self.idade = idade

    def latir(self):

            self.latir = True
            print(f" {self.nome} diz: Au Au!")

    def mostar_info(self):
        print(f"nome: {self.nome}, idade: {self.idade}, raça: {self.raça}")



cachorro1 = Cachorro( "rex","poodle", 8 )
cachorro2 = Cachorro( "thor","golden", 10 )

cachorro2.idade = "9"
print("alterou idade para",cachorro2.idade)

cachorro1.latir()
cachorro1.mostar_info()
cachorro2.mostar_info()




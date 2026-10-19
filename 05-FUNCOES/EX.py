#Oq ue é uma função

# Uma finção é um bloco de código criado para realizar
# Uma determinada tarefa
# Ela permite organizar e reutilizar código.

#1. Criando uma função
#utilizar a palavra def para uma função

def saudacao():
    print("Olá seja bem-vindo!")

saudacao()

#2. Criando uma função com parãmetro
#parâmetros permitem enviar informações para a função

def saudacao(nome):
        print(f"olá {nome}")

saudacao("Ana")
saudacao("João")

#3. Mais de um parâmetro
def apresentar(nome , idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")

apresentar(nome = "Maria", idade = 17)
apresentar(nome = "João", idade = 18)

#4. Função com calculo

def somar(num1, num2):
    resultado = num1 + num2
    print(f"Resultado {resultado}")
somar(num1 = 10, num2 = 20)
somar(num1 = 10, num2 = 90)

#5. Retornando um valor
# Devolve o valor para o local que a função foi chamada

def somar(num1, num2):
    return num1 + num2

print(somar(num1 = 10, num2 = 5))

#6 Função com condição
def verificarIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

print(verificarIdade(idade = 20))

#7 Parâmetro com valor padrão
def saudacao(nome="Aluno"):
    print(f"Ola {nome}")

saudacao("Joao")
saudacao()

#8 Função utilizando lista
def calcularMEDIA():
    for nota in notas:
        soma += nota

        return soma / len(notas)

notas = [8, 7, 9, 10]
media = calcularMedia(notas)
print(f"média: {media}")

#9. Funções para organizar um progama
def cadastrar_produto():

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    return nome, preco

def exibir_produto(nome, preco):

    print("\n=== PRODUTO ===")
    print(f"Nome: {nome}")
    print(f"Preço: {preco}")

nome, preco = cadastrar_produto()
exibir_produto(nome, preco)
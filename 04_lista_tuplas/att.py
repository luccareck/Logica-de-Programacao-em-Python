'''
1. Cadastro de filmes

Crie um programa para organizar uma lista de filmes. O programa deverá:

1. Criar uma lista contendo inicialmente 5 filmes.
2. Exibir todos os filmes cadastrados.
3. Exibir o primeiro filme da lista.
4. Exibir o último filme da lista.
5. Adicionar um novo filme ao final da lista.
6. Inserir um novo filme em uma posição específica.
7. Remover um filme da lista.
8. Alterar o nome de um dos filmes.
9. Exibir a quantidade de filmes cadastrados.
10. Verificar se um determinado filme está presente na lista. '''

#1:
filmes = ["Justice League", "Spider-man", "Batman", "Superman", "Iron Man"]

#2:
print("\nFilmes cadastrados: ")
print(filmes)

#3:
print("\nPrimeiro filme: ")
print(filmes[0])

#4:
print("\nÚltimo filme: ")
print(filmes[-1])

#5:
filmes.append("Ant Man")
print(filmes)

#6:
filmes.insert(1,"Captain America")
print(filmes)

#7:
filmes.remove("Superman")
print(filmes)

#8:
filmes[0] = "Avengers"
print(filmes)

#9:
print(f"\nA quantidade total de filmes é: {len(filmes)}")

#10:
if "Batman" in filmes:
    print("\nBatman está na lista")
else:
    print("\nBatman não está na lista")

'''
2. Controle de notas

Crie um programa para armazenar as notas de um estudante. O programa deverá:

1. Criar uma lista contendo 5 notas.
2. Exibir todas as notas.
3. Calcular a soma das notas.
4. Calcular a média das notas.
5. Identificar a maior nota.
6. Identificar a menor nota.
7. Verificar se existe uma nota igual a 10.
8. Informar se o estudante foi aprovado ou reprovado.
9. Considerar média igual ou superior a 7 como aprovação.
'''

#1:
notas = [8.0, 7.5, 6.0, 9.0, 10.0]

#2:
print("\nNotas do estudante: ")
print(notas)

#3:
soma = 0

for nota in notas:
    soma = soma + nota

print(f"\nA soma das notas é: {soma}")

#4:
media = soma / len(notas)

print(f"\nA média das notas é: {media}")

#5:
maior = notas[0]

for nota in notas:
    if nota > maior:
        maior = nota

print(f"\nA maior nota é: {maior}")

#6:
menor = notas[0]

for nota in notas:
    if nota < menor:
        menor = nota

print(f"\nA menor nota é: {menor}")

#7:
if 10 in notas:
    print("\nExiste uma nota igual a 10")
else:
    print("\nNão existe uma nota igual a 10")

#8 e #9:
if media >= 7:
    print("\nO estudante foi aprovado")
else:
    print("\nO estudante foi reprovado")

'''
3. Informações de um produto

Crie um programa para armazenar informações de um produto utilizando uma tupla.

A tupla deverá armazenar:

1. Nome do produto.
2. Categoria.
3. Preço.
4. Código do produto.

O programa deverá:

1. Exibir cada informação individualmente.
2. Exibir todas as informações utilizando uma estrutura de repetição.
3. Informar a quantidade de informações armazenadas.
4. Tentar alterar uma das informações da tupla.
5. Observar e explicar o que acontece ao tentar modificar um elemento.
'''

#1:
produto = ("Notebook", "Informática", 3500, 12345)

#2:
print("\nNome do produto: ")
print(produto[0])

print("\nCategoria: ")
print(produto[1])

print("\nPreço: ")
print(produto[2])

print("\nCódigo do produto: ")
print(produto[3])

#3:
print("\nInformações do produto: ")

for informacao in produto:
    print(informacao)

#4:
print(f"\nQuantidade de informações: {len(produto)}")

#5:
#produto[0] = "Computador"

print("\nNão é possível alterar uma informação da tupla.")
print("As tuplas não podem ser alteradas depois de criadas.")

'''
4. Cadastro de funcionário

Crie um programa para armazenar os dados de um funcionário utilizando um dicionário.

O cadastro deverá possuir:

1. Nome.
2. Idade.
3. Cargo.
4. Salário.
5. Setor.

O programa deverá:

1. Exibir cada informação do funcionário.
2. Alterar o salário do funcionário.
3. Adicionar uma nova informação ao cadastro.
4. Remover uma informação do cadastro.
5. Verificar se determinada chave existe.
6. Percorrer o dicionário exibindo as chaves e seus respectivos valores.
'''

#1:
funcionario = {
    "nome": "Carlos",
    "idade": 25,
    "cargo": "Programador",
    "salario": 3500,
    "setor": "Tecnologia"
}

#2:
print("\nNome: ")
print(funcionario["nome"])

print("\nIdade: ")
print(funcionario["idade"])

print("\nCargo: ")
print(funcionario["cargo"])

print("\nSalário: ")
print(funcionario["salario"])

print("\nSetor: ")
print(funcionario["setor"])

#3:
funcionario["salario"] = 4000

print("\nNovo salário: ")
print(funcionario["salario"])

#4:
funcionario["email"] = "carlos@email.com"

print("\nCadastro com nova informação: ")
print(funcionario)

#5:
funcionario.pop("idade")

print("\nCadastro após remover a idade: ")
print(funcionario)

#6:
if "cargo" in funcionario:
    print("\nA chave cargo existe no cadastro")
else:
    print("\nA chave cargo não existe no cadastro")

#7:
print("\nInformações do funcionário: ")

for chave in funcionario:
    print(chave, ":", funcionario[chave])

'''
5. Sistema de estoque

Uma loja de informática deseja organizar seu estoque.

Crie uma estrutura utilizando uma lista de dicionários para armazenar pelo menos 5 produtos.

Cada produto deverá possuir:

1. Nome.
2. Categoria.
3. Preço.
4. Quantidade em estoque.

O programa deverá:

1. Exibir todos os produtos cadastrados.
2. Exibir o nome, preço e quantidade em estoque de cada produto.
3. Calcular a quantidade total de itens armazenados no estoque.
4. Calcular o valor total do estoque.
5. Identificar os produtos que possuem menos de 10 unidades disponíveis.
6. Verificar se determinado produto está cadastrado.
7. Alterar a quantidade em estoque de um produto.
8. Adicionar um novo produto.
9. Exibir um relatório final com todos os produtos e suas respectivas informações.
'''

#1:
estoque = [
    {
        "nome": "Notebook",
        "categoria": "Informática",
        "preco": 3500,
        "quantidade": 8
    },
    {
        "nome": "Mouse",
        "categoria": "Periféricos",
        "preco": 80,
        "quantidade": 15
    },
    {
        "nome": "Teclado",
        "categoria": "Periféricos",
        "preco": 150,
        "quantidade": 7
    },
    {
        "nome": "Monitor",
        "categoria": "Informática",
        "preco": 1200,
        "quantidade": 12
    },
    {
        "nome": "Headset",
        "categoria": "Periféricos",
        "preco": 200,
        "quantidade": 5
    }
]

#2:
print("\nProdutos cadastrados: ")
print(estoque)

#3:
print("\nInformações dos produtos: ")

for produto in estoque:
    print("Nome:", produto["nome"])
    print("Preço:", produto["preco"])
    print("Quantidade:", produto["quantidade"])
    print()

#4:
quantidade_total = 0

for produto in estoque:
    quantidade_total = quantidade_total + produto["quantidade"]

print(f"A quantidade total de itens no estoque é: {quantidade_total}")

#5:
valor_total = 0

for produto in estoque:
    valor = produto["preco"] * produto["quantidade"]
    valor_total = valor_total + valor

print(f"\nO valor total do estoque é: R$ {valor_total}")

#6:
print("\nProdutos com menos de 10 unidades: ")

for produto in estoque:
    if produto["quantidade"] < 10:
        print(produto["nome"])

#7:
nome_produto = "Mouse"

encontrado = False

for produto in estoque:
    if produto["nome"] == nome_produto:
        encontrado = True

if encontrado:
    print(f"\n{nome_produto} está cadastrado")
else:
    print(f"\n{nome_produto} não está cadastrado")

#8:
for produto in estoque:
    if produto["nome"] == "Mouse":
        produto["quantidade"] = 20

print("\nQuantidade do Mouse alterada.")

#9:
novo_produto = {
    "nome": "Webcam",
    "categoria": "Periféricos",
    "preco": 300,
    "quantidade": 6
}

estoque.append(novo_produto)

#10:
print("\nRelatório final do estoque: ")

for produto in estoque:
    print("Nome:", produto["nome"])
    print("Categoria:", produto["categoria"])
    print("Preço:", produto["preco"])
    print("Quantidade:", produto["quantidade"])
    print("-------------------------")
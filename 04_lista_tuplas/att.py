# ==========================================
# 1. CADASTRO DE FILMES
# ==========================================

# 1. Lista inicial com 5 filmes
catalogo = ["Matrix", "Gladiador", "Inception", "Interstellar", "O Poderoso Chefão"]

# 2. Exibir todos
print("Catálogo atual de filmes:")
print(catalogo)

# 3. Primeiro filme
print(f"\nPrimeiro da lista: {catalogo[0]}")

# 4. Último filme
print(f"Último da lista: {catalogo[-1]}")

# 5. Adicionar ao final
catalogo.append("O Senhor dos Anéis")
print(f"\nApós adicionar no final: {catalogo}")

# 6. Inserir em posição específica (índice 1)
catalogo.insert(1, "O Sétimo Selo")
print(f"Após inserção na posição 1: {catalogo}")

# 7. Remover filme
catalogo.remove("Gladiador")
print(f"Após remover Gladiador: {catalogo}")

# 8. Alterar o nome de um filme
catalogo[0] = "Matrix Reloaded"
print(f"Após alterar o primeiro filme: {catalogo}")

# 9. Quantidade de filmes
print(f"\nTotal de títulos cadastrados: {len(catalogo)}")

# 10. Verificar presença de um filme
busca = "Inception"
if busca in catalogo:
    print(f"O filme '{busca}' está presente no catálogo.")
else:
    print(f"O filme '{busca}' não foi encontrado.")


# ==========================================
# 2. CONTROLE DE NOTAS
# ==========================================

# 1. Lista de notas
notas_aluno = [7.5, 8.0, 6.5, 9.5, 10.0]

# 2. Exibir notas
print("\nNotas registradas:", notas_aluno)

# 3. Calcular a soma
soma_notas = 0
for n in notas_aluno:
    soma_notas += n
print(f"Soma das notas: {soma_notas}")

# 4. Calcular a média
media_final = soma_notas / len(notas_aluno)
print(f"Média final: {media_final:.2f}")

# 5. Maior nota
maior_nota = notas_aluno[0]
for n in notas_aluno:
    if n > maior_nota:
        maior_nota = n
print(f"Maior nota obtida: {maior_nota}")

# 6. Menor nota
menor_nota = notas_aluno[0]
for n in notas_aluno:
    if n < menor_nota:
        menor_nota = n
print(f"Menor nota obtida: {menor_nota}")

# 7. Verificar se existe nota 10
if 10.0 in notas_aluno:
    print("O aluno tirou pelo menos uma nota 10.0!")
else:
    print("Nenhuma nota 10.0 foi encontrada.")

# 8 e 9. Situação de aprovação (média >= 7)
if media_final >= 7.0:
    print("Resultado: APROVADO")
else:
    print("Resultado: REPROVADO")


# ==========================================
# 3. INFORMAÇÕES DE UM PRODUTO (TUPLA)
# ==========================================

# 1. Definição da tupla
detalhes_produto = ("Smartphone Galaxy", "Eletrônicos", 2800.00, 98765)

# 2. Exibição individual
print("\n--- Detalhes do Produto ---")
print(f"Nome: {detalhes_produto[0]}")
print(f"Categoria: {detalhes_produto[1]}")
print(f"Preço: R$ {detalhes_produto[2]}")
print(f"Código: {detalhes_produto[3]}")

# 3. Exibição com loop
print("\nPercorrendo a tupla:")
for campo in detalhes_produto:
    print(f"- {campo}")

# 4. Quantidade de informações
print(f"\nTotal de atributos armazenados: {len(detalhes_produto)}")

# 5. Tentativa de alteração
# detalhes_produto[0] = "Smartphone Pro"
print("\nTentativa de modificação: Tuplas são imutáveis e geram um TypeError caso tente alterar algum valor diretamente.")


# ==========================================
# 4. CADASTRO DE FUNCIONÁRIO (DICIONÁRIO)
# ==========================================

# 1. Dicionário inicial
colaborador = {
    "nome": "Mariana Santos",
    "idade": 28,
    "cargo": "Analista de Dados",
    "salario": 4200.00,
    "setor": "BI"
}

# 2. Exibir informações individualmente
print(f"\nNome do colaborador: {colaborador['nome']}")
print(f"Idade: {colaborador['idade']}")
print(f"Cargo atual: {colaborador['cargo']}")
print(f"Salário: R$ {colaborador['salario']}")
print(f"Setor de atuação: {colaborador['setor']}")

# 3. Alterar salário
colaborador["salario"] = 4800.00
print(f"\nSalário atualizado: R$ {colaborador['salario']}")

# 4. Adicionar nova informação
colaborador["email"] = "mariana.santos@empresa.com"

# 5. Remover informação
del colaborador["idade"]

# 6. Verificar se chave existe
if "cargo" in colaborador:
    print("A chave 'cargo' existe no cadastro.")

# 7. Percorrer o dicionário (chaves e valores)
print("\n--- Ficha Cadastral Atualizada ---")
for chave, valor in colaborador.items():
    print(f"{chave.capitalize()}: {valor}")


# ==========================================
# 5. SISTEMA DE ESTOQUE
# ==========================================

# 1. Lista de dicionários
inventario = [
    {"nome": "Teclado Mecânico", "categoria": "Periféricos", "preco": 250.00, "quantidade": 6},
    {"nome": "Mouse Sem Fio", "categoria": "Periféricos", "preco": 90.00, "quantidade": 18},
    {"nome": "Monitor 24'", "categoria": "Monitores", "preco": 850.00, "quantidade": 4},
    {"nome": "Cabo HDMI", "categoria": "Acessórios", "preco": 30.00, "quantidade": 25},
    {"nome": "Headset Gamer", "categoria": "Áudio", "preco": 320.00, "quantidade": 8}
]

# 2. Exibir todos os produtos
print("\nEstoque cadastrado:", inventario)

# 3. Exibir dados resumidos
print("\n--- Lista de Produtos ---")
for item in inventario:
    print(f"Item: {item['nome']} | Preço: R$ {item['preco']} | Qtd: {item['quantidade']}")

# 4. Total de unidades
qtd_total_itens = 0
for item in inventario:
    qtd_total_itens += item["quantidade"]
print(f"\nQuantidade total de produtos no estoque: {qtd_total_itens}")

# 5. Valor total do estoque
valor_acumulado = 0.0
for item in inventario:
    valor_acumulado += item["preco"] * item["quantidade"]
print(f"Valor financeiro total em estoque: R$ {valor_acumulado:.2f}")

# 6. Produtos com estoque baixo (< 10)
print("\nProdutos com menos de 10 unidades:")
for item in inventario:
    if item["quantidade"] < 10:
        print(f"- {item['nome']} ({item['quantidade']} un.)")

# 7. Verificar se determinado produto está cadastrado
item_busca = "Mouse Sem Fio"
cadastrado = any(item["nome"] == item_busca for item in inventario)
if cadastrado:
    print(f"\nO item '{item_busca}' está cadastrado no sistema.")

# 8. Alterar quantidade de um produto
for item in inventario:
    if item["nome"] == "Mouse Sem Fio":
        item["quantidade"] = 22
        break

# 9. Adicionar novo produto
novo_item = {
    "nome": "Webcam HD",
    "categoria": "Vídeo",
    "preco": 210.00,
    "quantidade": 12
}
inventario.append(novo_item)

# 10. Relatório final
print("\n================ RELATÓRIO FINAL DE ESTOQUE ================")
for item in inventario:
    print(f"Produto: {item['nome']}")
    print(f"Categoria: {item['categoria']}")
    print(f"Preço Unitário: R$ {item['preco']:.2f}")
    print(f"Em Estoque: {item['quantidade']}")
    print("-" * 40)
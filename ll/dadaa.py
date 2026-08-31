idade = 20
possui_carteira = True

resultado = idade >= 18 and possui_carteira
print(resultado)


idade = 16
acompanhado = True

resultado = idade >= 18 or acompanhado
print(resultado)

aluno_matricula = True
print(not aluno_matricula)

idade = 18

print(idade == 18)
print(idade != 18)
print(idade > 18)
print(idade < 18)
print(idade >= 18)
print(idade <= 18)

idade = 18

if idade >= 18:
    print("maior de idade")


idade = 16
if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")

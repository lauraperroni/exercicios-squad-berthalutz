'''
  Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0.

Responsável: Cláudia
'''

medias_alunos = []
alunos_aprovados = []

for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    notas = [float(input(f"Informe a nota {j+1} para {nome}: ")) for j in range(4)]

    media = sum(notas) / len(notas)

    medias_alunos.append((nome, media))

    if media >= 7.0:
        alunos_aprovados.append((nome, media))

print(f"\nNúmero de alunos aprovados: {len(alunos_aprovados)}")
for nome, media in alunos_aprovados:
    print(f"{nome} teve média {media} e está aprovado.")
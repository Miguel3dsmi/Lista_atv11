'''9. Dada a lista de tuplas abaixo:
pessoas = [("Ana", 30, "Porto Alegre"), ("Bruno", 25, "Canoas"), ("Carla", 30, "Porto Alegre"), ("Diego", 22, "Canoas")]
Ordene por idade e, em caso de empate, por nome.
Crie um dicionário que agrupe os nomes por cidade, usando set como valor: {"Porto Alegre": {"Ana", "Carla"}, ...}.'''
from collections import defaultdict

pessoas = [("Ana", 30, "Porto Alegre"), ("Bruno", 25, "Canoas"), ("Carla", 30, "Porto Alegre"), ("Diego", 22, "Canoas"), ("Matheus", 35, "Osorio")]
pessoas_organizada = sorted(pessoas, key=lambda p: (p[1], p[0]))
print(f"Lista organizada em ordem de idade: {pessoas_organizada}")

po_cidade = defaultdict(set)
for nome, _, cidade in pessoas:
    po_cidade[cidade].add(nome)
cidades = dict(po_cidade)

print(f"Pessoas que vivem em cidades: {cidades}")
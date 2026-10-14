'''1. Crie uma tupla com 5 nomes de frutas. Mostre o primeiro, o último, o tamanho da tupla e as 3 primeiras frutas (fatiamento).'''
frutas = ("Maça","Amora","Abacaxi","Banana","Limão")
print(frutas[0])
print(frutas[-1])
print(len(frutas))
for i in range(3):
    print(f"{frutas[i]} ", end="")
'''4. Crie uma função estatisticas(numeros) que receba uma lista e retorne uma tupla com (menor, maior, média).
Na chamada, use desempacotamento para guardar os três valores em variáveis e imprimi-los.'''
def estatisticas(lista):
    media = sum(lista) / len(lista)
    return min(lista), max(lista), media

numeros = []
for i in range(6):
    num = int(input("Digite um numero: "))
    numeros.append(num)
menor, maior, media = estatisticas(numeros)

print(f"Maior valor: {maior}\nMenor valor: {menor}\nMédia: {media:.2f}")
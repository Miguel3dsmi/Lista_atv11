'''8. Escreva uma função remover_duplicados(lista) que remova os repetidos mantendo a ordem original. Dica:
set(lista) perde a ordem, então use um set auxiliar para registrar o que já foi visto.
Exemplo: [4, 1, 4, 2, 1, 3] → [4, 1, 2, 3]'''
def remover_duplicados(lista):
    visto = set()
    unico = []
    for num in lista:
        if num not in visto:
           unico.append(num)
           visto.add(num)
        else:
            continue
    return unico

num = 1
lista = []
while num != 0:
    num = int(input("informe um numero (digite 0 para encerrar): "))
    if num != 0:
        lista.append(num)
    else:
        continue
lista_unica = remover_duplicados(lista)
print(lista_unica)

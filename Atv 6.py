'''6. Crie um dicionário que use tuplas como chave para representar coordenadas (x, y) e como valor o nome do local
(ex.: (0, 0): "Casa"). Peça ao usuário um x e um y e informe qual local está ali, ou que não existe nada nessa posição.'''
x = int(input("informe o valor de X: "))
y = int(input("informe o valor de Y: "))
chave = (x,y)
nome = input("informe o nome do local: ")
coordenadas = {chave : nome}
print(coordenadas)
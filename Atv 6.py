'''6. Crie um dicionário que use tuplas como chave para representar coordenadas (x, y) e como valor o nome do local
(ex.: (0, 0): "Casa"). Peça ao usuário um x e um y e informe qual local está ali, ou que não existe nada nessa posição.'''
locais = {(0,0):"Casa", (10,90):"Escola",(66,66):"Igreja", (5,5):"Serviço"}
x = int(input("informe o valor de X: "))
y = int(input("informe o valor de Y: "))
coordenadas = (x,y)
if coordenadas in locais:
    print(f"{locais[coordenadas]} encontrada.")
else:
    print(f"Coordenadas não encontrada no dicionário.")
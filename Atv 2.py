'''2. Crie uma tupla com 3 números e tente alterar o primeiro elemento. Use try/except para capturar o erro e mostrar uma mensagem amigável.'''
numeros = (13,14,15)
try:
    num = int(input("Digite um número: "))
    numeros[0] = num
except TypeError:
    print(f"Tuplas não permitem mudanças, por a tupla números permanece: {numeros}")


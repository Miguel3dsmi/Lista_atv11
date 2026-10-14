'''7. Peça uma frase ao usuário e mostre quantas palavras diferentes ela tem, ignorando maiúsculas/minúsculas e pontuação básica (., ,, !, ?).
Exemplo: "Oi, oi! Tudo bem? Tudo." → 3 palavras diferentes (oi, tudo, bem).'''
import string

frase = input("Digite uma frase: ").lower().translate(str.maketrans('', '', string.punctuation))
conjunto = set(frase.split())
print(conjunto)
print(f"Total de palavras únicas: {len(conjunto)}")

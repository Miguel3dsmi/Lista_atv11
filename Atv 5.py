'''5. Dados dois sets, python = {"Ana", "Bruno", "Carlos", "Diana"} e sql = {"Carlos", "Diana", "Eduardo", "Fernanda"}, mostre:
A) quem faz os dois cursos
B) quem faz apenas SQL
C) todos os alunos, sem repetição'''

python = {"Ana", "Bruno", "Carlos", "Diana"}
sql = {"Carlos", "Diana", "Eduardo", "Fernanda"}
a = python & sql
b = sql - python
c = python | sql
print(f"Alunos que fazem ambos cursos: {a}\nAlunos que fazem apenas o curso de SQL: {b}\nTodos os alunos: {c}")
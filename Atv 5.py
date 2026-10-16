'''5. Dados dois sets, python = {"Ana", "Bruno", "Carlos", "Diana"} e sql = {"Carlos", "Diana", "Eduardo", "Fernanda"}, mostre:
A) quem faz os dois cursos
B) quem faz apenas Python
C) quem faz apenas SQL
D) todos os alunos, sem repetição'''

python = {"Ana", "Bruno", "Carlos", "Diana"}
sql = {"Carlos", "Diana", "Eduardo", "Fernanda"}
a = python & sql
b = python - sql
c = sql - python
d = python | sql
print(f"Alunos que fazem ambos cursos: {a}\nAlunos que fazem apenas o curso de Python: {b}\nAlunos que fazem apenas o curso de SQL: {c}\nTodos os alunos: {d}")
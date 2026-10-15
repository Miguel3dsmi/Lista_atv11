'''10. Sistema de sugestão de amigos. Dado o dicionário:
amigos = {"Ana": {"Bruno", "Carla"}, "Bruno": {"Ana", "Diego"}, "Carla": {"Ana", "Diego", "Eva"}, "Diego": {"Bruno", "Carla"}, "Eva": {"Carla"},}
Crie uma função sugerir(pessoa) que retorne os “amigos de amigos” que a pessoa ainda não tem como amigo e que não sejam ela mesma.
Crie também em_comum(p1, p2) que retorne os amigos em comum de duas pessoas.
Exemplo: sugerir("Ana") → {"Diego", "Eva"}'''
def recomendados (amigos,pessoa):
    sugestao = []
    visto = set()
    print(f"-- Usuario: {pessoa}")
    print("Amigos: ", end="")
    for usuario in amigos:
        if usuario == pessoa:
            for i, lista_amigos in enumerate(amigos[usuario]):
                if i != len(amigos[usuario]) - 1:
                    print(f"{lista_amigos}, ", end="")
                else:
                    print(f"{lista_amigos}.", end="")
                for amigos_de_amigos in amigos[lista_amigos]:
                    if amigos_de_amigos not in amigos[usuario] and amigos_de_amigos != pessoa and amigos_de_amigos not in visto:
                        sugestao.append(amigos_de_amigos)
                        visto.add(amigos_de_amigos)
                    else:
                        continue
        else:
            continue
        print()
    return sugestao

def em_comum(amigos, pessoa):
    marco = set()
    for usuario in amigos:
        igual = []
        visto = set()
        if usuario == pessoa:
            for lista_amigos in amigos[usuario]:
                marco.add(lista_amigos)
        else:
            for lista_amigos in amigos[usuario]:
                if lista_amigos in marco:
                    if lista_amigos not in visto:
                        igual.append(lista_amigos)
                        visto.add(lista_amigos)
            if igual:
                print(f"Os amigos em comum entre {alvo} e {usuario} são: {igual}")
            else:
                print(f"{alvo} e {usuario} Não possuem amigos em comum.")
    print()

social = {"Ana": {"Bruno", "Carla"},
          "Bruno": {"Ana", "Diego"},
          "Carla": {"Ana", "Diego", "Eva"},''
          "Diego": {"Bruno", "Carla"},
          "Eva": {"Carla"}}

for pessoa in social:
    alvo = pessoa
    sugestao = recomendados(social, alvo)
    print(f"Sugestão de amigos para {alvo}: {sugestao}\n")
    em_comum(social, alvo)
def sugerir(amigos):
    sugestao = []
    amigos_vistos = set()
    usuarios_vistos = set()
    for usuario in amigos:
        if usuario in usuarios_vistos:
            continue
        else:
            print(f"-- Usuario: {usuario}")
            print("Amigos: ", end="")
            for i, amigo in enumerate(amigos[usuario]):
                if i != len(amigos[usuario]) - 1:
                    print(f"{amigo}, ", end="")
                else:
                    print(f"{amigo}.", end="")
                for amigos_recomendados in amigos(amigo):
                    if amigos_recomendados not in amigos[
                        usuario] and amigos_recomendados != usuario and amigos_recomendados not in amigos_vistos:
                        sugestao.append(amigos_recomendados)
                        amigos_vistos.add(amigos_recomendados)
                print()
        usuarios_vistos.add(usuario)
    return sugestao

social = {"Ana": {"Bruno", "Carla"},
          "Bruno": {"Ana", "Diego"},
          "Carla": {"Ana", "Diego", "Eva"},
          "Diego": {"Bruno", "Carla"},
          "Eva": {"Carla"}}

for pessoa in social:
    sugestao = sugerir(social)
    print(f"Sugestão de amigos para {pessoa}: {sugestao}\n")
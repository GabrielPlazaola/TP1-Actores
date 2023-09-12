def top_10_pokemon(pokemon_lista, caracteristica):
    # Ordena la lista de Pokémon en función de la característica especificada
    pokemon_ordenados = sorted(pokemon_lista, key=lambda x: int(x[caracteristica]), reverse=True)

    # Devuelve los 10 primeros Pokémon
    top_10 = pokemon_ordenados[:10]

    return top_10
import requests
from bs4 import BeautifulSoup

# URL de la página web del Pokémon específico (por ejemplo, Bulbasaur)
url_pokemon = 'https://www.wikidex.net/wiki/Bulbasaur'  # Reemplaza 'URL_DEL_POKEMON' con la URL real del Pokémon

# Realizar una solicitud GET a la página del Pokémon
response = requests.get(url_pokemon)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Crear un objeto BeautifulSoup para analizar el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Buscar la sección de "Características de combate"
    caracteristicas_section = soup.find('span', {'id': 'Características_de_combate'})

    if caracteristicas_section:
        # Encontrar la tabla que contiene las características base
        tabla_caracteristicas = caracteristicas_section.find_next('table', {'class': 'tabpokemon'})

        if tabla_caracteristicas:
            # Buscar la fila que contiene la velocidad base
            filas = tabla_caracteristicas.find_all('tr')
            velocidad_base = None

            fila = filas[6]
            celdas = fila.find_all('td')
            velocidad_base = celdas[0].text.strip()

            if velocidad_base:
                print(f'Velocidad Base: {velocidad_base}')
            else:
                print('No se encontró la velocidad base.')

        else:
            print('No se encontró la tabla de características.')

    else:
        print('No se encontró la sección de "Características de combate".')

else:
    print('Error al realizar la solicitud a la página del Pokémon.')
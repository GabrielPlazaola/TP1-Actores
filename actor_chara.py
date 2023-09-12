import ray
import time
import requests
from bs4 import BeautifulSoup

# Define un actor remoto
@ray.remote
class MyActorChara:
    def __init__(self):
        self.value = 0

    def increment(self):
        time.sleep(3)
        self.value += 1
        return self.value
    
    def buscarpokemon(self, poke, carac):
        # URL de la página web del Pokémon específico (por ejemplo, Bulbasaur)
        url_pokemon = 'https://www.wikidex.net' + poke['Url']

        # Realizar una solicitud GET a la página del Pokémon
        response = requests.get(url_pokemon)
        num = 1

        caracsbase = ["PS","Ataque","Defensa","At. esp.","Def. esp.","Velocidad"]
        num = caracsbase.index(carac) - 1

        if carac == "PS":
            num = 1
        elif carac == "Ataque":
            num = 2
        elif carac == "Defensa":
            num = 3
        elif carac == "At. esp.":
            num = 4
        elif carac == "Def. esp.":
            num = 5
        elif carac == "Velocidad":
            num = 6

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
                    carac_base = None

                    fila = filas[num]
                    celdas = fila.find_all('td')
                    carac_base = celdas[0].text.strip()

                    if carac_base:
                        #print(f'Velocidad Base: {velocidad_base}')
                        poke[carac] = carac_base
                        return poke
                    else:
                        print('No se encontró la velocidad base.')

                else:
                    print('No se encontró la tabla de características.')

            else:
                print('No se encontró la sección de "Características de combate".')

        else:
            print('Error al realizar la solicitud a la página del Pokémon.')
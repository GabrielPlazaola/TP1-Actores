import requests
from bs4 import BeautifulSoup

# URL de la página web que contiene las tablas de generaciones de Pokémon
url = 'https://www.wikidex.net/wiki/Lista_de_Pok%C3%A9mon'

# Realizar una solicitud GET a la página
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Crear un objeto BeautifulSoup para analizar el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Buscar la fila que contiene el número 0001
    target_row = None
    target_table = None

    # Iterar a través de todas las tablas en la página
    for table in soup.find_all('table'):
        for row in table.find_all('tr'):
            # Verificar si la fila contiene el número 0001
            if '0001' in row.get_text():
                target_row = row
                target_table = table
                break
        if target_row:
            break

    # Verificar si se encontró la fila que contiene el número 0001
    if target_row:
        # Iterar a través de las filas de la tabla objetivo

        pokemones = []

        for row in target_table.find_all('tr'):
            # Obtener las celdas de la fila
            cells = row.find_all('td')

            # Verificar si hay suficientes celdas en la fila
            if len(cells) >= 4:
                # Extraer los datos relevantes de las celdas
                numero = cells[0].text.strip()
                nombre = cells[1].text.strip()
                japones = cells[3].text.strip()

                tipos = []
                for img in cells[2].find_all('img'):
                    tipo = img.get('alt', '').replace('Tipo ', '')
                    tipos.append(tipo.strip())
                
                url_pokemon = cells[1].find('a')['href']

                # Imprimir los datos extraídos
                print(f'Número: {numero}')
                print(f'Nombre: {nombre}')
                print(f'Tipos: {tipos}')
                print(f'Japonés: {japones}')
                print(f'Url: {url_pokemon}')
                print('-' * 40)  # Separador
                dic = {'Numero': numero, 'Nombre': nombre, 'Tipos': tipos, 'Url': url_pokemon}
                pokemones.append(dic)

    else:
        print('No se encontró la fila que contiene el número 0001 en ninguna tabla.')

else:
    print('Error al realizar la solicitud a la página.')

print(pokemones)
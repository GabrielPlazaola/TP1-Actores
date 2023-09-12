import requests
from bs4 import BeautifulSoup

# URL de la página de IMDb que deseas raspar
url = 'https://www.imdb.com/chart/top/'

# Realiza una solicitud HTTP para obtener la página
response = requests.get(url)
print(requests.get(url))

# Comprueba si la solicitud fue exitosa
if response.status_code == 200:
    # Analiza la página web con Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encuentra la tabla que contiene la lista de las 250 mejores películas
    movie_table = soup.find('table', {'class': 'chart full-width'})

    # Encuentra todas las filas de la tabla
    rows = movie_table.find_all('tr')

    # Itera a través de las filas para extraer información
    for row in rows[1:]:  # Omite la primera fila (encabezados)
        # Extrae el título de la película
        title = row.find('td', {'class': 'titleColumn'}).a.text
        # Extrae el año de la película
        year = row.find('span', {'class': 'secondaryInfo'}).text.strip('()')

        print(f'Título: {title}, Año: {year}')
else:
    print('Error al obtener la página de IMDb')

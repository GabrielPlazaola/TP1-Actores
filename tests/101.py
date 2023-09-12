import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.mercadolibre.com.ar/smart-tv-philips-7400-series-50pud740677-led-android-10-4k-50-110v240v/p/MLA18607070?pdp_filters=deal:MLA779357-1#searchVariation=MLA18607070&position=2&search_layout=grid&name=product&tracking_id=cfb6dfbb-4dbd-43e2-8622-070b5995432a&c_id=/home/promotions-recommendations/element&c_element_order=2&c_uid=79aa50a5-aded-43a9-980e-d0f7ed94bd0f'
response = requests.get(url)

if response.status_code == 200:
    html = response.text

# Analiza el contenido HTML
soup = BeautifulSoup(html, 'html.parser')

# Encuentra el elemento <head>
head = soup.find('head')

# Encuentra el título de la página
titulo = head.find('title').text

# Encuentra la descripción de la página (a menudo en una etiqueta meta)
descripcion = head.find('meta', attrs={'name': 'description'})
if descripcion:
    descripcion = descripcion.get('content')

name = soup.find("meta", property="og:name")
url = soup.find("meta", property="og:url")

print(name["content"] if name else "No meta name given")
print(url["content"] if url else "No meta url given")

# Encuentra otras etiquetas meta relevantes (por ejemplo, palabras clave)
palabras_clave = head.find('meta', attrs={'name': 'keywords'})
if palabras_clave:
    palabras_clave = palabras_clave.get('content')

# Imprime la metadata
#print(f'Título: {titulo}')
#print(f'Descripción: {descripcion}')
#print(f'Palabras clave: {palabras_clave}')

json_script = soup.find('script', {'type': 'application/ld+json'})

# Verifica si se encontró un script
if json_script:
    # Obtiene el contenido del script como texto
    json_text = json_script.string

    # Parsea el JSON
    try:
        data = json.loads(json_text)

        # Ahora puedes acceder a los datos en el JSON
        name = data.get('name', '')
        image = data.get('image', '')
        gtin14 = data.get('gtin14', '')
        description = data.get('description', '')
        brand = data.get('brand', '')
        sku = data.get('sku', '')
        offers = data.get('offers', '')

        # Imprime la información
        print(f'Nombre: {name}')
        print(f'Imagen: {image}')
        print(f'GTIN14: {gtin14}')
        print(f'Descripción: {description}')
        print(f'Marca: {brand}')
        print(f'SKU: {sku}')
        print(f'Precio: {offers}')

    except json.JSONDecodeError as e:
        print('Error al analizar JSON:', e)
else:
    print('No se encontró un script con type="application/ld+json" en el HTML.')
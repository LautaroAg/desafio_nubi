import requests
import json
from datetime import datetime
import os
import sys

if len(sys.argv) == 2:  # utiliza una url recibida como parametro o una por defecto
    url = sys.argv[1]
else:
    url = "https://api.mercadolibre.com/sites/MLA/search?category=MLA1000"
try:
    res = requests.get(url)
except Exception as e:
    print(e)
    exit(1)

try:  # Para el nombre del directorio elige 'search' si es que esta en la url, sino elige lo que quede despues de la ultima barra
    directory = f'./{"search" if "search" in url else url.split("/")[-1].split("?")[0]}json{datetime.today().strftime("%Y%m%d")}/'
    os.mkdir(directory)
except:  # directory already exists
    pass

# por ahora sobreescribe el archivo si ya existe
with open(f'{directory}/jsonfile.json','w') as thisone:
    json.dump(res.json(),thisone)
print(f'Archivo creado en {directory}')
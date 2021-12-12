from os import pathsep
import requests

URL="https://mapa.pid.cz/getData.php"

r= requests.get(URL)
data = r.json()
vehicles = data["trips"].values()
print(vehicles)



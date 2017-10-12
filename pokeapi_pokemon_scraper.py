import requests
import requests_cache
import json

requests_cache.install_cache()

url = "http://pokeapi.co/api/v2/pokemon/"

pokemon = []
pokemon_full = []

f = open("pokemon.json", "w")

while True:

    r = requests.get(url)

    rjson = r.json()
    pokemon = pokemon + rjson['results']
    url = rjson['next']
    if (url is None):
        break
    print(rjson['next'])

for i in pokemon:
    r = requests.get(i['url'])
    rjson = r.json()

    for j in i['moves']:
        pass
    print(i["url"])
    pokemon_full.append(rjson)
f.write(json.dumps(pokemon_full))

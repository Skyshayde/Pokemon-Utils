import requests
import requests_cache
import json

requests_cache.install_cache()

url = "http://pokeapi.co/api/v2/move/"

moves = []
moves_full = []

f = open("movelist.json", "w")

while True:

    r = requests.get(url)

    rjson = r.json()
    moves = moves + rjson['results']
    url = rjson['next']
    if (url is None):
        break
    print(rjson['next'])

for i in moves:
    r = requests.get(i['url'])
    rjson = r.json()
    rjson.pop("generation")
    rjson.pop("contest_combos")
    rjson.pop("contest_type")
    rjson.pop("contest_effect")
    rjson.pop("super_contest_effect")
    rjson['names'] = rjson['names'][0]
    rjson.pop("flavor_text_entries")
    print(i["url"])
    moves_full.append(rjson)
f.write(json.dumps(moves_full))

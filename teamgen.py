from Enums import Nature
import json
import random


class Pokemon():
    """docstring for Pokemon"""

    def __init__(self, pokemon):
        super(Pokemon, self).__init__()

        self.nature = Nature.HARDY

        self.ivs = {}
        self.ivs['hp'] = 0
        self.ivs['atk'] = 0
        self.ivs['def'] = 0
        self.ivs['spatk'] = 0
        self.ivs['spdef'] = 0
        self.ivs['spe'] = 0

        self.evs = {}
        self.evs['hp'] = 0
        self.evs['atk'] = 0
        self.evs['def'] = 0
        self.evs['spatk'] = 0
        self.evs['spdef'] = 0
        self.evs['spe'] = 0

        self.move1 = 0
        self.move2 = 0
        self.move3 = 0
        self.move4 = 0


class Trainer():

    def __init__(self, trainertype, difficulty, level, amount):
        trainer = json.loads(open("trainertype.json", "r").read())
        available_pokemon = []
        trainer = trainer['trainers'][trainertype]
        for i in trainer['pokemon']:
            if level in range(int(i['range'].split("-")[0]), int(i['range'].split("-")[1])):
                for j in range(i['chance']):
                    available_pokemon.append(i["name"])
        self.pokemon = []
        for i in range(amount):
            no = random.randrange(len(available_pokemon))
            self.pokemon.append(available_pokemon[no])
        print(json.dumps(self.pokemon, sort_keys=True,
                         indent=4, separators=(',', ': ')))

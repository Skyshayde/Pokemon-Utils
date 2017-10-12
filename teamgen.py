from Enums import Nature

class Pokemon():
    """docstring for Pokemon"""

    def __init__(self):
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
    def __init__(self, trainertype, available_pokemon):
        return

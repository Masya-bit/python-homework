from address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address       # тип Address (кому)
        self.from_address = from_address   # тип Address (от кого)
        self.cost = cost                   # число (стоимость)
        self.track = track                 # строка (трек-номер)
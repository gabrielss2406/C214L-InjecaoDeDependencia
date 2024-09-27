class Pokemon:
    def __init__(self, name: str, hp: int, attack: int):
        self.name = name
        self.hp = hp
        self.attack = attack

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_fainted(self):
        return self.hp == 0

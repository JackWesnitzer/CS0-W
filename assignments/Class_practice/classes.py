class Player:
    def __init__(self, hp=10, damage=2):
        self.hp = hp
        self.damage = damage

    def take_damage(self, enemy):
        self.hp -= enemy.damage
    def hit(self, enemy):
        enemy.hp -= self.damage
    def __str__(self):
        return f'HP = {self.hp}, Damage = {self.damage}'

Tau = Player(20,5)
Ion = Player(7,2)

Ion.hit(Tau)
print(Tau, Ion)
Ion.take_damage(Tau)
print(Tau, Ion)

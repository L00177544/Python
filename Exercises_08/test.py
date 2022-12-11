class Pokemon:
    # Class attribute
    species = "Mouse"
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack
         
pikachu = Pokemon("Pikachu", "Double Kick")
raichu = Pokemon("Raichu", "Thunder Punch")
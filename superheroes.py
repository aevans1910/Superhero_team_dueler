from random import randint

class Ability:
    def __init__ (self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength
        pass
    
    def attack (self):
        return randint(1, self.max_damage)

class Armor:
    def __init__ (self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block (self):
        return randint(1, self.max_block)

if __name__ == "__main__":
    ability = Ability ("Debugging Ability", 20)
    print (ability.name)
    print (ability.attack())


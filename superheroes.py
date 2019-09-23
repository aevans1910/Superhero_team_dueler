from random import randint

class Ability:
    #create variable to latter assign the amount of damage 
    #that has been done
    def __init__ (self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength
        pass
    
    #making each attack be in a range of strength
    def attack (self):
        return randint(1, self.max_damage)

class Armor:
    #creating a variable to later assign how much damage 
    #the armor can block
    def __init__ (self, name, max_block):
        self.name = name
        self.max_block = max_block

    #making it so the armor can block between 1 and the 
    #maximum blocking amount each time it gets damaged
    def block (self):
        return randint(1, self.max_block)

class Hero:
    #creating a Hero class that has certain properties
    def __init__ (self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability (self, ability):
        ''' Add ability to abilities list '''
        #adding an ability to the preexsisting list of abilities
        self.abilities.append(ability)

    def attack (self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int
        '''
        #our attacks are the total of the strength of our abilities 
        #at the moment when we attack
        total = 0
        for ability in self.abilities:
            total += ability.attack()
        return total

    def add_armor (self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        #adding another element of armor to the preexsisting 
        #list of armors
        self.armors.append(armor)

    def defend (self, damage_amount):
        '''Runs `block` method on each armor.
            Returns sum of all blocks
        '''
        #our damage is reduced depending on the amount of armor we 
        #are wearing. The damage amount is therefore substracted from our defense
        total = 0
        for armor in self.armors:
            total += armor.block()
        return abs(total - damage_amount)

    def take_damage (self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        #our current health is our health, minus the damage that has been done to 
        #us after we have defended ourself
        current_health = self.current_health
        damage_after_defense = self.defend(damage)
        self.current_health = current_health - damage_after_defense

    def is_alive (self):
        '''Return True or False depending on whether the hero is alive or not.
	    '''
        if self.current_health > 0: #if our current health is above 0, we are still alive
            return True
        else: #if our current health is under 0, we are no longer alive
            return False

    def fight (self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        while True:
            if self.is_alive (): #if our own hero is still alive
                own_damage = self.attack() #we get damage
                opponent.take_damage(own_damage) #the opponent gets damage
            else: #if we lose (are no longer alive), a message prints out 
                #that the opponent has won
                print (f'{opponent.name} has won!')
                return

            if opponent.is_alive (): #if the opponent is still alive
                opponent_damage =  opponent.attack() #the opponent gets damage
                self.take_damage(opponent_damage) #we get damage
            else: #if the opponents loses (is no longer alive), a message prints 
                #out that we have won
                print (f'{self.name} has won!')
                return    

if __name__ == "__main__":
    #here we are testing out a fight between Wonder Woman and Dumbledore
    hero1 = Hero ("Wonder Woman")
    hero2 = Hero ("Dumbledore")
    ability1 = Ability ("Super Eyes", 30)
    ability2 = Ability ("Super Speed", 100)
    ability3 = Ability ("Wizard Wand", 100)
    ability4 = Ability ("Wizard Beard", 200)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)




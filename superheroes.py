from random import randint, choice


class Ability:
    # create variable to latter assign the amount of damage
    # that has been done
    def __init__(self, name, attack_strength=100):
        self.name = name
        self.max_damage = attack_strength

    # making each attack be in a range of strength
    def attack(self):
        return randint(0, self.max_damage)


class Armor:
    # creating a variable to later assign how much damage
    # the armor can block
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    # making it so the armor can block between 1 and the
    # maximum blocking amount each time it gets damaged
    def block(self):
        return randint(0, self.max_block)


class Hero:
    # creating a Hero class that has certain properties
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health
        self.deaths = 0
        self.kills = 0

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        # adding an ability to the preexsisting list of abilities
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int
        '''
        # our attacks are the total of the strength of our abilities
        # at the moment when we attack
        total = 0
        for ability in self.abilities:
            total += ability.attack()
        return total


    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        # adding another element of armor to the preexsisting
        # list of armors
        self.armors.append(armor)

    def defend(self):
        '''Runs `block` method on each armor.
            Returns sum of all blocks
        '''
        # our damage is reduced depending on the amount of armor we
        # are wearing. The damage amount is therefore substracted from our defense
        total = 0
        for armor in self.armors:
            total += armor.block()
        return total

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # our current health is our health, minus the damage that has been done to
        # us after we have defended ourself
        defended = self.defend()
        dmg = damage - defended
        self.current_health -= dmg

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
            '''
        if self.current_health > 0:  # if our current health is above 0, we are still alive
            return True
        else:  # if our current health is under 0, we are no longer alive
            return False

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        while True:
            if self.is_alive():  # if our own hero is still alive
                own_damage = self.attack()  # we get damage
                opponent.take_damage(own_damage)  # the opponent gets damage
            else:  # if we lose (are no longer alive), a message prints out
                # that the opponent has won
                opponent.add_kill(1)
                self.add_deaths(1)
                break

            if opponent.is_alive():  # if the opponent is still alive
                opponent_damage = opponent.attack()  # the opponent gets damage
                self.take_damage(opponent_damage)  # we get damage
            else:  # if the opponents loses (is no longer alive), a message prints
                # out that we have won
                self.add_kill(1)
                opponent.add_deaths(1)
                break

    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths


class Weapon (Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return randint(self.max_damage // 2, self.max_damage)


class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        self.name = name
        self.heroes = []
        self.kills = 0
        self.deaths = 0

    def able_to_fight(self):
        available_heroes = []
        for hero in self.heroes:
            if hero.is_alive():
                available_heroes.append(hero)
        return available_heroes

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        while self.able_to_fight() and other_team.able_to_fight():
            nice_heroes = choice(self.able_to_fight())
            not_nice_heroes = choice(other_team.able_to_fight())
            nice_heroes.fight(not_nice_heroes)

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            self.kills += hero.kills
            self.deaths += hero.deaths
            if self.deaths < 0:
                k_d_ratio = self.kills // self.deaths
                return k_d_ratio
            else:
                return self.kills

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            return(hero.name)


class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team1 = None
        self.team2 = None

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        new_ability = input("Create a new ability: ")
        ability_damage = input("What is this ability's max damage: ")
        ability_max_damage = int(ability_damage)
        return Ability(new_ability, ability_max_damage)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        new_weapon = input("Create a new weapon: ")
        weapon_damage = input("What is this weapon's max damage: ")
        weapon_max_damage = int(weapon_damage)
        return Weapon(new_weapon, weapon_max_damage)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        new_armor = input("Create a new armor: ")
        armor_defend = input("How much does this armor defend: ")
        armor_max_defend = int(armor_defend)
        return Armor(new_armor, armor_max_defend)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        new_hero = input("Create a new hero: ")
        new_hero_health = input("What is the health amount for your hero: ")
        hero_max_health = int(new_hero_health)
        created_hero = Hero(new_hero, hero_max_health)

        new_abilities = input(
            "How many new abilities would you like to create for your hero?")
        amount_of_abilities = int(new_abilities)
        for _ in range(amount_of_abilities):
            created_ability = self.create_ability()
            created_hero.add_ability(created_ability)

        new_armor = input("How mamy new armors would you like to add?")
        amount_of_armor = int(new_armor)
        for _ in range(amount_of_armor):
            created_armor = self.create_armor()
            created_hero.add_armor(created_armor)

        new_weapon = input("How many new weapons would you like to add?")
        amount_of_weapons = int(new_weapon)
        for _ in range(amount_of_weapons):
            created_weapons = self.create_weapon()
            created_hero.add_weapon(created_weapons)
        return created_hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        create_team_one_name = input("What is the name of your first team? ")
        create_team_one = int(input("How many heroes are in team one? "))
        self.team1 = Team(create_team_one_name)
        for _ in range(create_team_one):
            team_one_hero = self.create_hero()
            self.team1.add_hero(team_one_hero)

    def build_team_two(self):
        '''Prompt the user to build team_one '''
        create_team_two_name = input("What is the name of your second team? ")
        create_team_two = int(input("How many heroes are in team two? "))
        self.team2 = Team(create_team_two_name)
        for _ in range(create_team_two):
            team_two_hero = self.create_hero()
            self.team2.add_hero(team_two_hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team1.attack(self.team2)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        print("Team 1 stats: " + str(self.team1.stats()))
        print("Team 2 stats: " + str(self.team2.stats()))
        for hero in self.team1.heroes:
            if hero.is_alive():
                print ("Surviving heroes in team 1 are: " + hero.name)
        for hero in self.team2.heroes:
            if hero.is_alive():
                print ("Surviving heroes in team 2 are: " + hero.name)
        if self.team1.stats() > self.team2.stats():
            print("Team 1 wins!")
        elif self.team1.stats() < self.team2.stats():
            print("Team 2 wins!")
        else:
            print("It's a tie!")


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team1.revive_heroes()
            arena.team2.revive_heroes()
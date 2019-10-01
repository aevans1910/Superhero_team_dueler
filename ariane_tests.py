"""
    <-- Tests created with love by Ben Lafferty -->
    Feel free to add more to the 'templates' I have here.  The first 3 tests should
    be universal based off of the function description. Everything can be changed if needed
    based on the values that are in the 'input_values' list in every function so feel free
    to edit to what works in your code.
​
    If you run this file directly, like `python3 arena_test.py` it should run all the way to
    your stats function so that you are able to test what it outputs without having to put your
    info in over and over.  You will probably have to change your inputs to be specific to your 
    project, but the underlying framework to set it up once and have it work for your code should
    be there!  Feel free to DM me on Slack with any questions. Hope this helps make writing Arena
    more fun!
"""
import pytest
import superheroes
import sys
import io
​
# Helper funcs
​
​
def capture_console_output(function_body):
    # _io.StringIO object
    string_io = io.StringIO()
    sys.stdout = string_io
    function_body()
    sys.stdout = sys.__stdout__
    return string_io.getvalue()
​
# tests
​
​
def test_create_ability():
    input_values = ["Amazing Ability", '200']
    # output = []
​
    def mock_input(s):
        # output.append(s)
        return input_values.pop(0)
    superheroes.input = mock_input
    # superheroes.print = lambda s: output.append(s)
​
    arena = superheroes.Arena()
    ability = arena.create_ability()
​
    assert ['Amazing Ability', 200] == [ability.name, ability.max_damage]
​
​
def test_create_weapon():
    input_values = ["Amazing Weapon", '200']
​
    def mock_input(s):
        return input_values.pop(0)
    superheroes.input = mock_input
​
    arena = superheroes.Arena()
    weapon = arena.create_weapon()
​
    assert ['Amazing Weapon', 200] == [weapon.name, weapon.max_damage]
​
​
def test_create_armor():
    input_values = ["Amazing Armor", '300']
​
    def mock_input(s):
        return input_values.pop(0)
    superheroes.input = mock_input
​
    arena = superheroes.Arena()
    armor = arena.create_armor()
​
    assert ['Amazing Armor', 300] == [armor.name, armor.max_block]
​
​
# testing create hero, could break based off of how you built this function so could be ignorable
def test_create_hero():
    # These are the values needed to create a hero. Could be different from application to application
    # due to implementation
    input_values = ['Ben', '100', '1', 'Ian is SUPER COOL', '100', '1',
                    'AMAZING ABILITY', '100', '1', 'AMAZIN', '200', 'GOD ARMOR']
​
    def mock_input(s):
        return input_values.pop(0)
    superheroes.input = mock_input
​
    arena = superheroes.Arena()
    hero = arena.create_hero()
​
    assert ['Ben', 100, True, 0, 0] == [hero.name,
                                        hero.current_health, hero.is_alive(), hero.kills, hero.deaths]
​
# this is also dependent on how you build a team. if you ask for a name you can add that input to the input values
​
​
def test_build_team_one():
    input_values = ['Team 2', '1', 'Ben is the Best', '100', '1', 'Ian is SUPER COOL', '100', '1',
                    'AMAZING ABILITY', '100', '1', 'AMAZIN', '200', 'GOD ARMOR']
​
    def mock_input(s):
        return input_values.pop(0)
    superheroes.input = mock_input
​
    arena = superheroes.Arena()
    arena.build_team_one()
​
    assert [1, 'Ben is the Best'] == [
        len(arena.team1.heroes), arena.team1.heroes[0].name]
​
​
# this is also dependent on how you build a team. if you ask for a name
def test_build_team_two():
    input_values = ['Team 1', '1', 'Ben is the Best', '100', '1', 'Ian is SUPER COOL', '100', '1',
                    'AMAZING ABILITY', '100', '1', 'AMAZIN', '200', 'GOD ARMOR']
​
    def mock_input(s):
        return input_values.pop(0)
    superheroes.input = mock_input
​
    arena = superheroes.Arena()
    arena.build_team_two()
​
    assert [1, 'Ben is the Best'] == [
        len(arena.team2.heroes), arena.team2.heroes[0].name]
​
​
def test_team_stats():
    input_values = ['Team 1', '1', 'Ben', '100', '1', 'Mondale', '100', '1',
                    'Amazin Ability', '100', '1', 'AMAZIN', '200',
                    'Team 2', '1', 'Ben', '100', '1', 'Ian', '100', '1',
                    'Amazin Ability', '100', '1', 'AMAZIN', '200']
​
    def mock_input(s):
        return input_values.pop(0)
    superheroes.input = mock_input
​
    arena = superheroes.Arena()
    arena.build_team_one()
    arena.build_team_two()
​
    arena.team_battle()
​
    arena.show_stats()
​
    output_str = capture_console_output(arena.show_stats)
    #assert 'Team 1 wins the game!' in output_str
​
​
if __name__ == '__main__':
    test_team_stats()

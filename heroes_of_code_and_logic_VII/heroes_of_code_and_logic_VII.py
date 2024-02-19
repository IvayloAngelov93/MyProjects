
class HeroesCodeLogic:

    def __init__(self):
        self.collection_of_heroes = {}

    def collect_heroes(self, name, hp_points, mp_points):
        self.collection_of_heroes[name] = [hp_points, mp_points]

    def reduce_mp_points(self, name, points, spell_name):
        if self.collection_of_heroes[name][1] >= points:
            self.collection_of_heroes[name][1] -= points
            return f"{name} has successfully cast {spell_name} and now has {self.collection_of_heroes[name][1]} MP!"
        else:
            return f"{name} does not have enough MP to cast {spell_name}!"

    def reduce_hp_points(self, name, points, attacker):
        self.collection_of_heroes[name][0] -= points
        if self.collection_of_heroes[name][0] > 0:
            return f"{name} was hit for {points} HP by {attacker} and now has {self.collection_of_heroes[name][0]} HP left!"
        else:
            self.collection_of_heroes.pop(name)
            return f"{name} has been killed by {attacker}!"

    def increase_mp_points(self, name, amount):
        free_space = 200 - self.collection_of_heroes[name][1]
        if amount > free_space:
            amount = free_space
        self.collection_of_heroes[name][1] += amount
        return f"{name} recharged for {amount} MP!"

    def increase_hp_points(self, name, amount):
        free_space = 100 - self.collection_of_heroes[name][0]
        if amount > free_space:
            amount = free_space
        self.collection_of_heroes[name][0] += amount
        return f"{name} healed for {amount} HP!"

    def __repr__(self):
        result = []
        for name, value in self.collection_of_heroes.items():
            result.append(name)
            result.append(f"HP: {value[0]}")
            result.append(f"MP: {value[1]}")
        return '\n'.join(result)

def main():
    heroes_code_logic = HeroesCodeLogic()
    number_of_heroes = int(input())
    for _ in range(number_of_heroes):
        heroes_info = input().split()
        name = heroes_info[0]
        hp_points = int(heroes_info[1])
        mp_points = int(heroes_info[2])
        heroes_code_logic.collect_heroes(name, hp_points, mp_points)

    while True:
        commands = input().split(' - ')
        if 'End' in commands:
            break
        if "CastSpell" in commands:
            name = commands[1]
            mp_needed = int(commands[2])
            spell_name = commands[3]
            print(heroes_code_logic.reduce_mp_points(name, mp_needed, spell_name))
        elif "TakeDamage" in commands:
            name = commands[1]
            damage = int(commands[2])
            attacker = commands[3]
            print(heroes_code_logic.reduce_hp_points(name, damage, attacker))
        elif "Recharge" in commands:
            name = commands[1]
            amount = int(commands[2])
            print(heroes_code_logic.increase_mp_points(name, amount))
        elif "Heal" in commands:
            name = commands[1]
            amount = int(commands[2])
            print(heroes_code_logic.increase_hp_points(name, amount))
    print(heroes_code_logic)

if __name__ == '__main__':
    main()
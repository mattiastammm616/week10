import random


def read_list(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def attack(attacker, defender):
    damage = len(attacker["weapon"])
    defender["health"] = max(0, defender["health"] - damage)
    print(f'{attacker["name"]} attacks {defender["name"]} with {attacker["weapon"]}!')
    print(f'Damage: {damage} | {defender["name"]} health: {defender["health"]}\n')


def main():
    heroes = read_list("heroes.txt")
    villains = read_list("villains.txt")
    weapons = list(dict.fromkeys(read_list("weapons.txt")))

    if not heroes or not villains or len(weapons) < 2:
        print("Please add heroes, villains, and at least two different weapons to the text files.")
        return

    hero_weapon, villain_weapon = random.sample(weapons, 2)
    hero = {"name": random.choice(heroes), "weapon": hero_weapon, "health": 100}
    villain = {"name": random.choice(villains), "weapon": villain_weapon, "health": 100}

    print("=== EPIC FIGHT ===")
    print(f'Hero: {hero["name"]} | Weapon: {hero["weapon"]} | Health: {hero["health"]}')
    print(f'Villain: {villain["name"]} | Weapon: {villain["weapon"]} | Health: {villain["health"]}\n')

    round_number = 1
    while hero["health"] > 0 and villain["health"] > 0:
        print(f'--- Round {round_number} ---')
        attack(hero, villain)
        if villain["health"] == 0:
            break
        attack(villain, hero)
        round_number += 1

    winner = hero if hero["health"] > 0 else villain
    print(f'🏆 WINNER: {winner["name"]} with {winner["health"]} health remaining!')


if __name__ == "__main__":
    main()

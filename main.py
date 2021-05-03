from classes.game import Person, bcolor
from classes.magic import Spell
from classes.inventory import Item

# Create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 10, 200, "white")

# Create Items
potion =  Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully restores", 9999)
hielixir = Item("MegaElixir", "elixir", "Fully restores", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [potion, hipotion, superpotion, elixir, hielixir, grenade]

# Instantiate People
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0

print(bcolor.FAIL + bcolor.BOLD + "ENEMY Attacks!" + bcolor.ENDC)

while running:
    print("-------------")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("Attacked for ", dmg, " points of damage. Enemy HP", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic: ")) - 1

        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolor.FAIL + "\nNot enoough MP \n" + bcolor.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolor.OKBLUE + "\n" + spell.name + "heals", str(magic_dmg), "HP", bcolor.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolor.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), "points of damage", bcolor.ENDC)
    elif index ==2:
        player.choose_item()
        item_choice = int(input("Choose Item ")) -1

        if item_choice == -1:
            continue

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "Player HP", player.get_hp())

    print("--------------")
    print("Enemy HP", bcolor.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolor.ENDC + "\n")

    print("Your HP", bcolor.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolor.ENDC + "\n")
    print("Your MP", bcolor.OKBLUE + str(player.get_mp()) + "/" +str (player.get_max_mp()) + bcolor.ENDC)

    if enemy.get_hp() == 0:
        print(bcolor.OKGREEN + "You WIN" + bcolor.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolor.FAIL + "You have lost" + bcolor.ENDC)
        running = False

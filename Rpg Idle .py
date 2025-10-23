print("=== Witaj w grze Python RPG ===")
name = input("What is your name? ")
age = int(input("How old are you? "))
print("Hello, " + name + "!")
print("Choose you class:")
print("1. Warrior⚔️")
print("2. Hunter🏹")
print("3. Mage🔮")

inventory = [] #pusta lista ekwipunku
level = 1
exp = 0
exp += 15


choice = int(input("Choose your option: "))
punkty = 15
bonus = 10
have_he_shield = False
class_name = ""
if choice == 1:
    class_name = "Warrior"
    have_he_shield = True
    punkty += 15
elif choice == 2:
    class_name = "Hunter"
    punkty += 12
elif choice == 3:
    class_name = "Mage"
    punkty += 20
else:
    print("You didn't choose any option, you will be a bastard")
    punkty += 1


if have_he_shield:
    print("God shields you!")
    punkty += bonus
else:
    print("God don't shields you!")
    punkty -= bonus
print(punkty)
if age >= 18:
    print("You are old enough")
    punkty += 10
elif age <= 18:
    print("You are  too young")
    punkty -= 10


print("=== Statistics ===")
print("Your name is " + name)
print("Your age is " + str(age))
print("Your punkty is " + str(punkty))
print("Your class is " + class_name)

if punkty >= 40:
    print("You are great hero")
elif punkty >= 30:
    print("You are ready to battle")
else:
    print("You are not enough to battle, better stay in the village")

import random

print("=== Second part of journey: FIGHT ===")
print("choose your enemy")
print("1 - Dragon (very strong)")
print("2 - Golem (Strong but slow)")
print("3 - Goblin (fast)")

choice = int(input("Choose your option: "))
if choice == 1:
    enemy = "Dragon"
    enemy_power = random.randint(15,30)
elif choice == 2:
    enemy = "Golem"
    enemy_power = random.randint(10,20)
elif choice == 3:
    enemy = "Goblin"
    enemy_power = random.randint(8,18)
else:
    enemy = "Shadow of death"
    enemy_power= random.randint(15,35)
your_power = punkty + random.randint(5,15)
print("Your power is " + str(your_power))
print(f"Power of your enemy ({enemy}): {enemy_power}")
if your_power > enemy_power:
    print(f"You defeat an enemy {enemy}. You gain 20 points")
    print("You drop a sword and 20 exp")
    inventory.append("Sword")
    punkty += 20
    exp += 25
elif your_power == enemy_power:
    print(f"Draw witf {enemy}. You gain 10 points")
    punkty += 10
    exp += 5
else:
    print(f"You lose this fight witf {enemy}. . . you lose 10 points")
    punkty -= 10
prize = random.randint(1,4)
if prize == 1:
    print("You dropped heal potion")
elif prize == 2:
    print("You dropped mana potion")
elif prize == 3:
    print("You dropped diamond")
elif prize == 4:
    print("You dropped 5 gold")
print("=== Results ===")
print("Your name is " + name)
print(f"You have now {punkty} points")


inventory.append("Heal Potion")
print("Your inventory", inventory)
if "Sword" in inventory:
    punkty += 10
if "Heal Potion" in inventory:
    punkty += 5

print(f"Your power after items: {punkty}")
if exp >= 20:
    level += 1
    exp -= 20
    print(f"Congratulations, You reached {level} level!" )
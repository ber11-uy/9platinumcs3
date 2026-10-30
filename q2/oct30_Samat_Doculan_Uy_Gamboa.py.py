"""
Gamboa 07#
Doculan 22#
Uy 31#
9-Samat
"""


class Healthpotion:
    def use(self):
        print("You regain 50 HP!")
        # dis the health fr


class Manapotion:
    def use(self):
        print("You restore 30 MP!")
        # dis the mana


class SpeedBoost:
    def use(self):
        print("Your speed increases for 10 seconds!")
        # for fast


def apply_item(item):
    item.use()
    # you use the item


potions = [Healthpotion(), Manapotion(), SpeedBoost()]

for potion in potions:
    apply_item(potion)
    # for output

    # hi sir we luv u

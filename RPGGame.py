# Room Class ----------------------------------------------------------------------------------------------------------
class Room:
    def __init__(self, name, desc, neighbors, has, enemy, objects):
        self.name = name
        self.desc = desc
        self.neighbors = neighbors
        self.has = has
        self.enemy = enemy
        self.objects = objects

    def room_initiate(self):
        print(self.desc)
        player.room = self
        if self.has:
            battle(self.enemy)
        else:
            self.room_descriptor()

    def room_descriptor(self):
        player.level_up()
        print(player.name, player.level, player.hp, player.max_hp)
        print("I - Inventory")
        for i in self.objects:
            print(str(self.objects.index(i)) + " - " + i.name)
        for i in self.neighbors:
            print(str(self.neighbors.index(i) + len(self.objects)) + " - Room - " + i.name)
        index = input("Select action to do:\n")
        if index == "I":
            player.inventory()
        elif int(index) >= len(self.objects):
            self.neighbors[int(index) - len(self.objects)].room_initiate()
        else:
            print(self.objects[index].desc)
            self.room_descriptor()


# Object Class --------------------------------------------------------------------------------------------------------
class Object:
    def __init__(self, name, desc, has, item):
        self.name = name
        self.desc = desc
        self.has = has
        self.item = item


# Unit Classes --------------------------------------------------------------------------------------------------------
class Unit:
    def __init__(self, name, attack, defense, hp, max_hp):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.max_hp = max_hp

    def defend(self):
        self.defense *= 2
        print("All that stuff after turn finishes")  # All that stuff that's written when turn is finished
        self.defense /= 2


class Player(Unit):
    def __init__(self, name, attack, defense, hp, max_hp, items, xp, level, room):
        super().__init__(name, attack, defense, hp, max_hp)
        self.items = items
        self.xp = xp
        self.level = level
        self.max_hp = max_hp
        self.room = room

    def level_up(self):
        while self.xp >= 100:
            self.xp -= 100
            self.level += 1
            self.max_hp += 10
            print("Level Up!")

    def inventory(self):
        for i in self.items:
            print(str(self.items.index(i)) + " - " + i.name)
        print("G - Go Back")
        index = input("Select action:\n")
        if index != "G":
            print(self.items[int(index)].desc)
            self.inventory()
        self.room.room_descriptor()


class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc


# Objects -------------------------------------------------------------------------------------------------------------
ob1 = Object("Object 1", "Description 1", False, [])
ob2 = Object("Object 2", "Description 2", False, [])
# Rooms ---------------------------------------------------------------------------------------------------------------
ro2 = Room("Room 2", "Very uncool room", [], False, 0, [ob1, ob2])
ro1 = Room("Room 1", "Very cool room", [ro2], False, 0, [ob1, ob2])
# Items ---------------------------------------------------------------------------------------------------------------
it1 = Item("Cool Item", "Description of cool item")
it2 = Item("Uncool Item", "Description of uncool item")
# Player --------------------------------------------------------------------------------------------------------------
player = Player("Player", 10, 2, 100, 100, [it1, it2], 0, 1, ro1)
# Enemies -------------------------------------------------------------------------------------------------------------
ro1.room_initiate()

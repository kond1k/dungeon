class Item:
    def __init__(self, name='', height=0, capacity=0, int=0, po=0):
        self.height = height
        self.capacity = capacity
        self.int = int
        self.po = po
        self.name = name

    def get_items(self):
        items = []
        sword = Sword()
        items.append(sword)
        axe = Axe()
        items.append(axe)
        staff = Staff()
        items.append(staff)
        magic_wand = MagicWand()
        items.append(magic_wand)
        ruby = Ruby()
        items.append(ruby)
        return items

    def get_name(self):
        return self.name


class Sword(Item):
    def __init__(self):
        Item.__init__(self, 'Sword', 5, 3, 0, 40)


class Axe(Item):
    def __init__(self):
        Item.__init__(self, 'Axe', 7, 5, 0, 50)


class Staff(Item):
    def __init__(self):
        Item.__init__(self, 'Staff', 3, 5, 50)


class MagicWand(Item):
    def __init__(self):
        Item.__init__(self, 'Magic Wand', 2, 3, 60)


class Ruby(Item):
    def __init__(self):
        Item.__init__(self, 'Ruby', 2, 1)


class Gold(Item):
    def __init__(self):
        Item.__init__(self, 'Gold', 1, 1)

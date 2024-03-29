import Item


class Character:
    def __init__(self, name, class_name, po):
        self.class_name = class_name
        self.name = name
        self.bag_capacity = 30
        self.max_height = po * 2
        self.bag = []

    def get_bag_capacity(self):
        print(f'Свободных ячеек {self.bag_capacity}')

    def open_bag(self):
        print('В вашей сумке лежит: ')
        for i in self.bag:
            print(i)

    def put_in_bag(self, item):
        self.bag.append(item)

    def take_out_item(self):
        for ind, i in enumerate(self.bag, 1):
            print(ind, i)
        take_out_ind = int(input('что вы хотит выкинуть? укажите номер \n'))
        return self.bag.pop(take_out_ind - 1)

    def get_name(self):
        return self.name

    def get_info(self):
        return [self.po, self.hp, self.int, self.class_name]


class Warrior(Character):
    po = 60
    hp = 80
    int = 40
    class_name = 'Воин'

    def __init__(self, name):
        Character.__init__(self, name, self.class_name, self.po)


class Mage(Character):
    po = 30
    hp = 60
    int = 80
    class_name = 'Маг'

    def __init__(self, name):
        Character.__init__(self, name, self.class_name, self.po)

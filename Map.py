import random
import Item


class MyMAP:
    map_capacity = 9
    current_location = [map_capacity - 1, int(map_capacity / 2)]
    world = []

    def __init__(self):
        self.world = [[0] * self.map_capacity for i in range(self.map_capacity)]
        items = Item.Item()
        count = 0
        while True:
            if count >= self.map_capacity / 2:
                break
            for i in range(0, len(self.world)):
                for j in range(0, len(self.world)):
                    z = random.randrange(0, 20)
                    if z == 2 and self.world[i][j] == 0:
                        self.world[i][j] = random.choice(items.get_items()).get_name()
                    if z == 1 and self.world[i][j] == 0:
                        self.world[i][j] = Item.Gold().get_name()
                        count += 1

    def check_map(self, i, j):
        if self.world[i][j]:
            print(f'здесь лежит {self.world[i][j]}')
        else:
            print('Здесь пусто')

    def step_forward(self):
        self.current_location[0] -= 1
        self.check_map(self.current_location[0], self.current_location[1])

    def step_right(self):
        self.current_location[1] += 1
        self.check_map(self.current_location[0], self.current_location[1])

    def step_left(self):
        self.current_location[1] -= 1
        self.check_map(self.current_location[0], self.current_location[1])

    def step_back(self):
        self.current_location[0] += 1
        self.check_map(self.current_location[0], self.current_location[1])

import Character
import Player
from Map import MyMAP
import os
import pickle
import json


def catch_up():
    if my_map.world[my_map.current_location[0]][my_map.current_location[1]] != 0:
        my_character.put_in_bag(my_map.world[my_map.current_location[0]][my_map.current_location[1]])
        my_map.world[my_map.current_location[0]][my_map.current_location[1]] = 0


def put_out():
    my_map.put_item_out(my_character.take_out_item())


def create_char():
    class_ = input('Выберите класс. Маг или Воин \n')
    if class_ == 'Воин':
        return Character.Warrior(input('Введите имя персонажа \n'))
    if class_ == 'Маг':
        return Character.Mage(input('Введите имя персонажа \n'))


def save_game(player, character, current_map):
    dir_path = os.path.join(os.getcwd(), 'Save')
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        pass
    os.chdir(dir_path)
    try:
        save = open(player.get_name(), 'r')
        my_load = json.load(save)
        save.close()
    except FileNotFoundError:
        my_load = {}
    save = open(player.get_name(), 'w')
    my_load[character.get_name()] = [current_map.world, character.get_info()]
    json.dump(my_load, save)
    save.close()


my_player = Player.Player()
my_character = create_char()
my_map = MyMAP()
move_list = {'вперед': my_map.step_forward, 'влево': my_map.step_left, 'вправо': my_map.step_right,
             'назад': my_map.step_back, 'задание': my_map.check_quest, 'открыть инвентарь': my_character.open_bag,
             'сохранение': 0, 'поднять': catch_up, 'положить': put_out}
my_str = ', '
save_game(my_player, my_character, my_map)
print(f'Добро пожаловать в игру, вы находитесь на старте в поле {my_map.current_location}')
while True:
    print(f'Вы находитесь в поле {my_map.current_location}')
    move = input(f'Что вы хотите сделать - {my_str.join([key for key in move_list.keys()])} \n')
    move_list[move]()

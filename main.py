import Character
import Player
from Map import MyMAP
import os
import pickle
import json


def save_game(player, character, current_map):
    dir_path = os.path.join(os.getcwd(), 'Save')
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        pass
    os.chdir(dir_path)
    try:
        save = open('Save.txt', 'r')
        my_load = json.load(save)
        save.close()
    except FileNotFoundError:
        my_load = {}
    save = open('Save.txt', 'w')
    if player.get_name() in my_load.keys():
        my_load[player.get_name()][character.get_name()] = [current_map.world, character.get_info()]
    else:
        my_load[player.get_name()] = {character.get_name(): [current_map.world, character.get_info()]}
    json.dump(my_load, save)
    save.close()


my_player = Player.Player()
my_mage = Character.Mage(input('Введите имя персонажа \n'))
print(my_mage.hp)
my_mage.get_bag_capacity()
print(my_mage.max_height)
my_map = MyMAP()
move_list = {'вперед': my_map.step_forward, 'влево': my_map.step_left, 'вправо': my_map.step_right,
             'назад': my_map.step_back, 'задание': 0, 'открыть инвентарь': 0, 'сохранение': 0}
my_str = ', '
save_game(my_player, my_mage, my_map)
print(f'Добро пожаловать в игру, вы находитесь на старте в поле {my_map.current_location}')
while True:
    print(f'Вы находитесь в поле {my_map.current_location}')
    move = input(f'Что вы хотите сделать - {my_str.join([key for key in move_list.keys()])} \n')
    move_list[move]()

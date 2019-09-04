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
my_character = Character.Mage(input('Введите имя персонажа \n'))
print(my_character.hp)
my_character.get_bag_capacity()
print(my_character.max_height)
my_map = MyMAP()
move_list = {'вперед': my_map.step_forward, 'влево': my_map.step_left, 'вправо': my_map.step_right,
             'назад': my_map.step_back, 'задание': my_map.check_quest, 'открыть инвентарь': my_character.open_bag,
             'сохранение': 0, 'поднять': 0}
my_str = ', '
save_game(my_player, my_character, my_map)
print(f'Добро пожаловать в игру, вы находитесь на старте в поле {my_map.current_location}')
while True:
    print(f'Вы находитесь в поле {my_map.current_location}')
    move = input(f'Что вы хотите сделать - {my_str.join([key for key in move_list.keys()])} \n')
    if move == 'поднять':
        my_character.put_in_bag(my_map.world[my_map.current_location[0]][my_map.current_location[1]])
        continue
    move_list[move]()

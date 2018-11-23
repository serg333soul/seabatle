# utf - 8
import copy

from general_func import gen_board
from general_func import print_board
from comp_board_field import *
from human_create_ships import *
from human_step import * 
from computer_step import *	
	
print()
print('ИГРА МОРСКОЙ БОЙ ПО СТАНДАРТНЫМ ПРАВИЛАМ')
print()

player_field_ships = gen_board()
input_position_ships(player_field_ships)
print_board(player_field_ships)
print()
enemy_field_ships = gen_board()
create_comp_ships(enemy_field_ships)
print_board(enemy_field_ships)
print()

my_field_shots = gen_board()
comp_field_shots = gen_board()

points = []
cp_list = []
comp_points_list = []

points_ship_computer = []
pv, ph = 0, 0
enemy_points_ship = []
count_icon = 0
tmp_count_icon = 0

count_app = 0
count_app_comp = 0
while True:
	points, cp_list, count_app = player_step(enemy_field_ships, my_field_shots, points, cp_list, comp_points_list)
	if count_app == 20:
		break
	m, points_ship_computer, pv, ph, enemy_points_ship, count_icon, tmp_count_icon, count_app_comp = computer_step(player_field_ships, comp_field_shots, points_ship_computer, pv, ph, enemy_points_ship, count_icon, tmp_count_icon)
	if count_app_comp == 20:
		break
	if count_icon > 0:	
		tmp_count_icon = copy.deepcopy(count_icon)
		
if count_app == 20:
	print('Вы победили')
elif count_app_comp == 20:
	print('Вы проиграли')
		
	
def who_first():
	pass
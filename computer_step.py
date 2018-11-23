import random
import pdb
import copy


#pdb.set_trace()

from comp_board_field import *
from general_func import gen_board
from general_func import print_board
from general_func import mark_around
from general_func import count_app_ships
from global_variable import *

#board_comp = gen_board()
#c_b = create_comp_ships(board_comp)

def computer_step(enemy_field, comp_field, points_ship, pv, ph, enemy_points_ship, count_icon, tmp_count_icon):
	#points_ship = []
	#enemy_points_ship = list(set(tuple([])))
	count_icon = 0
	my_icon_hit = 0
	miss = True
	while True:
		count_app_comp = count_app_ships(comp_field, HIT)
		enemy_points_ship = list(set(tuple([])))
		#print_board(enemy_field)
		print_board(comp_field)
		print(points_ship)
		#print(enemy_points_ship)
		#print(count_icon, my_icon_hit, tmp_count_icon)
		
		if len(points_ship) > 0:
			min_p, max_p = min_and_max_points(points_ship)
			#print(min_p, max_p)
		
		if count_icon > 0:
			tmp_count_icon = copy.deepcopy(count_icon)
		if tmp_count_icon > 0 and tmp_count_icon == my_icon_hit:
			mark_around(comp_field, points_ship)
			points_ship.clear()
			enemy_points_ship.clear()
			tmp_count_icon = 0
			my_icon_hit = 0
			#print_board(enemy_field)
			#print_board(comp_field)
		print('Ход компьютера нажмите Enter')
		chek = input('Enter')
		if len(points_ship) == 0:
			while True:
				pv = random.randint(1, 10)
				ph = random.randint(1, 10)
				if comp_field[pv][ph] == WATER:
					continue
				if enemy_field[pv][ph] == SPACE or enemy_field[pv][ph] == SHIP_ICON and comp_field[pv][ph] == SPACE:
					break
				else:
					continue
			print(pv, ph)		
			if enemy_field[pv][ph] == SHIP_ICON:
				comp_field[pv][ph] = HIT
				points_ship.append([pv, ph])
				count_icon = check_len_ship(enemy_field, pv, ph, SHIP_ICON, enemy_points_ship)
				my_icon_hit = check_len_ship(comp_field, pv, ph, HIT, enemy_points_ship)
				#print('Длина корабля', count_icon)
				#continue	
			else:
				comp_field[pv][ph] = WATER
				miss = False
				break
		else:
			tmp_points = [min_p, max_p]
			m = available_moves(enemy_field, comp_field, points_ship, tmp_points)
			my_icon_hit = check_len_ship(comp_field, pv, ph, HIT, enemy_points_ship)
			if m == False:
				break
				
		if count_icon > 0:
			tmp_count_icon = copy.deepcopy(count_icon)
		if tmp_count_icon > 0 and tmp_count_icon == my_icon_hit:
			mark_around(comp_field, points_ship)
			points_ship.clear()
			enemy_points_ship.clear()
			tmp_count_icon = 0
			my_icon_hit = 0
			#print_board(enemy_field)
			#print_board(comp_field)	
			
	return miss, points_ship, pv, ph, enemy_points_ship, count_icon, tmp_count_icon, count_app_comp
				
					
def available_moves(enemy_field, comp_field, points_ship, tmp_points):
	
	t_min = tmp_points[0]
	t_max = tmp_points[1]
	#pdb.set_trace()	
	def func(arr, enemy_field, comp_field, points_ship, tmp_points):
		miss = True
		flag = False
		point_v = [arr[0] - 1, arr[0], arr[0] + 1, arr[0]]
		point_h = [arr[1], arr[1] + 1, arr[1], arr[1] - 1]
		moves = [ 
				enemy_field[arr[0] - 1][arr[1]],
				enemy_field[arr[0]][arr[1] + 1],
				enemy_field[arr[0] + 1][arr[1]],
				enemy_field[arr[0]][arr[1] - 1],
				]
		if tmp_points[0] == tmp_points[1]:
			while True:
				ran_num = random.choice([0, 1, 2, 3])
				choice_num = moves[ran_num]
				if 1 <= point_v[ran_num] <= 10 and 1 <= point_h[ran_num] <= 10 and comp_field[point_v[ran_num]][point_h[ran_num]] != WATER:
					if choice_num == SHIP_ICON:
						comp_field[point_v[ran_num]][point_h[ran_num]] = HIT
						points_ship.append([point_v[ran_num], point_h[ran_num]])
						break
					elif choice_num == SPACE:
						comp_field[point_v[ran_num]][point_h[ran_num]] = WATER
						miss = False
						break

		elif tmp_points[0][0] == tmp_points[1][0]:
			while True:
				#ran_choice = random.choice([tmp_points[0][1], tmp_points[1][1]])
				if arr[1] < tmp_points[1][1]:
					if 1 <= point_h[3] <= 10 and comp_field[arr[0]][point_h[3]] != WATER:
						if enemy_field[arr[0]][point_h[3]] == SHIP_ICON:
							#print('слева', [arr[0], point_h[3]])
							comp_field[arr[0]][point_h[3]] = HIT
							points_ship.append([arr[0], point_h[3]])
							flag = True
							break
						elif enemy_field[arr[0]][point_h[3]] == SPACE:		
							comp_field[arr[0]][point_h[3]] = WATER
							miss = False
							flag = True	
							break
				if arr[1] == tmp_points[1][1]:
					if 1 <= point_h[1] <= 10 and comp_field[arr[0]][point_h[1]] != WATER:			
						if enemy_field[arr[0]][point_h[1]] == SHIP_ICON:
							#print('справа', [arr[0], point_h[1]])
							comp_field[arr[0]][point_h[1]] = HIT
							points_ship.append([arr[0], point_h[1]])
							flag = True
							break
						elif enemy_field[arr[0]][point_h[1]] == SPACE:		
							comp_field[arr[0]][point_h[1]] = WATER
							miss = False
							flag = True	
							break
				break
		elif tmp_points[0][1] == tmp_points[1][1]:
			while True:
				if arr[0] < tmp_points[1][0]:
					if 1 <= point_v[0] <= 10 and comp_field[point_v[0]][arr[1]] != WATER:
						if enemy_field[point_v[0]][arr[1]] == SHIP_ICON:
							comp_field[point_v[0]][arr[1]] = HIT
							points_ship.append([point_v[0], arr[1]])
							flag = True
							break
						elif enemy_field[point_v[0]][arr[1]] == SPACE:
							comp_field[point_v[0]][arr[1]] = WATER
							miss = False
							flag = True
							break
				if arr[0] == tmp_points[1][0]:
					if 1 <= point_v[2] <= 10 and comp_field[point_v[2]][arr[1]] != WATER:
						if enemy_field[point_v[2]][arr[1]] == SHIP_ICON:	
							comp_field[point_v[2]][arr[1]] = HIT
							points_ship.append([point_v[2], arr[1]])						
							flag = True
							break
						elif enemy_field[point_v[2]][arr[1]] == SPACE:
							comp_field[point_v[2]][arr[1]] = WATER
							miss = False
							flag = True
							break
				break			
		return flag, miss					

	if t_min == t_max:
		f, m = func(t_min, enemy_field, comp_field, points_ship, tmp_points)
	else:
		if t_min[0] == t_max[0]:
			while True: 
				#print(t_min, t_max)
				ran_choice = random.choice([t_min[1], t_max[1]])
				#print('ran_choice', ran_choice)
				if ran_choice == t_min[1]:
					f, m = func(t_min, enemy_field, comp_field, points_ship, tmp_points)
				elif ran_choice == t_max[1]:
					print('t_max', t_max)
					f, m = func(t_max, enemy_field, comp_field, points_ship, tmp_points)
				if f == True:
					break
		if t_min[1] == t_max[1]:
			while True:
				ran_choice = random.choice([t_min[0], t_max[0]])
				if ran_choice == t_min[0]:
					f, m = func(t_min, enemy_field, comp_field, points_ship, tmp_points)
				elif ran_choice == t_max[0]:
					f, m = func(t_max, enemy_field, comp_field, points_ship, tmp_points)
				if f == True:
					break
	return m				
			
def min_and_max_points(arr):
	vertical = []
	horizontal = []
	for i in range(len(arr)):
		vertical.append(arr[i][0])
		horizontal.append(arr[i][1])
	min_points = [min(vertical), min(horizontal)]
	max_points = [max(vertical), max(horizontal)]
	return min_points, max_points	
			
					
def check_len_ship(board, pv, ph, icon, arr):
		'''Узнаем длину корабля'''
		count = 1
		i = 1
		arr.append((pv, ph))
		if board[pv - 1][ph] == icon:
			while board[pv - i][ph] == icon:
				arr.append((pv - i, ph))
				count += 1
				i += 1
			i = 1	
		if board[pv][ph + 1] == icon:
			while board[pv][ph + i] == icon:
				arr.append((pv, ph + i))
				count += 1
				i += 1
			i = 1
		if board[pv + 1][ph] == icon:
			while board[pv + i][ph] == icon:
				arr.append((pv + i, ph))
				count += 1
				i += 1
			i = 1
		if board[pv][ph - 1] == icon:
			while board[pv][ph - i] == icon:
				arr.append((pv, ph - i))
				count += 1
				i += 1
			i = 1
		return count
			
#computer_step(c_b, comp_field)	
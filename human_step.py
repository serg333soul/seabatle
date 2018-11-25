
from general_func import gen_board
from general_func import print_board
from general_func import count_app_ships
from comp_board_field import *
from global_variable import *
# show git
#board_comp = gen_board()
#c_b = create_comp_ships(board_comp)

def player_step(board, empty_list, list_points, cp_list, comp_points_list):
	count_empty = -1
	#list_points = []
	#comp_points_list = []
	res = 0
	while True:
		try:
			count_app = count_app_ships(empty_list, HIT)
			#print_board(board)
			print_board(empty_list)
			cp_list = list(set(tuple(comp_points_list)))
			if count_app == 20:
				print('Вы победили')
				break
			#print(cp_list)
			#print(list_points)
			#print(comp_points_list)
			#print(count_app)
			
			x, y = map(str, input('Ваш ход: ').split())
			
			if board[int(y)][board[0].index(x)] == SHIP_ICON:
				if len(list_points) == 0:
					#print('Если длина list_points == 0')
					empty_list[int(y)][empty_list[0].index(x)] = HIT
					list_points.append([int(y), empty_list[0].index(x)])
					res = chek_len_ships(board, x, y, SHIP_ICON, comp_points_list)
					count_empty = chek_len_ships(empty_list, x, y, HIT, comp_points_list)
				else:
					print('Найдите расположение коробля, и уничтожте его полностью')
					for i in range(len(cp_list)):
						if int(y) == cp_list[i][0] and board[0].index(x) == cp_list[i][1]:
							empty_list[int(y)][empty_list[0].index(x)] = HIT
							list_points.append([int(y), empty_list[0].index(x)])
							res = chek_len_ships(board, x, y, SHIP_ICON, comp_points_list)
							count_empty = chek_len_ships(empty_list, x, y, HIT, comp_points_list)
						#else:
							#print('Найдите расположение коробля, и уничтожте его полностью')

			#print('корабль состоит из', res, 'клеток')
			#print('корабль состоит из', count_empty, 'клеток')					

			if res == count_empty:
				print('Вы уничтожили корабль')
				mark_around(empty_list, list_points)
				list_points.clear()
				comp_points_list.clear()
				res = 0
				
			if board[int(y)][board[0].index(x)] == SPACE:
				empty_list[int(y)][empty_list[0].index(x)] = WATER
				break
			if around_free(board, x, y) or res > 1:	
				continue
		except ValueError:
			print('Не коректный ввод данных')
		except IndexError:
			print('Вы вышли за граници поля')
	return list_points, cp_list, count_app		
		
def around_free(board, x, y):
	'''Проверяем нет ли продолжение корабля'''
	flag = False
	arr = [ 
			board[int(y) - 1][board[0].index(x)],
			board[int(y) ][board[0].index(x) + 1],
			board[int(y) + 1][board[0].index(x)],
			board[int(y)][board[0].index(x) - 1],
			]
	if SHIP_ICON in arr:
		flag = True		
	return flag

def chek_len_ships(board, x, y, app, comp_list):
		'''Узнаем длину корабля'''
		count = 1
		i = 1
		comp_list.append((int(y), board[0].index(x)))

		if board[int(y) - 1][board[0].index(x)] == app:
			while board[int(y) - i][board[0].index(x)] == app:
				comp_list.append((int(y) - i, board[0].index(x)))
				count += 1
				i += 1
			i = 1	
		if board[int(y) ][board[0].index(x) + 1] == app:
			while board[int(y)][board[0].index(x) + i] == app:
				comp_list.append((int(y), board[0].index(x) + i))
				count += 1
				i += 1
			i = 1
		if board[int(y) + 1][board[0].index(x)]	== app:
			while board[int(y) + i][board[0].index(x)] == app:
				comp_list.append((int(y) + i, board[0].index(x)))
				count += 1
				i += 1
			i = 1
		if board[int(y)][board[0].index(x) - 1] == app:
			while board[int(y)][board[0].index(x) - i] == app:
				comp_list.append((int(y), board[0].index(x) - i))
				count += 1
				i += 1
			i = 1
		return count

def mark_around(board, list_points):
	'''Отмечяем область вокруг корабля'''
	
	def sum_func(board, vertical, horizontal):
		'''Заполняем пустые клетки значками ~'''
		a = [
			vertical - 1, 
			vertical - 1, 
			vertical - 1, 
			vertical, 
			vertical + 1, 
			vertical + 1, 
			vertical + 1, 
			vertical
			]
		b = [
			horizontal - 1, 
			horizontal, 
			horizontal + 1, 
			horizontal + 1, 
			horizontal + 1, 
			horizontal, 
			horizontal - 1, 
			horizontal - 1
			]
			
		arr = [
			board[vertical - 1][horizontal - 1], 
			board[vertical - 1][horizontal],
			board[vertical - 1][horizontal + 1],
			board[vertical][horizontal + 1],
			board[vertical + 1][horizontal + 1],
			board[vertical + 1][horizontal],
			board[vertical + 1][horizontal - 1],
			board[vertical][horizontal - 1],
			]	
			
		for i in range(len(arr)):
			if arr[i] == SPACE and a[i] <= 10 and b[i] <= 10:
				board[a[i]][b[i]] = WATER
		return board		
		
	for i in range(len(list_points)):
		if board[list_points[i][0]][list_points[i][1]] == HIT:
			sum_func(board, list_points[i][0], list_points[i][1])
	return board				
	
		
	
#e_f = empty_field()		
#player_step(c_b, e_f)		
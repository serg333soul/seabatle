#SHIPS = {4: 1, 3: 2, 2: 3, 1: 4}
#APP_SHIPS = '[]'
#EMPTY_STR_SPACE = ' '
#ALFA = '0abcdefghij'

#from general_func import gen_board
from general_func import print_board
from global_variable import *

def input_position_ships(board):
	points = []
	count = 0
	alfa = '0abcdefghij'
	for key, val in SHIPS.items():
				#print(key, val)	
				while count != val:
					m = 2 if key > 1 else 4
					for i in range(m):
						print_board(board)
						#print(points)
						print('Постройте {} корабль(я) на {} клетки'.format(val, key))
						x = ' '
						y = ' '
						while not x in alfa[1:] or not y in [str(x) for x in range(1, 11)]:
							while True:
								try:	
									x, y = map(str, input('Введите точки координат, начало корабля и конец: ').split())
									if around_water(board, x, y, points, key):
										break
									else:
										print('Этот квадрат использовать нельзя')
										continue
								except ValueError:
									print('Не коректный ввод данных')
								except IndexError:
									print('Вы вышли за граници поля')
						points += [x, y]
						board[int(y)][board[0].index(x)] = SHIP_ICON
					if m == 4:
						break	
					if not check_pos_ship(points) or not cps(points, key, board):
						clear_board(board, points)
						continue			
					if points[1] == points[3]:
						for k in range(1, key-1):
							board[int(points[1])][min(board[0].index(points[0]), board[0].index(points[2])) + k] = SHIP_ICON
					if points[0] == points[2]:	
						for j in range(1, key):
							board[min(int(points[1]), int(points[3])) + j][board[0].index(points[2])] = SHIP_ICON
					print(points)
					points.clear()
					count += 1
					print(count)
				count = 0		

def check_pos_ship(arr):
	'''Проверяем что бы корабль располагался либо вертикально, либо горизонтально'''
	a = arr[0] == arr[2]
	b = arr[1] == arr[3]	
	if a == True or b == True:
		return True
	else:
		return False

def cps(arr, key, board):
	'''Проверяем длинну корабля что бы она соответствовала заданным параметрам'''
	if arr[0] == arr[2] and abs(int(arr[1]) - int(arr[3])) + 1 != key:		
		return False
	elif arr[1] == arr[3] and abs(board[0].index(arr[0]) - board[0].index(arr[2])) + 1 != key:
		return False
	else:
		return True	

def around_water(board, x, y, points, key):
	'''Проверяем нет ли рядом других кораблей'''
	flag = True
	arr = [
			board[int(y) - 1][board[0].index(x) - 1], 
			board[int(y) - 1][board[0].index(x)],
			board[int(y) - 1][board[0].index(x) + 1],
			board[int(y) ][board[0].index(x) + 1],
			board[int(y) + 1][board[0].index(x) + 1],
			board[int(y) + 1][board[0].index(x)],
			board[int(y) + 1][board[0].index(x) - 1],
			board[int(y)][board[0].index(x) - 1],
			]	
	for i in range(len(arr)):
		if len(points) == 2 and key == 2 and arr[i] == board[int(points[1])][board[0].index(points[0])]:
			board[int(points[1])][board[0].index(points[0])] = SPACE
		elif arr[i] == SHIP_ICON:
			flag = False
			break
	if len(points) == 2 and key == 2:		
		board[int(points[1])][board[0].index(points[0])] = SHIP_ICON		
	return flag		

def clear_board(board, points):
	'''Очистка начальных координат'''
	board[int(points[1])][board[0].index(points[0])] = SPACE
	board[int(points[3])][board[0].index(points[2])] = SPACE
	points.clear()
	print('Вы не правильно ввели координаты, попробуйте еще раз')		

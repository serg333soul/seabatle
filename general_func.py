from global_variable import *

def gen_board():
	'''Игральное поле, в виде двумерного списка'''
	f = [[i if j * i == 0 else SPACE for j in range(12)] for i in range(12)]
	f[0] = [LETTER_SYMBOLS[i] for i in range(12)]
	return f
	
def print_board(board):
	'''Печатаем доску в консоли'''
	for i in range(len(board) - 1):
		for j in range(len(board[i])):
			print('|'.rjust(2), str(board[i][j]).rjust(2), end=' ')
		print()
		print('-' * 68)

def around_water_comp(board, p1, p2):
	'''Проверяем нет ли рядом других кораблей'''
	flag = True
	arr = [
			board[p1 - 1][p2 - 1], 
			board[p1 - 1][p2],
			board[p1 - 1][p2 + 1],
			board[p1][p2 + 1],
			board[p1 + 1][p2 + 1],
			board[p1 + 1][p2],
			board[p1 + 1][p2 - 1],
			board[p1][p2 - 1],
			]	
	if SHIP_ICON in arr:
		flag = False
	return flag	

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

def count_app_ships(arr, value):
	count = 0
	for i in range(1, 11):
		for j in range(1, 11):
			if arr[i][j] == value:
				count += 1
	return count		
import random

from global_variable import *
#from general_func import gen_board

def create_comp_ships(board):
	for key, val in SHIPS.items():
		#print('key {} val {}'.format(key, val))
		for i in range(val):
				while True:
					p1 = random.randint(1, 10)
					p2 = random.randint(1, 10)
					if board[p1][p2] == SHIP_ICON:
						continue
					if around_water_comp(board, p1, p2):
						break
				#print(p1, p2)
				points = [(p1 - key) + 1, (p1 + key) - 1, (p2 - key) + 1, (p2 + key) - 1]
				#print(points)
				while True:
					ran_pos = random.randint(0, 3)
					#print('ran_pos :', ran_pos)
					if ran_pos == 0:
						if 1 <= points[0] <= 10 and around_water_comp(board, points[0], p2):
							for num1 in range(key):
								board[p1 - num1][p2] = SHIP_ICON
							break	
					if ran_pos == 1:			
						if 1 <= points[1] <= 10 and around_water_comp(board, points[1], p2):
							for num2 in range(key):
								board[p1 + num2][p2] = SHIP_ICON
							break	
					if ran_pos == 2:			
						if 1 <= points[2] <= 10 and around_water_comp(board, p1, points[2]):
							for num3 in range(key):
								board[p1][p2 - num3] = SHIP_ICON
							break	
					if ran_pos == 3:			
						if 1 <= points[3] <= 10 and around_water_comp(board, p1, points[3]):
							for num4 in range(key):
								board[p1][p2 + num4] = SHIP_ICON
							break	
					if ran_pos == False:
						continue				
	return board


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
	
#print_board(board_comp)
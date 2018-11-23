import random

SHIP = {4: 1, 3: 2, 2: 3, 1: 4}
APP_S = '[]'
EMPTY = ' '
ALFA_COMP = '0abcdefghij '


def comp_board():
	'''Игральная доска компьютера'''
	f = [[i if j * i == 0 else EMPTY for j in range(12)] for i in range(12)]
	f[0] = [ALFA_COMP[i] for i in range(12)]
	return f

def create_comp_ships(board):
	for key, val in SHIP.items():
		#print('key {} val {}'.format(key, val))
		for i in range(val):
				while True:
					p1 = random.randint(1, 10)
					p2 = random.randint(1, 10)
					if board[p1][p2] == APP_S:
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
								board[p1 - num1][p2] = APP_S
							break	
					if ran_pos == 1:			
						if 1 <= points[1] <= 10 and around_water_comp(board, points[1], p2):
							for num2 in range(key):
								board[p1 + num2][p2] = APP_S
							break	
					if ran_pos == 2:			
						if 1 <= points[2] <= 10 and around_water_comp(board, p1, points[2]):
							for num3 in range(key):
								board[p1][p2 - num3] = APP_S
							break	
					if ran_pos == 3:			
						if 1 <= points[3] <= 10 and around_water_comp(board, p1, points[3]):
							for num4 in range(key):
								board[p1][p2 + num4] = APP_S
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
	if APP_S in arr:
		flag = False
	return flag				

def print_board(board):
	'''Печатаем доску в консоли'''
	for i in range(len(board) - 1):
		for j in range(len(board[i])):
			#print(str(board[i][j]).rjust(2), '|'.rjust(2), end=' ')
			print('|'.rjust(2), str(board[i][j]).rjust(2), end=' ')
		print()
		print('-' * 68)	

board_comp = comp_board()
c_b = create_comp_ships(board_comp)	
print_board(board_comp)
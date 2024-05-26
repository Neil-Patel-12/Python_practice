def placeValue(entery, name, board):
	if name == name1:
		# "x" somewhere
		for i in range(6):
			value = board[i][entery]
			num = i+1
			if num != 6 and board[num][entery] == "\U0001F7E6":
				value = board[num][entery]
			else:
				board[i][entery] = "\U0001F7E5"
				break

	elif name == name2:
		# "o" somewhere
		for i in range(6):
			value = board[i][entery]
			num = i+1
			if num != 6 and board[num][entery] == "\U0001F7E6":
				value = board[num][entery]
			else:
				board[i][entery] = "\U0001F7E8"
				break


def viewBoard(board):
	numbers = ["|", "\uFF11", "\uFF12", "\uFF13", "\uFF14", "\uFF15", "\uFF16", "\uFF17", "|"]
	print()
	for i in range(6):
		print(board[i])
		print()
	print(numbers)
	print()


def left_to_right_winner():
	dim = "\U0001F7E5"
	light = "\U0001F7E8"

	# xxxx
	for i in range(0, 6):
		for j in range(1, 5):
			if board[i][j] == dim:
				count = 0
				for k in range(j, j+4):
					if board[i][k] == dim:
						count += 1
						if count >= 4:
							if board[i][k+1] == dim:
								print("WOW! 5 in a row")
							print(f"{name1} ({dim}) is WINNER!")
							print("You won by (left_to_right_winner)")
							return True
					else:
						count = 0
			else:
				continue
	# xxxx
	for i in range(0, 6):
		for j in range(1, 5):
			if board[i][j] == light:
				count = 0
				for k in range(j, j+4):
					if board[i][k] == light:
						count += 1
						if count >= 4:
							if board[i][k+1] == light:
								print("WOW! 5 in a row")
							print(f"{name2} ({light}) is WINNER!")
							print("You won by (left_to_right_winner)")
							return True
					else:
						count = 0
			else:
				continue
	return False


def top_to_bottom_winner():
	dim = "\U0001F7E5"
	light = "\U0001F7E8"

	# x
	# x
	# x
	# x
	for i in range(5, -1, -1):
		for j in range(1, 8):
			if board[i][j] == dim:
				count = 0
				for k in range(i, -1, -1):
					if board[k][j] == dim:
						count += 1
						if count == 4:
							print(f"{name1} ({dim}) is WINNER!")
							print("You won by (top_to_bottom_winner)")
							return True
					else:
						count = 0
			else:
				continue

	for i in range(5, -1, -1):
		for j in range(1, 8):
			if board[i][j] == light:
				count = 0
				for k in range(i, -1, -1):
					if board[k][j] == light:
						count += 1
						if count == 4:
							print(f"{name2} ({light}) is WINNER!")
							print("You won by (top_to_bottom_winner)")
							return True
					else:
						count = 0
			else:
				continue
	return False


def topRight_to_bottonLeft_winner():
	dim = "\U0001F7E5"
	light = "\U0001F7E8"

	#    x
	#   x
	#  x
	# x
	for i in range(3):
		for j in range(4, 8):
			if board[i][j] == dim:
				count = 0
				for k in range(i, i+1):
					for jth in range(j, j-4, -1):
						if 0 <= k < len(board) and 0 <= jth < len(board[0]):
							if board[k][jth] == dim:
								k += 1
								count += 1
								if count == 4:
									print(f"{name1} ({dim}) is WINNER!")
									print("You won by (topRight_to_bottonLeft_winner)")
									return True
							else:
								count = 0
								# break
						else:
							break
			else:
				continue

	for i in range(3):
		for j in range(4, 8):
			if board[i][j] == light:
				count = 0
				for k in range(i, i+1):
					for jth in range(j, j-4, -1):
						if 0 <= k < len(board) and 0 <= jth < len(board[0]):
							if board[k][jth] == light:
								k += 1
								count += 1
								if count == 4:
									print(f"{name2} ({light}) is WINNER!")
									print("You won by (topRight_to_bottonLeft_winner)")
									return True
							else:
								count = 0
								# break
						else:
							break
			else:
				continue
	return False


def topLeft_to_bottomRight_winner():
	dim = "\U0001F7E5"
	light = "\U0001F7E8"

	# x
	#  x
	#   x
	#    x
	for i in range(3):
		for j in range(1, 5):
			if board[i][j] == dim:
				count = 0
				for k in range(i, i+1):
					for jth in range(j, j+4):
						if 0 <= k < len(board) and 0 <= jth < len(board[0]):
							if board[k][jth] == dim:
								k += 1
								count += 1
								if count == 4:
									print(f"{name1} ({dim}) is WINNER!")
									print("You won by (topLeft_to_bottomRight_winner)")
									return True
							else:
								count = 0
								# break
						else:
							break
			else:
				continue

	for i in range(3):
		for j in range(1, 5):
			if board[i][j] == light:
				count = 0
				for k in range(i, i+1):
					for jth in range(j, j+4):
						if 0 <= k < len(board) and 0 <= jth < len(board[0]):
							if board[k][jth] == light:
								k += 1
								count += 1
								if count == 4:
									print(f"{name2} ({light}) is WINNER!")
									print("You won by (topLeft_to_bottomRight_winner)")
									return True
							else:
								count = 0
								# break
						else:
							break
			else:
				continue


def winner(board):
	if left_to_right_winner():
		return True
	elif top_to_bottom_winner():
		return True
	elif topRight_to_bottonLeft_winner():
		return True
	elif topLeft_to_bottomRight_winner():
		return True
	elif checkTie(board):
		return True
	else:
		return False


def checkTie(board):
	count = 0
	for i in range(0, 6):
		for j in range(1, 8):
			if board[i][j] != "\U0001F7E6":
				count += 1
			if count == 42:
				print(f"{name1} and {name2}, its a Tie!")
				return True
	return False


name1 = input("Enter your name: ")
name2 = input("What is the other players name: ")

print(f"{name1} is (\U0001F7E5)")
print(f"{name2} is (\U0001F7E8)")

board = [["\U0001F7E6" for j in range(9)] for i in range(6)]
for num in board:
	num[0] = "|"
	num[8] = "|"

viewBoard(board)


check = 0
while not winner(board):

	if check % 2 == 0:
		entery = input(f"{name1} Pick item (1-7): ")
		if entery == "q":
			print(f"{name2} is really good!")
			break
		placeValue(int(entery), name1, board)
	else:
		entery2 = input(f"{name2} Pick item (1-7): ")
		if entery2 == "q":
			print(f"{name1} is really good!")
			break
		placeValue(int(entery2), name2, board)

	viewBoard(board)
	check += 1

print("Thank You For Playing!\n")

# Red Square: \U0001F7E5 - 🟥
# Blue Square: \U0001F7E6 - 🟦
# Yellow Square: \U0001F7E8 - 🟨


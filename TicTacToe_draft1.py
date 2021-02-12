
class Game: 
	#row = 3
	#col = 3
	#game_board = [[0,0,0],[0,0,0],[0,0,0]]
	
	def __init__(self, r = 3, c= 3): 
		self.row = r 
		self.col = c 
		self.u1 = ''
		self.u2 = ''
		self.game_board = [[1,0,-1],[0,1,0],[-1,1,0]]
		
	def set_name(self, user1, user2):
		self.u1 = user1
		self.u2 = user2
	

	def play_game():
		print("playing")	

	def menu(self):
		option = 0
		print("1. Level 1: multi-player\n")
		print("2. Level 2: against computer\n")
		print("3. Level 3: against computer competitive\n")
		print("4. Exit\n\n")
	
		option = input("Enter an option from above: ")
		if type(option) != int: 
			print("Please enter an integer number\n")
		else: 
			option = int(option )
			if option > 4: 
				print("Please pick an option from the given list\n") 
	
		if int(option) ==1: 
			name = input("User1 name: ")
			name2 = input("User2 name: ")
			self.set_name(name, name2)
			print("Hi, "+name+" and "+name2, end= "\n")
	
		elif int(option) == 2: 
			print("Easy mode")
		elif int(option) ==3: 
			print("Hard mode")
		elif int(option) == 4: 
			print("Thank you for playing")


	def __str__(self): 
		printer = ''
		for i in range(self.row): 
			for j in range(self.col):
				printer += "|"
				if (self.game_board[i][j] == 0):
					printer += "___" 
				elif (self.game_board[i][j] == 1):
					printer += "_X_" 
				elif (self.game_board[i][j] == -1): 
					printer+= "_O_"
			printer += "|\n"
		return printer

	def clear_board(self):
		global game_board; 
		game_board = [[0]*self.col]*self.row 
	
	def move(self, user,row, col): 
		if(user == self.u1): 
			game_board[row, col] = 1
		elif(user == self.u2): 
			game_board[row, col] = -1 
	
	#def play(): 
			# enter the whole game print
			# check for tile filled or not 
			# should be an infinte loop?
			



  
def main(): 
	tester = Game()
	tester.menu()
	print(tester)
	#tester.printboard()
main()
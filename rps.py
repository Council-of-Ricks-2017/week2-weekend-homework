import random

class Player:
	def __init__(self, wins=0):
		self.name = input("Enter your name: ")
		self.wins = wins
		self.choice = None

	def ask_choice(self):
		player_choice = input("{}, choose [1]rock, [2]paper, or [3]scissor?".format(self.name))
		if player_choice not in ["1", "2", "3"]:
			print("Invalid, please enter a number")
			self.make_choice()
		else:
			self.choice = player_choice

class Game:
	def __init__(self, target_score=5):
		self.players = []
		self.add_player()
		self.round()
		self.target = target_score
		self.winner = None


	def add_player(self):
		self.players.append(Player())
		
		more_players = input("will there be more players? [y or n]")
		#validate correct input ^
		if more_players == "y":
			self.add_player()

		return self.players

	def round(self):
		for player in self.players:
			player.make_choice()
		self.compare()
		if self.check_end_game():
			self.results()
		else:
			self.round()


	def rand_comp_choice(self):
		rps = ["1", "2", "3"]
		comp_choice = random.choice(rps)
		return comp_choice

	def compare(self):
		comp_choice = self.rand_comp_choice()
		for player in self.players:
			if (comp_choice =="1" and player.choice =="2"):
				player.wins +=1
			if (comp_choice =="2" and player.choice =="3"):
				player.wins +=1
			if (comp_choice =="3" and player.choice =="1"):
				player.wins +=1

	def check_end_game(self):
		for player in self.players:
			if player.wins == self.target_score:
				self.winner = player
				# what will happen if multiple ppl reach target score?
				return True
			else:
				return False

	def results(self):
	
	print("{}, wins!".format(player.name))		



g = Game()
# print (g.add_player())
# print (g.rand_comp_choice())


#clear screen after each round and display the results




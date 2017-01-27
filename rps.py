class Player:
	def __init__(self, name, wins=0):
		self.name = name
		self.wins = wins


class Guess:
	def __init__(self, choice):
		self.choice = choice

	def player_choice(self):
		pass


class Game:
	def __init__(self):
		self.players = []
		self.score

	def add_player(self):
		name = input("Enter your name: ")
		player = Player(name)
		self.players.append(player.name) #only append the player name

		more_players = input("will there be more players? [y or n] ")
		if more_players = "y":
			self.add_player()
		return self.players

	def rand_comp_choice(self):
		rps = ["rock", "paper", "scissor"]
		comp_choice = random.choice(rps)
		return comp_choice

	def compare(self):
		pass

	def results(self):

g = Game()
g.add_player()
g.rand_comp_choice()

#multiple people hit 5
#screen should clear after every round
#print scoreboard and repeat round
#clear screen 
#



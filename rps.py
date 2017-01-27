class Player: 
	def __init__(self, name, wins):
		self.name = name 
		self.wins = wins

class Guess: 
	def __init__(self, choice):
		self.choice = choice 

	def player_choice(self):
		print('Players choice is {}'.format(self.name, self.choice))


class Game: 
	def __init__(self): 
		self.player = []
		self.score 

	def add_player(self):		
		player = Player(name)
		self.players.append(player)
		print(self.players)
		return self.players

	def rand_comp_choice(self):

	def compare(self):

	def results(self): 
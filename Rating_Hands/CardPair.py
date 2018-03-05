import pickle

class CardPair():

	with open('Hands.pickle', 'rb') as pickle_in:
		hands = pickle.load(pickle_in) 

	all_cards = [i for i in range(1,11)]
	all_cards.extend(['J', 'Q', 'K', 'A'])

	def __init__(self, cards = []):
		#Cards in terms of['card pair', bool: same suit]
		self.cards = cards
		# print(self.hands)

	def get_cards(self):
		return self.cards

	def give_rank(self):
		for i in range(len(self.hands)):
			if self.hands[i][0]==self.cards[0] and self.hands[i][2]==self.cards[1]:
				return self.hands[i][1]
		return "Nothing Found"


a = CardPair(["AK", True])
print(a.give_rank())
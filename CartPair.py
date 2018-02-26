#http://twodimes.net/poker/?g=h&b=&d=&h=3h+4h+%0D%0A%0D%0A

class Card():
	'''
	Card class to define a single card object. 
	'''

	cards = [str(card) for card in range(1,11)]
	cards.extend(('J', 'Q', 'K', 'A'))
	suits = ['h', 'd', 'c', 's']

	all_cards = []

	for suit in suits:
		for card in cards:
			all_cards.append(card+suit)

	def __init__(self, card):
		self.card = card
		assert self.card in self.all_cards, "{} is not a type of card. Declare card type in the form of card number + suit. For example Jh or 1d.".format(self.card)

	def getCardValue(self):
		return Card.cards.index(self.getNumber())

	def getNumber(self):
		return self.card[0]

	def getSuit(self):
		return self.card[1]

class CardPair(Card):

	def __init__(self, cardA, cardB):

		self.cardA = super().__init__(cardA)
		self.cardB = super().__init__(cardB)

	def getRating(self):
		pass
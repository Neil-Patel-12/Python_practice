from random import shuffle
# deck Of Cards

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		return f"{self.value} of {self.suit}"


print("<---- Card Class ---->\n")
c = Card("A", "hearts")
print(c)


class Deck:
	def __init__(self):
		suits = ["Spades", "Diamonds", "Clubs", "Hearts"]
		values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
		self.cards = [Card(val, sui) for sui in suits for val in values]

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def count(self):
		return len(self.cards)

	def _deal(self, num_to_remove):
		count = self.count()
		items_to_remove = min(count, num_to_remove)
		print(f"Going to remove {items_to_remove} cards from Deck.")
		if count == 0:
			raise ValueError("All cards have been dealt")
		dealt_cards = self.cards[-items_to_remove:]
		self.cards = self.cards[:-items_to_remove]
		return dealt_cards

	def shuffle(self):
		if self.count() < 52:
			raise ValueError("Only full decks can be shuffled.")
		else:
			shuffle(self.cards)
		return self


	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self, hand_size):
		return self._deal(hand_size)


print("<---- Deck Class ---->")
d = Deck()
d.cards
print(d.count())
print(d)

d2 = Deck()
d2.shuffle()
hand = d2.deal_hand(5)
print(hand)
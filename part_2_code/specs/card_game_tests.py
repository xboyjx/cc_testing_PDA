import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Hearts", 10)
        self.card2 = Card("Spades", 8)
        self.card3 = Card("Diamonds", 7)
        self.cards = [self.card1, self.card2, self.card3]

    def test_check_for_ace(self):
        self.assertEqual(CardGame.check_for_ace(self.card1), False)

    def test_highest_card(self):
        self.assertEqual(CardGame.highest_card(self, self.card1, self.card2), self.card1)
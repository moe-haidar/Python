from Card_Deck import Card,Deck
import unittest

class CardTests(unittest.TestCase):

    def setUp(self):
        self.card=Card("Hearts","A")
        #Test for the card's suit and value attributes being set correctly during initialization of a new instance

    def test_init(self):
        """Cards Should have a suit and a value"""
        self.assertEqual(self.card.suit,"Hearts")
        self.assertEqual(self.card.value,"A")


if __name__ == "__main__":
   unittest.main()
            
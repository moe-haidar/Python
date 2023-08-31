import random
class Card:

   def __init__(self,suit,value):
       self.suit=suit
       self.value=value

   def __repr__(self):
       return f"{self.value} of {self.suit}"
   
   @classmethod
   def from_string(cls,data_str):
        suit,value = data_str.split(",")
        return cls(suit,value)



#print(Card.from_string("heart,a"))


class Deck :

    def __init__(self):
        suit=("Hearts", "Diamonds", "Clubs","Spades")
        value=("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        self.cards=[]
        for s in suit:
            for v in value:
                card=""
                card=str(s)+","+str(v)
                self.cards.append(card)
        #print(self.cards)
       
     


    def __repr__(self):
       
        return f"Deck of {self.count()} Cards"
    
    def __iter__(self):
        return iter(self.cards)
    
    def count(self):
        return len(self.cards)


    def _deal(self,number):
          removed_cards=[]
          count=self.count()
          if count==0:
              raise ValueError("All cards have been dealt")
          elif number > count:
              removed_cards=self.cards.copy()
              self.cards.clear()
          else:    
            removed_cards=self.cards[-number:]
            self.cards=self.cards[:-number]  
          return removed_cards  


  
   
    def shuffle(self):
        if len(self.cards) == 52:
            
            return random.shuffle(self.cards)  # Shuffle the new_cards list
            
        else:
            raise ValueError("Only full decks can be shuffled") 


    def deal_card(self):
        single_card=self._deal(1)[0]
        
        return Card.from_string(single_card) 
    
    def deal_hand(self,number):
        single_card_list=[]
        single_card=self._deal(number)
        

        for card in single_card:
            
            card_obj=Card.from_string(card)
            single_card_list.append(card_obj)

        return single_card_list


d=Deck()
# print(d)
#print(d.deal_card())
# print(d._deal(53))
# print(d.count())
# print(len(d.cards))

for card in d:
    print(card+"\n")

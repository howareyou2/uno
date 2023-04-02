import random

class UNODeck:
    def __init__(self): 
        self.colors = ['RED', 'YELLOW', 'GREEN', 'BLUE']
        self.values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'SKILL_0', 'SKILL_1', 'SKILL_2']
        self.special_cards = ['BLACK_SKILL_3', 'BLACK_SKILL_4']
        self.cards = []
        
        # Generate all the cards
        for color in self.colors:
            for value in self.values:
                self.cards.append(color + '_' + value)
                if value != '0':
                    self.cards.append(color + '_' + value)
        for card in self.special_cards:
            for i in range(4):
                self.cards.append(card)
                
        # Shuffle the deck
        random.shuffle(self.cards)
        
    def deal(self, num_players, num_cards=7): # 카드 분배
        if num_players < 2 or num_players > 10:
            raise ValueError("Number of players must be between 2 and 10.")
        if num_cards < 1 or num_cards > 108 // num_players:
            raise ValueError("Number of cards per player must be between 1 and {}.".format(108 // num_players))
        
        hands = [[] for _ in range(num_players)]
        for _ in range(num_cards):
            for i in range(num_players):
                hands[i].append(self.cards.pop(0))
                
        return hands
    
    def getCards(self): # 분배하고 남은 카드
        return self.cards

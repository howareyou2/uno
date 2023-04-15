import random

class UNODeck:
    def __init__(self): 
        self.colors = ['RED', 'YELLOW', 'GREEN', 'BLUE']
        self.values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'SKIP', 'REVERSE', 'DRAW2']
        self.special_cards = ['BLACK_CHANGE', 'BLACK_DRAW4']
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

    def dealALL(self):
        num_players=4
        hands = [[] for _ in range(num_players)]
        j=0
        for i in range(103):
            hands[j].append(self.cards.pop(0))
            if j==3:
                j=0
            else:
                j+=1
        return hands 
    
    def storyshuffle(self): # 지역 A용 hands[0]=user hands[1]=computer
        self.cards=[]
        hands=[[] for _ in range(2)]
        for color in self.colors:
            for value in self.values:
                self.cards.append(color + '_' + value)
                if value != '0':
                    self.cards.append(color + '_' + value)
        for card in self.special_cards:
            for i in range(4):
                self.cards.append(card)
        weighten=[]
        for card in self.cards:
            card_attribute=card.split('_')
            if card_attribute[1]=='1' or card_attribute[1]=='2' or card_attribute[1]=='3' or card_attribute[1]=='4' or card_attribute[1]=='5'\
               or card_attribute[1]=='6' or card_attribute[1]=='7' or card_attribute[1]=='8' or card_attribute[1]=='9' or card_attribute[1]=='0':
                weighten.append(10)
            else:
                weighten.append(15)    
        for _ in range(7):    
            temp=random.choices(self.cards,weights=weighten,k=1)
            temp_index=self.cards.index(temp[0])
            self.cards.remove(temp[0])
            weighten.pop(temp_index)
            hands[1].append(temp[0])
        random.shuffle(self.cards)
        for _ in range(7):
            hands[0].append(self.cards.pop(0))
        
        return hands
                
        

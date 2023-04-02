import random

class UnoPlayer:
    def __init__(self,hand):
        self.hand = hand
    
    def play_card(self, top_card):
        valid_cards = [card for card in self.hand if card.can_play_on(top_card)]
        if valid_cards:
            chosen_card = random.choice(valid_cards)
            self.hand.remove(chosen_card)
            return chosen_card
        else:
            return None
    
    def draw_card(self, card):
        self.hand.append(card)
    
    def choose_color(self): # 색깔 변경 카드를 냈을 때 
        color_counts = {'RED': 0, 'YELLOW': 0, 'GREEN': 0, 'BLUE': 0}
        for card in self.hand: # 자기 핸드의 가장 많은 색깔로 바뀌게 함
            card_attribute=card.split('_');
            if card_attribute[0] != 'BLACK':
                color_counts[card_attribute[0]] += 1
        chosen_color = max(color_counts, key=color_counts.get)
        return chosen_color if color_counts[chosen_color] > 0 else random.choice(['RED', 'YELLOW', 'GREEN', 'BLUE'])

import random

class UnoPlayer:
    def __init__(self,hand):
        self.hand = hand
    
    def play_card(self, top_card, color):
        valid_cards = []
        top_card_attribute=top_card.split('_')
        for card in self.hand: # 핸드에 있는 모든 카드의 색깔과 숫자를 방금 나온 카드 색깔과 숫자를 비교해 유효한 카드 카드 선택
            card_attribute=card.split('_')
            if card_attribute[0]==color: # 색이 같으면 추가
                valid_cards.append(card)     
            elif card_attribute[1]==top_card_attribute[1]: # 모양이 같으면 추가
                valid_cards.append(card)
            elif card_attribute[0]=='BLACK' and card_attribute[1] == 'DRAW4': # 블랙draw 카드는 top_card의 색과 같은 색의 카드가 없을때만 낼 수 있음
                color_counts = {color: 0} # 현재 색깔과 같은 카드 카운트
                for card in self.hand: # 
                    card_attribute=card.split('_')
                    if card_attribute[0] == color:
                        color_counts[color] += 1
                if color_counts[color]==0: # 카운트가 0이면 BLACK_DRAW 카드 유효
                    valid_cards.append(card)
            elif card_attribute[0]=='BLACK': # 색 변경 카드 추가 
                valid_cards.append(card)
        if valid_cards:
            chosen_card = random.choice(valid_cards)
            self.hand.remove(chosen_card)
            return chosen_card
        else:
            return None
    
    def draw_card(self, card): # 한장 드로우
        self.hand.append(card)
    
    def choose_color(self): # 색깔 변경 카드를 냈을 때 
        color_counts = {'RED': 0, 'YELLOW': 0, 'GREEN': 0, 'BLUE': 0}
        for card in self.hand: # 자기 핸드의 가장 많은 색깔로 바뀌게 함
            card_attribute=card.split('_');
            if card_attribute[0] != 'BLACK':
                color_counts[card_attribute[0]] += 1
        chosen_color = max(color_counts, key=color_counts.get)
        return chosen_color if color_counts[chosen_color] > 0 else random.choice(['RED', 'YELLOW', 'GREEN', 'BLUE'])
    
    def gethand(self): # 핸드의 수
        return self.hand.len();
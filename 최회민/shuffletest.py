import random
colors = ['RED', 'YELLOW', 'GREEN', 'BLUE']
values = ['1', '2', '3', '4', 'SKIP', 'REVERSE', 'DRAW2']
special_cards = ['BLACK_CHANGE', 'BLACK_DRAW4']
cards = []
for color in colors:
    for value in values:
        cards.append(color + '_' + value)
        if value != '0':
            cards.append(color + '_' + value)
for card in special_cards:
    for i in range(4):
        cards.append(card)
weighten=[]
for card in cards:
    card_attribute=card.split('_')
    if card_attribute[1]=='1' or card_attribute[1]=='2' or card_attribute[1]=='3' or card_attribute[1]=='4':
        weighten.append(10)
    else:
        weighten.append(15)       
temp=random.choices(cards,weights=weighten,k=1000)
Number_count=0
Skill_count=0
for card in temp:
    card_attribute=card.split('_')
    if  card_attribute[1] == '1' or card_attribute[1] == '2' or card_attribute[1] == '3' or card_attribute[1] == '4':
        Number_count+=1
    elif card_attribute[1] == 'DRAW2' or card_attribute[1] == 'CHANGE' or card_attribute[1] == 'SKIP' or card_attribute[1] == 'REVERSE' or card_attribute[1] == 'DRAW4':
        Skill_count+=1    
print(Number_count)
print(Skill_count)
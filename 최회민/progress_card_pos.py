from loadcard import Card
from shuffle import UNODeck
from config import Configset
import pygame
deck=UNODeck()
hands=deck.deal(2)
card=deck.getCards()

cf=Configset()
default=cf.getChange()
screen_width= int(default[0])
screen_height= int(default[1])
screen=pygame.display.set_mode((screen_width,screen_height))

# 게임 시작할 때 
user_card=[]
for item in hands[0]:
    cards=Card(item, (120,110))
    user_card.append(cards)
i=0
temp_list=[]
for item in user_card:
    item.update((50+screen_width/10*i, screen_height*0.35/2))
    temp_list.append(item)
    i+=1
user_group=pygame.sprite.renderPlain(*temp_list) 
user_group.draw(screen) # 그리기

# 카드 낼때
sprite=user_group[0] # sprite는 내는 카드
user_group.remove(sprite) # 핸드에서 내려는 카드를 제거하고                    
for temp in user_group: # 남아있는 카드들에 대해
    temp.move(sprite.getposition()) # 제거한 카드의 위치에 대해 빈자리를 채우게 카드 이동  
pygame.display.update() # 화면 업데이트

#카드 뽑을때
temp=card.pop(0)
lastcard1=len(user_group)
temp = Card(item, (120, 110))
current_pos = lastcard1
if lastcard1 > 8:
    x=50+screen_width/10*(lastcard1-8)
    y=screen_height*0.35
else:
    x=50+screen_width/10*lastcard1 
    y=screen_height*0.35/2     
temp.setposition(x, y)
user_group.add(temp)
pygame.display.update() # 화면 업데이트
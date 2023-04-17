player_deck = []
temp_list=[]
i=0
for item in player_deck: # player_deck 해당 컴퓨터의 카드 리스트
    cards=Card('BACK',(800,600))
    cards.transform(30,40)
    cards.update((600+200/len(player_deck)*i, 100))
    temp_list.append(cards)
    i+=1
player_group=pygame.sprite.RenderPlain(*temp_list)
player_group.draw(screen)


# 내거나 드로우 했을때 실행
i=0
for item in player_group:
    item.update(((600+200/len(player_group.sprites())*i), 100))
    i+=1
player_group.draw(screen)
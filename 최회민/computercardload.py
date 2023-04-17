player_deck = []
temp_list=[]
i=0
for item in player_deck: # player_deck 해당 컴퓨터의 카드 리스트
    cards=Card('BACK',(800,600))
    cards.transform()
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


#플레이어 내는거 처음
user_card = []
for item in players[0]:
    cards = Card(item, (screen_width, screen_height))
    user_card.append(cards)
i = 0
temp_list = []
for item in user_card:
    # item.update((50 + (screen_width / 10) * i, (screen_height * 0.35) / 2))
    item.update((50 + 50 * i, 500))
    temp_list.append(item)
    i += 1
user_group = pygame.sprite.RenderPlain(*temp_list)
user_group.draw(screen)  # 그리기
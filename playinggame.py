import shuffle
import random
import pygame
import shuffle
import config
import loadcard
import Computerplay
import singlegame


from loadcard import Card
from shuffle import UNODeck
from config import Configset

#문제 우노와 와일드 드로우 4 둘다 게임도중구현??
#추가 구현 우노 1장인데 걸리면 ->2장챙기기
# 똑같이 우노버튼으로 만들고 1장이 아닌사람이 우노 버튼 누르면 1장인 사람 2장 챙기고
#와일드 드로우 4 -> 낸사람 손에 그색 카드 없어야한다 -> 도전 / 도전자 6장, 공격자 4장


#와일드 스왑 -> 교체후 색 고르기





#게임 실행할수 있게 모듈화
def gameplay():


    # 카드뽑기 함수, top에서
    def drawCards(numCards):
        cardsDrawn = []
        for x in range(numCards):
            cardsDrawn.append(unodeck.pop(0))

        return cardsDrawn

    # 플레이어가 플레이 가능한지 판단, 버린카드보고
    def canPlay(colour, value, playerHand):
        for card in playerHand:
            if "Black" in card:
                return True
            elif colour in card or value in card:
                return True
        return False





    # 버리는카드
    discards = []
    colours = ["Red", "Green", "Yellow", "Blue"]

    # 플레이어
    players = []

    #플레이어 인원 입력받기
    numPlayers = int(input("몇명?"))
    while numPlayers < 2 or numPlayers > 4:
        numPlayers = int(input("2명~4명으로 다시 입력하시오"))

    #플레이어 점수
    playerscore = []
    for i in range(numPlayers):
        playerscore.append(0)

    # 덱만들고 섞기
    unodeck = shuffle.UNODeck()
    temp = unodeck.deal(numPlayers)
    for hand in temp:
        players.append(hand)

    card = unodeck.getCards()

    cf = Configset()
    default = cf.getChange()
    screen_width = int(default[0])
    screen_height = int(default[1])
    screen = pygame.display.set_mode((screen_width, screen_height))


    deck = loadcard.Card('./최회민/img/BACK.png', (int(singlegame.section1_width*0.20), int(singlegame.section1_height*0.45)))
    back = pygame.image.load('./최회민/img/BACK.png')

    # 다음 턴
    playerTurn = 0
    # 시계방향1 반시계방향 -1
    playDirection = 1

    #게임 종료조건
    playing = True

    #처음 카드 1장 버리기
    discards.append(unodeck.cards.pop(0))

    #와일드 드로우 4인거 체크하기
    while discards[0] == 'Black_Draw Four':
        unodeck.append(discards.pop(0))
        discards.append(unodeck.pop(0))

    splitCard = discards[0].split("_", 1)


    #처음 카드색
    curruntcolour = splitCard[0]
    if curruntcolour != "Black":
        cardVal = splitCard[1]
    else:
        cardVal = "Any"

    #승자
    winner = -1

    # 게임 시작할 때
    user_card = []
    for item in players[0]:
        cards = Card(item, (120, 110))
        user_card.append(cards)
    i = 0
    temp_list = []
    for item in user_card:
        item.update((50 + screen_width / 10 * i, screen_height * 0.35 / 2))
        temp_list.append(item)
        i += 1
    user_group = pygame.sprite.renderPlain(*temp_list)
    user_group.draw(screen)  # 그리기


    while playing:
        #플레이서 손에 있는거 보여주기
        #showHand(playerTurn, players[playerTurn])

        # 0번 플레이어로 하고 나머지 컴퓨터로 하기

        #버린 카드 top에 있는 거 보여주기
        #print("Card on top of discard pile :  {}".format(discards[-1]))
        # 플레이 가능한지 체크
        if canPlay(curruntcolour, cardVal, players[playerTurn]):

            #플레이인지 체크
            if players[0]:
                # 플레이 가능한지 체크
                cardChosen = int(input("어떤 카드 고를거니?"))
                while not canPlay(curruntcolour, cardVal, [players[playerTurn][cardChosen - 1]]):
                    cardChosen = int(input("유효하지 않아 다시 선택해?"))
                print("You played {}".format(players[playerTurn][cardChosen - 1]))
                discards.append(players[playerTurn].pop(cardChosen - 1))
                # 카드 낼때
                sprite = user_group[cardChosen-1]  # sprite는 내는 카드
                user_group.remove(sprite)  # 핸드에서 내려는 카드를 제거하고

                for temp in players[playerTurn]:  # 남아있는 카드들에 대해
                    temp.move(sprite.getposition())  # 제거한 카드의 위치에 대해 빈자리를 채우게 카드 이동
                pygame.display.update()  # 화면 업데이트


                    #1장 남았다면 우노 누르기
                    #if len(players[playerTurn]) == 1:
                        # if 우노버튼 누르면

                        # 우노버튼 안눌르면 드로두 2개




                # 플레이어 이기는거 체크
                if len(players[playerTurn]) == 0:
                    playing = False
                    winner = playerTurn + 1
                #바로 못이기는 경우
                else:
                    # 버린카드 특별카드 체크
                    splitCard = discards[0].split("_", 1)
                    curruntcolour = splitCard[0]

                    # 와일드면 카드값에 any부여
                    if curruntcolour == "Black":
                        cardVal = "Any"
                    else:
                        cardVal = splitCard[1]
                    # 와읻드면 색 선택하게
                    if curruntcolour == "Black":
                        newColour = Computerplay.UnoPlayer.choose_color(players[playerTurn])
                        curruntcolour = colours[newColour - 1]
                    # 리버스면 다음턴 회전반대로
                    if cardVal == "Rerverse":
                        playDirection = playDirection * (-1)
                        if len(players) == 2:
                            playerTurn += playDirection
                            if playerTurn == numPlayers:
                                playerTurn = 0
                            elif playerTurn < 0:
                                playerTurn = numPlayers - 1

                    # 스킵하기
                    elif cardVal == "Skip":
                        playerTurn += playDirection
                        if playerTurn == numPlayers:
                            playerTurn = 0
                        elif playerTurn < 0:
                            playerTurn = numPlayers - 1
                    # 2장 뽑기
                    elif cardVal == "Draw Two":
                        playerDraw = playerTurn + playDirection
                        if playerDraw == numPlayers:
                            playerDraw = 0
                        elif playerDraw < 0:
                            playerDraw = numPlayers - 1
                        players[playerDraw].extend(drawCards(2))
                    # 와일드 드로우 4
                    elif cardVal == "Draw Four":
                        playerDraw = playerTurn + playDirection
                        if playerDraw == numPlayers:
                            playerDraw = 0
                        elif playerDraw < 0:
                            playerDraw = numPlayers - 1
                        players[playerDraw].extend(drawCards(4))
                    print("")

            #컴퓨터인 경우
            else:
                #이함수 hand넘겨받는기능추가필요
                res = Computerplay.play_card(discards[0], curruntcolour, players[playerTurn])
                #컴퓨터 낼수 있는경우
                discards.append(res)
                players[playerTurn].pop(players[playerTurn].index(res))

                #컴퓨터도 카드 내서 카드 수 감소하는거 구현필요


                #if len(players[playerTurn]) == 1:
                    #컴퓨터 우노구현
                #컴퓨터 승리조건
                if len(players[playerTurn]) == 0:
                    playing = False
                    winner = playerTurn + 1

                else:
                    # 버린카드 특별카드 체크
                    splitCard = discards[-1].split("_", 1)
                    curruntcolour = splitCard[0]

                    # 와일드면 카드값에 any부여
                    if curruntcolour == "Black":
                        cardVal = "Any"
                    else:
                        cardVal = splitCard[1]
                    # 와읻드면 색 선택하게
                    if curruntcolour == "Black":
                        newColour = Computerplay.UnoPlayer.choose_color(players[playerTurn])
                        curruntcolour = colours[newColour - 1]
                    # 리버스면 다음턴 회전반대로
                    if cardVal == "Rerverse":
                        playDirection = playDirection * (-1)
                        if len(players) == 2:
                            playerTurn += playDirection
                            if playerTurn == numPlayers:
                                playerTurn = 0
                            elif playerTurn < 0:
                                playerTurn = numPlayers - 1

                    # 스킵하기
                    elif cardVal == "Skip":
                        playerTurn += playDirection
                        if playerTurn == numPlayers:
                            playerTurn = 0
                        elif playerTurn < 0:
                            playerTurn = numPlayers - 1
                    # 2장 뽑기
                    elif cardVal == "Draw Two":
                        playerDraw = playerTurn + playDirection
                        if playerDraw == numPlayers:
                            playerDraw = 0
                        elif playerDraw < 0:
                            playerDraw = numPlayers - 1
                        players[playerDraw].extend(drawCards(2))
                    # 와일드 드로우 4
                    elif cardVal == "Draw Four":
                        playerDraw = playerTurn + playDirection
                        if playerDraw == numPlayers:
                            playerDraw = 0
                        elif playerDraw < 0:
                            playerDraw = numPlayers - 1
                        players[playerDraw].extend(drawCards(4))

        else:
            # 카드선택할 수 없으면
            players[playerTurn].extend(drawCards(1))
            if playerTurn==0: #플레이어라면

                # 카드 뽑을때
                item = players[playerTurn][-1]
                lastcard1 = len(user_group)
                temp = Card(item, (120, 110))

                if lastcard1 > 8:
                    x = 50 + screen_width / 10 * (lastcard1 - 8)
                    y = screen_height * 0.35
                else:
                    x = 50 + screen_width / 10 * lastcard1
                    y = screen_height * 0.35 / 2
                temp.setposition(x, y)
                user_group.add(temp)
                pygame.display.update()  # 화면 업데이트
            #else:
                #컴퓨터일때 구현, 카드 드로우해서 추가하는거 구현


        # 턴 이동
        playerTurn += playDirection
        if playerTurn == numPlayers:
            playerTurn = 0
        elif playerTurn < 0:
            playerTurn = numPlayers - 1
        #탑카드 바꾸기

        pygame.display.update()  # 화면 업데이트


    #점수계산
    #일반카드 숫자대로 / 와일드와 와일드 드로우4 50점/ 500점 나오면 전체 승리
    #드로우2, 리버스, 스킵 20점
    score = 0
    for player in players:
        for j in range(len(player)):
            curruntcard = player[j].split("_", 1)
            # 처음 카드색
            if splitCard[0] == "Black":
                score += 50
            else:
                if splitCard[1] == "Rerverse" or splitCard[1] == "Skip"  or splitCard[1] == "Draw Two":
                    score += 20
                else:
                    score += splitCard[1]
    #토탈 점수 계산해 500이상이면 완전끝
    playerscore[playerTurn-1] += score
                
            
            

    return winner


import shuffle
import random
import pygame


# 문제 우노와 와일드 드로우 4 둘다 게임도중구현??
# 추가 구현 우노 1장인데 걸리면 ->2장챙기기
# 똑같이 우노버튼으로 만들고 1장이 아닌사람이 우노 버튼 누르면 1장인 사람 2장 챙기고
# 와일드 드로우 4 -> 낸사람 손에 그색 카드 없어야한다 -> 도전 / 도전자 6장, 공격자 4장


# 와일드 스왑 -> 교체후 색 고르기


# 게임 실행할수 있게 모듈화
def gameplay():
    # 108카드 우노 덱 만들기
    def bulidDeck():
        deck = []
        # 레7 그8 블루스킵
        colours = ["Red", "Green", "Yellow", "Blue"]
        values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "SKip", "Reverse"]
        wilds = ["wild", 'wild Draw Four']
        for colour in colours:
            for value in values:
                cardVal = "{}_{}".format(colour, value)
                deck.append(cardVal)
                if value != 0:
                    deck.append(cardVal)
        for i in range(4):
            deck.append(wilds[0])
            deck.append(wilds[1])

        return deck

    # 리스트 섞기
    def shuffleDeck(deck):
        for cardPos in range(len(deck)):
            randPos = random.randint(0, 107)
            deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
        return deck

    # 카드뽑기 함수, top에서
    def drawCards(numCards):
        cardsDrawn = []
        for x in range(numCards):
            cardsDrawn.append(unoDeck.pop(0))

        return cardsDrawn

    # 플레이의 손의 카드개수?
    def showHand(player, playerHand):

        print("Player {}'s Turn".format(player + 1))
        print("Your hand")
        print("----------------")
        y = 1
        for card in playerHand:
            print("{} {}".format(y, card))
            y += 1
        print("")

    # 플레이어가 플레이 가능한지 판단, 버린카드보고
    def canPlay(colour, value, playerHand):
        for card in playerHand:
            if "wild" in card:
                return True
            elif colour in card or value in card:
                return True
        return False

    # 덱만들고 섞기
    unoDeck = bulidDeck()
    unoDeck = shuffleDeck(unoDeck)
    # 버리는카드
    discards = []
    # 플레이어
    players = []
    colours = ["Red", "Green", "Yellow", "Blue"]
    # 플레이어 인원 입력받기
    numPlayers = int(input("몇명?"))
    while numPlayers < 2 or numPlayers > 4:
        numPlayers = int(input("2명~4명으로 다시 입력하시오"))
    # 카드 나눠갖기
    for player in range(numPlayers):
        players.append(drawCards(5))

    # 다음 턴
    playerTurn = 0
    # 시계방향1 반시계방향 -1
    playDirection = 1

    # 게임 종료조건
    playing = True

    # 처음 카드 1장 버리기
    discards.append(unoDeck.pop(0))

    # 와일드 드로우 4인거 체크하기
    while discards[0] == 'wild Draw Four':
        unoDeck.append(discards.pop(0))
        discards.append(unoDeck.pop(0))

    splitCard = discards[0].split("_", 1)

    # 처음 카드색
    curruntcolour = splitCard[0]
    if curruntcolour != "wild":
        cardVal = splitCard[1]
    else:
        cardVal = "Any"

    while playing:
        # 플레이서 손에 있는거 보여주기
        showHand(playerTurn, players[playerTurn])
        print("Card on top of discard pile :  {}".format(discards[-1]))
        # 플레이 가능한지 체크
        if canPlay(curruntcolour, cardVal, players[playerTurn]):
            cardChosen = int(input("어떤 카드 고를거니?"))
            # 플레이 가능한지 체크
            while not canPlay(curruntcolour, cardVal, [players[playerTurn][cardChosen - 1]]):
                cardChosen = int(input("유효하지 않아 다시 선택해?"))
            print("You played {}".format(players[playerTurn][cardChosen - 1]))
            discards.append(players[playerTurn].pop(cardChosen - 1))

            # 1장 남았다면 우노 누르기
            # if len(players[playerTurn]) == 1:
            # if 우노버튼 누르면

            # 우노버튼 안눌르면 드로두 2개

            # 플레이어 이기는거 체크
            if len(players[playerTurn]) == 0:
                playing = False
                winner = playerTurn + 1
            else:

                # 특별카드 체크
                splitCard = discards[-1].split("_", 1)
                curruntcolour = splitCard[0]

                # 와일드면 카드값에 any부여
                if len(splitCard) == 1:
                    cardVal = "Any"
                else:
                    cardVal = splitCard[1]
                # 와읻드면 색 선택하게
                if curruntcolour == "wild":
                    for x in range(len(colours)):
                        print("{} {}".format(x + 1, colours[x]))
                    newColour = int(input("어떤 색을 선택할꺼니?"))
                    while newColour < 1 or newColour > 4:
                        newColour = int(input("색 다시 선택해줘"))
                    curruntcolour = colours[newColour - 1]
                # 리버스면 다음턴 회전반대로
                if cardVal == "Rerverse":
                    playDirection = playDirection * (-1)
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
        else:
            # 카드선택할 수 없으면
            players[playerTurn].extend(drawCards(1))
        print("")
        # 턴 이동
        playerTurn += playDirection
        if playerTurn == numPlayers:
            playerTurn = 0
        elif playerTurn < 0:
            playerTurn = numPlayers - 1

    # 점수계산
    # 일반카드 숫자대로 / 와일드와 와일드 드로우4 50점/ 500점 나오면 전체 승리
    # 드로우2, 리버스, 스킵 20점
    score = 0
    for player in players:
        for j in range(len(player)):
            curruntcard = player[j].split("_", 1)
            # 처음 카드색
            if splitCard[0] == "whild":
                score += 50
            else:
                if splitCard[1] == "Rerverse" or splitCard[1] == "Skip" or splitCard[1] == "Draw Two":
                    score += 20
                else:
                    score += splitCard[1]
    # 토탈 점수 계산해 500이상이면 완전끝

    return winner


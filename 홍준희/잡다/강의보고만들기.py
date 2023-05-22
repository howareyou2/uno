import pygame
import random


#108카드 우노 덱 만들기
def bulidDeck():
    deck = []
    # 레7 그8 블루스킵
    colours = ["Red","Green","Yellow", "Blue"]
    values = [0,1,2,3,4,5,6,7,8,9,"Draw Two","SKip", "Reverse"]
    wilds = ["wild", 'wild Draw Four']
    for colour in colours:
        for value in values:
            cardVal = "{} {}".format(colour, value)
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
        deck[cardPos], deck[randPos]=  deck[randPos], deck[cardPos]
    return deck

#카드뽑기 함수, top에서
def drawCards(numCards):
    cardsDrawn = []
    for x in range(numCards):
        cardsDrawn.append(unoDeck.pop(0))

    return cardsDrawn

#플레이의 손의 카드개수?
def showHand(player, playerHand):

    print("Player {}'s Turn".format(player+1))
    print("Your hand")
    print("----------------")
    y = 1
    for card in playerHand:
        print("{} {}".format(y, card))
        y += 1
    print("")

#플레이어가 플레이 가능한지 판단, 버린카드보고
def canPlay(colour, value, playerHand):
    for card in playerHand:
        if "wild" in card:
            return True
        elif colour in card or value in card:
            return True
    return False








unoDeck = bulidDeck()
unoDeck = shuffleDeck(unoDeck)
discards = []


players = []
colours = ["Red","Green","Yellow", "Blue"]


numPlayers = int(input("몇명?"))
while numPlayers<2 or numPlayers>4:
    numPlayers = int(input("2명~4명으로 다시 입력하시오"))

for player in range(numPlayers):
    players.append(drawCards(5))
print(players)

#다음 누구? 방향?
playerTurn = 0
#양의방향1 음의방향 -1
playDirection =1
playing = True
discards.append(unoDeck.pop(0))
splitCard = discards[0].split(" ",1)
curruntcolour = splitCard[0]
if curruntcolour != "wild":
    cardVal = splitCard[1]
else:
    cardVal = "Any"

while playing:
    showHand(playerTurn, players[playerTurn])
    print("Card on top of discard pile :  {}".format(discards[-1]))
    if canPlay(curruntcolour, cardVal, players[playerTurn]):
        cardChosen = int(input("어떤 카드 고를거니?"))
        #가능한지 체크
        while not canPlay(curruntcolour, cardVal, [players[playerTurn][cardChosen-1]]):
            cardChosen = int(input("유효하지 않아 다시 선택해?"))
        print("You played {}".format(players[playerTurn][cardChosen-1]))
        discards.append(players[playerTurn].pop(cardChosen-1))

        #플레이어이기는거 체크
        if len(players[playerTurn]) == 0:
            playing = False
            winner = "Player {}".format(playerTurn+1)
        else:


            # 특별카드 체크
            splitCard = discards[-1].split(" ", 1)
            curruntcolour = splitCard[0]

            # 와일이면 카드값에 any부여
            if len(splitCard) == 1:
                cardVal = "Any"
            else:
                cardVal = splitCard[1]

            if curruntcolour == "wild":
                for x in range(len(colours)):
                    print("{} {}".format(x + 1, colours[x]))
                newColour = int(input("어떤 색을 선택할꺼니?"))
                while newColour < 1 or newColour > 4:
                    newColour = int(input("색 다시 선택해줘"))
                curruntcolour = colours[newColour - 1]
            if cardVal == "Rerverse":
                playDirection = playDirection * (-1)

            elif cardVal == "Skip":
                playerTurn += playDirection
                if playerTurn == numPlayers:
                    playerTurn = 0
                elif playerTurn < 0:
                    playerTurn = numPlayers - 1

            elif cardVal == "Draw Two":
                playerDraw = playerTurn + playDirection
                if playerDraw == numPlayers:
                    playerDraw = 0
                elif playerDraw < 0:
                    playerDraw = numPlayers - 1
                players[playerDraw].extend(drawCards(2))
            elif cardVal == "Draw Four":
                playerDraw = playerTurn + playDirection
                if playerDraw == numPlayers:
                    playerDraw = 0
                elif playerDraw < 0:
                    playerDraw = numPlayers - 1
                players[playerDraw].extend(drawCards(4))
            print("")
    else:
        print("너는 카드를 선택할 수 없어")
        players[playerTurn].extend(drawCards(1))
    print("")

    playerTurn += playDirection
    if playerTurn == numPlayers:
        playerTurn = 0
    elif playerTurn < 0:
        playerTurn = numPlayers-1


print("게임끝")
print("{} 가 승자다".format(winner))









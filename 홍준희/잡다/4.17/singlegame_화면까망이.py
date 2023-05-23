import pygame
import sys
import shuffle
from loadcard import Card
import Computerplay
from config import Configset


pygame.init()




def start_game():
    '''
    # 이전 저장파일 불러오기
    cf = Configset()
    default = cf.getChange()
    screen_width = int(default[0])
    screen_height = int(default[1])
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("UNO Game")
    '''
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # 배경 이미지 불러오기
    background_image = pygame.image.load("./이채은/image/Sback.png")
    # 배경이미지 크기 조정
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))


    pygame.display.set_caption("UNO Game")
    ''



    # 카드뽑기 함수, top에서
    def drawCards(numCards):
        cardsDrawn = []
        for x in range(numCards):
            cardsDrawn.append(card.pop(0))

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
    colours = ["RED", "GREEN", "YELLOW", "BLUE"]
    # 플레이어
    players = []

    # 플레이어 인원 입력받기

    #일단 7명으로 임의로 지정
    numPlayers = 7

    # 플레이어 점수
    playerscore = []
    for i in range(numPlayers):
        playerscore.append(0)

    # 덱만들고 섞기
    unodeck = shuffle.UNODeck()
    temp = unodeck.deal(numPlayers)
    for hand in temp:
        players.append(hand)

    card = unodeck.getCards()



    # 다음 턴
    playerTurn = 0
    # 시계방향1 반시계방향 -1
    playDirection = 1



    # 처음 카드 1장 버리기
    discards.append(unodeck.cards.pop(0))

    # 와일드 드로우 4인거 체크하기
    while discards[-1] == 'BLACK_DRAW4':
        card.append(discards.pop(0))
        discards.append(card.pop(0))

    splitCard = discards[-1].split("_", 1)

    # 처음 카드색
    curruntcolour = splitCard[0]
    if curruntcolour != "BlACK":
        cardVal = splitCard[1]
    else:
        cardVal = "Any"

    # 승자
    winner = -1


    #'배경1.mp3' 파일 재생
    pygame.mixer.music.load('./이채은/sound/배경1.mp3')
    pygame.mixer.music.play(-1)
    '''
    # 전체화면 설정
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("UNO Game")
    '''





    # 게임 시작할 때
    print(players[0])
    print(discards[-1])
    user_card = []
    for item in players[0]:
        cards = Card(item, (screen_width, screen_height))
        user_card.append(cards)
    i = 0
    temp_list = []
    for item in user_card:
        #item.update((50 + (screen_width / 10) * i, (screen_height * 0.35) / 2))
        item.update((50 + 50 * i, 500))
        temp_list.append(item)
        i += 1
    user_group = pygame.sprite.RenderPlain(*temp_list)
    user_group.draw(screen)  # 그리기


    pygame.display.flip()

    # 팝업창 폰트 지정
    font = pygame.font.SysFont('comicsansms', 20)

    running = True
    # 게임 루프 실행
    while running:



        # 0번 플레이어로 하고 나머지 컴퓨터로 하기

        # 컴퓨터인 경우 먼저하기
        if playerTurn != 0:
            pygame.time.wait(700)

            print("top ", discards[-1], "player turn",playerTurn+1)

            # 이함수 hand넘겨받는기능추가필요
            unoplayer = Computerplay.UnoPlayer(players[playerTurn])
            res = unoplayer.play_card(discards[-1], curruntcolour)

            # 컴퓨터 낼수 없는경우
            if res == None:
                players[playerTurn].extend(drawCards(1))
                # 1장 추가되는거 이미지로 구현
                # 턴 이동
                playerTurn += playDirection
                if playerTurn == numPlayers:
                    playerTurn = 0
                elif playerTurn < 0:
                    playerTurn = numPlayers - 1


            else:
                # 컴퓨터 낼수 있는경우

                discards.append(res)
                # 이거 이미 컴퓨터 메소드 호출시 삭제해준다
                # players[playerTurn].remove(res)

                # 컴퓨터도 카드 내서 카드 수 감소하는거 구현필요

                # if len(players[playerTurn]) == 1:
                # 컴퓨터 우노구현
                # 컴퓨터 승리조건
                if len(players[playerTurn]) == 0:
                    playing = False
                    winner = playerTurn + 1

                else:
                    # 버린카드 특별카드 체크
                    splitCard = discards[-1].split("_", 1)
                    curruntcolour = splitCard[0]

                    # 와일드면 카드값에 any부여
                    if curruntcolour == "BLACK":
                        cardVal = "Any"
                    else:
                        cardVal = splitCard[1]
                    # 와읻드면 색 선택하게
                    if curruntcolour == "BLACK":
                        unoplayer = Computerplay.UnoPlayer(players[playerTurn])
                        newColour = unoplayer.choose_color(players[playerTurn])
                        # curruntcolour = colours[newColour - 1]
                        curruntcolour = newColour
                    # 리버스면 다음턴 회전반대로
                    if cardVal == "REVERSE":
                        playDirection = playDirection * (-1)
                        if len(players) == 2:
                            playerTurn += playDirection
                            if playerTurn == numPlayers:
                                playerTurn = 0
                            elif playerTurn < 0:
                                playerTurn = numPlayers - 1

                    # 스킵하기
                    elif cardVal == "SKIP":
                        playerTurn += playDirection
                        if playerTurn == numPlayers:
                            playerTurn = 0
                        elif playerTurn < 0:
                            playerTurn = numPlayers - 1
                    # 2장 뽑기
                    elif cardVal == "DRAW2":
                        playerDraw = playerTurn + playDirection
                        if playerDraw == numPlayers:
                            playerDraw = 0
                        elif playerDraw < 0:
                            playerDraw = numPlayers - 1
                        players[playerDraw].extend(drawCards(2))
                    # 와일드 드로우 4
                    elif cardVal == "DRAW4":
                        playerDraw = playerTurn + playDirection
                        if playerDraw == numPlayers:
                            playerDraw = 0
                        elif playerDraw < 0:
                            playerDraw = numPlayers - 1
                        players[playerDraw].extend(drawCards(4))

                    # 턴 이동
                    playerTurn += playDirection
                    if playerTurn == numPlayers:
                        playerTurn = 0
                    elif playerTurn < 0:
                        playerTurn = numPlayers - 1

                    # top카드 이미지 변화
                    back = pygame.image.load('./최회민/img/{}.png'.format(discards[-1]))
                    back = pygame.transform.scale(back, (int(section1_width * 0.20), int(section1_height * 0.45)))
                    section1.blit(back, (300, 110, 10, 10))
                    pygame.display.update()

        # 사람인경우
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            # "Pause" 버튼을 누르면 게임이 일시정지
            if event.type == pygame.MOUSEBUTTONDOWN:
                '''
                if pause_button_rect.collidepoint(event.pos):
                    pygame.time.wait(1000)
                    pygame.display.update()
                    # "Pause" 버튼을 누르면 "Continue", "Restart", "EndGame" 버튼 생성
                    pygame.draw.rect(screen, WHITE, (300, 230, 180, 40))
                    pygame.draw.rect(screen, WHITE, (300, 275, 180, 40))
                    pygame.draw.rect(screen, WHITE, (300, 320, 180, 40))
                    # 각각의 버튼에 "Continue", "Restart", "EndGame" 텍스트 생성
                    co_text = font.render("Continue", True, BLACK)
                    co_text_rect = co_text.get_rect(center=(300 + 150 / 2, 230 + 40 / 2))
                    screen.blit(co_text, co_text_rect)
                    re_text = font.render("Restart", True, BLACK)
                    re_text_rect = re_text.get_rect(center=(300 + 165 / 2, 275 + 40 / 2))
                    screen.blit(re_text, re_text_rect)
                    ex_text = font.render("EndGame", True, BLACK)
                    ex_text_rect = ex_text.get_rect(center=(300 + 140 / 2, 320 + 40 / 2))
                    screen.blit(ex_text, ex_text_rect)
                    pygame.display.flip()
                # ex_text를 누르면 게임이 종료되고 'startPage.py'로 돌아감
                if ex_text_rect.collidepoint(event.pos):
                    running = False
                # re_text를 누르면 'singlegame.py'가 다시 실행
                if re_text_rect.collidepoint(event.pos):
                    import singlegame
                    singlegame.singlegame()
                # co_text를 누르면 ex_text, re_text, co_text가 닫히고 '배경.mp3'가 다시 실행되며 게임이 이어서 진행됨
                # 계속 수정..
                if co_text_rect.collidepoint(event.pos):
                    pygame.draw.rect(screen, (255, 255, 0), (300, 230, 180, 40))
                    pygame.draw.rect(screen, (255, 255, 0), (300, 275, 180, 40))
                    pygame.draw.rect(screen, (255, 255, 0), (300, 320, 180, 40))
                    pygame.mixer.music.unpause()
                    pygame.display.flip()
                pygame.display.flip()
                '''


            if event.type == pygame.MOUSEBUTTONUP:
                if playerTurn == 0:
                    print("top ", discards[-1], "player turn", playerTurn + 1)
                    mouse_pos = pygame.mouse.get_pos()
                    # 내 카드 선택
                    for sprite in user_group:
                        if sprite.get_rect().collidepoint(mouse_pos):
                            if canPlay(curruntcolour, cardVal, players[playerTurn]):

                                # 카드 낼때
                                discards.append(sprite.get_name())
                                user_group.remove(sprite)  # 핸드에서 내려는 카드를 제거하고
                                players[playerTurn].remove(sprite.get_name())



                                for temp in user_group: # 남아있는 카드들에 대해
                                    temp.move(sprite.getposition()) # 제거한 카드의 위치에 대해 빈자리를 채우게 카드 이동
                                sprite.setposition(430, 300)
                                pygame.display.update()  # 화면 업데이트

                                # top카드 이미지 변화
                                #print(sprite.get_name())
                                #print(discards)

                                '''
                                #print(discards[-1],11,"그만 좀 허락해줘")
                                top = pygame.image.load('./최회민/img/{}.png'.format(discards[-1]))
                                top = pygame.transform.scale(top,
                                                              (int(section1_width * 0.20),
                                                               int(section1_height * 0.45)))
                                section1.blit(top, (300, 110, 10, 10))
                                pygame.display.update()
                                '''

                                # 플레이어의 카드 변화
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

                                # 버린카드 특별카드 체크
                                splitCard = discards[-1].split("_", 1)
                                curruntcolour = splitCard[0]

                                # 와일드면 카드값에 any부여
                                if curruntcolour == "BLACK":
                                    cardVal = "Any"
                                else:
                                    cardVal = splitCard[1]
                                # 와읻드면 색 선택하게
                                if curruntcolour == "BLACK":
                                    unoplayer = Computerplay.UnoPlayer(players[playerTurn])
                                    newColour = unoplayer.choose_color(players[playerTurn])
                                    curruntcolour = newColour

                                    '''
                                    newColour = Computerplay.UnoPlayer.choose_color(players[playerTurn])
                                    curruntcolour = colours[newColour - 1]
                                    '''
                                # 리버스면 다음턴 회전반대로
                                if cardVal == "REVERSE":
                                    playDirection = playDirection * (-1)
                                    if len(players) == 2:
                                        playerTurn += playDirection
                                        if playerTurn == numPlayers:
                                            playerTurn = 0
                                        elif playerTurn < 0:
                                            playerTurn = numPlayers - 1

                                # 스킵하기
                                elif cardVal == "SKIP":
                                    playerTurn += playDirection
                                    if playerTurn == numPlayers:
                                        playerTurn = 0
                                    elif playerTurn < 0:
                                        playerTurn = numPlayers - 1
                                # 2장 뽑기
                                elif cardVal == "DRAW2":
                                    playerDraw = playerTurn + playDirection
                                    if playerDraw == numPlayers:
                                        playerDraw = 0
                                    elif playerDraw < 0:
                                        playerDraw = numPlayers - 1
                                    players[playerDraw].extend(drawCards(2))
                                # 와일드 드로우 4
                                elif cardVal == "DRAW4":
                                    playerDraw = playerTurn + playDirection
                                    if playerDraw == numPlayers:
                                        playerDraw = 0
                                    elif playerDraw < 0:
                                        playerDraw = numPlayers - 1
                                    players[playerDraw].extend(drawCards(4))

                                # 턴 이동
                                playerTurn += playDirection
                                if playerTurn == numPlayers:
                                    playerTurn = 0
                                elif playerTurn < 0:
                                    playerTurn = numPlayers - 1
                                break
                    # 이건 덱에서 카드 뽑기

                    if sprite.get_rect().collidepoint(mouse_pos):

                        # 카드선택할 수 없으면
                        players[playerTurn].extend(drawCards(1))

                        # 플레이어의 카드 변화
                        item = players[playerTurn][-1]
                        lastcard1 = len(user_group.sprite())
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

                        # 턴 이동
                        playerTurn += playDirection
                        if playerTurn == numPlayers:
                            playerTurn = 0
                        elif playerTurn < 0:
                            playerTurn = numPlayers - 1

                        break





    # 점수계산
    # 일반카드 숫자대로 / 와일드와 와일드 드로우4 50점/ 500점 나오면 전체 승리
    # 드로우2, 리버스, 스킵 20점
    score = 0
    for player in players:
        for j in range(len(player)):
            curruntcard = player[j].split("_", 1)
            # 처음 카드색
            if splitCard[0] == "BLACK":
                score += 50
            else:
                if splitCard[1] == "REVERSE" or splitCard[1] == "SKIP" or splitCard[1] == "DRAW2":
                    score += 20
                else:
                    score += splitCard[1]

    # 토탈 점수 계산해 500이상이면 완전끝
    playerscore[playerTurn - 1] += score
    if playerscore[playerTurn - 1] >= 500:
        running= False

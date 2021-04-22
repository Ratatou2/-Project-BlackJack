import random
import time

deck = ['1', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4',
        '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8',
        '9', '9', '9', '9', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K',
        'A', 'A', 'A', 'A']

myMoney = 1000
count_card = 51
bodyCount = 11
partOfBody = ['오른쪽 눈', '왼쪽 눈', '오른쪽 귀', '왼쪽 귀', '오른손', '왼손', '오른발', '왼발', '입술', '코', '왼쪽 콩팥', '오른쪽 콩팥']

# 딜러가 A를 갖는 경우의 수 모두를 계산해주기 위해 총합 계산하는 결과값은 2가지를 줌
D_total_Sum1ver = 0
D_total_Sum11ver = 0
finaldealerDeck = []

def gameRule():
    print("「made by JH」\n"
          "개선사항 전달은 ratatou.duleum@gmail.com으로 부탁드립니다\n\n"
          "<< BlackJack(블랙잭) 게임룰 설명 >>\n"
          "1) 블랙잭은 카드를 뽑아서 총합을 21을 만드는 게임입니다\n"
          "2) J, Q, K는 10으로 계산하며, A는 1또는 11로 계산할수 있습니다.\n"
          "3) 카드는 원하는만큼 뽑을 수 있습니다(다만 21을 넘어가면 버스트)\n"
          "4) 총합 21은 '블랙잭'으로, 베팅한 금액의 1.5배를 받습니다\n"
          "5) 딜러와 같은 점수라면 무승부로 베팅한 금액을 다시 돌려받습니다\n"
          "6) 기본적으로 1000원이 주어지며, 모두 소진시 게임은 끝납니다\n"
          "\n"
          "미흡한 점이 있을 수 있으며 재미로 즐겨주시기 바랍니다\n\n")

# 플레이어 덱 총합 변환 코드
def checkCard(define):
    if define == 'J':
        return 10
    elif define == 'Q':
        return 10
    elif define == 'K':
        return 10
    elif define == 'A':
        print("A를 1과 11 둘중 하나로 사용할 수 있습니다\n 어느쪽으로 사용하시겠습니까?")
        while True:
            try:
                ans = int(input())

                if ans < 0:
                    print("다시 입력하세요.")
                else:
                    print(ans)
                    break

            except ValueError:
                print("A를 1과 11 둘중 하나로 사용할 수 있습니다\n 어느쪽으로 사용하시겠습니까?")

        if ans == 1:
            return 1
        else:
            return 11

    else: return int(define)

# 플레이어와 딜러의 카드 드로우
def playerAndDealer():
    global myMoney, count_card, D_total_Sum1ver, D_total_Sum11ver, finaldealerDeck, bodyCount, partOfBody


    print("현재 보유 금액 >>>", myMoney)
    print("<System> 베팅 금액을 입력하십시오 >>> ", end='')

    # 게임이 반복됐을 때를 위한 초기화 부분
    playerDeck = []
    dealerDeck = []
    finaldealerDeck = []

    while True:
        try:
            betMoney = int(input())

            if betMoney > myMoney:
                print("<System> 올인하셨습니다.")
                betMoney = myMoney
                print("<System> 현재 베팅 금액 >>>", betMoney, "\n")
                break
            elif betMoney <= 0:
                print("<System> 밑장빼기 시도 확인, 신체 일부를 잘라갑니다.")
                print("<System> 주사위를 굴려 나온 갯수만큼 잘라갑니다")
                dice = random.randint(1, 6)
                print("<System> 주사위 >>>", dice)

                for i in range(0, dice):
                    part = partOfBody[random.randint(0, bodyCount)]
                    partOfBody.remove(part)
                    bodyCount -= 1
                    print("<System>「", part, "」 압수")

                    if len(partOfBody) == 0:
                        print('\n<System> 당신은 모두 잘려 쓸모없습니다.')
                        print('<System> 게임 진행 불가')
                        print('<System> 30초 후에 자동으로 꺼집니다')
                        time.sleep(300)
                        exit()

                print("<System> 위로금을 받습니다 +300")
                myMoney += 300

                print("<System> 남은 재산 >>>", myMoney, "\n")
                print("<System> 베팅 금액을 입력하십시오 >>> ", end='')
            else:
                print("<System>", betMoney,"원을 걸었습니다.\n")
                break;


        except ValueError:
            print("입력한 값이 없거나 정확하지 않습니다. 정확한 베팅 금액을 입력하세요")

    # 딜러 드로우
    def dealerDraw():
        global count_card
        D_card = deck[random.randint(0, count_card)]
        deck.remove(D_card)
        dealerDeck.append(D_card)
        finaldealerDeck.append(D_card)
        count_card -= 1

    # 플레이어 드로우
    def playerDraw():
        global count_card
        P_card = deck[random.randint(0, count_card)]
        deck.remove(P_card)
        playerDeck.append(P_card)
        count_card -= 1


    # 첫번째 드로우
    playerDraw()
    dealerDraw()

    # 두번째 드로우
    playerDraw()
    dealerDraw()

    print("※ 현재 플레이어 카드 >>>", playerDeck)
    print("※ 현재 딜러의 첫번째 카드 >>>", dealerDeck[0], '\n')

    # 블랙잭 실제 플레이 영상을 참고했는데 플레이어의 카드를 보고나서 플레이어가 더 먹을지 말지 선택을 함
    # 딜러가 추가 드로우하는 타이밍은 따로 있었음
    # 또한 딜러의 카드 한장을 볼 수 있음

    # 플레이어 추가 드로우 while문
    while True:
        print("___________________________")
        print("<System> 더 뽑으시겠습니까?\n (1) 예 / (2) 아니오")
        while True:
            try:
                ans = int(input())
                if ans < 0:
                    print("1과 2 둘중 하나를 골라주세요")
                else:
                    print(ans)
                    break

            except ValueError:
                print("입력한 값이 없거나 제대로 된 값이 아닙니다")
                print("<System> 더 뽑으시겠습니까?\n (1) 예 / (2) 아니오")

        print("---------------------------")

        if ans == 1:
            playerDraw()
            print("현재 플레이어 카드 >>>", playerDeck)

        elif ans == 2: break

    # 플레이어 점수 변환
    playerTotal = 0
    for card in playerDeck:
        cardToScore = checkCard(card)
        playerTotal += cardToScore

    print("<System> 플레이어의 총합 >>>", playerTotal)

    if playerTotal == 21:
        print("<System> 블랙잭입니다!\n") # 블랙잭이면 1.5배를 받음
        print("<System> 배팅금액의 1.5배를 받습니다\n")
        betMoney = int(betMoney * 1.5)

    elif playerTotal > 22:
        print("<System> 플레이어 버스트\n")

    # 딜러는 플레이어와 달리 유동적인 A 선택이 불가능함
    # 이를 해결하기 위해 2가지 경우의 수를 모두 계산해줌
    D_total_Sum1ver, D_total_Sum11ver = 0, 0
    def checkCardForDealer(define):
        global D_total_Sum1ver, D_total_Sum11ver

        if define == 'J':
            D_total_Sum1ver += 10
            D_total_Sum11ver += 10
            return [D_total_Sum1ver, D_total_Sum11ver]

        elif define == 'Q':
            D_total_Sum1ver += 10
            D_total_Sum11ver += 10
            return [D_total_Sum1ver, D_total_Sum11ver]

        elif define == 'K':
            D_total_Sum1ver += 10
            D_total_Sum11ver += 10
            return [D_total_Sum1ver, D_total_Sum11ver]

        elif define == 'A':
            D_total_Sum1ver += 1
            D_total_Sum11ver += 11
            return [D_total_Sum1ver, D_total_Sum11ver]

        else:
            trnas = int(define)
            D_total_Sum1ver += trnas
            D_total_Sum11ver += trnas
            return [D_total_Sum1ver, D_total_Sum11ver]


    for card in dealerDeck:
        checkCardForDealer(card)

    tempList = [D_total_Sum1ver, D_total_Sum11ver]

    for score in tempList:
        break

    # 딜러는 항상 17 미만일 경우 추가 드로우를 해야한다
    # 이떈 직접 하나 드로우하게 함
    transToScore = []
    while True :
        if score >= 17:
            fir = tempList[0]
            sec = tempList[1]
            break

        elif score < 17:

            D_card = deck[random.randint(0, count_card)]
            deck.remove(D_card)
            finaldealerDeck.append(D_card)
            count_card -= 1
            transToScore = checkCardForDealer(D_card)

            m1 = transToScore[0]
            m2 = transToScore[1]
            transToScore.clear()

            transToScore.append(m1)
            transToScore.append(m2)


            if transToScore[0] >= 17:
                fir = transToScore[0]
                sec = transToScore[1]
                break
            elif 17 <= transToScore[1] <= 21:
                fir = transToScore[0]
                sec = transToScore[1]
                break




    dealerTotal = 0
    print("딜러의 패 >>>", finaldealerDeck)
    if fir > 21:
        print("딜러의 총합 >>>", fir, '\n')
        dealerTotal = fir
    elif fir <= 21:
        if fir == sec:
            print("딜러의 총합 >>>", fir, '\n')
            dealerTotal = fir
        else:
            if sec > 21:
                print("딜러의 총합 >>>", fir, '\n')
                dealerTotal = fir
            else:
                print("딜러의 총합 >>>", sec, '\n')
                dealerTotal = sec


    if playerTotal > 21:
        print("<<플레이어 버스트, 패배했습니다>>")
        myMoney -= betMoney
    elif playerTotal <= 21 and dealerTotal > 21:
        print("<<플레이어의 승리>>")
        myMoney += betMoney
    elif playerTotal <= 21:
        if playerTotal == dealerTotal:
            print("<<무승부, 베팅한 금액을 돌려받습니다>>")
        elif playerTotal > dealerTotal:
            print("<<플레이어의 승리>>")
            myMoney += betMoney
        elif playerTotal < dealerTotal:
            print("<<딜러의 승리>>")
            myMoney -= betMoney

    print("\n현재 잔액 >>>", myMoney)
    print("________________________\n")

#플레이 시작
playCount = 0
print("<System> 게임에 대한 설명이 필요하신 분은 엔터대신 'rule'을 입력해주세요")
while True:
    print("<System> 현재 플레이한 횟수는", playCount, "회 입니다.")
    print("<System> 엔터를 치면 게임을 시작합니다")
    start = str(input())

    if start == 'rule':
        gameRule()

    playerAndDealer()
    playCount += 1

    # 매 게임마다 덱을 리셋
    count_card = 51
    deck = ['1', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4',
            '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8',
            '9', '9', '9', '9', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K',
            'A', 'A', 'A', 'A']

    # 돈이 없을 경우 게임 종료
    if myMoney <= 0:
        print('<System> 당신은 파산하였습니다')
        print('<System> 30초 후에 자동으로 꺼집니다')
        time.sleep(300)
        break

    else: pass

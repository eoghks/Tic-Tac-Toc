import random

def click(button_list, player, index):
    if(player[0]==1):
        button_list[index][0]="O"
        player[0]=2
    else:
        button_list[index][0]="X"
        player[0]=1

def checkwinner(list, player, winner):
    check=""
    if player[0]==2:#플레이어의 턴을 넘겨줫기때문에
        check="O"
    else:
        check="X"
#가로
    for i in range(3):
        if(list[i][0]!=check):
            break;
        if(i==2):
            if(player[0]==2):
                winner[0]=1
            else:
                winner[0]=2

    for i in range(3,6):
        if(list[i][0]!=check):
            break;
        if(i==5):
            if(player[0]==2):
                winner[0]=1
            else:
                winner[0]=2

    for i in range(6,8):
        if(list[i][0]!=check):
            break;
        if(i==8):
            if(player[0]==2):
                winner[0]=1
            else:
                winner[0]=2
        
#세로
    for i in range(0,7,3):
        if(list[i][0]!=check):
            break;
        if(i>=6):
            if(player[0]==2):
                winner[0]=1
            else:
                winner[0]=2
                
    for i in range(1,8,3):
        if(list[i][0]!=check):
            break;
        if(i>=7):
            if(player[0]==2):
                winner[0]=1
            else:
                winner[0]=2

    for i in range(2,9,3):
        if(list[i][0]!=check):
            break;
        if(i>=8):
            if(player[0]==2):
                winner[0]=1
            else:
                winner[0]=2

#정대각선
    for i in range(0,9,4):
        if(list[i][0]!=check):
            break;
        if(i>=8):
            if(player[0]==2):
                winner[0]=1
            else:
                winner[0]=2

#역대각선
    for i in range(2,7,2):
        if(list[i][0]!=check):
            break;
        if(i>=6):
            if(player[0]==2):
                winner[0]=1
            else:
                winner[0]=2
            
def computer(button_list):
    while(True):
        number=random.randint(0,8)
        if(button_list[number][0]==" "):
            return number
        

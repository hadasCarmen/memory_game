import random
import time
import copy
symbols = ["\U0001F600","\U0001F603","\U0001F604","\U0001F601","\U0001F606","\U0001F605","\U0001F923","\U0001F602","\U0001F642","\U0001F643","\U0001F609","\U0001F60A","\U0001F607"]


def create_boards(size: int, symbols: list[str]) ->dict:
    board=[]
    mone2=0
    mone1=0
    for i in range(size):
        mat_emoji=[]
        for j in range(size):
            mone2+=1
            if mone2%2!=0:
                mone1+=1
            mat_emoji.append(symbols[mone1])
        board.append(mat_emoji)
    for i in range(200):
        x=random.sample(range(0,size),2)
        y=random.sample(range(0,size),2)
        board[x[0]][x[1]],board[y[0]][y[1]]=board[y[0]][y[1]],board[x[0]][x[1]]
    board_game=[]
    for i in range(size):
        arr=[]
        for j in range(size):
            arr.append("X")
        board_game.append(arr)
    
    return {"board":board,"board_game":board_game}
# boards=create_boards(4,symbols)
# board=boards["board"]
# board_game=boards["board_game"]

def choose_card1(boards):
    print(boards["board_game"])
    try:
        row=int(input("choose location card first,2 points,now the first "))
        col=int(input("now the second "))
    except:
        return choose_card1(boards)
    if row>len(boards["board"])-1 or col>len(boards["board"])-1 :
        print("you need in range")
        return choose_card1(boards)
    elif boards["board_game"][row][col]!="X":
        print("this choose before,choose another")
        return choose_card1(boards)
    return row,col

def choose_card2(boards):
    print(boards["board_game"])
    try:
        row=int(input("choose location card second,2 points,now the first "))
        col=int(input("now the second "))
    except:
        print("you need number")
        return choose_card2(boards)
    if row>len(boards["board"])-1 or col>len(boards["board"])-1 :
        print("you need in range")
        return choose_card1(boards)
    elif boards["board_game"][row][col]!="X":
        print("this choose before,choose another")
        return choose_card1(boards)
    return row,col

# point1=choose_card1(boards)

def reveal_tile(boards,point1) -> str | None:
    print(boards["board"][point1[0]][point1[1]])
    boards["board_game"][point1[0]][point1[1]]=boards["board"][point1[0]][point1[1]]
    return boards["board"][point1[0]][point1[1]]
# card1=reveal_tile(board,point1)
# point2=choose_card2(boards)
# card2=reveal_tile(board,point2)

def hide_tiles(boards,point1,point2) -> None:
    print(boards["board_game"])
    if boards["board"][point1[0]][point1[1]]!=boards["board"][point2[0]][point2[1]]:
        boards["board_game"][point1[0]][point1[1]]="X"
        boards["board_game"][point2[0]][point2[1]]="X"
        print("cards not same")
        time.sleep(3)
        print(boards["board_game"])
        return True
    return False
# hide_tiles(boards,point1,point2)






from memory.board import *
from memory.logic import *

def play_memory_game(size):
    boards=create_boards(size,symbols)
    mone=0
    while not is_won(boards):
        point1=choose_card1(boards)
        card1=reveal_tile(boards,point1)
        point2=choose_card2(boards)
        card2=reveal_tile(boards,point2)
        if not hide_tiles(boards,point1,point2):
            chek_match(boards,point1,point2)
        mone+=1
    print("you succeed in",mone,"tries")
    return

play_memory_game(2)
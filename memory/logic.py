def chek_match(boards,point1,point2):
    if boards["board"][point1[0]][point1[1]]==boards["board"][point2[0]][point2[1]]:
        print("cards same")
        return True
    return False

def is_won(boards):
    for cards in boards["board_game"]:
        for card in cards:
            if card=="X":
                return False
    return True
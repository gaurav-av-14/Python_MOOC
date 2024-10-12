# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if 2<x or x<0 or 2<y or y<0:
        return False
    if game_board[y][x]!="":
        return False
    else:
        game_board[y][x]=piece
        return True
if __name__ == "__main__":
    game_board = [["", "", ""], ["", "X", ""], ["X", "", ""]]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)
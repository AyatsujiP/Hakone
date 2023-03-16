def read_fen_from_current_position(move_board):
    ret = ""
    for i in range(0,8):
        counter = 0
        for j in range(0,8):
            if move_board[i][j] == "br":
                ret = ret + "r"
            elif move_board[i][j] == "bn":
                ret = ret + "n"
            elif move_board[i][j] == "bb":
                ret = ret + "b"
            elif move_board[i][j] == "bq":
                ret = ret + "q"
            elif move_board[i][j] == "bk":
                ret = ret + "k"
            elif move_board[i][j] == "bp":
                ret = ret + "p"
            elif move_board[i][j] == "wr":
                ret = ret + "R"
            elif move_board[i][j] == "wn":
                ret = ret + "N"
            elif move_board[i][j] == "wb":
                ret = ret + "B"
            elif move_board[i][j] == "wq":
                ret = ret + "Q"
            elif move_board[i][j] == "wk":
                ret = ret + "K"
            elif move_board[i][j] == "wp":
                ret = ret + "P"
            else: #"em"
                counter = counter + 1
                if j==7:
                    ret = ret + str(counter)
                else:
                    if move_board[i][j+1] != "em":
                        ret = ret + str(counter)
                        counter = 0
        if i!=7:
            ret = ret + "/"        
    return ret

def load_fen(fen):
    current_board = []
    print(fen)
    fsp = fen.split("/")
    for f in fsp: #one by one
        inner = []
        for l in f:
            if l in ['1','2','3','4','5','6','7','8']:
                for i in range(0,int(l)):
                    inner.append("em")
            elif l == "K":
                inner.append("wk")
            elif l == "Q":
                inner.append("wq")
            elif l == "R":
                inner.append("wr")
            elif l == "B":
                inner.append("wb")
            elif l == "N":
                inner.append("wn")
            elif l == "P":
                inner.append("wp")
            elif l == "k":
                inner.append("bk")
            elif l == "q":
                inner.append("bq")
            elif l == "r":
                inner.append("br")
            elif l == "b":
                inner.append("bb")
            elif l == "n":
                inner.append("bn")
            elif l == "p":
                inner.append("bp")            
        current_board.append(inner.copy())
        inner = []
    print(current_board)
    return current_board
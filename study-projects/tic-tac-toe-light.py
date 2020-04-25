turn = input("Enter cels:")
 

if turn.count("X") > 5:
    print("Impossible")
elif turn.count("O") > 5:
    print("Impossible")

def print_table():
    line1 = turn [0:3]
    line1_spaces = " ".join(line1)
    line2 = turn [3:6]
    line2_spaces = " ".join(line2)
    line3 = turn [6:]
    line3_spaces = " ".join(line3)

    print(
f"""
---------
| {line1_spaces} |
| {line2_spaces} |
| {line3_spaces} |
---------""")
    
def input_x():
    if turn.startswith("XXX"):
        print("X wins")
    elif turn.endswith("XXX"):
        print("X wins")
    elif turn[3] == "X":
        if turn[4] == "X":
            if turn[5] == "X":
                print_table()
                print("X wins")
    elif turn[0] == "X":
        if turn[3] == "X":
            if turn[6] == "X":
                print_table()
                print("X wins")           
    elif turn[1] == "X":
        if turn[4] == "X":
            if turn[7] == "X":
                print_table()
                turn("X wins")
    elif turn[2] == "X":
        if turn[5] == "X":
            if turn[8] == "X":
                print("X wins")
    elif turn[0] == "X":
        if turn[4] == "X":
            if turn[8] == "X":
                print_table()
                turn("X wins")
    elif turn[2] == "X":
        if turn[4] == "X":
            if turn[6] == "X":
                print_table()
                turn("X wins")
    elif turn.count("X") > 5:
        print("Impossible")

def input_o():
    if turn.startswith("OOO"):
        print("O wins")
    elif turn.endswith("OOO"):
        print("O wins")
    elif turn[3] == "O":
        if turn[4] == "O":
            if turn[5] == "O":
               print_table() 
               print("O wins")
    elif turn[0] == "O":
        if turn[3] == "O":
            if turn[6] == "O":
               print_table() 
               print("O wins")
    elif turn[2] == "O":
        if turn[5] == "O":
            if turn[8] == "O":
                print_table()
                print("O wins")
    elif turn[1] == "O":
        if turn[4] == "O":
            if turn[7] == "O":
                print_table()
                print("O wins")           
    elif turn[0] == "O":
        if turn[4] == "O":
            if turn[8] == "O":
                print_table()
                print("O wins")
    elif turn[2] == "O":
        if turn[4] == "O":
            if turn[6] == "O":
                print_table()
                print("O wins")
    elif turn.count("O") > 5:
        print_table()
        print("Impossible")


while True:
    if '_' in (turn):
        if not input_x() and not input_o():
            print_table()
            print("Game not finished")
            break
    elif '_' not in (turn):
        if not input_x() and not input_o():
            print_table()
            print("Draw")
            break

          

           





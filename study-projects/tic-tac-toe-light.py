turn = input("Enter cels:")
 
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
        return ("X wins")
    elif turn.endswith("XXX"):
        return ("X wins")
    elif turn[3] == "X" and turn[4] == "X" and turn[5] == "X":
        return ("X wins")
    elif turn[0] == "X" and turn[3] == "X" and turn[6] == "X":
        return ("X wins")           
    elif turn[1] == "X" and turn[4] == "X" and turn[7] == "X":
        return ("X wins")
    elif turn[2] == "X" and turn[5] == "X" and turn[8] == "X":
        return ("X wins")   
    elif turn[0] == "X" and turn[4] == "X" and turn[8] == "X":
        return ("X wins")
    elif turn[2] == "X" and turn[4] == "X" and turn[6] == "X":
        return ("X wins")


def input_o():
    if turn.startswith("OOO"):
        return ("O wins")
    elif turn.endswith("OOO"):
        return ("O wins")
    elif turn[3] == "O" and turn[4] == "O" and turn[5] == "O":
        return ("O wins")
    elif turn[0] == "O" and turn[3] == "O" and turn[6] == "O":
        return ("O wins")
    elif turn[1] == "O" and turn[4] == "O" and turn[7] == "O":
        return ("O wins")
    elif turn[2] == "O" and turn[5] == "O" and turn[8] == "O":
        return ("O wins")
    elif turn[0] == "O" and turn[4] == "O" and turn[8] == "O":
        return ("O wins")
    elif turn[2] == "O" and turn[4] == "O" and turn[6] == "O":
        return ("O wins")

def draw():
    if turn.count("X") == 5 and turn.count("O") == 4 or turn.count("X") == 4 and turn.count("O") == 5:
        if not input_x () and not input_o():
            return("Draw")

while True:
    if input_x():
        print_table()
        print('X wins')
        break   
    
    elif input_o():
        print_table()
        print('O wins')
        break 
    
    elif input_x() and input_o():
        print_table()
        print ('Impossible')
        break
    
    elif turn.count("X") - turn.count("O") > 2 or turn.count("O") - turn.count("X"):
        print_table()
        print ('Impossible')
        break       

    
    elif not input_x() and not input_o() and not draw():
        print_table()
        print("Game not finished")
        break
   
    elif draw():
        print_table()
        print("Draw")
        break
   

    

           





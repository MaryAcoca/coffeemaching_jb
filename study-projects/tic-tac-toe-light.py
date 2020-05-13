

 
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

def coordinates_check():
    if 1 1:
        if 


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
        return ("O Wins")
    elif turn.endswith("OOO"):
        return ("O Wins")
    elif turn[3] == "O" and turn[4] == "O" and turn[5] == "O":
        return ("O Wins")
    elif turn[0] == "O" and turn[3] == "O" and turn[6] == "O":
        return ("O Wins")
    elif turn[1] == "O" and turn[4] == "O" and turn[7] == "O":
        return ("O Wins")
    elif turn[2] == "O" and turn[5] == "O" and turn[8] == "O":
        return ("O Wins")
    elif turn[0] == "O" and turn[4] == "O" and turn[8] == "O":
        return ("O Wins")
    elif turn[2] == "O" and turn[4] == "O" and turn[6] == "O":
        return ("O Wins")

def draw():
    if turn.count("X") == 5 and turn.count("O") == 4 or turn.count("X") == 4 and turn.count("O") == 5:
        if not input_x () and not input_o():
            return("Draw")

while True:
    turn = input("Enter cels:")
    print_table()
    enter_the_coordinates = input("Enter the coordinates:")


    if input_x():
        if input_o():
            print_table()
            print()
            print ('Impossible')
            break

        else:
            print_table()
            print()
            print ("X wins")
            break

    elif input_o():
        print_table()
        if input_x():
            print_table()
            print()
            print ('Impossible')
            break

        else:
            print_table()
            print()
            print ("O wins")
            break
        
    elif turn.count("X") - turn.count("O") >= 2:
        print_table()
        print()
        print ('Impossible')
        break

    elif turn.count("O") - turn.count("X") >= 2:
        print_table()
        print()
        print ('Impossible')
        break

    elif draw():
        print_table()
        print()
        print("Draw")
        break

    elif not input_x() and not input_o() and not draw():
        print_table()
        print()
        print("Game not finished")
        break
    
   

   
  

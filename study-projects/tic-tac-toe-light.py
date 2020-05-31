
import string
grid_input = list(input("Enter cells: "))
playing_grid = [grid_input[:3], grid_input[3:6], grid_input[6:]]
game_complete = "_" not in playing_grid

# def win_condition(line):
#     if set(line) == {"X"}:
#         return "X"
#     if set(line) == {"O"}:
#         return "O"
#     else:
#         return False

def print_grid():
    print("---------")
    print("| " + " ".join(playing_grid[0]) + " |")
    print("| " + " ".join(playing_grid[1]) + " |")
    print("| " + " ".join(playing_grid[2]) + " |")
    print("---------")

print_grid()

while True:
    input_coord = input("Enter the coordinates: ").split()
    if any(coord not in string.digits for coord in input_coord):
        print("You should enter numbers!")
        continue
    int_coord = [int(coord) for coord in input_coord ]
    if any(coord < 1 or coord > 3 for coord in int_coord):
        print("Coordinates should be from 1 to 3!")
        continue
    grid_coord = [-1 * (int_coord[1] - 3), int_coord[0] - 1]
    if playing_grid[grid_coord[0]][grid_coord[1]] != "_":
        print("This cell is occupied! Choose another one!")
        continue
    else:
        playing_grid[grid_coord[0]][grid_coord[1]] = "X"
    print_grid()
    if game_complete:
        break
   
  
# # Defining the other possible winning lines
# column_0 = [row[0] for row in playing_grid]
# column_1 = [row[1] for row in playing_grid]
# column_2 = [row[2] for row in playing_grid]
# diagonal_0 = [row[count] for count, row in enumerate(playing_grid)]
# diagonal_1 = [row[count + (count - 1) * -2] for count, row in enumerate(playing_grid)]

# # Check of all lines for the given win condition
# winning_lines = [playing_grid[0], playing_grid[1], playing_grid[2], column_0,
#                  column_1, column_2, diagonal_0, diagonal_1]
# win_check = [win_condition(line) for line in winning_lines]
#
# if abs(grid_input.count("X") - grid_input.count("O")) > 1:
#     print("Impossible")
# elif "X" in win_check and "O" in win_check:
#     print("Impossible")
# elif "X" in win_check:
#     print("X wins")
# elif "O" in win_check:
#     print("O wins")
# elif set(win_check) == {False}:
#     if game_complete == True:
#         print("Draw")
#     elif game_complete == False:
#         print("Game not finished")
def game_logic(var1, var2):

    player2 = 0

    if var1 == "A":
        if var2 =="X":
            player2 += (1 + 3)
        elif var2 == "Y":
            player2 += (2 + 6)
        elif var2 == "Z":
            player2 += (3 + 0)

    elif var1 == "B":
        if var2 =="X":
            player2 += (1 + 0)
        elif var2 == "Y":
            player2 += (2 + 3)
        elif var2 == "Z":
            player2 += (3 + 6)
            
    elif var1 == "C":
        if var2 =="X":
            player2 += (1 + 6)
        elif var2 == "Y":
            player2 += (2 + 0)
        elif var2 == "Z":
            player2 += (3 + 3)

    return player2


with open('C:/Users/Jakub/Documents/GitHub/Advent-of-Code-2021/Advent_2022/Day_02/Part_01/Official_input.txt', 'r') as f:
    file = f.readlines()

    player2_score = 0

    for lines in file:
        line = lines.strip()
        player2_score += game_logic(line[0], line[2])

    print(player2_score)


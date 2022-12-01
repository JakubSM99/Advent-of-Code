with open('C:/Users/Jakub/Documents/GitHub/Advent-of-Code-2021/Advent_2022/Day_01/Part_01/Official_input.txt', 'r') as f:

    my_list = []
    highest_sum = 0
    sum = 0 
    file = f.readlines()
    for x in file:
        x = x.strip()
        my_list.append(x)
    
    for x in my_list:
        try:
            x = int(x)
            sum += x
        except:
            if sum > highest_sum:
                highest_sum = sum
            
            sum = 0
    
    print(highest_sum)

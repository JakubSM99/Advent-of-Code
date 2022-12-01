with open('C:/Users/Jakub/Documents/GitHub/Advent-of-Code-2021/Advent_2022/Day_01/Part_02/Official_input.txt', 'r') as f:

    my_list = []
    Sums = []
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
            Sums.append(sum)
            
            sum = 0
    
    sorted_sums = sorted(Sums, reverse=True)

    highest_sum = int(sorted_sums[0]) + int(sorted_sums[1]) + int(sorted_sums[2])
    
    print(highest_sum)

with open('C:/Users/Jakub/Documents/GitHub/Advent-of-Code-2021/Advent_2022/Day_04/Part_01/Official_input.txt','r') as f:
    line = f.readlines()

    elements = []

    

    for element in line:
        var = element.strip()
        elements.append(var)
    
    count = 0

    for element in elements:       
        two_elfs = []
        ranges = element.split(",")
        for val in ranges:
            x = val.split("-")
            two_elfs.append(x)
        
        elf_one = two_elfs[0]
        elf_two = two_elfs[1]

        elf1_min = int(elf_one[0])
        elf1_max = int(elf_one[1])
        elf2_min = int(elf_two[0])
        elf2_max = int(elf_two[1])
        
        if (elf2_min <= elf1_max) and (elf2_min >= elf1_min):
            count += 1
        elif (elf1_min <= elf2_max) and (elf1_min >= elf2_min):
            count += 1

    print(count)
with open('C:/Users/Jakub/Documents/GitHub/Advent-of-Code-2021/Advent_2022/Day_04/Part_01/Test_input.txt','r') as f:
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
        
        print(elf_one, elf_two)
        if elf1_min >= elf2_min:
            if elf1_max <= elf2_max:
                count += 1
                print("Pierwszy w drugim")
        elif elf2_min >= elf1_min:
            if elf2_max <= elf1_max:
                count += 1
                print("Drugi w pierwszym")

    
    print(count)
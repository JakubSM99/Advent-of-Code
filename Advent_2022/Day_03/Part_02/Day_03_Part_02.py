dictionary = {
            "a": 1 ,
            "b": 2 ,
            "c": 3 ,
            "d": 4 ,
            "e": 5 ,
            "f": 6 ,
            "g": 7 ,
            "h": 8 ,
            "i": 9 ,
            "j": 10 ,
            "k": 11 ,
            "l": 12 ,
            "m": 13 ,
            "n": 14 ,
            "o": 15 ,
            "p": 16 ,
            "q": 17 ,
            "r": 18 ,
            "s": 19 ,
            "t": 20 ,
            "u": 21 ,
            "v": 22 ,
            "w": 23 ,
            "x": 24 ,
            "y": 25 ,
            "z": 26 ,
            "A": 27 ,
            "B": 28 ,
            "C": 29 ,
            "D": 30 ,
            "E": 31 ,
            "F": 32 ,
            "G": 33 ,
            "H": 34 ,
            "I": 35 ,
            "J": 36 ,
            "K": 37 ,
            "L": 38 ,
            "M": 39 ,
            "N": 40 ,
            "O": 41 ,
            "P": 42 ,
            "Q": 43 ,
            "R": 44 ,
            "S": 45 ,
            "T": 46 ,
            "U": 47 ,
            "V": 48 ,
            "W": 49 ,
            "X": 50 ,
            "Y": 51 ,
            "Z": 52
                }


def comparison(list1, list2, list3):

    appearing_items = []

    for x in list1:
            for y in list2:
                for z in list3:
                    if x == y and x == z:
                        appearing_items.append(x)
    
    appearing_item = list(set(appearing_items))

    return appearing_item[0]


with open('C:/Users/Jakub/Documents/GitHub/Advent-of-Code-2021/Advent_2022/Day_03/Part_01/Official_input.txt', 'r') as f:
    lines = f.readlines()

    my_list = []

    new_list = []

    for x in lines:
        my_list.append(x.strip())

    for x, y, z in zip(my_list[0::3], my_list[1::3], my_list[2::3]):
        first_element = [element for element in x]
        second_element = [element for element in y]
        third_element = [element for element in z]
        
        new_list.append(comparison(first_element, second_element, third_element))

    values_of_items = [dictionary[item] for item in new_list]

    sum = 0 
    for value in values_of_items:
        sum += value

    print(sum)
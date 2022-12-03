
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

def comparison(list1, list2):

    appearing_items = []

    for x in list1:
            for y in list2:
                if x == y:
                    appearing_items.append(x)
    
    appearing_item = list(set(appearing_items))

    return appearing_item[0]

with open('C:/Users/Jakub/Documents/GitHub/Advent-of-Code-2021/Advent_2022/Day_03/Part_01/Official_input.txt', 'r') as f:
    file = f.readlines()

    my_list = []

    appearing_item = []

    for x in file:
        my_list.append(x.strip())

    for element in my_list:
        new_list1 = []
        new_list2 = []

        a = int(len(element)/2)

        for x in element[0:a:1]:
            new_list1.append(x)
        
        for x in element[a::1]:
            new_list2.append(x)

        a = comparison(new_list1, new_list2)

        appearing_item.append(a)
        
values_of_items = [dictionary[item] for item in appearing_item]
    
print(appearing_item)
print(values_of_items)

sum = 0

for item in values_of_items:
    sum += item

print(sum)
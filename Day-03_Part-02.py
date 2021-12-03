#--- Part Two ---
#Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.
#
#Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part. Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:
#
#Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
#If you only have one number left, stop; this is the rating value for which you are searching.
#Otherwise, repeat the process, considering the next bit to the right.
#The bit criteria depends on which type of rating value you want to find:
#
#To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
#To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
#For example, to determine the oxygen generator rating value using the same example diagnostic report from above:
#
#Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
#Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
#In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
#In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
#In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
#As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
#Then, to determine the CO2 scrubber rating value from the same example above:
#
#Start again with all 12 numbers and consider only the first bit of each number. There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
#Then, consider the second bit of the 5 remaining numbers: there are fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second position: 01111 and 01010.
#In the third position, there are an equal number of 0 bits and 1 bits (one each). So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
#As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.
#Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.
#
#Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)
#
# Code:

#Takes input

a = input().split()

#Creates lists 'lista', 'listb', 'listc'

lista=[]
listb=[]
listc=[]

#defines function 'number'

def number(x):

    #checks which number occurs more often and returns it, when it is a draw returns 1

    if x.count('1')>x.count('0'):
        return '1'
    elif x.count('1')<x.count('0'):
        return '0'
    elif x.count('1')==x.count('0'):
        return '1'

#Defines function 'number_neg'

def number_neg(x):

    #checks which number occurs less often and returns it, wgen it is a draw returns 0

    if x.count('1')>x.count('0'):
        return '0'
    elif x.count('1')<x.count('0'):
        return '1'
    elif x.count('1')==x.count('0'):
        return '0'    
    
#Defines function 'most_loop'

def most_loop(a):

    #Creates lists 'lista', 'listb', 'listc'

    lista=[]
    listb=[]
    listc=[]

    #makes list from first row of numbers

    for x in a :
        c=[x]
        aa=x[:1]
        lista.append(aa)

    #returns value from 'number' function

    z=number(lista)

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(lista):
        if j == z:
            listb.append(a[i])

    #makes list from another row of numbers

    for x in listb:
        c=[x]
        aa=x[1:2]
        listc.append(aa)

    #returns value from 'number' function

    z=number(listc)

    #clears list

    lista.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(listc):
        if j == z:
            lista.append(listb[i])

    #clears list

    listb.clear()

    #makes list from another row of numbers
    
    for x in lista:
        c=[x]
        aa=x[2:3]
        listb.append(aa)

    #returns value from 'number' function

    z=number(listb)

    #clears list

    listc.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(listb):
        if j == z:
            listc.append(lista[i])

    #clears list

    lista.clear()

    #makes list from another row of numbers

    for x in listc:
        c=[x]
        aa=x[3:4]
        lista.append(aa)

    #returns value from 'number' function

    z=number(lista)

    #clears list

    listb.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(lista):
        if j == z:
            listb.append(listc[i])

    #clears list

    listc.clear()

    #makes list from another row of numbers

    for x in listb:
        c=[x]
        aa=x[4:5]
        listc.append(aa)

    #returns value from 'number' function

    z=number(listc)

    #clears list

    lista.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(listc):
        if j == z:
            lista.append(listb[i])

    #clears list

    listb.clear()

    #makes list from another row of numbers

    for x in lista:
        c=[x]
        aa=x[5:6]
        listb.append(aa)

    #returns value from 'number' function

    z=number(listb)

    #clears list

    listc.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(listb):
        if j == z:
            listc.append(lista[i])

    #clears list

    lista.clear()

    #makes list from another row of numbers

    for x in listc:
        c=[x]
        aa=x[6:7]
        lista.append(aa)

    #returns value from 'number' function

    z=number(lista)

    #clears list

    listb.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(lista):
        if j == z:
            listb.append(listc[i])

    #clears list

    listc.clear()

    #makes list from another row of numbers

    for x in listb:
        c=[x]
        aa=x[7:8]
        listc.append(aa)

    #returns value from 'number' function

    z=number(listc)

    #clears list

    lista.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(listc):
        if j == z:
            lista.append(listb[i])

    #clears list

    listb.clear()

    #makes list from another row of numbers

    for x in lista:
        c=[x]
        aa=x[8:9]
        listb.append(aa)

    #returns value from 'number' function

    z=number(listb)

    #clears list

    listc.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(listb):
        if j == z:
            listc.append(lista[i])

    #clears list

    lista.clear()

    #makes list from another row of numbers

    for x in listc:
        c=[x]
        aa=x[9:10]
        lista.append(aa)

    #returns value from 'number' function

    z=number(lista)

    #clears list

    listb.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(lista):
        if j == z:
            listb.append(listc[i])

    #clears list

    listc.clear()

    #makes list from another row of numbers

    for x in listb:
        c=[x]
        aa=x[10:11]
        listc.append(aa)

    #returns value from 'number' function

    z=number(listc)

    #clears list

    lista.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(listc):
        if j == z:
            lista.append(listb[i])

    #clears list

    listb.clear()

    #makes list from another row of numbers

    for x in lista:
        c=[x]
        aa=x[11:12]
        listb.append(aa)

    #returns value from 'number' function

    z=number(listb)

    #clears list

    listc.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(listb):
        if j == z:
            listc.append(lista[i])
    
    #converts list into binary, and then binary into integer

    a_string = "".join(listc)
    a_integer = int(a_string,2)

    #returns integer

    return a_integer

#Defines function 'least_loop'

def least_loop(a):

    #Creates lists 'lista', 'listb', 'listc'

    listb=[]
    listb=[]
    listc=[]

    #makes list from another row of numbers

    for x in a :
        c=[x]
        aa=x[:1]
        lista.append(aa)

    #returns value from 'number_nef' function

    z=number_neg(lista)

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(lista):
        if j == z:
            listb.append(a[i])

    #makes list from another row of numbers

    for x in listb:
        c=[x]
        aa=x[1:2]
        listc.append(aa)

    #returns value from 'number_nef' function

    z=number_neg(listc)

    #clears list

    lista.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(listc):
        if j == z:
            lista.append(listb[i])

    #clears list

    listb.clear()

    #makes list from another row of numbers

    for x in lista:
        c=[x]
        aa=x[2:3]
        listb.append(aa)

    #returns value from 'number_nef' function

    z=number_neg(listb)

    #clears list

    listc.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(listb):
        if j == z:
            listc.append(lista[i])

    #clears list

    lista.clear()

    #makes list from another row of numbers

    for x in listc:
        c=[x]
        aa=x[3:4]
        lista.append(aa)

    #returns value from 'number_nef' function

    z=number_neg(lista)

    #clears list

    listb.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(lista):
        if j == z:
            listb.append(listc[i])

    #clears list

    listc.clear()

    #makes list from another row of numbers

    for x in listb:
        c=[x]
        aa=x[4:5]
        listc.append(aa)

    #returns value from 'number_nef' function

    z=number_neg(listc)

    #clears list

    lista.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(listc):
        if j == z:
            lista.append(listb[i])

    #clears list

    listb.clear()

    #makes list from another row of numbers

    for x in lista:
        c=[x]
        aa=x[5:6]
        listb.append(aa)

    #returns value from 'number_nef' function

    z=number_neg(listb)

    #clears list

    listc.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(listb):
        if j == z:
            listc.append(lista[i])

    #clears list

    lista.clear()

    #makes list from another row of numbers

    for x in listc:
        c=[x]
        aa=x[6:7]
        lista.append(aa)

    #returns value from 'number_nef' function

    z=number_neg(lista)

    #clears list

    listb.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(lista):
        if j == z:
            listb.append(listc[i])

    #clears list

    listc.clear()

    #makes list from another row of numbers

    for x in listb:
        c=[x]
        aa=x[7:8]
        listc.append(aa)

    #returns value from 'number_nef' function

    z=number_neg(listc)

    #clears list

    lista.clear()

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(listc):
        if j == z:
            lista.append(listb[i])

    #clears list

    listb.clear()

    #makes list from another row of numbers

    for x in lista:
        c=[x]
        aa=x[8:9]
        listb.append(aa)

    #returns value from 'number_nef' function

    z=number_neg(listb)

    #clears list

    listc.clear

    #checks where the moust common item from list is, and adds items from previous list with that index to another list

    for i, j in enumerate(listb):
        if j == z:
            listc.append(lista[i])

    #converts list into binary, and then binary into integer

    a_string = "".join(listc)
    a_integer = int(a_string,2)
    
    #returns integer

    return a_integer

#Defines function 'multipla'

def multipla(x, y):
    
    #multiplys x and y

    print(x*y)

#Starts function multipla and uses function 'most_loop', and finction 'least_loop'

multipla(most_loop(a), least_loop(a))

#The End of Code
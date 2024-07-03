# def simvolsplit(word):
#     if len(word) == 1:
#         return word
#     else:
#         return word[0] + "!" + simvolsplit(word[1 :])
    
# print(simvolsplit("Dollar"))    

# def parenteses(word):
#     if len(word) < 3:
#         return word
#     else:
#         return word[0] + "(" + parenteses(word[1:-1]) + ")" + word[-1]
    
# print(parenteses("sdfghjk"))

# def power(n, pow):
#     if n == 1 or pow == 0:
#         return 1
#     elif pow == 1:
#         return n
#     else:
#         return n * power(n, pow - 1)
# print(power(5, 5)) 
#                     #    Ex---176   
# def printwords(word):
#     if len(word) == 0:
#         return word
#     mydict = {
#         "A": "Alpha",    "J" :"Juliet",      "S" :"Sierra",
#         "B": "Bravo",    "K" :"Kilo",        "T" :"Tango",
#         "C" :"Charlie",  "L" :"Lima",        "U" :"Uniform",
#         "D" :"Delta",    "M" :"Mike",        "V" :"Victor",
#         "E" :"Echo",     "N" :"November",    "W" :"Whiskey",
#         "F" :"Foxtrot",  "O" :"Oscar",       "X" :"Xray",
#         "G" :"Golf",     "P" :"Papa",        "Y" :"Yankee",
#         "H" :"Hotel",    "Q" :"Quebec",      "Z" :"Zulu",
#         "I" :"India",    "R" :"Romeo"
#     }
#     return mydict[word[0]] + " " + printwords(word[1:])

# print(printwords("HELLO"))


#                     #    Ex---178
# def palidrom(word):
#     if len(word) == 0:
#         return word
#     return word[-1] + palidrom(word[:-1])

#                     #    Ex---175
# def binary(num):
#     if num//2 == 0: 
#         return str(num)

#     return str(binary(num//2)) + str((num % 2)) 
# print(binary(17))




# def summ(lst):
#     return lst[0] + summ[lst[1:]]

# print(sum([4,5,4,3,65]))

# def summ(num*):
#     num = input("Enter the number: ")
#     if num == "":
#         return num
#     return int(num) + summ(int(num))
    
# print(summ())
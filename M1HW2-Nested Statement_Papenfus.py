# Exercise 3.7 page 112
# january 23, 2020
# CSC 121 M1HW2-Nested Statement
# Bettina Papenfus
print(" ")
print(" ")
for num in range(0, 1):
    print('A')
print(" ")
print("---------------------------------------------")
BASE_SIZE = 10
for r in range(BASE_SIZE):
    for c in range(r + 1):
        print('*', end='')
    print()
print(" ")
print(" ")
print("============================================")    
##################################################
# use the for and range statement                #
# Print break line to seperate                   #
# use a space statement to add a break           #                         
# Create a code that displays a triangle pattern #
##################################################
print(" ")
print(" ")
for num in range(0, 1):
    print('B')
print("-------------------------------------------")
print(" ")
character = '*'    
SIZE = 10
for r in range(SIZE):
    for col in range(SIZE, r, -1):
        print(character, end='')
    print()
print(" ")
print(" ")    
print("============================================")   
 
from curses.ascii import isdigit
import random

top_of_range=input("Type a number : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

if top_of_range <= 0:
    print('Please type a number a number larger than 0 next time.')
    quit()

else:
    print('Type a number next time.')
    quit()

random_number = random.randit(0,top_of_range)
print(random_number)
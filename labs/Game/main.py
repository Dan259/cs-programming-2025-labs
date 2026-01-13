from Stats import *
def create_char():
    global char
    char = Character()
    char.char_stats()
    char.show_stats()

create_char() 
while True:
    char.menu()
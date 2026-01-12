from Stats import *
def lvl_up():
    global char, exp, req_exp, lvl, stat_point
    while exp >= req_exp:
        req_exp += lvl
        lvl += 1
        exp = exp - req_exp
        stat_point += 1
        char.up_stats()

def create_char():
    global char
    char = Character()
    char.char_stats()
    char.show_stats(lvl,exp,req_exp)

req_exp = 5
exp = 0
lvl = 1
stat_point = 0

create_char() 
char.show_inventory()
char.use_items()
char.use_items()
char.show_stats(lvl,exp,req_exp)
# exp += 10
# lvl_up()
# char.show_stats(lvl,exp,req_exp)
symbolic_table_1 = {"NOT": ["¬", "~", "!"]}
sentence = None

def find(where, to_find, turn = 0):
    length = len(to_find)
    reached = 0

    for word in where:
        while word[turn] == to_find[turn]:
            turn += 1
            reached += 1
            if length == reached:
                return turn - reached
            find(where, to_find[turn], turn)

def replace_with_symbols(complete_input):
    i = 0
    for symbol in complete_input:
        if symbol in symbolic_table_1:

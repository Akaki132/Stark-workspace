symbolic_table_1 = {"Negation" : ["\u00ac", "~"], "Conjunction" : ["∧", "&", "•"],
                    "Disjunction" : ["∨"], "Condition" : ["\u2192", "\u2283", "\u2287"],
                    "Biconditional" : ["\u21D4", "\u2194"]}

def replace_with_symbols(complete_input):
    i = 0
    for symbol in complete_input:
        if symbol in symbolic_table_1:
            pass
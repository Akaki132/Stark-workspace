from sys import exit

quote_owner = ""

try:
    with open("quote_owners.txt", "r") as f:
        #each name shall have number assigned according to when they come in list
        #number assigned to it such way is expected
        quote_owner = input("whose quotes would you like to hear among " + name for name in f.readlines())
except FileNotFoundError:
    exit(1)

with open("quote_owners.txt", "r") as f:
    all_quotes = [name for name in f.readlines()]
    print(all_quotes[ int(quote_owner) - 1])
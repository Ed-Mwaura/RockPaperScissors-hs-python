# Write your code here
import random

name = input("Enter your name: ")
print('Hello,', name)
print("Enter your list of options: (Leave blank to use default rock, paper, scissors)")
opt = input()
opts = opt.split(",")

print("Okay, let's start")

f = open('rating.txt', 'r')

# name not in records
if name in f.read():
    pass
if name not in f.read():
    f2 = open('rating.txt', 'a')
    f2.write(name + ' ' + str(0) + '\n')
    f2.close()

# created a dictionary to store player name and score
recs_dict = {}

for line in f:
    records = line.replace('\n', '')
    recs = records.split()

    # The value is of type int for purpose of calculations later on
    recs_dict[recs[0]] = int(recs[1])

f.close()
# if name is in records, do nothing
if name in recs_dict:
    pass

# if name not in records, append the name with a zero score
else:
    f = open('rating.txt', 'a')
    f.write(name + ' ' + str(0) + '\n')
    f.close()

while True:
    user_choice = input().lower()
    default_options = ['rock', 'paper', 'scissors']

    if len(opts) < 3:
        options = default_options
    else:
        options = opts

    comp_guess = random.choice(options)

    selected = options.index(comp_guess)

    beaters = options[selected + 1:]

    beaten = options[:selected]

    if len(beaten) > len(beaters):
        while len(beaten) > len(beaters):
            # print()
            beaters.append(beaten.pop(0))
            # print(beaten)
            # print("gap")
            # print(beaters)
            if len(beaten) == len(beaters):
                break

    elif len(beaters) > len(beaten):
        while len(beaters) > len(beaten):
            beaten.append(beaters.pop())
            # print(beaters)
            # print("gap")
            # print(beaten)
            if len(beaten) == len(beaters):
                break

    if user_choice == "!exit":
        print("Bye!")
        break
    elif user_choice == '!rating':
        print("Your rating:", str(recs_dict[name]))
    elif user_choice not in options:
        print("Invalid input")
    elif user_choice == comp_guess:
        print("There is a draw (" + user_choice + ")")
        # update score since player drew
        recs_dict[name] += 50

    elif user_choice in beaters:
        print("Well done. Computer chose " + comp_guess + " and failed")
        # update score since player won
        recs_dict[name] += 100

    else:
        # no score to update, just print
        print("Sorry, but computer chose " + comp_guess)

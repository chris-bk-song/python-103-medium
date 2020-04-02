# Write a program that will prompt user for how many coins you want.
# initially i have no coins.
# Ask user if I want a coin and if user types "yes", give user one coin
# and print out the current tally.
# if user types "no", stop the program

count = 0
print('You have 0 coins.')
free_coin = input('Do you want a coin? (say either yes or no) ')
while free_coin == "yes":
    count = count + 1
    print(f'You have ' + str(count) + ' coins.')
    free_coin = input('Do you want another? (say either yes or no) ')
else:
    print('bye\n')

print('')

UserInput = input('Starting Number: ')

while UserInput.isdigit() == False:
    UserInput = input('Invalid. Enter a number: ')

UserInput = int(UserInput)
UserRange = UserInput + 33

NumbersList = []

for x in range(UserRange): 
    if x >= UserInput: 
        if x % 2 == 0:
            NumbersList.append(x) 

Index = 0

for row in range(4):
    print('\n')
    for column in range(4): 
        print(NumbersList[Index], end = ' ')
        Index = Index + 1

print('\n')

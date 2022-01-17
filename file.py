import random #importar libreria

print('Welcome to Python!') #variable declaration, string

print('This is a loop printing 5 times') # variable declaration Strings

for x in range(1, 6):    #loop start stop
    print(f'x is: {x}')

#variable declaration, list initialize 
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] 
day = random.choice(weekdays)
print(f'Today is: {day}')

if day == 'Monday':  # conditional- if-else
    print('It will be a long week!')
elif(day == 'Friday'):
    print('Woohoo, time for the weekend!')
else:
    print('Not quite there yet.')  #else
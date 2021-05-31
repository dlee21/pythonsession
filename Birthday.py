birthdays = {'JoeBiden':'July 4', 'David':'Nov 10'}

while True:

    name = input("enter a name (black to quit): " )

    if name == '':
        print('Exiting out of program')
        break;

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print(' I do not have birthday information for ' + name)
        bday = input('What is their birthday?')
        birthdays[name] = bday
        print('Birthday database updated')






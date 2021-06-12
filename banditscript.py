from pwn import *

nextpass = ''

for i in range(6):
    data = []
    myfile = open("bandit"+str(i)+".cfg", "r")
    while myfile:
        line  = myfile.readline()
        data.append(line)
        if line == "":
            break
    myfile.close()


    address = data[0].rstrip("\n").split(": ")[1]
    porta = int(data[1].rstrip("\n").split(": ")[1])
    username = data[2].rstrip("\n").split(": ")[1]
    passworda = ''
    commands = []
    if(i == 0):
        passworda = data[3].rstrip("\n").split(": ")[1]
        commands = data[4].rstrip("\n").split(",")

    else:
        passworda = nextpass[2:-1]
        commands = data[3].rstrip("\n").split(",")


    session = ssh(username, address, password=passworda, port= porta)
    command = ''

    if(len(commands)>1):
        command = '&&'
        command = command.join(commands)
        print(command)

    else:
        command = commands[0]


    nextpass = repr(session(command))
    print(nextpass)
    '''
    for commandind in range(len(commands)):
        if(commandind == len(commands)-1):
            nextpass = repr(session(commands[commandind]))
            print(nextpass)
        else:
            print(repr(session(commands[commandind])))

    '''
'''
session2 = ssh('bandit1', 'bandit.labs.overthewire.org', password=pass1[2:-1], port= 2220)
'''

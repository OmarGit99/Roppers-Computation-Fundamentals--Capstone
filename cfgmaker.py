
for x in range(1,6):
    cfgf = open("bandit"+str(x)+".cfg", "w")
    cfgf.write("Address: bandit.labs.overthewire.org\nPort: 2220\nUsername: bandit"+str(x)+"")
    cfgf.close()

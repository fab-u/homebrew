tempSet = 0
i = 1

def setTemp(temp):
    tempSet = temp

def update(tempActual):
    if(tempActual>tempSet):
        i=0
        #Heat off
    else:
        i=1
        #Heat on

def off():
    i=2
    #Heat off
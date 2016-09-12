#import sys
from random import randint
from random import sample
 

def checkio(data):
    isSecure = hasDigit = hasUpper = hasLower = isLenSecure = False
    if len(data) < 10:
        return False, len(data)
    for i in data:
        if i.isdigit() == True:
            hasDigit = True
        if i.isupper() == True:
            hasUpper = True
        if i.islower() == True:
            hasLower = True
        if (hasDigit and hasUpper and hasLower) == True:
            return True, 0
    return False, 0

#try:
#    sys.argv[1]
#except IndexError:
#password = ''.join(map(str,sample('0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM', randint(1,20))))
#else:
#    password = sys.argv[1]


ii=0
outPutTrue = 0
outPutFalse = 0
outPutLenght = 0
while ii < 1000000:
    password = ''.join(map(str,sample('0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM', randint(1,20))))
    a =  checkio(password)
    if a[0] == True:
        outPutTrue += 1
    elif a[0] == False:
        outPutFalse += 1
        if a[1] > 0:
            outPutLenght += 1
    ii+=1

print('True: ', outPutTrue, '\nFalse: ', outPutFalse, '\nLeng: ', outPutLenght)


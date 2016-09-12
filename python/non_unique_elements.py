#from sys import argv
from random import randint

def nonUniqElems(data):
    return [x for x in data if data.count(x) > 1]

def nonUniqElemsTuenut(data):

    elements = {}
    dataOut = []
    
    for i in data:
        if i in elements:
            elements[i] += 1
        else:
            elements.update({i:1})
    
    for i in range(len(data)):
        if elements[data[i]] > 1:
            dataOut = dataOut + [data[i]]

    return dataOut


for ii in range(10000):
    rawData = []
    for i in range(randint(6,11)):
        rawData = rawData + [randint(1,4)]
    nonUniqElems(rawData)


import json
import requests
from time import ctime

req = requests.get('https://www.wemineltc.com/api?api_key=c29e4832d0d047dbb65bc817e5316341200f51491de9ea8188e0eb49dd6b94a5', verify=False)

#req = requests.get('http://192.168.10.109/api.html')
reqDict = json.loads(req.content)

displayedNamesList = ('Username', 'Round shares', 'Total hashrate', 'Balance', 'Round estimate', 'Payout history')
i = 0
replacedReqDict = {}
for dictKey in reqDict.keys():
    if type(reqDict[dictKey]) == unicode:
        replacedReqDict[displayedNamesList[i]] = reqDict[dictKey]
        i += 1
    elif type(reqDict[dictKey]) == dict:
        replacedReqDict[dictKey] = reqDict[dictKey]

def formatText(key, value, offset=20):
    key = str(key)
    value = str(value)
    if key in ('Balance', 'Round estimate', 'Payout history'):
        value = value[0:6] + ' LTC'
    elif key == "Alive":
        value = str(bool(value))
    elif key == "Last share":
        value = ctime(float(value))
    if key == "Worker":
        outputString = '\n' + key + ':' + value.rjust(offset - len(str(key)) + len(str(value)))
    else:
        outputString = key + ':' + value.rjust(offset - len(str(key)) + len(str(value)))
    return outputString

for dictKey in sorted(replacedReqDict):
    if dictKey == 'workers':
        workersDict = replacedReqDict.get('workers')
        for workersDictKey in sorted(workersDict):
            workerStatDict = workersDict.get(workersDictKey)
            print formatText("Worker", workersDictKey, 24)

            displayedNamesWorkerStatList = ('Alive', 'Hashrate', 'Last share')
            i = 0
            replacedWorkerStatDict = {}
            for workerStatDictKey in sorted(workerStatDict.keys()):
                 replacedWorkerStatDict[displayedNamesWorkerStatList[i]] = workerStatDict[workerStatDictKey]
                 i += 1

            for replacedWorkerStatDictKey in sorted(replacedWorkerStatDict):
               print formatText(replacedWorkerStatDictKey, replacedWorkerStatDict.get(replacedWorkerStatDictKey),24)
    else:
        print formatText(dictKey, replacedReqDict.get(dictKey), 24)




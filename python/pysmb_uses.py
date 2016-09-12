from smb.SMBConnection import SMBConnection
from sys import argv

def myMakeConnection(client, host, login='', passwd=''):
    conn = SMBConnection('tuenut','skyes','FILSHARE', 'STPD8', use_ntlm_v2=True)
    return conn.connect('192.168.10.11')

def getFilesListFromShareDir(shareName, sharePath):
    filenames = conn.listPath(shareName,sharePath)
    return [(i.filename, i.isDirectory) for i in filenames]


#usage:
#   netshare --look [destination_host_name] -u [user_name] -p [password]

try:
    argv[1],argv[2],argv[3]
except IndexError:
    print('Use arguments!')
    exit()
else:
    destinationHostName = argv[1]
    userName = argv[2]
    userPasswd = argv[3]

for i in range(len(argv)):
    print(argv[i])

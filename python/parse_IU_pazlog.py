
logFile = open('C:\\Users\\a.groshev\\Documents\\pazlog\\401\\20160928\\9401_CCMProduction10 testlog.txt','r')

logLines = list(logFile)

for line in logLines:
    #находим, когда нажали кнопку
	if line.find('Taste bearbeitenSingle',) != -1:
		newPallet = 1                               #ставим единичку, как знак того, что задание запустилось
		newPalletDateTime = line.split('|')[0:2]    #дата+время нажатия на кнопку
		print ('Button Load Single at ', newPalletDateTime)

	elif line.find('Taste Start',) != -1\           #Находим, когда запустилось задание. Чисто формальная проверка
    and newPallet == 1\                             #Проверяем, что задание запущено. Хотя сейчас это не очень универсальная проверка
    and endCommonparameters != 1:                   #Когда все параметры считаны в первый раз, больше проверять не надо
		print ('Lets go on')
		newPalletArticle = 1                        #Устанавливаем временно артикул, наверно, можно отказаться

	elif line.find('AbdruckNr3',) == 0\             #Находим параметр артикула
    and newPalletArticle == 1\                      #если задание загрузилось, начинаем искать артикул
    and endCommonparameters != 1:
		newPalletArticle = line.split('=')[1]
		print ('Find article:', newPalletArticle)

	elif line.find('LosNr',) == 0\                  #Находим LosNr
    and newPalletArticle != -1\                     #проверяем, что артикул найден
    and endCommonparameters != 1:
		newPalletLosNr = line.split('=')[1]
		print ('LosNr:', newPalletLosNr)

	elif line.find('DLosNr',) == 0\                 #Находим номер партии (дата + смена)
    and newPalletArticle != -1\
    and endCommonparameters != 1: 
		newPalletDLosNr = line.split('=')[1]
		print ('Номер партии:', newPalletDLosNr)

	elif line.find('DPartieNr',) == 0\
    and newPalletArticle != -1\
    and endCommonparameters != 1: #смена
		newPalletDPartieNr = line.split('=')[1]
		print ('Смена:', newPalletDPartieNr)

	elif line.find('DPartieDatum',) == 0\
    and newPalletArticle != -1\
    and endCommonparameters != 1: #дата партии
		newPalletDPartieDatum = line.split('=')[1]
		print ('Дата партии:', newPalletDPartieDatum)

	elif line.find('Datum4',) == 0\
    and newPalletArticle != -1\
    and endCommonparameters != 1: #годен до
		newPalletDatum4 = line.split('=')[1]
		print ('Годен до:', newPalletDatum4)

	elif line.find('PartieDatum',) == 0\
    and newPalletArticle != -1\
    and endCommonparameters != 1: #дата задания
		newPalletPartieDatum = line.split('=')[1]
		print ('Дата задания:', newPalletPartieDatum)

	elif line.find('Stations_Nr',) == 0\
    and newPalletArticle != -1\
    and endCommonparameters != 1: #номер станции
		newPalletStations_Nr = line.split('=')[1]
		print ('Номер станции:', newPalletStations_Nr)

	elif line.find('ERPUser',) == 0\
    and newPalletArticle != -1\
    and endCommonparameters != 1: #номер станции
		newPalletERPUser = line.split('=')[1]
		print ('Пользователь:', newPalletERPUser)

	elif line.find('Instance',) == 0\
    and newPalletArticle != -1\
    and endCommonparameters != 1: #номер станции
		newPalletInstance = line.split('=')[1]
		print ('Instance', newPalletInstance)
		endCommonparameters = 1

	elif line.find('|Start:') != -1\
    and newPalletDLosNr != -1:
		start = 1

	elif start == 1\
    and newPalletDLosNr != -1:
		if line.find('DT>CCM') != -1\
        and line.find('Tag_NVE=2') != -1:
			l = line.find('Tag_NVE')+len('Tag_NVE=')
			boxSSCC = line[l:18+l]
			sampleNum = line[line.find('Tag_IstAnzahl'):line.find(' 6A')].split('=')[1]
			boxDateTime = line.split('|')[0:2]
			print ('Кусок №',sampleNum ,' в коробе', boxSSCC, 'at', boxDateTime)

		elif line.find('DT>CCM') != -1\
        and line.find('Tag_NVE=3') != -1:
			l = line.find('Tag_NVE')+len('Tag_NVE=')
			palleteSSCC = line[l:18+l]
			sampleNum = line[line.find('Tag_IstAnzahl'):line.find(' 6A')].split('=')[1]
			palleteDateTime = line.split('|')[0:2]
			print ('Короб №', sampleNum, 'в паллете' , palleteSSCC, 'at', palleteDateTime)
			start = -1
            
jsonVar =   { palleteSSCC:\
                        { "Время запуска задания":newPalletDateTime, "Время, когда появилась паллета":palleteDateTime,\
                        "Артикул":newPalletArticle, "LosNr":newPalletLosNr, "Номер партии":newPalletDLosNr, \
                        "Номер смены":newPalletDPartieNr, "Дата партии":newPalletDPartieDatum, "Годен до":newPalletDatum4,\
                        "Дата задания":newPalletPartieDatum, "Номер cтанции":newPalletStations_Nr, "ERP user":newPalletERPUser,\
                        "Инстанс":newPalletInstance, boxSSCC:\
                            { "Время создания ящика":boxDateTime }\
                        },\
            }

for key in jsonVar:
	print(key, ':')
	for key2 in sorted(jsonVar[key].keys()):
		try:
			for key3 in sorted(jsonVar[key][key2].keys()):
				print('    ',key2, ':\n        ', key3, '', jsonVar[key][key2][key3])
		except:
			print('    ', key2, ':',jsonVar[key][key2])

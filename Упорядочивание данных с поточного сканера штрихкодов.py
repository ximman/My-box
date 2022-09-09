import pandas as pd #библиотека для работы с таблицами
import re #регулярные выражения для сортировки штрихкодов (ШК)
import socket #библиотека для связи сканера ШК и ПК через сокет

host = '192.168.188.2' #IP-адрес сканера, указан в настройках устройства
port = 30002 #порт также берём из настроек

client_socket = socket.socket() #создаём сокет
client_socket.connect((host, port)) #создаём подключение по указанным выше адресу и порту

table = pd.DataFrame(columns = ['EAN 128', 'GS1', 'UPC']) #создаём таблицу со столбцами по названиям ШК
while True: #создаём бесконечный цикл считывания
    data = client_socket.recv(1024).decode() #получаем пакеты данных по 1024 байта
    print(data) #выводим в строку считанные данные
    table.loc[len(table)] = [re.findall(r'\b\d{29}\b', data), re.findall(r'\b\d{58}\b', data), re.findall(r'\b\d{13}\b', data)]
            #записываем каждый раз в новую строчку снизу отфильтрованные ШК (так как они считываются в случайном порядке)
    with pd.ExcelWriter('c:/Users/Zip/Downloads/For_1C.xlsx',mode='a') as writer:  #сохраняем таблицу в формате Excel для интеграции в 1С
        table.to_excel(writer, sheet_name='09.07.2022', header = True)
    print(table)

    
client_socket.close()

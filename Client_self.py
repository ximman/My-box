import pandas as pd
import re
import socket

host = '192.168.188.2'
port = 30002

client_socket = socket.socket()
client_socket.connect((host, port))

#table = pd.DataFrame(columns = ['EAN 128', 'GS1', 'UPC'])
while True:
    data = client_socket.recv(1024).decode()
    print(data)
    #table.loc[len(table)] = [re.findall(r'\b\d{29}\b', data), re.findall(r'\b\d{58}\b', data), re.findall(r'\b\d{13}\b', data)]
    #with pd.ExcelWriter('c:/Users/Zip/Downloads/For_1C.xlsx',mode='a') as writer:  
        #table.to_excel(writer, sheet_name='09.07.2022', header = True)
    #print(table)

    
client_socket.close()  # close the connection
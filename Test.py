from NeutrinosBase import *
levels = [[Commander(),Executer()],[Commander(),Executer()],[Commander(),Executer()],[Commander(),Executer()],[Commander(),Executer()],[Commander(),Executer()],[Commander(),Executer()]]
connector = Connector()
for i in range(len(levels)-1):
    levels[i].append(connector.connectNeutrinos(levels[i][0],levels[i][1]))
    levels[i].append(connector.connectNeutrinos(levels[i][1],levels[i+1][0]))
    
levels[-1].append(levels[-2][-1])
for i in levels:
    print(i)
from NeutrinosBase import *
connector = Connector()
levels= [[Commander(),Executer()],[Commander(),Executer()],[Commander(),Executer()],[Commander(),Executer()]]
for level in range(len(levels)-1):
    levels[level].append(connector.connectNeutrinos(levels[level][0],levels[level][1]))
    levels[level].append(connector.connectNeutrinos(levels[level][1],levels[level+1][0]))
for i in levels:
    print(i)
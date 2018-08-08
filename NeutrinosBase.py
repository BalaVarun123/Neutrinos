class Commander :
    commander_count = 0
    FUNC_TYPE = type(lambda : None)
    def __init__(self):
        self.connection = None
        commander_count = commander_count+1
    def send(self,function,data):
        if (type(function) != Commander.FUNC_TYPE) or (type(data) != tuple):
            return -1
        self.connection.loadf((function,data))
    def connect(self,connect):
        self.connection = connection
    def disconnect(self):
        self.connection = None

class Executer:
    executer_count = 0
    def __init__(self):
        self.connection = None
        executer_count = executer_count + 1
    def execute(self):
        function , data = self.connection.getf()
        for i in map(function,data):
            pass
        
    def connect(self,connection):
        self.connection = connection
    def disconnect(self):
        self.connection = None

class Connection:
    connection_count = 0
    def __init__(self,commander,executer,connector):
        self.COMMANDER = commander
        self.EXECUTER = executer
        self.CONNECTOR = connector
        self.func_data = []
        connection_count = connection_count + 1
    def loadf(self,func_data):
        self.func_data.append(func_data)
    def getf(self):
        return self.func_data.pop(0)
    def __del__(self):
        self.disconnect()

class Connector :
    connector_count = 0
    def __init__(self):
        self.connection = None
        self.connections = []
        connector_count = connector_count + 1
    def connectNeutrinos(self,commander,executer):
        connection = Connection(commander,executer)
        self.connections.append(connection)
        return connection
    def disconnectNeutrinos(self,connection):
        if connection not in self.connection:
            return -1
        self.connections.pop(self.connections.index(connection)
        connection.COMMANDER.disconnect()
        connection.EXECUTER.disconnect()


        
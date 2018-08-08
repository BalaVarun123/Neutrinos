class Commander :
    count = 0
    FUNC_TYPE = type(lambda : None)
    def __init__(self):
        self.connection = None
        Commander.count = Commander.count + 1
        self.oid = Commander.count
    def __repr__(self):
        return "<Commander %d>" % self.oid
    def send(self,function,data):
        if (type(function) != Commander.FUNC_TYPE) or (type(data) != tuple):
            return -1
        self.connection.loadf((function,data))
    def connect(self,connect):
        self.connection = connection
    def disconnect(self):
        self.connection = None
    
class Executer:
    count = 0
    def __init__(self):
        self.connection = None
        Executer.count = Executer.count+1
        self.oid = Executer.count
    def __repr__(self):
        return "<Executer %d>" % self.oid
    def execute(self):
        function , data = self.connection.getf()
        if data == () : function()
        for i in map(function,data):
            pass
        
    def connect(self,connection):
        self.connection = connection
    def disconnect(self):
        self.connection = None

class Connection:
    count = 0
    def __init__(self,commander,executer,connector):
        self.COMMANDER = commander
        self.EXECUTER = executer
        self.CONNECTOR = connector
        commander.connection = self
        executer.connection = self
        self.func_data = []
        Connection.count = Connection.count + 1
        self.oid = Connection.count
    def __repr__(self):
        return "<Connection %d" %self.oid+":"+repr(self.COMMANDER)+","+repr(self.EXECUTER)+","+repr(self.CONNECTOR)+">"
    def loadf(self,func_data):
        self.func_data.append(func_data)
    def getf(self):
        return self.func_data.pop(0)
    def __del__(self):
        self.CONNECTOR.disconnectNeutrinos(self)

class Connector :
    count = 0
    def __init__(self):
        self.connection = None
        self.connections = []
        Connector.count = Connector.count + 1
        self.oid = Connector.count
    def __repr__(self):
        return "<Connector %d>" %self.oid
    def connectNeutrinos(self,commander,executer):
        connection = Connection(commander,executer,self)
        self.connections.append(connection)
        return connection
    def disconnectNeutrinos(self,connection):
        if connection not in self.connections:
            return -1
        self.connections.pop(self.connections.index(connection))
        connection.COMMANDER.disconnect()
        connection.EXECUTER.disconnect()

        
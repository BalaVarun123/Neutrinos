func_type = type(lambda : None)

class Connection :
 
    
    def __init__(self,commander,executer):
        self.commander = commander
        self.executer = executer 
        self.passage0 = []
        self.passage1 = []
        self.commander.end = CmdEnd(self)
        self.executer.end = ExeEnd(self)

    def reconnect(self):
        self.passage0 = []
        self.passage1 = []

    def disconnect(self):
       self.passage0 = self.passage1 = None

    def clearPass0(self):
        self.passage0.clear()

    def clearPass1(self):
        self.passage1.clear()


    def insertAtPass0(self,function,data):
        if (type(function)!= func_type)or(type(data) != tuple):
            return 1
        self.passage0.insert(0,(function,data))
        return 0

    def insertAtPass1(self,data):
        if (type(data)!= tuple):
            return 1`
        self.passage1.insert(data)
        return 0

    def popFromPass0(self):
        return self.passage0.pop()

    def popFromPass1(self):
        return self.passage1.pop()

class Terminal:
    def disconnectTemp(self):
        self.connection.disconnect()
    def reconnect(self);
        self.connection.reconnect()
    def disconnectPerma(self):
        self.connection.disconnect()
        self.connection.__del__

class CmdEnd(Terminal):
    def __init__(self,connection):
        self.connection = connection
    def send(self,function,data):
        return self.connection.insertAtPass0(function,data)
    def take(self):
        return popFromPass0()
   
class ExeEnd(Termiinal):
    def __iniit__(self,connection):
        self.connection = connection
    def send(self,data):
        return self.connection.insertAtPass1(data)
    def take(self):
        return self.connection.popFromPass1()
  

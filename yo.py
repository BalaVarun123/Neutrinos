def Neutrino:
    
    DEFAULT_COMMANDS = {
    "SAVE_FUNC" = 1,
    "CALL_FUNC" = 2,
    "DEL_FUNC" = -1,
    "SAVE_CMD" = 3,
    "EXE_CMD" = 4,
    "DEL_CMD" = -3,
    "SAVE_CMD_SET" = 5,
    "EXE_CMD_SET" = 6,
    "DEL_CMD_SET" =-5,}
    
    def __setitem__(self , index ,value):
        neutrino_class = type(self)
        if index = 0:
            if (value[0] in neutrino_class
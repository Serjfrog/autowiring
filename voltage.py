from propertycontainer import Property, PropertyContainer

class Voltage(PropertyContainer):
    def __init__(self,name: str, value = 0, currenttype = None):
        super().__init__(name)
        self.add(Property("Value",value))
        self.add(Property("CurrentType",currenttype))

class Ground(Voltage):
    def __init__(self):
        super().__init__("GND",0,)

# Example usage
if __name__ == "__main__":
    line = Voltage("L",110,"AC")
    neutral = Voltage("N",0,"AC")
    vdc = Voltage("VDC",24,"DC")
    vdc0 = Voltage("0VDC",0,"DC")
    gnd = Voltage("GND",0,"AC/DC")

    print(line)
    print(neutral)

    terminalL = PropertyContainer("TerminalL")
    terminalN = PropertyContainer("TerminalN")
    terminalG = PropertyContainer("TerminalG")
    terminalL.add(line)
    terminalN.add(neutral)
    terminalG.add(gnd)

    terminalVDC = PropertyContainer("Terminal+")
    terminal0VDC = PropertyContainer("Terminal-") 
    terminalVDC.add(vdc)
    terminal0VDC.add(vdc0)
    
    socket = PropertyContainer("Socket")
    socket.add(terminalL)
    socket.add(terminalN)
    socket.add(terminalG)

    terminalblock = PropertyContainer("TB1")
    terminalblock.add(terminalVDC)
    terminalblock.add(terminal0VDC)

    print(socket)
    print(terminalblock)
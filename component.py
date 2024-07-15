from terminal import Property, PropertyContainer, Voltage, Terminal, Ground

class Component(PropertyContainer):
    def __init__(self, name: str, label: str):
        super().__init__(name)
        self.add(Property("label",label))
        self.add(PropertyContainer("Terminals"))
        self["Terminals"].add(Property("label","Power Input"))

if __name__ == "__main__":
    compi = Component("Component1", "compi1")
    compi["Terminals"].add(Terminal("+",Voltage("24V",24,"DC")))
    compi["Terminals"].add(Terminal("-",Voltage("0V",24,"DC")))
    compi["Terminals"].add(Terminal("GND",Ground()))
    
    print(compi)


from terminal import Property, PropertyContainer, Voltage, Terminal, Ground

class Component(PropertyContainer):
    def __init__(self, name: str, label: str):
        super().__init__(name)
        self.add(Property("label",label))
        self.add(PropertyContainer("id"))
        self["id"].add(Property("PartNumber"))
        self["id"].add(Property("Model"))
        self["id"].add(Property("Brand"))
        self.add(PropertyContainer("Terminals"))

if __name__ == "__main__":
    compi = Component("Component1", "compi1")
    compi["Terminals"].add(Terminal("+",Voltage("DC",24,"DC"),"out"))
    compi["Terminals"].add(Terminal("-",Voltage("0V",24,"DC"),"out"))
    compi["Terminals"].add(Terminal("GND",Ground(),"in"))
    compi["Terminals"].add(Terminal("DC",io_dir = "in"))
    compi["Terminals"].add(Terminal("0V",io_dir = "in"))
    
    print(compi["Terminals"])


    #Test Ruleset Active

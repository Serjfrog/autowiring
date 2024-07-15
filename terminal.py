from voltage import Property, PropertyContainer, Voltage, Ground

class Terminal(PropertyContainer):
    def __init__(self, name: str, volts = Voltage("voltage"), io_dir = "out"):
        super().__init__(name)
        self.add(volts)
        self.add(Property("direction",io_dir))


if __name__ == "__main__":
    line_terminal = Terminal("L",Voltage("Line", 110, "AC"))
    neutral_terminal = Terminal("N",Voltage("Line", 110, "AC"))
    ground_terminal = Terminal("G",Ground())
    print(line_terminal)    
    print(neutral_terminal)
    print(ground_terminal)
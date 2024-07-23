from voltage import Property, PropertyContainer, Voltage, Ground

class Terminal(PropertyContainer):
    def __init__(self, name: str, volts = Voltage("VoltageRating"), io_dir = "out", label = ""):
        super().__init__(name)
        self.add(volts)
        self.add(Property("direction",io_dir))
        self.add(Property("label",label))

# TODO: Define classes for common groups of terminals, connectors
#       Dynamic Terminal sizes


class TerminalBlock(PropertyContainer):
    pass

class Connector(PropertyContainer):
    pass

if __name__ == "__main__":
    line_terminal = Terminal("1")
    empty_terminal = Terminal("2")
    print(line_terminal)
    print(empty_terminal)
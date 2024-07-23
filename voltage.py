from propertycontainer import Property, PropertyContainer

class Voltage(PropertyContainer):
    def __init__(self, pname: str, value = 0, type = "AC/DC"):
        super().__init__(pname)
        self.add(Property("Voltage",value))
        self.add(Property("unit","V"))
        self.add(Property("type", type))

class Ground(Voltage):
    def __init__(self):
        super().__init__("Ground",0)

# TODO: Add classes for common voltage ratings like TTL(5v), PLC(24v), etc...

# Example usage
if __name__ == "__main__":
    line = Voltage("Line",110,"AC")
    neutral = Voltage("Neutral",0, "AC")
    vdc = Voltage("VDC",24, "DC")
    vdc0 = Voltage("0VDC",0, "DC")
    gnd = Ground()

    print(line)
    print(neutral)
    print(vdc)
    print(vdc0)
    print(gnd)
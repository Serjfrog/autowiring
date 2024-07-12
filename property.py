class Property:
    def __init__(self, name: str, value = None):
        self.name = name
        self.level = 0
        self.setvalue(value)

    def setvalue(self,value):
        self.value = value             
    
    def setlevel(self,level = 0):
        self.level = level

    def __str__(self):
        return "\t" * self.level + f"{self.name}: " + str(self.value)
    
    def display(self,level=0):
        return "\t" * self.level + f"{self.name}: " + str(self.value)
    
# Example usage
if __name__ == "__main__":
    desc = Property("Description")
    desc.value = "This is a property"
    volt = Property("Voltage", 110)
    print(desc)
    print(volt)
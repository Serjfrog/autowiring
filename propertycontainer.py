from property import Property

class PropertyContainer(Property):
    def __init__(self,name: str):
        self.name = name
        self.value = {}
        self.setlevel()

    # def setvalue(self,value):
    #     pass

    def setlevel(self, level = 0):
        self.level = level
        for prop in self.value.values():
            prop.setlevel(self.level + 1)

    def add(self,prop: Property):
        prop.setlevel(self.level + 1)
        self.value[prop.name] = prop
        return self.value[prop.name]
    
    def remove(self,key: str):
        del self.value[key]

    def __getitem__(self,key: str):
        return self.value[key]
        
    def __setitem__(self,key,value):
        if key in self.value.keys():
            self.value[key] = value
            return True
        return False 
    
    def __str__(self):
        ret = "\t" * self.level + f"{self.name}: " + "{\n"
        for prop in self.value.values():
            ret += str(prop) + "\n"
        ret += "\t" * (self.level) + "}"
        return ret
    

# Example usage
if __name__ == "__main__":
    desc = Property("Description")
    desc.value = "This is a property"
    volt = Property("Voltage", 110)
    print(desc)
    print(volt)
    terminal = PropertyContainer("Terminal")
    terminal.add(desc)
    terminal.add(volt)
    print(terminal)
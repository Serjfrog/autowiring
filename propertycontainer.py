from property import Property

class PropertyContainer(Property):
    def __init__(self,name: str,level = 0):
        self.__name = name
        self.value = {}
        self.__level = level

    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, level: int):
        self.__level = level
        for prop in self.value.values():
            prop.level = self.level + 1

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name

    def add(self,prop: Property):
        prop.level = self.level + 1
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
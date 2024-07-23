class Property:
    def __init__(self, name: str, value = None, level = 0):
        self.__name = name
        self.__level = level
        self.__value = value

    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name

    def __str__(self):
        return "\t" * self.level + f"{self.name}: " + str(self.value)
    
# Example usage
if __name__ == "__main__":
    desc = Property("Description")
    desc.value = "This is a property"
    volt = Property("Voltage", 110)
    print(desc)
    print(volt)
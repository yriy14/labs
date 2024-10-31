import textwrap

class laptop:
    def __init__(self,  developer = "", frequency = 0.0, ram = 0):

        self.__developer = developer
        self.__frequency = frequency
        self.__ram = ram
        
        
        self.date_of_manufacture = 2021
        self.display_type = "OLED"

    def get_developer(self):
        return self.__developer

    def get_frequency(self):
        return self.__frequency
    
    def get_ram(self):
        return self.__ram
    
    def __str__(self):
        return f"laptop {self.__developer}, {self.__frequency}, {self.__ram},"
    
    def __repr__(self):
        return textwrap.dedent(f''' developer:  {self.__developer}: " 
    frequency = {self.__frequency}GHz "
    ram = {self.__ram}GB "
    date_of_manufacture: {self.date_of_manufacture} "
     display_type {self.display_type} 
    ''')
    
    def __del__(self):
        print(f"{self.__str__()} is wiped off")

def main():
        
    obj1 = laptop("mac", 3.6, 16)
    obj2 = laptop("dell", 2.5, 16)
    obj3 = laptop("asus", 5.2, 32)
        
    print(repr(obj1))
    print(repr(obj2))
    print(repr(obj3))

if __name__ == '__main__':
    main()


import textwrap

class Laptop:
    max_hours = 4000
    def __init__(self, manufacturer = "China", frequency = 0.0, ram = 0, work_hour=0):

        self.__manufacturer = manufacturer
        self.__frequency = frequency
        self.__ram = ram
        
        self.date_of_manufacture = 2021
        self.display_type = "OLED"

        self.__work_hour = work_hour

    def get_manufacturer(self):
        return self.__manufacturer

    def get_frequency(self):
        return self.__frequency
    
    def get_ram(self):
        return self.__ram
    
    def get_work_hour(self):
        return self.__work_hour
    
    def set_work_hour(self, hours):
        if hours >=0:
            self.__work_hour = hours
        
    def __str__(self):
        return f"laptop from {self.__manufacturer}, {self.__frequency}Ghz, {self.__ram}GB, {self.__work_hour}h"
    
    def __repr__(self):
        return textwrap.dedent(f''' manufacturer: {self.__manufacturer} 
    frequency = {self.__frequency}GHz 
    ram = {self.__ram}GB 
    date_of_manufacture: {self.date_of_manufacture} 
    display_type {self.display_type} 
    time_of_work {self.__work_hour}h
    ''')
    
    def __del__(self):
        print(f"{self.__str__()} is wiped out")


def main():
        
    obj1 = Laptop("mac", 3.6, 16, 200)
    obj2 = Laptop("dell", 2.5, 16, 3100)
    obj3 = Laptop("asus", 5.2, 32, 5350)
    
    obj1.set_work_hour(300)
    obj2.set_work_hour(6000)
    obj3.set_work_hour(5050)

    print(repr(obj1))
    print(repr(obj2))
    print(repr(obj3))
    
    laptops = [obj1, obj2, obj3]
    
    #max_work_hour_laptop = max(laptops, key=lambda x: x.get_work_hour())
    #print("laptop with the most hours")
    #print(max_work_hour_laptop, "\n")

    for laptop in laptops:
        if laptop.get_work_hour() > Laptop.max_hours:
            print(f"{laptop.get_manufacturer()} laptop needs to be thrown away","\n")

    mv = laptops[0]
    for elem in laptops:
        if mv.get_work_hour() < elem.get_work_hour():
            mv = elem

    print("laptop with the most hours")
    print(mv,"\n")


if __name__ == '__main__':
    main()

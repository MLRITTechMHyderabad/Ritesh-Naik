from abc import ABC,abstractmethod

class Chai(ABC):
    def __init__(self,name,base_price,quantity):
        self.name=name
        self.base_price=base_price
        self.quantity=quantity
        
    def calculate_price(self):
        pass
    
    def display_info(self):
        pass

class MasalaChai(Chai):
    def calculate_price(self):
        return self.base_price+10

    def display_info(self):
        print(f"name={self.name} price={self.calculate_price()} quantity={self.quantity}")

class GingerChai(Chai):
    def calculate_price(self):
        return self.base_price+8

    def display_info(self):
        print(f"name={self.name} price={self.calculate_price()} quantity={self.quantity}")

class ElaichiChai(Chai):
    def calculate_price(self):
        return self.base_price+12

    def display_info(self):
        print(f"name={self.name} price={self.calculate_price()} quantity={self.quantity}")

class ChaiInventory:

    def __init__(self):
        self.chai_list=[]
    
    def add_chai(self,chai_obj):
        self.chai_list.append(chai_obj)

    def show_inventory(self):
        for i in self.chai_list:
            i.display_info()


    def get_total_inventory_value(self):
        total=0
        for i in self.chai_list:
            total+=i.calculate_price()*i.quantity
        return total

inventory = ChaiInventory()

chai1 = MasalaChai("Masala Chai", 20, 50)
chai2 = GingerChai("Ginger Chai", 18, 40)
chai3 = ElaichiChai("Elaichi Chai", 25, 30)

inventory.add_chai(chai1)
inventory.add_chai(chai2)
inventory.add_chai(chai3)

inventory.show_inventory()

print("Total Inventory Value: ₹", inventory.get_total_inventory_value())

            

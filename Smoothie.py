## Week 3 Inheritance
## Babatunde Salisu


class Smoothie:
    def __init__(self):
        
        self.fruit = []
        self.veggies = []
        self.dairy = ""
        self.more  = "y"
        
    def addFruit(self):
        while (self.more != "n"):
            self.fruitInput = input(f"Please enter fruits to add. ")
            self.more = input(f"Enter 'n' to finish adding fruits or Press enter to continue adding...")
            self.fruit.append(self.fruitInput)
    
    def addDairy(self,milkType):
        
        self.dairy =  DairyKindAdd(milkType)
        
            
    def __str__(self):
        return f"These are the recipes for smoothie preparation {self.fruit} {self.veggies} {self.dairy}"
    
class DairyKindAdd:
    def __init__(self,milkType):
        self.milkType = milkType
    def __str__(self):
        return (self.milkType)
        
            
        
    
        
def main():    
    a =  Smoothie()   
    a.addFruit()
    a.addDairy("almondMilk")
    print(a)

main()
        
        
    
        

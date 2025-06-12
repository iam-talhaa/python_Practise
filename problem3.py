class Animal:
    def __init__(self,animal):
        self.animal1=animal
        print(f"Animal {Animal}")


class pets(Animal):
    def __init__(self):
        super().__init__()
    

class Dog(pets):
    def __init__(self,mystr):
        self.mystr=mystr
        super().__init__()
        
    def Bark(self):
        print(f"The Dog is :{self.mystr}")
       

class hh(pets):
    def __init__(self,mystr):
        self.mystr=mystr
        super().__init__()
        
    def no(self):
        print(f"The Dog is :{self.mystr}")
                
        
        

obj =Dog('BARKING :')
class hh(pets):
    def __init__(self,mystr):
        self.mystr=mystr
        super().__init__()
        
    def no(self):
        print(f"The Dog is :{self.mystr}")
                
        
obj.Bark()
            
class TwoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
        
    def TwoShow(self):
        print(f"This is i{self.i} + j{self.j}")

class ThreeDVector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)       
        self.k=k
    
    def show3(self):
        print(f"i{self.i} + j{self.j} + k{self.k}")
        
    
    
a=TwoDvector(2,5)
b=ThreeDVector(3,4,6)

a.TwoShow()
b.show3()
    
        
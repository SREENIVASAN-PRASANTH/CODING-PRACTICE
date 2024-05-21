#created a single tower
class tower:
    def __init__(self,size:int,values:list):
        self.size = size
        self.values = values
        for i in range(size):
            if self.values[i] is int:
                self.top_index = i
                break
        else:
            self.top_index = self.size
            
    def is_full(self):
        if self.top_index == 0:
            return True
        else:
            return False
        
    def is_empty(self):
        if self.top_index == self.size:
            return True
        else:
            return False
    
#cerated a game environment
class towers:
    def __init__(self,size:int):
        self.size = size
        self.A = tower(size,[i for i in range(1,size + 1)])
        self.B = tower(size,["-" for j in range(size)])
        self.C = tower(size,["-" for j in range(size)])
        
    def mov_disc(self,from_tower:str,to_tower:str):
        towers_list = {"A":self.A,"B":self.B,"C":self.C}
        from_tower = towers_list[from_tower.upper()]
        to_tower = towers_list[to_tower.upper()]
        
        if from_tower.is_empty():
            print(from_tower.top_index)
            print(from_tower.values)
            print("From tower is empty")
            return
        
        if to_tower.is_full():
            print("To tower is full")
            return
            
        to_tower.top_index -= 1
        to_tower.values[to_tower.top_index] = from_tower.values[from_tower.top_index]
        from_tower.values[from_tower.top_index] = "-"
        from_tower.top_index += 1
        
    
    def display(self):
        for i in range(self.size):
            print(self.A.values[i],self.B.values[i],self.C.values[i])
            
    
if __name__ == "__main__":
    t = towers(3)
    t.mov_disc("A","B")
        
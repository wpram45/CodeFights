
class Prizes(object):
    def __init__(self,purchases,n,d):
        self.n=n
        self.d=d
        self.cur_index=0
        self.purchases=purchases
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.cur_index < len(self.purchases):
            
            
            if self.purchases[self.cur_index]%self.d==0 and  (self.cur_index+1)%self.n==0:
                self.cur_index+=1
                
                
                return self.cur_index
                
                
            else:
                
                self.cur_index+=1
                
        
        raise StopIteration
def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))

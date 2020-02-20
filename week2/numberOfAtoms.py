class Solution:
    def parse(self, formula):
        ms = collections.Counter()
        while self.i < len(formula):
            
            #if uppercase
            if formula[self.i].isupper():
                cur= formula[self.i]
                while self.i+1<len(formula) and formula[self.i+1].islower():
                    cur+=formula[self.i+1]
                    self.i+=1
                if (self.i+1<len(formula) and not formula[self.i+1].isdigit()) or self.i+1 == len(formula):
                    ms.update({cur: 1})
            
            #if number
            elif formula[self.i].isdigit():
                num = formula[self.i]
                while self.i+1<len(formula) and formula[self.i+1].isdigit():
                    num+=formula[self.i+1]
                    self.i+=1

                ms.update({cur: int(num)})
            
            #if '('
            elif formula[self.i]=='(':
                self.i+=1
                ms += self.parse(formula)
            
            elif formula[self.i]==')':
                num =""
                while self.i+1<len(formula) and formula[self.i+1].isdigit():
                    num+=formula[self.i+1]
                    self.i+=1
                for j in ms:
                    ms[j] *= int(num)
                    
                return ms
            self.i+=1
        return ms
    
    def countOfAtoms(self, formula: str) -> str:
        res = ""
        self.i = 0
            
        ms = self.parse(formula)
            
            
        for i in sorted(ms):
            res+= i
            if ms[i] >1:
                res+= str(ms[i])
        
        
        return res
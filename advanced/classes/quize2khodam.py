from random import choices
from copy import copy
from string import ascii_letters, punctuation

print(punctuation)
class Password:
    
    inputuniverse={'numbers':list(range(10)),'letters':list(ascii_letters),'punctuation':list(punctuation)}
    default_lengths={'low':8,'mid':12,'high':16}
    
    def __init__(self,strength='mid',length=None):
        self.strength=strength
        self.length=length
         
    # @classmethod
    # def showinputuniverse(cls):
    #     return cls.inputuniverse
    
    def generatepassword(self):
        # in baes mishe list har dafe mogheye estefade copy beshe(be track  20 morajee shavad)
        population= copy(self.inputuniverse['letters'])
        # be nahveye estefade az variable init tavajjoh shavad. az get estefade shode:
        length=self.length or self.default_lengths.get(self.strength)
       

        if self.strength=='high':
            population += self.inputuniverse['numbers'] + self.inputuniverse['punctuation']
        else:
            population +=self.inputuniverse["numbers"]
    
        return "".join(list(map(str,choices(population,k=length))))

pweak=Password(strength='low',length=40)
print('low',pweak.generatepassword())

pmid=Password(strength='mid',length=40)
print(pmid.generatepassword())

phigh=Password(strength='high' )
print(phigh.generatepassword())

pdefault=Password()
print(pdefault.generatepassword())


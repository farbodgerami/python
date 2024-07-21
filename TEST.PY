class Animal:
    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']

    def type(self, t = None):
        if t: self._type = t
        try: return self._type
        except AttributeError: return None

    def name(self, n = None):
        if n: self._name = n
        try: return self._name
        except AttributeError: return None

    def sound(self, s = None):
        if s: self._sound = s
        try: return self._sound
        except AttributeError: return None

class Duck(Animal):
    def __init__(self, **kwargs):
        self._type = 'duck'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)

class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)
    def kill(self,s):
        print(f'{self.name()} kills {s}')

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print(f'The {o.type()} is named "{o.name()}" and says "{o.sound()}".')


a0 = Kitten(name = 'fluffy', sound = 'rwar')
a1 = Duck(name = 'donald', sound = 'quack')
print_animal(a0)#The kitten is named "fluffy" and says "rwar".
print_animal(a1)#The duck is named "donald" and says "quack".
a0.kill('soosk')#fluffy kills soosk


# Python3 code to demonstrate
# convert dictionary string to dictionary
# using json.loads()
import json  
words=[{"word":"word1","meaning":"meaningyechi","level":"1"},{"word":"word2","meaning":"meaningyechi","level":"1"},{"word":"word3","meaning":"meaningyechi","level":"1"}]
test_string = '{"word1": 17,"word2":2,"word3":17}' 
  
res = json.loads(test_string)
  
print(res)
for i in words:
    if i['word'] in res:
        i['level']=int(res[i['word']])
    print(i['level']) 

print(words)

l=["a","c","a","b","r","r"]

 

class Tekraryab:
    def __init__(self,list):
        self.list=list
#gets the list and shows the repeated elements
    
    def tek(self):
        du=[]
        for i in l:
          if l.count(i)>1:
             if i not in du:
                du.append(i)
        return du
#gets the list and shows repeatation of any member
    def teks(self):
        du=[]
        c=[]
        for i in l:
            k=l.count(i)
            if i not in c:
             c.append(i)
             du.append(f"{i}={k}")
        return du
l=["a","c","a","b","r","r"]
ab=Tekraryab(l)
print(ab.tek())
print(ab.teks())

 
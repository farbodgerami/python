class dock:
    band='metallica'
    instrument='gitar'
    def abc(self):
        print('abc')
        print(self.instrument)
    def df(self):
        print('def')
jack=dock()
jack.abc()#abc gitar
jack.df()#def
print(jack.band)#metallica
 
class ossd:
    def __init__(self,side,area):
        self.side=side
        self.area=area
    def sq(self):
        return self.side*self.area
    def reportreturn(self):
        return "side is: %s" %self.side
    def report(self):
        print("side is:%s"%self.side)
        print("area is:%s"%self.area)
        print("square is:%s"%self.sq( ))         
j=ossd(34,4)
print(j.side)#34
print(j.area)#4
print(j.sq())#136
print(j.reportreturn())#side is: 34
j.report()#side is:34 area is:4 square is:136

class sq:
    def __init__(self,sidelength,areaa):
        self.sidelenght=sidelength
        self.areaa=areaa
    def area(self):
        return self.sidelenght*self.sidelenght
    def permeter(self):
        return self.sidelenght*4

a=sq(10,22)
print(a.areaa)#22
print(a.sidelenght)#10
print(a.area())#100
print(a.permeter())#40

 
class Animal:
    def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))

a0 = Animal('kitten', 'fluffy', 'rwar')
a1 = Animal('duck', 'donald', 'quack')
print_animal(a0)#The kitten is named "fluffy" and says "rwar".
print_animal(a1)#The duck is named "donald" and says "quack".
print_animal(Animal('velociraptor', 'veronica', 'hello'))#The velociraptor is named "veronica" and says "hello".

class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


 
a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')

print_animal(a0)#The kitten is named "fluffy" and says "rwar".
print_animal(a1)#The duck is named "donald" and says "quack".
# vase pain bayad mesle ghablia ye * bashe yani faghat arg vagar na keyword aruge mikhad
# print_animal(Animal('velociraptor', 'veronica', 'hello')) 


class Animal:
    x=[1,2,3]
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    def type(self, t = None):
        if t: self._type = t
        return self._type

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

 
a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
a2=Animal()
# ino ezafe kardam:
a0.sound('bark')
print(a0)#The kitten is named "fluffy" and says "bark".
print(a1)#The duck is named "donald" and says "quack".
print(a2)#The kitten is named "fluffy" and says "meow".
print(a0.x)#[1, 2, 3]
print(a1.x)#[1, 2, 3]
a0.x[0]=10
print(a0.x)#[10, 2, 3]
a1.x[1]=20
print(a1.x)#[10, 20, 3]
# vase set:
a0.type('abc')
print(a0)#The abc is named "fluffy" and says "bark".
# vase get:
print(a0.type())#abc


 

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




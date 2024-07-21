def tekraryab1(l):#it doesnt add uniqus
    du=[]
    for i in l:
        # if l.count(i)>1:
            if i not in du:
                du.append(i)
    du.sort()
    return du
j=["a","c","a","b","r","r","g","g","b"]  
print(tekraryab1(j))#['a', 'r', 8, 5]

a=list(set(j))
a.sort()
print(a)

def jaam(i,j):
    '''it adds the items'''
    x=i+j
    return x
print(jaam(3,4))#7
print(jaam(2,3))#5
print(jaam.__doc__)#it adds the items

def iseven(n):return n%2==0
print(iseven(4))#True

t=6
def count():
    global t
    t+=1
    return t
count();count();count()
print(count())

t=6
def count(t):
    t+=1
    return t

print(count(t))
print(count(count(count(count(t)))))

l=[1,2,3,4]
     
def mu(l):
    ll=[]
    for i in l:
        ll.append(i*2)
    return ll
print(mu(l))
#map:
def mu(a):return a*2
j=list(map(mu,l))
print(j)
 # filter:
lll=[1,2,3,4,5,6,7,8,5,34345]
def oddonly(item):
    return item%2!=0
j=list(filter(oddonly,lll))
print(j)

a=1
b=2 
def jam(*args):#only numbers
    return sum(args)
print(jam(1,2,3,b))

# ba dadane ** mitonim moteghayer ham biarim.
def jam(*args,**kargs):
    return sum(args)
print(jam(1,2,3,4,a,b))
# rule:params,*args,default params,**kwargs
print('sssss')
def k(*args):
    if len(args):
        for i in args:
            print(i)
    else:
        print('no args')
# *arges=arguments
k(1,23,4)#1 23 4
k()#no args
x=[1,2,4,76,8]
k(*x)#1 2 4 76 8
k(x)#[1, 2, 4, 76, 8]

def a(**j):#** MEANS KEYWORD ARGUMENT
    if len(j):
        for k in j:
            print(k,j[k])
a(a="aa",b="bb")#a aa b bb
b=dict(a="aa",b="bb")
a(**b)#a aa b bb
# a(b) wont work

def isprime(n):
    if n<=1 or n==2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
print(isprime(7))#True
print(isprime(8))#False
def listprime(n):
    for i in range(n):
        if isprime(i):
            print(i,end=' ')
listprime(100)#3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
def a(x):
    x=3
    print('mew')
    print(x)
x=5
a(5)
print(x)
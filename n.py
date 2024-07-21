#down casting to int:
print(10/3)#3.3333333333333335
print(int(10/3))#3
#to round the result:
print(round((10/3),2))#3.33
h=2
if h>6:print("h is greater than 6")#h is less than 6 
elif h==6:print("h is equal 6")#
else: print("h is less than 6")#
# multiple condition
if h>10 and h<100:print("h is between them")#
elif h>10 or h<100:print("one of the statements")# one of the statements
print(bool(0))#False
print(bool(12))#True
m=[[2,4,6],[1,3,5],[0,9,8]];print(m[0][1])#4
a=True;b='dorost' if a else 'ghalat'
print(b)#dorost
l=[1,2,3,4,5]
for i in l:
    for j in ['a','b']:
        print(f'1 {i} 2 {j}')
l=range(1,10,2);j=1
for i in l:
    j=j+i;print(j)
jj=enumerate('hello')
for k in jj:
    i,j=k;print(i);print(j);print(k)
# 0 h (0, 'h') 1 e (1, 'e') 2 l (2, 'l') 3 l (3, 'l') 4 o (4, 'o')
print(jj)#<enumerate object at 0x000002090177B680>
print('in fargh mikone:')
x=7;print(type(x))#<class 'int'>
import decimal
a=decimal.Decimal('.10')
print(a)#0.10
x=range(0,50,5)
for i in x:
    print(i)#0 5 10 15 20 25 30 35 40 45
hungry=False
x='hungry' if hungry else 'not hungry'

print(x)#not hungry
count=0
a='abc'
maxattempt=5
auth=False
while count<maxattempt:
    count+=1
    pw=input(f'{count}, enter the password:')
    if pw==a:
        auth=True
        break
print('authorized' if auth else 'calling the FBI') 

name=input('Enter your name:') 
print(f'chetori {name}')

# arthmetic operators
# bitwise operators
# generator 8-6
# decorator
def f1(f):
    def f2():
        print('avval')
        f()
        print('dovvom')
    return f2
@f1
def f3():
    print('this is f3')

# f3=f1(f3)
f3()

# bejaye range dar js va python az in estefade kon:
a=10
i=1
while i<=a:
    print(i)
    i=i+1


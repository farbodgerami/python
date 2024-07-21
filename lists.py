# list#######################################
b='ee';a=["james","lars",b,'a',];a1=["james","lars",b,'a',]
print(id(a))#2876298069440
print(id(a1))#2876301182144
print(id(a[0]))#2876292779568
print(id(a1[0]))#2876292779568
i=a.index("lars");print(i)#1
print(a[i])#lars
a.insert(2,'jack');print(a)#['james', 'lars', 'jack', 'ee', 'a']
a.remove('a');print(a)#['james', 'lars', 'jack', 'ee']
a.pop();print(a)#['james', 'lars', 'jack']
', '.join(a);print(','.join(a))#james,lars,jack
print(a.pop())#jack
print(a)#['james', 'lars']
a.pop(1);print(a)#['james']
print(a==a1)#False
del a[0];print(a)#[]
kk=a.append('nser');print(kk)#None
print(a)#['nser']
print(len(a))#1
print(a[len(a)-1])#naser
a.insert(3,12);print(a)#['nser', 12]
a.extend([33,44]);print(a)#['nser', 12, 33, 44]
ss=['aa','dd','cc','bb']
ss.sort();print(ss)#['aa', 'bb', 'cc', 'dd']
ee=sorted(ss);print(ee)#['aa', 'bb', 'cc', 'dd']
j=[1,2,3]
o=j+a;print(o)#[1, 2, 3, 'nser', 12, 33, 44]
print(o[0:4])#[1, 2, 3, 'nser']
l1=[0,1,2,3,4,5]
l2=[2,3,4,5,6,7]
l2=l1
l2[0]=33
l1[1]=77
print(l1)#[33, 77, 2, 3, 4, 5]
print(l2)#[33, 77, 2, 3, 4, 5]
l=[]
for i in "hellow a":
    l.append(i)
print(l)#['h', 'e', 'l', 'l', 'o', 'w', ' ', 'a']
# raveshe jadid:
l=[i for i in 'hellow a']
print(l)#['h', 'e', 'l', 'l', 'o', 'w', ' ', 'a']
ll=[i for i in range(0,10)]
print(ll[len(ll)-1])#9
t=[123,3456,567,87,456,324]
del t[1:3]
print(t)#[123, 87, 456, 324]
t.append(222222222222);print(t)#[123, 87, 456, 324, 222222222222]
lll=[i*2 for i in ll]
print(lll)#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# odd:
ll=[i for i in range(0,10) if i%2!=0]
print(ll)#[1, 3, 5, 7, 9]

# # zip:
l=[1,2,3]
ll=[4,5,6]  
j=list(zip(l,ll,))
print(j)#[(1, 4), (2, 5), (3, 6)]
ls=[1,2,3,4,2,3,45,5,1,2,4,3]
b=set(ls);print(b)#{1, 2, 3, 4, 5, 45}
l=["a","c","a","b","r","r"]
du=[]
for i in l:
    if l.count(i)>1:
        if i not in du:
            du.append(i)
print(du)#['a', 'r']


p=[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]
for i in p:
    for j in i:
        if j==0:
            print(" ",end= '')
        else:
            print("*",end= '')
    print("")
s=range(10)
print(s)#range(0, 10)
s2=[x*2 for x in s]
print(s2)#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
t=[(x,x**2) for x in s]
print(t)#[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]
from math import pi
r=[round(pi,i) for i in s]
print(r)#[3.0, 3.1, 3.14, 3.142, 3.1416, 3.14159, 3.141593, 3.1415927, 3.14159265, 3.141592654]
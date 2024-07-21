ddj= {"james":"hetfield","elan":"musk","react":"javascript","django":"python"}
for i,j in ddj.items():print(i)#james elan react django
for i,j in ddj.items():print(j)#hetfield musk javascript python
print(ddj['elan']) #musk
abc='elan'
print(ddj[abc])#musk
print(ddj.get('g'))#musk rahe dorost ine. chon agar abc vojood nadashte bashe error nemide
del ddj["james"];print(ddj)#{'elan': 'musk', 'react': 'javascript', 'django': 'python'}
ddj["james"]="hetfield2";print(ddj)
#{'elan': 'musk', 'react': 'javascript', 'django': 'python', 'james': 'hetfield2'}
ddj["slipknot"]="correy tylor";print(ddj)
#{'elan': 'musk', 'react': 'javascript', 'django': 'python', 'james': 'hetfield2', 'slipknot': 'correy tylor'}
ddj.update({"beatles":"john lenon"});print(ddj)
#{'elan': 'musk', 'react': 'javascript', 'django': 'python', 'james': 'hetfield2', 'slipknot': 'correy tylor', 'beatles': 'john lenon'}
a={"james":"hetfield","lars":"ulrich"}
for k in a.items():
    i,j=k
    # vase for i,j in a.items():
    #  i,j=k#bug dare,paini doroste
    # k=i,j
    print(i)# james# lars
    print(j)# hetfield# ulrich
    print(k)# ('james', 'hetfield') # ('lars', 'ulrich')
 
for i in a:print(i)#james lars
print(a.keys())#dict_keys(['james', 'lars'])
for i in a.keys():print(i)#james lars
print(a.items())#dict_items([('james', 'hetfield'), ('lars', 'ulrich')])
for i in a.items():print(i)#('james', 'hetfield') ('lars', 'ulrich')
print(a.values())#dict_values(['hetfield', 'ulrich'])
for i in a.values():print(i)#hetfield ulrich
jj={x for x in 'superduper' if x not in 'pd'};print(jj)#{'s', 'e', 'r', 'u'}
s=[1,3,6]
di={x:x**2 for x in s};print(di)#{1: 1, 3: 9, 6: 36}
user={1:3,2:4,5:6}
user2=user.copy()
print(user2)#{1: 3, 2: 4, 5: 6}
d={True:3,3:4}
# print(d['g']) error mide
# rahesh ine:
print(d.get('g'))#None
l=range(1,10)
di={"a":1,"b":2}
dj={key:value*2 for key,value in di.items()}
print(dj)#{'a': 2, 'b': 4}

ddj= {"james":"hetfield","elan":"musk","react":"javascript","django":"python"}
goal=[{"james":"hetfield"},{"elan":"musk"},{"react":"javascript"},{"django":"python"}]
goal1=[]
for i,j in ddj.items():
    c={i:j}
    goal1.append(c)
print(goal1)
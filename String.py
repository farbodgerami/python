mt='I\'m gonna make \'em pay for what they did to us'
print(mt)#I'm gonna make 'em pay for what they did to us
mt='how to make '
kk=mt.upper();print(kk)#HOW TO MAKE
kk=mt.title();print(kk)#How To Make
aa='fARboD';mm=aa.swapcase();print(mm)#FarBOd
print(len(mm))#6
print(mm[0])#F
print(mm[3:6])#BOd
print(mm[3:len(mm)])#BOd
mm='how to make \'em pay for what they did?'
print(mm.split())#['how', 'to', 'make', "'em", 'pay', 'for', 'what', 'they', 'did?']
print(mm.split()[3])#'em
print(mm.split()[3].upper())#'EM
matn='i am the richest man in the world'#\n beaks the string
a=matn.__len__()
print(a)#33
print(matn[3:len(matn)])#m the richest man in the world
print(matn.split(' '))#['i', 'am', 'the', 'richest', 'man', 'in', 'the', 'world']
print(matn.split(' ')[3].upper())#RICHEST
# reverse the string:
print(matn[::-1])#dlrow eht ni nam tsehcir eht ma i
j=matn.replace('am','AM')
print(j)#i AM the richest man in the world
# Online Python compiler (interpreter) to run Python online.
from collections import Counter
s=input("Enter String ")
v=['A','E','I','O','U']
final_result={}
stuart=[]
stuartlist=[]
kevin=[]
somb=[]
ss=0
sk=0

for i in s:
    for j in v:
        if i==j:
            kevin.append(i)
            break
        else:
            stuart.append(i)
            break

sc=Counter(stuart)
kc=Counter(kevin)

stuart.clear()
kevin.clear()
for i,j in sc.items():
    ss=ss+j
    stuart.append(i)
for i,j in kc.items():
    sk=sk+j
    kevin.append(i)

length=len(s)
count=0


somb.append(stuart)
somb.append(kevin)

somblen=len(somb)
co=0
for z in somb:
    co=co+1
    for i in z:
        string=''
        count=0
       
        for j in s:
            count=count+1
            if i==j:
                string=''
                strings=s[count:length]
            
            
                sount=0
                for k in strings:
                   
                    sount=sount+1
                    if sount==1:
                        string=string+i+k
                        
                        stuartlist.append(string)
                    else:
                        string=string+k
                      
                        stuartlist.append(string)
            
    
    if co==1:
        stuartlistfinal=Counter(stuartlist)
        for i,j in stuartlistfinal.items():
            ss=ss+j
       
    else:
        stuartlistfinal=Counter(stuartlist)
    
        for i,j in stuartlistfinal.items():
            sk=sk+j
       
        
    stuartlist.clear()

if ss>sk:
    print("Stuart",ss)
elif sk>ss:
    print('Kevin',sk)
else:
    print("Draw")
# q.1 get keys corresponding to a value in user defined dictionary
dic=eval(input('dic: '))
e=int(input("enter the keys value"))
flag=False
for i in dic.items():
    
    if(e==i[1]):
        
        print(i[0])


# q.2 nested dictionary
d={}
for i in range(4):
    p=input("enter a name")
    for j in range(4):
        a=input("enter subject ")
        b=input("enter marks")
        
        dic1[p,a]=[a,b]
name=input("enter name")
for j in d.items():
    for r in range(4):
        if(j[r][0]==name):
            print(j[1])

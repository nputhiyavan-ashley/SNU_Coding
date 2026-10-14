print("Enter n and head with space")
a=input()
s1=list(map(int,a.split()))
print("Enter Val with space")
b=input()
nodes=list(map(int,b.split()))

s=set()
d={}
for i in range(len(nodes)):
    if nodes[i]==-1:
        print(-1) 

    if nodes[i] not in s:
        s.add(nodes[i])
        d[nodes[i]]=i
        continue
    print(d[nodes[i]])


        
 




    
    






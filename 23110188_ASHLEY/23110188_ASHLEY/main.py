input = [["AI",80],["CSE",70],["AI",90],["DS",75],["CSE",80]]
dept=[]
sum=[]
count=[]
max=[]

for entry in input:
    if entry[0] not in dept:
        dept.append(entry[0])
        sum.append(entry[1])
        count.append(1)
        max.append(entry[1])
    
    if entry[0] in dept:
        ind=dept.index(entry[0])
        sum[ind]+=entry[1]
        count[ind]+=1
        if max[ind] < entry[1]:
            max[ind] =entry[1]

for i in range(len(dept)):
    sum[i]=sum[i]/count[i]
    sum[i]=sum[i]*100
    sum[i]=sum[i]//1
    sum[i]=sum[i]/100

for j in range(len(dept)):
  for i in range(len(dept)):
    if dept[i]<dept[i+1]:
      tempd=dept[i]
      tempa=sum[i]
      tempm=max[i]
  
      dept[i]=dept[i+1]
      sum[i]=sum[i+1]
      max[i]=max[i+1]

print(dept)
print(sum)# sum array contains the average score ineach dept
print(max)

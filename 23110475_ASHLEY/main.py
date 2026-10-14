x=8
vals=[10,12,11,13,12,14,100,9]

y=sorted(vals)

def findmedian(length,values):
  if x%2==0:
    med=(values[(length//2)]+values[(length//2)-1])//2
  elif x%2!=0:
    med=values[length//2]
  return med

m=findmedian(x,y)

if x%2==0:
  lh=y[0:m]
  uh=y[m:]
  p=x//2
elif x%2!=0:
  lh=y[0:m]
  uh=y[m+1:]
  p=(x-1)//2

q1=findmedian(p,lh)
q3=findmedian(p,uh)

iqr=q3-q1
lb=q1-1.5*iqr
ub=q3+1.5*iqr

outliers=[]

for i in vals:
  if i<lb or i>ub:
    outliers.append(i)
  
if len(outliers)!=0:
  print(outliers)
else:
  print("NONE")

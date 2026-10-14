a = int(input("Enter no. of columns"))
b = int(input("Enter no of rows"))
sum =0
i =0
j=0
while (i<a):
    while(j<b):
        num=int(input("Enter value"))
        if(i==0):
           sum=sum + num
        elif(j ==0):
           sum = sum+num
        elif(i==a-1):
            sum = sum+num
        elif(j==b-1):
            sum= sum+num
        j=j+1
    i=i+1
print(sum)
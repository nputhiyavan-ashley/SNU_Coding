n=int(input("Enter length of array:"))
arr=[]
for i in range(n):
    number=int(input("Enter:"))
    arr.append(number)

print(arr)

d1={}
l1=[]
for num in range(len(arr)):
    if arr[num] not in d1:
        d1[arr[num]]=[num]
    else:
        if d1[arr[num]]==2:
            break
        else:
            d1[arr[num]].append(num)
            ans=d1[arr[num]]
            l1.append(ans)
            ans.append(arr[num])
            break


if l1==[]:
    print(None)
else:
    print(l1[0][-1],l1[0][1]-l1[0][0])



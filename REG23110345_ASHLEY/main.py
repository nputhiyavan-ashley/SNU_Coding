r=int(input())
c=int(input())
mat=[]
for i in range(r):
    row=[]
    for j in range(c):
        row.append(float(input()))
    mat.append(row)
mat1=[]
for j in range(c):
    max_col=[]
    for k in range(r):
        max_col.append(mat[k][j])  
        maxi=max(max_col)
        mini=min(max_col)
        mat2=[]
        if(maxi==mini):
            mat2.append(0)
        else:
            mat2.append(round((mat[i][j]-mini)/(maxi-mini),4))
    mat1.append(mat2)
    
    
for i in range(r):
    for j in range(c):
        print(mat1[i][j])
    print()

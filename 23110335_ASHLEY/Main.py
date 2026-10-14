def lcs(n,arr):
    #lcs
    dp=list()
    arr.sort()
    arr=set(arr)
    c=0
    for i in range(n):
        for j in range(i+1):
            if arr[i]-arr[j]==1:
                c+=1
                dp[i][j]=c
    return dp[n][n]
def main():
    print(lcs(6,[100,4,200,1,3,2]))
    print(lcs(8,[10,5,12,10,11,5,13,14]))

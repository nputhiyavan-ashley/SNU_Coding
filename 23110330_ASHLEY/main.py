def consecutive(n,k,threshold,tasks):
    res = []
    i = 0
    while tasks[i][1] > threshold and i < n:
        sub = []
        sub.append(tasks[i][0])   
        i += 1  
    else:
        res.append(sub)
        sub = []

    ans = []
    for i in range(res):
        if len(res[i]) > k:
            ans.append(res[i])  


    return ans





# 6 2 80
# t1,70
# t2,90
# t3,95
# t4,60
# t5,85
# t6,88 

# tasks = [[]]
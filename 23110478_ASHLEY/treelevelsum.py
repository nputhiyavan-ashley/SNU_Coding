def sumr(tree):
    #checking if null tree
    if tree[0] == "null":
        return 0
    # initializing variables
    level = 1
    sum = 0
    for i in range (len(tree)):
        #skipping null nodes
        if tree[i] == "null":
            continue
        #checking negative value
        if int(tree[i])<0:
            continue
        sum = sum + int(tree[i])
        #checking each level
        if i == (2**level):
            level +=1
            print(sum)
            sum = 0
            

tree = input()
sumr(tree)
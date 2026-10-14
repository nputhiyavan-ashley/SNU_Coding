def count_err(n,k, mainL):
    count_d = dict() #dictionary of error code : count
    #seen = {}
    for i in range(len(mainL)):
        for j in mainL:
            if mainL[i][2] == "ERROR" :
                mainL[i][3] = errc
                count += 1
                d[errc] = count

    #s = sorted(count_d ) sort by k and alphabetically

    #return top k items from dictionary
            



# n = int(input("Enter num of logs: "))
# k = int(input("Enter number of top error codes to return: "))

#input loop
#example
mainL = [["t1", "ERROR", "E02" ], ["t2","INFO","E01"], ["t3","ERROR","E01"], ["t4","ERROR","E02"],["t5","ERROR","E03"]]
count_err(n,k,mainL)

import sys;

def merge_intervals():
    input_data=sys.stdin.read().split()
    if not input_data:
        return

    n=int(input_data[0])
    intervals=[]
    idx=1
    for _ in range(n):
        start=int(input_data[idx])
        end=int(input_data[idx+1])
        intervals.append([start,end])
        idx+=2

        intervals.sort(key= lambda x: x[0])
        
        merged=[]
        for current in intervals:
            if not merged or merged[-1][1] < current[0]:
                merged.append(current)
            else:
                merged[-1][1]=max(merged[-1][1], current[1])

        for start,end in merged:
            print(f"{start} {end}")

if __name__=="__main__":
    merge_intervals()




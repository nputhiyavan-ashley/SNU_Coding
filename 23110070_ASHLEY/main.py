#INPUT:
#Line 1: number of meetings (n)
#Lines 2 to n+1: <start time (int) <space> <end time- EXCLUDED (int)>

#OUTPUT:
#minimum number of rooms required

#Logic: Get the list of start and end time in a list. Traverse the list with a jump of 2 elements. Have an interval 5 minutes each. increment rooms count at each interval accordingly
def min_rooms(l):
  li=len(l)
  room=0
  for i in range(0,li+1,2):
    start=l[i]
    end=l[i+1]
    intervals:(end-start)/5
    room+=1
  return room




#TIME COMPLEXITY: O(n^2)
#SPACE COMPLEXITY: O(n)
    
#Logic: firt get the number of meetings(n). then input all the timings as strings. then split all those strings and put that into a list such that each element of the list is either the start or end time. so every 2 elements of the list is as follows:first, the strt time and followed by the end time. upon creating that list, traverse it, and explicitly implement type conversion of the strings to numbers, and push it to a new list. this list is passed to the implemented function.
def main():
  n=int(input())
  l=[]
  for i in range(n):
    s=input()
    s.split(' ')
  for j in s:
    num=int(j)
    l.append(num)
  min_rooms(l)


#Unit Test Cases:

#Input: 4
#0 30
#5 10
#15 20
#20 25 
#Output: 2

#Input: 3
#0 10
#5 15
#10 20 
#Ouput: 2
  

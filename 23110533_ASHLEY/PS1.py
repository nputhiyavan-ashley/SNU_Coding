
n = int(input)
for _ in range(n):
    arr = int(input)

def main():
  sum_score = 0
  max_score = 0

  for i in arr:
    sum_score += i
    
  avg_score = sum_score/n
  max_score = max(arr)

  return [arr, avg_score, max_score]

  


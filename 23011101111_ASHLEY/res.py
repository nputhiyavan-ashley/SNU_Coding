input_k_n = input()
input_nums = input()

# PROCESS INPUT
array_k_n = input_k_n.split(" ")
n, k = int(array_k_n[0]), int(array_k_n[1])

input_data = input_nums.split(" ")

for i in range(n):
  input_data[i] = int(input_data[i])

# SOLUTION
res = []
for i in range(n - k + 1):
  average = 0
  max_val = input_data[i]
  wind = []
  
  for j in range(i, i + k):
    average += input_data[j]

    if max_val < input_data[j]:
      max_val = input_data[j]
  
  average = round(average / k, 2)
  res.append((average, max_val))

# OUTPUT
for average_val, max_val in res:
  print(average_val, end = "")
  print(",", end = "")
  print(max_val)
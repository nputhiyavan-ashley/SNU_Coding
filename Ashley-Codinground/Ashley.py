# Online Python compiler (interpreter)
# Write and run Python online using this editor.
n = int(input("Enter the number of Records: ")) 
id = int(input("Enter your id: "))
name = input("Enter your name: ")
email = input("Enter your Email: ")

l = len(n)

for i in range (0,l-1):
    CleanedRecords = clean(id,name,email)
    print("Cleaned Records")


def trim(id,name,email):
  for i in range (0,l-1):
    if ("% %" in i):
      RejectedRecords = append(id[i])
      i = i+1
      print("invalid records: ",RejectedRecords)
    else:
      valid = append(id[i])
      print("Valid record: ",valid)

def EmailNormalization(email):
  for i in range(0,l-1):
    valid = normalize(email[i])
    print("Valid Record: ",valid)
    i = i+1

print(n)
print(Trim(id,name,email))
print(EmailNormalization(email))
print("valid: ",len(valid))
print("rejected: ",len(RejectedRecords))







    
  
  
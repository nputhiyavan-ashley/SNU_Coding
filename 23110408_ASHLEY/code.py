def validbracker(s):
  open='{[('
  close='}])'
  s=input('Enter the string')
  stack=[]
  for i in range(len(s)):
    if s[i] in open:
    
      stack.append(s[i])

    if s[i] in close:
      if len(stack)==0:
        return 'ERROR'
      if s[i]=='}':
        curr=stack.pop
        if curr!='{':
          return 'ERROR'
      if s[i]==']':
        curr=stack.pop
        if curr!='{':
          return 'ERROR'
      if s[i]==')':
        curr=stack.pop
        if curr!=')':
          return 'ERROR'
  if len(stack)==0:
    return 'BALANCED'

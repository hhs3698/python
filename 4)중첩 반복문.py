# 1. 
for i in range(5):
  for j in range(5):
    print(j, end=" ")
  print()
# 0 1 2 3 4 
# 0 1 2 3 4 
# 0 1 2 3 4 
# 0 1 2 3 4 
# 0 1 2 3 4 

# 2. 
for i in range(5):
   for j in range(i+1):
     print("*", end=" ")
   print()
# * 0일 때
# * * 1일 때 
# * * * 2일 때 
# * * * * 3일 때 
# * * * * * 4일 때 
    
# 3. 
for i in range(5):
  for j in range(5-i):
    print("*", end=" ")
  print()
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 


